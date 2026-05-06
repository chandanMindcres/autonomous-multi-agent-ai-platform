# 🚀 Advanced Production Multi-Agent AI System

Production-ready autonomous multi-agent AI platform.

## Features
- Planner Agent
- Executor Agent
- Critic Agent
- FastAPI Backend
- Streamlit Frontend
- Docker Support
- AWS Ready
- Vector Memory

## Run Project

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
```

### Linux/Mac
```bash
source venv/bin/activate
```

### 2. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Run Backend
```bash
uvicorn main:app --reload
```

### 4. Run Frontend
```bash
cd frontend
streamlit run app.py
```

Backend:
http://127.0.0.1:8000

Frontend:
http://localhost:8501

## Docker
```bash
docker-compose up --build
```
