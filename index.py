# Calculadora de partidas Rankeadas
# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões
# - Funções

# Objetivo:

# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
# depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito
# através do calculo (vitórias - derrotas)

def calcular_nivel(vitorias, derrotas):

    # Calcula o saldo de vitórias

    saldoRankeadas = vitorias - derrotas

    # Estrutura de decisão para determinar o nível

    if vitorias <= 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    elif vitorias >= 101:
        nivel = "Imortal"
    else:
        nivel = "Indefinido"
    return saldoRankeadas, nivel

# Laço de repetição para múltiplos jogadores

num_jogadores = int(input("Digite o número de jogadores para calcular o nível: "))
for i in range(num_jogadores):
    print(f"\nJogador {i+1}:")

    # Variáveis para armazenar vitórias e derrotas

    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))
    saldoRankeadas, nivel = calcular_nivel(vitorias, derrotas)

    # Exibe o resultado formatado

    print(f"O Herói tem de saldo de {saldoRankeadas} está no nível de {nivel}")