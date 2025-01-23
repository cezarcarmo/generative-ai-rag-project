from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.generic.database import SQL  # Alternativa ao Database
from diagrams.custom import Custom  # Para ícones personalizados
from diagrams.programming.language import Python

# Caminho para salvar o diagrama
output_path = "docs/diagrams/architecture_diagram"

with Diagram("Arquitetura do Projeto", filename=output_path, outformat="png", direction="LR"):
    # Componentes de Armazenamento
    with Cluster("Base de Dados"):
        s3 = S3("AWS S3")
        dynamodb = SQL("DynamoDB")  # Usando SQL como alternativa

    # Componentes de Recuperação
    with Cluster("Recuperação de Informação"):
        elasticsearch = Custom("ElasticSearch", "./docs/icons/elasticsearch.png")  # Ícone personalizado para Elasticsearch
        pinecone = Custom("Pinecone", "./docs/icons/pinecone.png")  # Ícone personalizado para Pinecone

    # Componentes de Geração
    with Cluster("Geração de Respostas"):
        openai = Custom("OpenAI GPT", "./docs/icons/openai.png")  # Ícone personalizado para OpenAI
        bedrock = Custom("AWS Bedrock", "./docs/icons/bedrock-color.png")  # Ícone personalizado para AWS Bedrock
        langchain = Python("LangChain")

    # Componentes de Agentes
    with Cluster("Agentes"):
        langgraph = Custom("LangGraph", "./docs/icons/langgraph.png")  # Ícone personalizado para LangGraph

    # Conexões entre os componentes
    s3 >> Edge(color="brown") >> elasticsearch
    dynamodb >> Edge(color="brown") >> pinecone
    elasticsearch >> Edge(color="blue") >> langchain
    pinecone >> Edge(color="blue") >> langchain
    langchain >> Edge(color="green") >> openai
    langchain >> Edge(color="green") >> bedrock
    langchain >> Edge(color="purple") >> langgraph