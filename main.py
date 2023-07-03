import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import random

class FormatosVagao:
    RETANGULO_FECHADO = 1
    RETANGULO_ABERTO = 2
    DUPLO_RETANGULO_ABERTO = 3
    ELIPSE = 4
    LOCOMOTIVA = 5
    HEXAGONO = 6
    TOPO_DENTADO = 7
    TRAPEZIO_ABERTO = 8
    TOPO_TRIANGULAR_FECHADO = 9

class FormatosCarga:
    CIRCULO = 1
    HEXAGONO = 2
    RETANGULO = 3
    TRIANGULO = 4
    QUADRADO = 5
    LOSANGO = 6
    TRIANGULO_INVERTIDO = 7

class Direcao:
    LESTE = 1
    OESTE = -1

class Comprimento:
    CURTO = 1
    LONGO = 2

# Define os casos de treinamento
training_data = np.array([
    [
        [
            [2, 1, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, FormatosCarga.CIRCULO],
            [3, 1, Comprimento.LONGO, FormatosVagao.RETANGULO_ABERTO, FormatosCarga.HEXAGONO],
            [2, 1, Comprimento.CURTO, FormatosVagao.TOPO_TRIANGULAR_FECHADO, FormatosCarga.TRIANGULO],
            [2, 3, Comprimento.LONGO, FormatosVagao.RETANGULO_ABERTO, FormatosCarga.QUADRADO]
        ],
        [Direcao.LESTE]
    ],
    [
        [
            [2, 2, Comprimento.CURTO, FormatosVagao.RETANGULO_FECHADO, FormatosCarga.CIRCULO],
            [2, 3, Comprimento.CURTO, FormatosVagao.TRAPEZIO_ABERTO, FormatosCarga.RETANGULO],
            [2, 2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, FormatosCarga.TRIANGULO],
        ],
        [Direcao.LESTE]
    ],
    [
        [
            [3, 1, Comprimento.LONGO, FormatosVagao.RETANGULO_FECHADO, FormatosCarga.TRIANGULO_INVERTIDO],
            [2, 1, Comprimento.CURTO, FormatosVagao.HEXAGONO, FormatosCarga.TRIANGULO],
            [2, 1, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, FormatosCarga.CIRCULO],
        ],
        [Direcao.LESTE]
    ],
    [
        [
            [2, 1, Comprimento.LONGO, FormatosVagao.RETANGULO_ABERTO, FormatosCarga.RETANGULO],
            [2, 1, Comprimento.CURTO, FormatosVagao.ELIPSE, FormatosCarga.LOSANGO],
            [2, 1, Comprimento.CURTO, FormatosVagao.DUPLO_RETANGULO_ABERTO, FormatosCarga.CIRCULO],
            [2, 1, Comprimento.CURTO, FormatosVagao.TRAPEZIO_ABERTO, FormatosCarga.TRIANGULO],
        ],
        [Direcao.LESTE]
    ],
    [
        [
            [2, 1, Comprimento.CURTO, FormatosVagao.RETANGULO_FECHADO, FormatosCarga.CIRCULO],
            [3, 1, Comprimento.LONGO, FormatosVagao.RETANGULO_FECHADO, FormatosCarga.RETANGULO],
            [2, 1, Comprimento.CURTO, FormatosVagao.DUPLO_RETANGULO_ABERTO, FormatosCarga.TRIANGULO],
        ],
        [Direcao.LESTE]
    ]
], dtype=object)

def questao1():
    # Define a arquitetura da rede neural
    model = Sequential()
    model.add(Dense(20, input_shape=(None, 5), activation='relu'))  # Correção na dimensão do input_shape
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='tanh'))

    # Repete os experimentos
    num_experiments = len(training_data)
    accuracies = []

    for i in range(num_experiments):
        train_data = training_data[i]
        X_train = np.array([train_data[0]])
        y_train = np.array([train_data[1]])

        # Treina a rede neural
        model.compile(optimizer='adam', loss='mean_squared_error')
        model.fit(X_train, y_train, epochs=1000, verbose=0)

        # Testa a rede neural com o caso de teste atual
        test_data = training_data[i]
        X_test = np.array([test_data[0]])
        y_test = np.array([test_data[1]])
        prediction = model.predict(X_test)

        accuracy = 1 if (prediction[0][0] > 0 and y_test[0][0] > 0) or (prediction[0][0] < 0 and y_test[0][0] < 0) else 0
        accuracies.append(accuracy)

        print(f"Experimento {i + 1}:")
        print(f"Direção esperada: {y_test[0][0]}")
        print(f"Direção prevista: {prediction[0][0]}")
        print("-----------------------")

    # Comparação da eficácia dos testes
    total_experiments = len(accuracies)
    correct_predictions = sum(accuracies)
    accuracy_percentage = (correct_predictions / total_experiments) * 100

    print("Relatório de Eficácia:")
    print(f"Total de experimentos: {total_experiments}")
    print(f"Total de previsões corretas: {correct_predictions}")
    print(f"Acurácia: {accuracy_percentage}%")

questao1()
