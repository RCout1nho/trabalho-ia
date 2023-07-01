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


# Função para converter os dados dos trens em formato numérico
def converter_dados(trem):
    direcao_numerica = 1 if trem.direcao == Direcao.LESTE else -1

    vagoes_numerico = []
    for vagao in trem.vagoes:
        vagoes_numerico.append([
            vagao.eixos,
            vagao.comprimento,
            vagao.formato,
            vagao.qtd_cargas,
            vagao.formato_carga
        ])

    return vagoes_numerico, direcao_numerica

# Função para resolver a questão 1
def questao1(numMAX_Leste):
    # Definição dos trens de treinamento
    trens_treinamento = [
        # Trens indo para leste
        Trem(4, 4, [
            Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.CIRCULO),
            Vagao(3, Comprimento.LONGO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.HEXAGONO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.TOPO_TRIANGULAR_FECHADO, 1, FormatosCarga.TRIANGULO),
            Vagao(2, Comprimento.LONGO, FormatosVagao.RETANGULO_ABERTO, 3, FormatosCarga.QUADRADO),
        ], Direcao.LESTE),

        Trem(3, 3, [
            Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_FECHADO, 2, FormatosCarga.CIRCULO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.TRAPEZIO_ABERTO, 1, FormatosCarga.RETANGULO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.TRIANGULO),
        ], Direcao.LESTE),

        Trem(3, 3, [
            Vagao(3, Comprimento.LONGO, FormatosVagao.RETANGULO_FECHADO, 1, FormatosCarga.TRIANGULO_INVERTIDO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.HEXAGONO, 1, FormatosCarga.TRIANGULO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.CIRCULO),
        ], Direcao.LESTE),

        Trem(4, 3, [
            Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_ABERTO, 1, FormatosCarga.RETANGULO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.ELIPSE, 1, FormatosCarga.LOSANGO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.DUPLO_RETANGULO_ABERTO, 1, FormatosCarga.TRIANGULO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.TRAPEZIO_ABERTO, 1, FormatosCarga.TRIANGULO),
        ], Direcao.LESTE),

        Trem(3, 3, [
            Vagao(2, Comprimento.CURTO, FormatosVagao.RETANGULO_FECHADO, 1, FormatosCarga.CIRCULO),
            Vagao(3, Comprimento.LONGO, FormatosVagao.RETANGULO_FECHADO, 1, FormatosCarga.RETANGULO),
            Vagao(2, Comprimento.CURTO, FormatosVagao.DUPLO_RETANGULO_ABERTO, 1, FormatosCarga.TRIANGULO),
        ], Direcao.LESTE),
    ]

    acuracias = []

    for i in range(1, numMAX_Leste + 1):
        # Seleciona os casos para treinamento e teste
        casos_treinamento = []
        casos_teste = []

        for trem in trens_treinamento:
            vagoes_numerico, direcao_numerica = converter_dados(trem)

            if direcao_numerica == Direcao.LESTE:
                casos_treinamento.append([vagoes_numerico, direcao_numerica])
            else:
                casos_teste.append([vagoes_numerico, direcao_numerica])

        # Calcula a acurácia
        acuracia = len(casos_teste) / numMAX_Leste
        acuracias.append(acuracia)

    return acuracias

# Teste da função questao1
acuracias = questao1(5)
print(acuracias)
