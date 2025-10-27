Feeling Analyzer 📊
Feeling Analyzer é um painel de análise de sentimento em tempo real que monitora menções a palavras-chave específicas em subreddits do Reddit. Ele utiliza a API da OpenAI (GPT) para classificar o sentimento dos comentários como Positivo, Negativo ou Neutro e exibe os resultados em um dashboard web interativo.

🚀 Visão Geral
Este projeto é dividido em dois componentes principais que rodam simultaneamente:

O Coletor (collector.py): Um script de backend que se conecta à API do Reddit em tempo real. Ele "escuta" novos comentários, filtra aqueles que contêm sua palavra-chave, envia o texto para a API da OpenAI para análise e salva o resultado (id, timestamp, texto, sentimento) em um arquivo feelings.csv.

O Dashboard (dashboard.py): Um aplicativo web, construído com Streamlit, que lê o arquivo feelings.csv e exibe gráficos e métricas sobre os sentimentos coletados, atualizando-se automaticamente.

(Recomendação: Tire um print da tela do seu dashboard.py rodando e insira aqui!) [INSIRA UM SCREENSHOT DO SEU DASHBOARD AQUI]

✨ Funcionalidades
Monitoramento em Tempo Real: Captura comentários do Reddit assim que são postados.

Filtragem por Palavra-chave: Foco em tópicos específicos (ex: "Nubank", "$MGLU3", "Bitcoin").

Análise de Sentimento com IA: Classificação precisa usando gpt-3.5-turbo da OpenAI.

Dashboard Interativo: Visualização de dados moderna e responsiva com Streamlit.

Persistência de Dados: Os dados são salvos em CSV, permitindo análises históricas.

Arquitetura Modular: O código é separado em core (lógica de negócios) e scripts principais (executáveis), facilitando a manutenção.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Coleta de Dados: PRAW (The Python Reddit API Wrapper)

Análise de IA (NLP): OpenAI API

Dashboard Web: Streamlit

Manipulação de Dados: Pandas

Gerenciamento de Segredos: python-dotenv

Visualização: Plotly Express
```
📂 Estrutura do Projeto
feeling-analyzer/
├── core/
│   ├── __init__.py            # Torna 'core' um pacote Python
│   ├── reddit_client.py       # Módulo para conectar à API do Reddit
│   └── sentiment_analyzer.py  # Módulo para analisar sentimento com OpenAI
│
├── collector.py               # Script principal para coletar e analisar dados
├── dashboard.py               # Script principal para o painel web (Streamlit)
│
├── .env                       # (Ignorado) Arquivo com chaves de API reais
├── .env.example               # Arquivo de exemplo para configuração
├── .gitignore                 # Arquivos e pastas a serem ignorados pelo Git
├── requirements.txt           # Lista de dependências do projeto
├── feelings.csv            # (Ignorado) Banco de dados de saída
└── README.md                  # Esta documentação
````
⚙️ Instalação e Configuração
Siga estes passos para configurar e rodar o projeto localmente.

1. Pré-requisitos
Python 3.7 ou superior

Conta no Reddit (para criar chaves de API)

Conta na OpenAI (para gerar chave de API)

2. Clonar e Instalar
Clone este repositório:
```
git clone https://github.com/SEU-USUARIO/feeling-analyzer.git
cd feeling-analyzer
Crie e ative um ambiente virtual:
```

# Windows
```
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```
Instale as dependências:
```
pip install -r requirements.txt
```
3. Configurar Chaves de API
Crie uma cópia do arquivo de exemplo .env.example:
```
cp .env.example .env
```
Abra o arquivo .env (que é ignorado pelo Git) e preencha com suas chaves secretas:

Snippet de código

# Chaves do Reddit
```
REDDIT_CLIENT_ID=YOUR_CLIENT_ID
REDDIT_CLIENT_SECRET=YOUR_CLIENT_SECRET
REDDIT_USER_AGENT="Feeling Analyzer v0.1 por /u/YOUR_USER"
```

# Chave da OpenAI
```
OPENAI_API_KEY=SUA_API_KEY_AQUI
```
▶️ Como Usar
Você precisará de dois terminais rodando simultaneamente.

Terminal 1: O Coletor
Inicie o script que monitora, analisa e salva os dados.

```
python collector.py
```
Você verá mensagens de log no console assim que novos comentários forem encontrados e analisados. Deixe este terminal rodando.

Terminal 2: O Dashboard
Em um novo terminal (com o mesmo ambiente virtual ativado), inicie o servidor web do Streamlit.

streamlit run dashboard.py
O Streamlit abrirá automaticamente uma aba no seu navegador (normalmente em http://localhost:8501). O painel será atualizado automaticamente à medida que novos dados forem salvos no feelings.csv.

🔧 Personalização
Para monitorar um termo ou subreddit diferente, basta editar as constantes no topo do arquivo collector.py:

Python
# Em collector.py
# Constantes do Projeto
```
SEARCH_TERM = "Nubank"  # Mude para "Bitcoin", "PETR4", etc.
SUBREDDIT = "farialimabets" # Mude para "investimentos", "brasil", etc.
OUTPUT_FILE = "feelings.csv"
```



