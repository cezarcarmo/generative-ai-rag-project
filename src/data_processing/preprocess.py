import pandas as pd
import json
import os

# Função para carregar o dataset com amostragem opcional
def load_nq_data(file_path, sample_size=None):
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if sample_size and i >= sample_size:
                break
            data.append(json.loads(line))
    print(f"Carregados {len(data)} registros de {file_path}")
    return data

# Função para converter o dataset em um DataFrame
def nq_to_dataframe(nq_data):
    processed_data = []
    for item in nq_data:
        question = item.get("question_text", "No question provided")
        for annotation in item.get("annotations", []):
            if annotation.get("yes_no_answer") == "NONE":
                # Verificar se "short_answers" existe e não está vazio
                if "short_answers" in annotation and annotation["short_answers"]:
                    answer = annotation["short_answers"][0].get("text", "")
                else:
                    answer = ""  # Caso não haja "short_answers"
            else:
                answer = annotation.get("yes_no_answer", "No answer provided")
            processed_data.append([question, answer])
    return pd.DataFrame(processed_data, columns=["question", "answer"])

# Função para salvar o dataset pré-processado
def save_cleaned_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Dados salvos em {output_path}")

# Pipeline completo
def preprocess_pipeline(input_path, output_path, sample_size=None):
    nq_data = load_nq_data(input_path, sample_size)
    df = nq_to_dataframe(nq_data)
    save_cleaned_data(df, output_path)

# Executar o pipeline
if __name__ == "__main__":
    base_dir = r"D:\bases_gen_ai"  # Atualize para o seu diretório
    input_path = os.path.join(base_dir, "v1.0-simplified_simplified-nq-train.jsonl")
    output_path = os.path.join(base_dir, "processed", "cleaned_dataset_train.csv")
    preprocess_pipeline(input_path, output_path, sample_size=1000)

    # Processar o arquivo de validação com amostragem
    input_path_dev = os.path.join(base_dir, "v1.0-simplified_nq-dev-all.jsonl")
    output_path_dev = os.path.join(base_dir, "processed", "cleaned_dataset_dev.csv")
    preprocess_pipeline(input_path_dev, output_path_dev, sample_size=500)
