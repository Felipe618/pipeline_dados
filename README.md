# Pipeline de Dados - ETL em Python

Pipeline ETL em Python orientado a objetos para leitura, padronização e fusão de dados de múltiplas fontes (JSON e CSV).

---

## 📁 Estrutura do Projeto

```text
pipeline_dados/
├── data_raw/               # Arquivos brutos de entrada (JSON e CSV)
├── data_processed/         # Arquivos consolidados de saída
├── scripts/                # Módulos e scripts de execução
│   ├── processamento_dados.py # Classe com métodos de leitura, transformação e gravação
│   └── fusao_mercado_fev.py   # Script de orquestração do pipeline
├── .gitignore              # Arquivos/pastas ignorados pelo Git
├── LICENSE                 # Licença do repositório
├── README.md               # Documentação do projeto
└── requirements.txt        # Configurações de ambiente e dependências
