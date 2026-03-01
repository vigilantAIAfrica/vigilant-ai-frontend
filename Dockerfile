FROM python:3.10-slim
WORKDIR /app
RUN pip install fastapi uvicorn
RUN pip install streamlit
COPY . .
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
