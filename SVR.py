import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import regression


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

tuned_parameters = [
    {
        'kernel': ['rbf'],
        'gamma': [1e-3, 1e-4],
        'epsilon': [0.001, 0.01, 0.1, 1, 10],
        'C': [1, 10, 100, 1000]
    },
    {
        'kernel': ['linear'],
        'C': [1, 10, 100, 1000],
        'epsilon': [0.001, 0.01, 0.1, 1, 10]
    }
]

print("# Tuning hyper-parameters for precision")
print()

clf = GridSearchCV(SVR(), tuned_parameters, cv=5)
clf.fit(X_train, y_train)

print("Best parameters set found on development set:")
print()
print(clf.best_params_)
print()
print("Grid scores on development set:")
print()
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"
        % (mean, std * 2, params))
print()

print("Detailed classification report:")
print()
print("The model is trained on the full development set.")
print("The scores are computed on the full evaluation set.")
print()
y_true, y_pred = y_test, clf.predict(X_test)
print(regression.r2_score(y_true, y_pred))
print()

