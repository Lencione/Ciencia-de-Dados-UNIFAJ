import matplotlib.pyplot as plt
import numpy as np
import random

import pandas as pd
import time as tm
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Entradas
# N1, N2, N3, TEMP_OPERACIONAL, TEMP_MAX, PRESSAO_OPERACIONAL, PRESSAO_MAX
X=[
    [1,1,0,1,0,1,0],
    [1,0,0,1,0,1,0],
    [0,0,0,1,0,1,0],
    [1,1,0,0,1,1,0],
    [1,1,0,1,0,0,1],
    [1,1,1,1,0,0,1],
    [1,1,1,0,1,0,1],
    [1,1,1,1,0,1,0],


]

# SAIDAS
# ENTRADA_AGUA, SAIDA_AGUA, IGNICAO_CHAMA, VALVULA_GAS, SAIDA_VAPOR
Y=[
    [0,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,1,1,1,1],
]

# CRIANDO A ESTRUTURA DA REDE
rover = MLPClassifier(solver='lbfgs',activation='logistic', alpha=1e-8,hidden_layer_sizes=(450,450), random_state=1)

# TREINAMENTO
rover.fit(X, Y)

while(True):
    if(int(input("Deseja continuar? (1 = sim / 0 = nao)")) == 0):
        break
# N1, N2, N3, TEMP_OPERACIONAL, TEMP_MAX, PRESSAO_OPERACIONAL, PRESSAO_MAX
# ENTRADA_AGUA, SAIDA_AGUA, IGNICAO_CHAMA, VALVULA_GAS, SAIDA_VAPOR


    n1 = int(input("Agua esta acima do N1? \n(1 = sim / 0 = nao)"))
    n2 = int(input("Agua esta acima do N2? \n(1 = sim / 0 = nao)"))
    n3 = int(input("Agua esta acima do N3? \n(1 = sim / 0 = nao)"))
    temp_operacional = int(input("Temperatura em nivel operacional? \n(1 = sim / 0 = nao)"))
    temp_max = int(input("Temperatura no nivel maximo? \n(1 = sim / 0 = nao)"))
    pressao_operacional = int(input("Pressao em nivel operacional? \n(1 = sim / 0 = nao)"))
    pressao_max = int(input("Pressao no nivel maximo? \n(1 = sim / 0 = nao)"))
    aux = rover.predict([[n1,n2,n3,temp_operacional,temp_max,pressao_operacional,pressao_max]])
    print(aux)

     
