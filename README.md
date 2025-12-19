Inspirart Academy - Plataforma LMS High-End para Tatuadores

![Status](https://img.shields.io/badge/Status-Sprint_2_Iniciado-orange?style=for-the-badge)
![Backend](https://img.shields.io/badge/Backend-Django_REST-green?style=for-the-badge&logo=django)
![Frontend](https://img.shields.io/badge/Frontend-React_Vite-blue?style=for-the-badge&logo=react)
![AI-Powered](https://img.shields.io/badge/Dev-AI_Assisted-purple?style=for-the-badge&logo=google-gemini)

> **A Primeira Plataforma de Ensino de Tatuagem com Feedback Técnico em Tempo Real.**

---

## 📸 O Problema vs. Solução
No ensino tradicional de tatuagem online, o aluno perde a referência técnica crucial (Voltagem, Agulha, Velocidade).
A **Inspirart Academy** resolve isso com o **Active HUD**: sincronização de metadados do equipamento com o vídeo em tempo real.

## 🤖 Desenvolvimento "AI-First"
Este projeto é um case prático de **Engenharia de Software Assistida por IA**.
Utilizando *Large Language Models* (LLMs) como pares de programação, o foco do desenvolvimento deslocou-se da "escrita de código repetitivo" para a **Arquitetura, Regra de Negócio e User Experience**.

* **Tech Lead:** Humano (Decisões de Arquitetura, Review de Código, Design System).
* **Coding Partner:** Google Gemini (Geração de Boilerplate, Refatoração, Testes Unitários).
* **Ganho de Produtividade:** Estimativa de aceleração de 3x no ciclo de desenvolvimento dos Sprints.

---

## 🛠 Tech Stack & Arquitetura

Arquitetura **Headless** focada em escalabilidade.

### 🧠 Backend (API REST)
* **Framework:** Python 3.12 + Django 5 + DRF.
* **Auth:** JWT (SimpleJWT).
* **Database:** PostgreSQL.
* **Architecture:** Modular (Apps desacoplados: `courses`, `gamification`, `accounts`).

### 🎨 Frontend (SPA)
* **Core:** React 18 + Vite.
* **Style:** Tailwind CSS (Custom Dark Theme).
* **Http:** Axios + Interceptors.

---

## 🗺️ Roadmap (Metodologia Ágil)

### ✅ Sprint 1: Fundação (Concluído)
* [x] Infraestrutura Docker/Local e Banco de Dados.
* [x] Autenticação JWT Completa.
* [x] Setup do Frontend "Dark Mode".

### 🚀 Sprint 2: Core Product (Em Progresso)
* [ ] Cadastro de Usuários (Aluno/Instrutor).
* [ ] **HUD Engine:** Modelagem de metadados de vídeo (`EquipmentTimestamp`).
* [ ] Player de Vídeo Sincronizado.

### 📅 Sprint 3 & 4 (Planejado)
* [ ] Gamificação (XP, Níveis, Badges).
* [ ] Reviews Ponderados.

---

## 📦 Como Rodar Localmente

### Pré-requisitos
* **Node.js v18+** (Para rodar o Vite/React).
* **Python 3.10+** (Para o Django).
* **PostgreSQL** (Banco de dados).

### Instalação
**1. Backend**
```bash
git clone [https://github.com/seu-usuario/inspirart-academy.git](https://github.com/seu-usuario/inspirart-academy.git)
cd inspirart-academy
python -m venv venv
# Ative o venv (Windows: .\venv\Scripts\activate | Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
2. Frontend

Bash

cd frontend
npm install
npm run dev
🤝 Autor Guilherme Galvão - Desenvolvedor Full Stack & AI-Assisted Engineer

Guilherme Galvão Desenvolvedor Full Stack & AI-Assisted Engineer

LinkedIn | Portfólio
