import matplotlib.pyplot as plt
import numpy as np
import random

import pandas as pd
import time as tm
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# ENTRADAS
# s1,s2,s3,t1,t2
X=[
    [1,1,1],
    [1,1,0],
]

# SAIDAS
# VALVULA
Y=[
    [1],
    [0],
]

# CRIANDO A ESTRUTURA DA REDE
rover = MLPClassifier(solver='lbfgs',activation='logistic', alpha=1e-8,hidden_layer_sizes=(20,20), random_state=1)

# TREINAMENTO
rover.fit(X, Y)

while(True):
    if(int(input("Deseja continuar? (1 = sim / 0 = nao)")) == 0):
        break
# s1,s2,s3
# ENTRADA_AGUA, SAIDA_AGUA, IGNICAO_CHAMA, VALVULA_GAS, SAIDA_VAPOR

    S1 = int(input("Agua esta acima do S1? \n(1 = sim / 0 = nao)"))
    S2 = int(input("Agua esta acima do S2? \n(1 = sim / 0 = nao)"))
    S3 = int(input("Agua esta acima do S3? \n(1 = sim / 0 = nao)"))
    aux = rover.predict([[S1,S2,S3]])
    print(aux)
