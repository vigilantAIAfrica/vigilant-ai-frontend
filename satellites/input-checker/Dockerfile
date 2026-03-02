FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir streamlit transformers torch  # Add transformers (and torch for ML backends)

CMD ["streamlit", "run", "main.py"]  # Assuming your file is main.py; change if not