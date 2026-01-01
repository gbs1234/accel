# Classificação de Movimentos Humanos com Smartphone  
**Produto Educacional – MNPEF (Polo 03 UFTM / Barra do Garças)**

Este repositório contém um aplicativo educacional desenvolvido como **Produto Educacional do Mestrado Nacional Profissional em Ensino de Física (MNPEF)**.

O aplicativo utiliza **dados do acelerômetro de smartphones** para classificar movimentos humanos ao longo do tempo, permitindo aos estudantes investigar conceitos de **movimento, aceleração, modelagem, análise de dados e inteligência artificial** de forma prática e interdisciplinar.

---

## 🎯 Objetivo Educacional

O objetivo do aplicativo é:

- Introduzir conceitos de **movimento e cinemática** por meio de dados reais;
- Trabalhar **aquisição e análise de dados experimentais** com sensores do smartphone;
- Explorar noções básicas de **aprendizado de máquina (Machine Learning)**;
- Estimular o pensamento científico e investigativo no Ensino Médio.

Os movimentos analisados são:

- 🧍 **Parado**
- 🚶 **Caminhando**
- 🏃 **Correndo**
- 💃 **Dançando**

Cada classificação corresponde a uma janela temporal de **2 segundos**.

---

## 📱 Geração dos Dados com o aplicativo PHYPHOX

Os dados utilizados pelo modelo são gerados com o aplicativo gratuito **PHYPHOX**, disponível para Android e iOS.

### Passo a passo para gerar os dados

1. Instale o aplicativo **PHYPHOX** no smartphone.
2. Abra o PHYPHOX e selecione o experimento:
   - **Aceleração (sem gravidade)**  
3. Inicie a gravação.
4. Realize o movimento desejado:
   - ficar parado
   - caminhar
   - correr
   - dançar (ou movimentos aleatórios)
6. Finalize a gravação.
7. Exporte os dados no formato **CSV**.
8. (opcional) Transfira o arquivo CSV para o computador.

Os dados no formato CSV são usados como entrada para o aplicativo. 

---

## 🧪 Como testar o modelo (interface web)

O aplicativo pode ser testado em:
https://mnpef-movimentos-app-515597877919.us-east1.run.app/

O aplicativo possui uma interface web simples, acessível pelo navegador:

1. Abra a página inicial do aplicativo.
2. Faça upload do arquivo CSV ou ZIP gerado pelo PHYPHOX.
3. Clique em **Enviar e Predizer**.
4. O sistema exibirá:
   - um **resumo geral** dos movimentos detectados;
   - uma **linha do tempo**, com emojis e intervalos de tempo;


---

## 💻 Como rodar o aplicativo localmente (no seu computador)

### Requisitos

- Python 3.9 ou superior
- Pip
- (Opcional) Docker

---

### 🔹 Opção 1: Rodar diretamente com Python

1. Clone o repositório:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO



2. É recomendável criar um ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows


3. Instale as dependências

cd my-app
pip install -r requirements.txt


4. Execute o aplicativo

python app.py

5. Abra o navegador e acesse:

http://localhost:8080



###  🔹 Opção 2: Rodar com o Docker

1. Construa a imagem Docker

cd my-app
docker build -t mnpef-movimentos .


2. Execute o container

docker run --rm -p 8080:8080 mnpef-movimentos


3. Abra o navegador

http://localhost:8080


----

🧠 Sobre o Modelo

O modelo foi treinado para reconhecer padrões de aceleração associados a diferentes tipos de movimento.

As classes internas do modelo são mantidas em inglês por convenção técnica, mas a interface apresenta todas as informações em português, de forma acessível aos estudantes do ensino médio no Brasil.

O foco do projeto não é apenas a acurácia, mas o uso pedagógico dos dados e das previsões.

Ele pode ser utilizado em atividades envolvendo:

- Física (cinemática, análise de movimento)
- Matemática (estatística, análise de dados)
- Tecnologia e Computação
- Projetos interdisciplinares

Este projeto é destinado a fins educacionais e acadêmicos.

Para referenciar esse código, use:

Silva, G. B. (2025).
Classificação de movimentos humanos com smartphone [Software].
MNPEF – Polo UFTM/Barra do Garças.
https://github.com/gbs1234/accel

Contato: george.silva@ufmt.br