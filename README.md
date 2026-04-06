# 🎓 Intucate Case Study: Backend API
> A robust Flask-based Educational Assistant API integrated with MongoDB Atlas for dynamic prompt management and request tracking.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://www.postman.com/)

---

## 🚀 Overview
This project demonstrates a production-ready backend architecture for an AI-driven educational tool. It features dynamic template retrieval from a cloud database, asynchronous batch processing capabilities, and secure environment configuration.

### ✨ Key Features
- **Dynamic Prompting**: Fetches expert-curated templates from MongoDB Atlas.
- **Request Logging**: Automatically stores every interaction in a `history` collection for audit and analytics.
- **Async Processing**: Implements `asyncio` for high-performance batch request handling.
- **Secure Architecture**: Utilizes `.env` masking for sensitive API credentials and database URIs.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **Framework** | Flask (WSGI Server) |
| **Database** | MongoDB Atlas (NoSQL Cloud) |
| **Libraries** | PyMongo, Python-Dotenv, Asyncio |

---

## 📂 Project Structure
```text
case-study/
├── app.py              # Main Application Logic
├── .env                # Environment Variables (Ignored by Git)
├── .gitignore          # Security rules for Git
├── requirements.txt    # Project Dependencies
└── README.md           # Documentation
