"""
Arquivo para carregar instância e retornar um dicionário com informações
organizadas para resolução do problema.
"""

import tsplib95


def load_instance(filepath):
    problem = tsplib95.load(filepath)

    nodes = list(problem.get_nodes())

    return {
    "name": problem.name,
        "dimension": problem.dimension,
        "nodes": nodes,
        "problem": problem,
    }
