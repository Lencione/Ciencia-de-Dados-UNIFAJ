import matplotlib.pyplot as plt
import numpy as np
import random

import pandas as pd
import time as tm
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
]

Y = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],

]

# CRIANDO A ESTRUTURA DA REDE
rover = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(450, 450), random_state=1)

# TREINAMENTO
rover.fit(X, Y)

while (True):
    s1 = int(input("Digite o sensor 1: "))
    s2 = int(input("Digite o sensor 2: "))
    s3 = int(input("Digite o sensor 3: "))
    s4 = int(input("Digite o sensor 4: "))

    aux = rover.predict([[s1, s2, s3, s4]])
    print(aux)
    for index, value in enumerate(aux[0]):
        sinal = "LIGADO" if value == 1 else "DESLIGADO"
        comp = "LED" if index == 3 else "RESISTOR " + str((index + 1))
        print(comp + " " + sinal)
