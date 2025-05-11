# 🎙 Prince’s NLP Chatbot

> A real-time, full-stack NLP-powered customer support chatbot built with Python, Flask-SocketIO, and React.

---

## 🛠️ Features

- **Real-Time Messaging**  
  Bi-directional chat powered by Flask-SocketIO and socket.io in React.

- **NLP Response Generation**  
  Plug in your favorite NLP library (spaCy, Hugging Face, or OpenAI API) in the Flask handlers to craft dynamic replies.

- **Persistent Conversation History**  
  SQLite-backed `messages` table via SQLAlchemy stores every user query and bot response for context and analytics.

- **Modular Architecture**  
  - **Backend**: Python + Flask + Flask-SocketIO  
  - **Frontend**: React with Hooks & socket.io-client  
  - **DB**: SQLite (can be switched to PostgreSQL, MySQL, etc.)

- **Easy Deployment**  
  One-click deploy to Heroku, Render, or any Docker-ready platform.

---

## 📂 Tech Stack

| Layer        | Technologies                                    |
| ------------ | ----------------------------------------------- |
| Backend      | Python, Flask, Flask-SocketIO, SQLAlchemy       |
| Frontend     | React, socket.io-client, React Hooks            |
| Database     | SQLite (via SQLAlchemy)                        |
| NLP          | Your choice: spaCy / Transformers / OpenAI API |
| Deployment   | Heroku / Render / Docker                       |

---

## ⚙️ Installation & Local Setup

1. **Fork & Clone**  
   ```bash
   git clone https://github.com/PrinceObasi/Flask-Chat-App.git
   cd Flask-Chat-App
