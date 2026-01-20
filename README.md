# 🎫 Ticket AI Service — Classificação Inteligente de Chamados

Este projeto é um **serviço de Inteligência Artificial** para **classificação automática de chamados (tickets)** a partir de texto livre.

A IA analisa a descrição do chamado e retorna automaticamente:

- 🧩 **Tipo** do chamado (Bug, Suporte, Melhoria, Dúvida)
- 🚦 **Prioridade** (Alta, Média, Baixa)
- 🏢 **Área responsável** (Sistemas, Infra, Geral)

O objetivo é **automatizar triagem**, reduzir trabalho manual e acelerar o fluxo de atendimento.

---

## 🎯 Objetivo do Projeto

Criar uma base sólida de IA que possa ser facilmente integrada com:

- Backend (.NET, Java, Node, etc)
- Frontend (Web / Mobile)
- APIs REST (FastAPI)

Este repositório representa a **camada de IA**, separada do backend e frontend.

---

## 🧠 Como a IA funciona

O sistema utiliza técnicas clássicas de **Processamento de Linguagem Natural (NLP)**:

- **TF-IDF** para vetorização de texto
- **Logistic Regression** para classificação
- **Um modelo por decisão**, seguindo boas práticas:
  - Um modelo para `type`
  - Um modelo para `priority`
  - Um modelo para `area`

Cada modelo é treinado de forma independente a partir de um dataset em CSV.

---

## 🧱 Estrutura do Projeto

ticket-ai-service/
│
├── data/
│ └── tickets.csv # Dataset de treino
│
├── models/
│ ├── type_model.pkl # Modelo treinado – Tipo
│ ├── priority_model.pkl # Modelo treinado – Prioridade
│ └── area_model.pkl # Modelo treinado – Área
│
├── training/
│ └── train_model.py # Script genérico de treinamento
│
├── test_all_models.py # Script para testar os modelos
├── .gitignore
└── README.md


⚠️ **Importante:**  
A pasta `models/` e o `venv/` **não devem ser versionados** no GitHub.

---

## 📦 Pré-requisitos

- **Python 3.10+** (recomendado 3.11)
---

## ▶️ Como rodar localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/ticket-ai-service.git
cd ticket-ai-service
```

### 2. Criar e ativar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Treinar modelos
```bash
py training/train_model.py type # treinar TIPO
py training/train_model.py priority # treinar PRIORIDADE
py training/train_model.py area # treinar ÁREA
```

### 5. Testar os modelos
```bash
py test_all_models.py
```

### Exemplo de classificação
Entrada:
Erro ao cadastrar cliente

Saída:
Tipo: Bug
Prioridade: Média
Área: Sistemas



