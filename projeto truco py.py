class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"
    


baralho = []
naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
valores= ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']
for valor in valores:
 for naipe in naipes:
    carta = Carta(valor, naipe)
    baralho.append(carta)
    
#for carta in baralho:
    #print(carta)
    
import itertools
import random
def criar_baralho():
    naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
    valores = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']

    baralho = [{'valor': valor, 'naipe': naipe}for valor, naipe in itertools.product(valores, naipes)]
    return baralho

baralho_completo = criar_baralho()

def embaralhar_baralho(baralho):
    random.shuffle(baralho)
    return baralho

baralho_embaralhado = embaralhar_baralho(baralho_completo)

def criar_baralho():
    naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
    valores = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']
    baralho = [(valor, naipe)for valor in valores for naipe in naipes]
    return baralho

def distribuir_cartas(baralho, num_jogadores, cartas_por_jogador):
    random.shuffle(baralho)

    jogadores = {f'jogador {i+1}' : [] for i in range(num_jogadores)}

    for _ in range (cartas_por_jogador):
        for jogador in jogadores:
            carta = baralho.pop()
            jogadores[jogador].append(carta)
    return jogadores

def exibir_mao(jogador, mao):
    print(f'{jogador}: {", ".join([f"{valor} de {naipe}" for valor, naipe in mao])}')

baralho = criar_baralho()
num_jogadores = 2
cartas_por_jogador = 3
maos = distribuir_cartas(baralho, num_jogadores, cartas_por_jogador)
for jogador, mao in maos.items():
    exibir_mao(jogador, mao)
