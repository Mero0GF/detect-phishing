FROM python:3.10

WORKDIR /app

# Mudar ára os nomes dos arquivos
COPY app.py .
COPY KNN.pkl .
COPY Logistic_Regression.pkl .
COPY Random_Forest.pkl .

# Instala Streamlit e outras dependências necessárias
RUN pip install streamlit pandas joblib scikit-learn seaborn matplotlib

# Usar esta porta no navegador
EXPOSE 8501

# Comando para iniciar o streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]