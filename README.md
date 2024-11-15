# Detecção de Phishing com Machine Learning  
  
# Visão Geral

Este projeto explora a utilização de algoritmos de machine learning para a detecção automatizada de sites de phishing, com base em características extraídas de URLs e conteúdo das páginas. O estudo compara os desempenhos de três algoritmos: Regressão Logística, K-Nearest Neighbors (KNN) e Random Forest, usando um dataset que contém 5.780 amostras, sendo 578 de sites phishing e 5.000 de sites legítimos. 
  
# Datasets  
Para o projeto coletamos dados do site Zenodo (Link: https://zenodo.org/records/8041387 ). Nele são apresentados diveros datasets separados em phishing e não phishing (legitimos).
Nós análisamos e selecionamos dois datasets, um com 5000 casos de phishing e outro com 5000 casos legitimos, ambos com as mesmas colunas (valores).  
Os datasets baixados foram o *not-phishing.csv* e *phishing.csv*

O tratamento dos dados está descrito no artigo.  
  
# Algoritmos Utilizados  
  
Regressão Logística: Modelo simples e interpretável para classificação binária.  
K-Nearest Neighbors (KNN): Algoritmo baseado em instâncias que classifica com base na proximidade de vizinhos.  
Random Forest: Modelo de ensemble que utiliza múltiplas árvores de decisão para melhorar a precisão.  

# Resultados  
  
KNN e Regressão Logística tiveram boa acurácia para sites legítimos, mas dificuldades em identificar phishing, com altos falsos negativos.  
Random Forest teve melhor desempenho na detecção de phishing, com menos falsos negativos, mas mais falsos positivos.  
  
# Conclusão  
   
O modelo Random Forest é o mais eficaz para detectar phishing, embora com um custo maior de falsos positivos, o que é aceitável para segurança, pois falsos negativos são mais prejudiciais.   

# Informações Adicionais 
Mais detalhes sobre o projeto estão no artigo "Detecção de Sites Phishing com Machine Learning_ Uma Abordagem Baseada em Análise de Dados de Sites Autênticos e Maliciosos".  
  
Também disponibilizamos um .ipynb, com os codigos organizados para melhor visualização das informações, sendo uma versão extra sobre os códigos presentes no Docker do projeto.  
  
