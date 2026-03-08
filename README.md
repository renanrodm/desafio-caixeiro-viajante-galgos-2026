# Desafio – Problema do Caixeiro Viajante (TSP)

## Descrição do problema

O Problema do Caixeiro Viajante (Travelling Salesman Problem – TSP) consiste em encontrar a rota de menor custo que visita um conjunto de cidades exatamente uma vez e retorna à cidade inicial.

Formalmente, dado um conjunto de cidades e os custos de deslocamento entre cada par de cidades, o objetivo é determinar um ciclo Hamiltoniano de custo mínimo.

Neste projeto utilizamos a instância **brazil58** da biblioteca **TSPLIB**, composta por **58 cidades** e uma matriz explícita de custos entre os nós.

---

## Abordagem adotada

A solução implementada utiliza a heurística **Vizinho Mais Próximo (Nearest Neighbor)**.

Essa heurística é um algoritmo guloso que constrói a rota iterativamente:

1. Escolhe uma cidade inicial.
2. Entre todas as cidades ainda não visitadas, seleciona a cidade com menor custo de deslocamento a partir da cidade atual.
3. Atualiza a rota e marca a cidade como visitada.
4. Repete o processo até visitar todas as cidades.
5. Ao final, retorna à cidade inicial para fechar o ciclo.

---

## Estrutura do projeto

```
.
├── data/
│   └── raw/
│       └── brazil58.tsp
├── src/
│   ├── parser.py
│   ├── heuristics.py
│   └── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

### parser.py

Responsável por carregar a instância TSPLib e retornar um dicionário com as informações necessárias para o algoritmo.

### heuristics.py

Contém a implementação da heurística **vizinho mais próximo**, responsável por construir a rota e calcular seu custo.

### main.py

Arquivo responsável por executar o programa, calcular métricas e exibir os resultados.

---

## Dependências

O projeto utiliza as seguintes bibliotecas:

- Python 3.10+
- tsplib95

Instalação das dependências:

```bash
pip install tsplib95
```

---

## Como rodar o projeto

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd desafio-caixeiro-viajante
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

Ative o ambiente virtual.

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python src/main.py
```

---

## Resultados obtidos

Executando o algoritmo com a cidade inicial **1**, obtivemos:

| Instância | Método | Cidade inicial | Custo obtido |
|----------|-------|---------------|-------------|
| brazil58 | Vizinho mais próximo | 1 | 28429 |

O valor ótimo conhecido para a instância **brazil58** é:

```
25395
```

Diferença percentual aproximada:

```
≈ 11.95%
```

---

## Uso de Inteligência Artificial

Ferramentas de Inteligência Artificial foram utilizadas como **apoio ao desenvolvimento do projeto**, principalmente para:

- esclarecimento de conceitos relacionados ao Problema do Caixeiro Viajante (TSP);
- discussão de estratégias de implementação da heurística do **Vizinho Mais Próximo**;
- auxílio na organização da estrutura do projeto;
- revisão e melhoria da documentação do README.

A implementação do algoritmo, entendimento do funcionamento da heurística e validação dos resultados foram realizados manualmente, garantindo compreensão completa da solução proposta.

A IA foi utilizada como **ferramenta de suporte**, semelhante à consulta de documentação técnica ou materiais de estudo.

## Discussão sobre limitações

A heurística do vizinho mais próximo possui algumas limitações:

- O resultado depende da **cidade inicial escolhida**.
- O algoritmo faz decisões **locais**, o que pode levar a soluções subótimas.
- Não possui mecanismo de melhoria posterior da rota.

Mesmo assim, o método é útil como solução inicial ou como base para heurísticas mais avançadas.


## Referências

- TSPLIB: http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/