## Projeto em desenvolvimento
![apsindex](https://github.com/user-attachments/assets/ef53a5d3-5d48-4468-a1a8-57ab92e0956a)

Aqui está uma documentação completa para o seu projeto, abrangendo a estrutura do projeto, instruções de configuração, uso e objetivos do código.

---

# Documentação do Projeto de Reconhecimento Facial e Chatbot de Qualidade do Ar

## Objetivo do Projeto
Este projeto foi criado para integrar um chatbot com funcionalidades de previsão e um sistema de reconhecimento de qualidade do ar para diferentes localidades. Ele utiliza um modelo de processamento de linguagem natural (PLN) para entender e responder às perguntas dos usuários e coleta dados de qualidade do ar por meio de uma API externa, retornando informações específicas sobre os níveis de poluição e sua classificação em cores.

## Estrutura do Projeto
A estrutura do projeto está organizada em arquivos e pastas conforme listado abaixo, cada um com uma função específica:

### Arquivos principais
- **README.md**: Arquivo de documentação com instruções de configuração e uso.
- **app.py**: Script principal que executa o aplicativo Flask para interação com o chatbot e a API de qualidade do ar.
- **chat.py**: Código de suporte ao chatbot para análise de frases de entrada e resposta automatizada.
- **data.pth**: Arquivo contendo o modelo de dados treinado, necessário para o chatbot.
- **intents.json** e **intents_utf8.json**: Arquivos de dados que definem os padrões de conversa e respostas esperadas pelo chatbot.
- **model.py**: Arquivo que contém a definição da arquitetura do modelo de rede neural.
- **nltk_utils.py**: Utilitários para processamento de texto, como tokenização e criação de “bag of words”.
- **train.py**: Script para treinar o modelo do chatbot com os dados de intenção e padrões de linguagem.

### Pastas do projeto
- **__pycache__**: Contém os arquivos compilados do Python.
- **static**: Inclui arquivos estáticos como imagens, `app.js` e `style.css`, que são usados na interface do aplicativo.
- **templates**: Armazena arquivos HTML, incluindo `index.html`, o layout principal da interface.

## Configuração Inicial

### Clonar o Repositório
Para começar, clone o repositório do projeto usando o comando:

```bash
$ git clone <URL_DO_REPOSITORIO>
```

### Instalar Dependências
Este projeto utiliza `nltk` para processamento de texto. No ambiente Python, execute os seguintes comandos para instalar as dependências e baixar os dados necessários:

```python
>>> import nltk
>>> nltk.download('punkt')
```

### Treinar o Modelo
Para treinar o modelo de linguagem, utilize o seguinte comando:

```bash
$ (venv) python train.py
```

O script `train.py` lerá os dados de intenção, treinará o modelo e salvará os parâmetros no arquivo `data.pth`.

### Executar o Projeto
Com o modelo treinado e o ambiente configurado, execute o aplicativo com o comando:

```bash
$ (venv) python app.py
```

O aplicativo será executado no modo de depuração, disponível no `localhost` na porta 5000.

---

## Descrição dos Principais Arquivos

### app.py
Este arquivo configura o servidor web usando Flask e define três rotas principais:

1. **Rota raiz (`/`)**: 
   - Método: `GET`, `POST`
   - Esta rota exibe a interface principal e, quando uma cidade é enviada via formulário, faz uma requisição à API de qualidade do ar (`api.waqi.info`), processando a resposta para exibir o índice de qualidade do ar (AQI) com uma classificação em cores.

2. **Rota de chat (`/chat`)**: 
   - Método: `GET`, `POST`
   - Recebe a entrada do usuário e, ao ser submetida, usa a função `get_response()` do módulo `chat.py` para retornar uma resposta gerada pelo chatbot.

3. **Rota de previsão (`/predict`)**:
   - Método: `POST`
   - Recebe uma mensagem JSON com a entrada do usuário, processa essa entrada com o modelo de PLN e retorna uma resposta JSON.

### chat.py
Arquivo responsável por processar as entradas do usuário e retornar respostas contextuais. 

- **Função `get_response`**: Recebe a frase do usuário e:
   - Realiza tokenização, converte a entrada em vetores “bag of words”.
   - Gera uma previsão de probabilidade de resposta, selecionando a mais relevante com probabilidade maior que 75%.
   - Retorna uma resposta contextualizada ou um aviso de "Não entendi a sua pergunta".

### train.py
Script de treinamento do modelo de chatbot, usando uma rede neural personalizada para associar padrões de frases a respostas.

- **Processamento de Dados**: Tokeniza e reduz as palavras para seu radical, criando vetores de treinamento.
- **Treinamento**: Utiliza `torch` para treinar a rede neural, otimizando a correspondência entre frases e respostas.
- **Armazenamento de Resultados**: Ao final do treinamento, salva o estado do modelo no arquivo `data.pth`.

---

## Exemplo de Uso

1. Acesse o aplicativo em `http://localhost:5000/`.
2. Insira o nome de uma cidade para verificar a qualidade do ar ou use o chatbot para perguntas sobre qualidade do ar ou temas relacionados, conforme os padrões em `intents.json`.

