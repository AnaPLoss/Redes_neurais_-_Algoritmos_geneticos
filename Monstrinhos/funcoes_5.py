import random
import matplotlib.pyplot as plt


###############################################################################
#                               Caixas binárias                               #
###############################################################################


def gene_Himmelblau():
    """Sorteia um valor para uma caixa no problema das caixas binárias"""
    
    valor_minimo = -6
    valor_maximo = 6

    gene = random.uniform(-6,6)
    return gene


def cria_candidato_Himmelblau():
    """Cria uma lista com n valores zero ou um.

    Args:
      n: inteiro que representa o número de caixas.

    """
    candidato = []
    for _ in range(2):
        gene = gene_Himmelblau()
        candidato.append(gene)
    return candidato


def populacao_Himmelblau(tamanho):
    """Cria uma população para o problema das caixas binárias.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa o número de caixas de cada indivíduo.

    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato_Himmelblau())
    return populacao


def funcao_objetivo_Himmelblau(candidato):
    """Computa a função objetivo no problema das caixas binárias

    Args:
      candidato: uma lista contendo os valores das caixas binárias do problema

    """
    x = candidato[0]
    y = candidato[1]
    
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def funcao_objetivo_pop_Himmelblau(populacao):
    """Computa a função objetivo para uma população no problema das caixas binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_Himmelblau(individuo))
    return fitness


###############################################################################
#                                   Seleção                                   #
###############################################################################

def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_uniforme(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento uniforme

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        filho1 = []
        filho2 = []

        for gene_pai, gene_mae in zip(pai, mae):
            if random.choice([True, False]):
                filho1.append(gene_pai)
                filho2.append(gene_mae)
            else:
                filho1.append(gene_mae)
                filho2.append(gene_pai)

        return filho1, filho2
    else:
        return pai, mae

###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_simples(populacao, chance_de_mutacao):
    """Realiza mutação simples

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            individuo[gene] = random.uniform(-6,6)
