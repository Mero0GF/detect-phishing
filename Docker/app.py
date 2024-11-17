import streamlit as st
import pandas as pd
import joblib  # Para carregar o modelo
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar modelo previamente treinado
modelKNN = joblib.load("KNN.pkl")
modelLogisticRegression = joblib.load("Logistic_Regression.pkl")
modelRandomForest = joblib.load("Random_Forest.pkl")

# Função de classificação
def classifyKNN(data):
    if 'is_phishing' in data.columns:
        data = data.drop(columns=['is_phishing'])
    return modelKNN.predict(data)

def classifyRandomForest(data):
    if 'is_phishing' in data.columns:
        data = data.drop(columns=['is_phishing'])
    return modelRandomForest.predict(data)

def classifyLogisticRegression(data):
    if 'is_phishing' in data.columns:
        data = data.drop(columns=['is_phishing'])
    return modelLogisticRegression.predict(data)

# Função para plotar a matriz de confusão
def plot_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Não Phishing', 'Phishing'], yticklabels=['Não Phishing', 'Phishing'])
    plt.title(f'Matriz de Confusão: {model_name}')
    plt.xlabel('Predição')
    plt.ylabel('Real')
    st.pyplot(plt)

# Função para gerar análise comparativa entre os modelos
def generate_comparative_analysis(accuracy_knn, accuracy_lr, accuracy_rf, y_true, y_pred_knn, y_pred_lr, y_pred_rf):
    st.write("### Análise Comparativa dos Modelos")
    
    st.write(f"1. **Acurácia**: O modelo com melhor desempenho em termos de acurácia foi o ", end="")
    if accuracy_knn > accuracy_lr and accuracy_knn > accuracy_rf:
        st.write(f"KNN com {accuracy_knn * 100:.2f}% de acurácia.")
    elif accuracy_lr > accuracy_knn and accuracy_lr > accuracy_rf:
        st.write(f"Regressão Logística com {accuracy_lr * 100:.2f}% de acurácia.")
    else:
        st.write(f"Random Forest com {accuracy_rf * 100:.2f}% de acurácia.")
    
    st.write("\n2. **Matriz de Confusão**: Para entender melhor os tipos de erros cometidos pelos modelos, vamos analisar suas matrizes de confusão.")
    
    # Comparação entre os modelos com base na matriz de confusão
    cm_knn = confusion_matrix(y_true, y_pred_knn)
    cm_lr = confusion_matrix(y_true, y_pred_lr)
    cm_rf = confusion_matrix(y_true, y_pred_rf)

    # Análise de falsos positivos, falsos negativos, verdadeiros positivos e verdadeiros negativos
    st.write(f"\n3. **Matriz de Confusão Detalhada**:")
    st.write(f"**KNN**:")
    st.write(f"   - Verdadeiros Positivos: {cm_knn[1, 1]}")
    st.write(f"   - Falsos Positivos: {cm_knn[0, 1]}")
    st.write(f"   - Verdadeiros Negativos: {cm_knn[0, 0]}")
    st.write(f"   - Falsos Negativos: {cm_knn[1, 0]}")
    st.write("-------------------------------------------------------------------------------------------------------")

    st.write(f"**Regressão Logística**:")
    st.write(f"   - Verdadeiros Positivos: {cm_lr[1, 1]}")
    st.write(f"   - Falsos Positivos: {cm_lr[0, 1]}")
    st.write(f"   - Verdadeiros Negativos: {cm_lr[0, 0]}")
    st.write(f"   - Falsos Negativos: {cm_lr[1, 0]}")
    st.write("-------------------------------------------------------------------------------------------------------")
    
    st.write(f"**Random Forest**:")
    st.write(f"   - Verdadeiros Positivos: {cm_rf[1, 1]}")
    st.write(f"   - Falsos Positivos: {cm_rf[0, 1]}")
    st.write(f"   - Verdadeiros Negativos: {cm_rf[0, 0]}")
    st.write(f"   - Falsos Negativos: {cm_rf[1, 0]}")
    st.write("-------------------------------------------------------------------------------------------------------")

    st.write("\n4. **Conclusão**: A escolha do melhor modelo depende de vários fatores além da acurácia, como o número de falsos positivos e falsos negativos. Um modelo com boa acurácia mas muitos falsos negativos pode ser indesejável em casos de detecção de phishing, onde queremos minimizar o número de usuários expostos a possíveis sites de phishing classificados erroneamente.")

# Configurar título de página
st.title("Classificação de Dados Tabulares")

# Exemplo de upload de dados pelo usuário
uploaded_file = st.file_uploader("Carregue um arquivo CSV para a classificação", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Dados carregados:", data.head())

    # Se houver a coluna 'is_phishing' no conjunto de dados, separamos as variáveis e os rótulos
    if 'is_phishing' in data.columns:
        X = data.drop(columns=['is_phishing'])  # Variáveis independentes
        y = data['is_phishing']  # Rótulos (variável dependente)

        # Realizar a classificação com KNN
        y_pred_knn = classifyKNN(X)
        accuracy_knn = accuracy_score(y, y_pred_knn)
        st.write("Dados classificados KNN:")
        st.write(pd.DataFrame({"Predição": y_pred_knn}))
        st.write(f"Acurácia do KNN: {accuracy_knn * 100:.2f}%")
        plot_confusion_matrix(y, y_pred_knn, 'KNN')

        # Realizar a classificação com Logistic Regression
        y_pred_lr = classifyLogisticRegression(X)
        accuracy_lr = accuracy_score(y, y_pred_lr)
        st.write("Dados classificados Logistic Regression:")
        st.write(pd.DataFrame({"Predição": y_pred_lr}))
        st.write(f"Acurácia da Regressão Logística: {accuracy_lr * 100:.2f}%")
        plot_confusion_matrix(y, y_pred_lr, 'Regressão Logística')

        # Realizar a classificação com Random Forest
        y_pred_rf = classifyRandomForest(X)
        accuracy_rf = accuracy_score(y, y_pred_rf)
        st.write("Dados classificados Random Forest:")
        st.write(pd.DataFrame({"Predição": y_pred_rf}))
        st.write(f"Acurácia do Random Forest: {accuracy_rf * 100:.2f}%")
        plot_confusion_matrix(y, y_pred_rf, 'Random Forest')

         # Análise comparativa
        generate_comparative_analysis(accuracy_knn, accuracy_lr, accuracy_rf, y, y_pred_knn, y_pred_lr, y_pred_rf)

    else:
        st.warning("O conjunto de dados não contém a coluna 'is_phishing'. Não foi possível calcular o score.")
