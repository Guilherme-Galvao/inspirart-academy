


# 🦅 Inspirart Academy - Plataforma LMS High-End para Tatuadores

![Status](https://img.shields.io/badge/Status-Sprint_2_Iniciado-orange?style=for-the-badge)
![Backend](https://img.shields.io/badge/Backend-Django_REST-green?style=for-the-badge&logo=django)
![Frontend](https://img.shields.io/badge/Frontend-React_Vite-blue?style=for-the-badge&logo=react)
![Security](https://img.shields.io/badge/Security-Throttling_&_DotEnv-red?style=for-the-badge&logo=security)
![AI-Powered](https://img.shields.io/badge/Dev-AI_Assisted-purple?style=for-the-badge&logo=google-gemini)

> **O Ecossistema Definitivo para a Arte da Tatuagem: Do Aprendiz ao Mestre.**

---

## 🎯 O Problema vs. Solução

O mercado de ensino de tatuagem enfrenta dois grandes gargalos:
1.  **Para o Aprendiz:** A falta de referência técnica precisa em vídeo-aulas convencionais ("Qual voltagem ele usou?", "Que agulha é essa?").
2.  **Para o Mestre:** A dificuldade de tatuadores experientes em monetizar seu conhecimento de forma estruturada, sem depender de workshops presenciais esporádicos.

A **Inspirart Academy** resolve isso com dois pilares:

### 1. Active HUD (Head-Up Display)
Tecnologia proprietária que sincroniza metadados do equipamento (Voltagem, Modelo da Máquina, Tipo de Agulha, Velocidade) com o timestamp do vídeo. O aluno vê os ajustes técnicos mudando em tempo real na tela.

### 2. Marketplace de Conhecimento (SaaS)
Uma plataforma "Two-Sided" que conecta:
* **Área do Mestre (Instrutor):** Tatuadores experientes podem criar cursos, submeter para análise de qualidade (Diretrizes Inspirart) e monetizar seu legado.
* **Área do Aprendiz:** Acesso a conteúdo curado com gamificação e feedback técnico visual.

---

## 🛡️ Segurança & Engenharia (Enterprise Grade)

Neste projeto, a segurança não foi deixada para depois. Adotamos práticas de **AppSec** desde o primeiro Sprint:

* **Gestão de Segredos:** Uso estrito de Variáveis de Ambiente (`python-dotenv`) para proteger credenciais e Chaves Secretas. Nenhuma senha hardcoded.
* **Rate Limiting (Throttling):** Proteção ativa contra ataques de Força Bruta e DDoS na API (Login/Register), configurada via Django Rest Framework.
* **Autenticação Stateless:** JWT (JSON Web Tokens) com ciclo de vida curto e Refresh Tokens seguros.

---

## 🤖 Desenvolvimento "AI-First"

Este projeto é um case prático de **Engenharia de Software Assistida por IA**.
Atuando como Tech Lead, utilizo *Large Language Models* (LLMs) para acelerar a codificação, permitindo foco total na **Arquitetura e Regra de Negócio**.

* **Tech Lead:** Humano (Design System, Segurança, Modelagem de Dados).
* **Coding Partner:** Google Gemini (Boilerplate, Refatoração, Testes).
* **Ganho de Produtividade:** Estimativa de aceleração de 3x no ciclo de desenvolvimento dos Sprints.
---

## 🛠 Tech Stack

Arquitetura **Headless** focada em performance e escalabilidade.

### 🧠 Backend (API REST)
* **Core:** Python 3.12 + Django 5.
* **API:** Django Rest Framework (DRF).
* **Segurança:** `django-cors-headers`, `python-dotenv`, Throttling Classes.
* **Database:** PostgreSQL (Relacional).

### 🎨 Frontend (SPA)
* **Core:** React 18 + Vite.
* **Estilo:** Tailwind CSS (Inspirart Dark Theme).
* **Integração:** Axios + Interceptors.

---

## 🗺️ Roadmap (Metodologia Ágil)

###  Sprint 1: Fundação & Segurança (Concluído)
* [x] Infraestrutura Docker/Local e Banco de Dados PostgreSQL.
* [x] Autenticação JWT Completa.
* [x] **Security Hardening:** Implementação de `.env` e Rate Limiting.
* [x] Setup do Frontend "Dark Mode".

###  Sprint 2: Core Product (Em Progresso)
* [ ] **Cadastro Dual-Role:** Fluxos distintos para Aluno e Instrutor.
* [ ] **HUD Engine:** Modelagem de metadados de vídeo (`EquipmentTimestamp`).
* [ ] Player de Vídeo Sincronizado.

###  Sprint 3: Gamificação & Monetização (Planejado)
* [ ] Sistema de XP e Níveis (Aprendiz -> Mestre).
* [ ] Dashboard do Instrutor (Upload e Analytics de vendas).
* [ ] Validação de Qualidade de Conteúdo.

---

## 📦 Como Rodar Localmente

### Pré-requisitos
* **Node.js v18+**
* **Python 3.10+**
* **PostgreSQL**

### Instalação

**1. Backend**
```bash
git clone https://github.com/Guilherme-Galvao/inspirart-academy.git
cd inspirart-academy
python -m venv venv
# Ative o venv...
pip install -r requirements.txt

# ⚠️ IMPORTANTE: Crie um arquivo .env na raiz com suas credenciais:
# SECRET_KEY=sua_chave_segura
# DB_PASSWORD=sua_senha

python manage.py migrate
python manage.py runserver

2. Frontend

Bash

cd frontend
npm install
npm run dev
🤝 Autor
Guilherme Galvão Desenvolvedor Full Stack & AI-Assisted Engineer
