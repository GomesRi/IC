import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

dados_X = pd.read_excel("Apendice 2.xlsx", header=None, skiprows=1, usecols='B:AF')
dados_y = pd.read_excel("Apendice 3.xlsx", header=None, skiprows=1, usecols='B:D')

dados_X_index = ['Id', 'Objeto_1', 'Objeto_2', 'Objeto_3', 'Objeto_4', 'Objeto_5', 'Objeto_6', 'Objeto_7',
                 'Objeto_8', 'Objeto_9', 'Objeto_10', 'Objeto_11', 'Objeto_12', 'Objeto_13', 'Salario_1', 'Salario_2',
                 'Salario_3', 'Salario_4', 'Tipo', 'Tempo_1', 'Tempo_2', 'Tempo_3', 'Profissao_1', 'Profissao_2',
                 'Profissao_3', 'Profissao_4', 'Juiz_1', 'Juiz_2', 'Juiz_3', 'Dep', 'Acordo']

dados_y_index = ['Id', 'Tempo', 'Cod']

for i in range(len(dados_X_index)):
    dados_X.rename(columns={i+1: dados_X_index[i]}, inplace=True)

for j in range(len(dados_y_index)):
    dados_y.rename(columns={j+1: dados_y_index[j]}, inplace=True)

dados_X.set_index('Id', inplace=True)
dados_y.set_index('Id', inplace=True)

X = dados_X.values
y = dados_y['Tempo'].tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = SVR(C=1.0, epsilon=0.2, kernel='linear')
clf.fit(X_train, y_train)

print(clf.predict(X_test))
