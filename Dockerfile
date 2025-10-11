FROM python:3.11-slim

WORKDIR /app

# copy dependencies
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# copy source code
COPY app/ .

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
