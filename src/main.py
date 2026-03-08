from parser import load_instance
from heuristics import vizinho_mais_proximo

def calcular_gap(custo_encontrado, custo_otimo):
    return ((custo_encontrado - custo_otimo) / custo_otimo) * 100

def main():
    problem_data = load_instance("data/raw/brazil58.tsp")
    cidade_inicial = 1
    custo_otimo = 25395

    rota, custo_total = vizinho_mais_proximo(problem_data, cidade_inicial)
    gap = calcular_gap(custo_total, custo_otimo)

    print(f"Instância: {problem_data['name']}")
    print(f"Número de cidades: {problem_data['dimension']}")
    print(f"Cidade inicial: {cidade_inicial}")
    print(f"Custo total: {custo_total}")
    print(f"Gap para o ótimo: {gap:.2f}%")
    print(f"Tamanho da rota: {len(rota)}")


if __name__ == "__main__":
    main()