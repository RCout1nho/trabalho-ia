import numpy as np
from tensorflow import keras

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

class Vagao:
    def __init__(self, eixos: int, comprimento: Comprimento, formato: FormatosVagao, qtd_cargas: int, formato_carga: FormatosCarga):
        self.eixos = eixos # entre 2 e 3
        self.comprimento = comprimento # objeto da classe Comprimento
        self.formato = formato # atributo da classe FormatosVagao
        self.qtd_cargas = qtd_cargas # entre 0 e 3
        self.formato_carga = formato_carga # atribudo da class FormatosCarga

        self.retangulo_proximo_retangulo = False
        self.retangulo_proximo_triangulo = False
        self.retangulo_proximo_hexagono = False
        self.retangulo_proximo_circulo = False
        self.triangulo_proximo_triangulo = False
        self.triangulo_proximo_hexagono = False
        self.triangulo_proximo_circulo = False
        self.circulo_proximo_circulo = False

class Trem:
    def __init__(self, qtd_vagoes: int, qtd_cargas_dif: int, vagoes, direcao: Direcao):
        self.qtd_vagoes = qtd_vagoes # entre 3 e 5
        self.qtd_cargas_dif = qtd_cargas_dif # entre 1 e 4
        self.vagoes = vagoes # objeto da classe Vagao
        self.direcao = direcao


# Trens de treinamento
# Trens indo para leste
tremL1 = Trem(4, 4, [
    Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.CIRCULO),
    Vagao(3, Comprimento.LONGO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.HEXAGONO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.TOPO_TRIANGULAR_FECHADO, 1, FormatosCarga.TRIANGULO),
    Vagao(2, Comprimento.LONGO, FormatosVagao.RETANGULO_ABERTO, 3, FormatosCarga.QUADRADO),
], Direcao.LESTE)

tremL2 = Trem(3, 3, [
    Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_FECHADO, 2, FormatosCarga.CIRCULO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.TRAPEZIO_ABERTO, 1, FormatosCarga.RETANGULO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.TRIANGULO),
], Direcao.LESTE)

tremL3 = Trem(3, 3, [
    Vagao(3, Comprimento.LONGO, FormatosVagao.RETANGULO_FECHADO, 1, FormatosCarga.TRIANGULO_INVERTIDO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.HEXAGONO, 1, FormatosCarga.TRIANGULO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.CIRCULO),
], Direcao.LESTE)

tremL4 = Trem(4, 3, [
    Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.RETANGULO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.ELIPSE, 1, FormatosCarga.LOSANGO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.DUPLO_RETANGULO_ABERTO, 1, FormatosCarga.TRIANGULO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.TRAPEZIO_ABERTO, 1, FormatosCarga.TRIANGULO),
], Direcao.LESTE)

tremL5 = Trem(3, 3, [
    Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_FECHADO, 1, FormatosCarga.CIRCULO),
    Vagao(3, Comprimento.LONGO, FormatosVagao.RETANGULO_FECHADO, 1, FormatosCarga.RETANGULO),
    Vagao(2, Comprimento.CURTO, FormatosVagao.DUPLO_RETANGULO_ABERTO, 1, FormatosCarga.TRIANGULO),
], Direcao.LESTE)


def converter_dados(trem: Trem):
    # Converter a direção para -1 (oeste) ou 1 (leste)
    direcao_numerica = trem.direcao

    # Converter os atributos de cada vagão em uma lista de valores numéricos
    vagoes_numerico = []
    for vagao in trem.vagoes:
        vagoes_numerico.append([
            vagao.eixos,
            vagao.comprimento,
            vagao.formato,
            vagao.qtd_cargas,
            vagao.formato_carga
        ])

    # Retornar a lista de vagoes numericos e a direção numerica
    return vagoes_numerico, direcao_numerica


# Converter os dados para o formato numérico
vagoes_numerico_L1, direcao_numerica_L1 = converter_dados(tremL1)
vagoes_numerico_L2, direcao_numerica_L2 = converter_dados(tremL2)
vagoes_numerico_L3, direcao_numerica_L3 = converter_dados(tremL3)
vagoes_numerico_L4, direcao_numerica_L4 = converter_dados(tremL4)
vagoes_numerico_L5, direcao_numerica_L5 = converter_dados(tremL5)

# Concatenar as amostras de trem
vagoes_numerico = np.concatenate((vagoes_numerico_L1, vagoes_numerico_L2, vagoes_numerico_L3, vagoes_numerico_L4, vagoes_numerico_L5))
direcao_numerica = [direcao_numerica_L1, direcao_numerica_L2, direcao_numerica_L3, direcao_numerica_L4, direcao_numerica_L5]

# Convertendo para arrays numpy
vagoes_numerico = np.array(vagoes_numerico)
direcao_numerica = np.array(direcao_numerica)

# Imprimir os dados convertidos
print("Vagoes numéricos:")
print(vagoes_numerico)
print("Direção numérica:")
print(direcao_numerica)
