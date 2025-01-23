# Arquitetura do Projeto

O sistema é composto pelos seguintes componentes principais:

1. **Base de Dados**:
   - Armazenamento de documentos em **AWS S3** ou **DynamoDB**.
   - Indexação de dados usando **Pinecone** ou **ElasticSearch**.

2. **Recuperação de Informação**:
   - Geração de embeddings com **sentence-transformers**.
   - Busca de documentos relevantes usando **Pinecone**.

3. **Geração de Respostas**:
   - Integração com modelos generativos como **OpenAI GPT** e **AWS Bedrock**.
   - Uso do **LangChain** para criar fluxos de perguntas e respostas.

4. **Agentes**:
   - Criação de agentes personalizados com **LangChain** e **LangGraph**.
   - Orquestração de tarefas complexas.

## Diagrama da Arquitetura

Abaixo está um diagrama que ilustra a arquitetura do sistema:

![Diagrama da Arquitetura](diagrams/architecture_diagram.png)