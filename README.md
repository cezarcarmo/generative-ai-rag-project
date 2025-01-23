# Generative AI RAG Project

Este projeto demonstra a implementação de um sistema de **Recuperação de Informação + Geração de Respostas (RAG)** utilizando ferramentas modernas como **AWS Bedrock**, **LangChain**, **Pinecone** e **OpenAI**.

## Objetivo
Desenvolver um sistema que combine técnicas de recuperação de informação com modelos generativos para responder perguntas de forma contextualizada e precisa.

## Funcionalidades
- **Recuperação de Informação**: Indexação e busca de documentos usando Pinecone ou ElasticSearch.
- **Geração de Respostas**: Integração com modelos generativos como OpenAI GPT e AWS Bedrock.
- **Agentes Inteligentes**: Criação de agentes personalizados com LangChain e LangGraph.

## Estrutura do Repositório

```
generative-ai-rag-project/
│
├── README.md
├── docs/
│   ├── introduction.md
|   ├── diagrams/
│       ├── arquitetura.puml
│       └── arquitetura.png  
│   ├── architecture.md
│   ├── tools-and-cases.md
├── src/
│   ├── data_processing/
│   ├── models/
│   ├── pipelines/
│   └── agents/
├── notebooks/
│   ├── exploration.ipynb
│   ├── training.ipynb
│   └── deployment.ipynb
├── tests/
├── requirements.txt
└── LICENSE
```

# Arquitetura

![Diagrama de Arquitetura](./docs/diagrams/arquitetura.png)