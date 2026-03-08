"""
Pergunta chave: Entre todas as cidades que faltam e/ou não foram visitadas, qual é a mais barata de alcançar a partir da minha cidade atual?

1 -> Qual é a cidade atual;
2 -> Quais cidades ainda não foram visitadas;
3 -> Qual é o custo de ir da cidade atual para cidade candidata;


Etapa 1: 

Escolher cidade inicial. [1]
rota atual: [1]
visitadas: [1]
atual: 1

Etapa 2:

Consultar cidades candidatas;

Etapa 3: Consultar os custos a partir da cidade atual;

Etapa 4: Localizar o menor custo

Ao localizar o menor custo, definimos:

Ex: 1 -> 17; 
rota [1, 17]
visitadas: [1, 17]
atual: 17

Etapa 5:

Ciclo se repete até o fim do arquivo.

"""
from parser import load_instance

problem_data = load_instance("data/raw/brazil58.tsp")


def vizinho_mais_proximo(problem_data, cidade_inicial):
    
    tsp_problem = problem_data["problem"]
    nodes = problem_data["nodes"]
    cidades_candidatas = set(nodes)

    rota = [cidade_inicial]
    cidades_candidatas.remove(cidade_inicial)
    cidade_atual = cidade_inicial
    custo_total = 0


    while cidades_candidatas:
        melhor_cidade = None
        menor_custo = None
        
        for cidade_cadidata in cidades_candidatas:
            custo = tsp_problem.get_weight(cidade_atual, cidade_cadidata)

            if menor_custo is None or custo < menor_custo:
                menor_custo = custo
                melhor_cidade = cidade_cadidata
        
        rota.append(melhor_cidade)
        cidades_candidatas.remove(melhor_cidade)
        cidade_atual = melhor_cidade
        custo_total += menor_custo

    rota.append(cidade_inicial) #Considerando a volta para cidade de origem;
    custo_total += custo_total + tsp_problem.get_weight(cidade_atual, cidade_inicial) #Somando o custo da volta para cidade de origem;
    return rota, custo_total







