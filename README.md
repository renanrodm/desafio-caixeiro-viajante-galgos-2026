# Desafio: Problema do Caixeiro Viajante (TSP)

## Descricao do problema

O Problema do Caixeiro Viajante (TSP) busca a rota de menor custo que visita cada cidade exatamente uma vez e retorna para a cidade inicial.

Neste projeto, a instancia usada e `brazil58` (TSPLIB), com 58 cidades.

## Abordagem adotada

A solucao implementa a heuristica **Vizinho Mais Proximo**:

1. Comeca em uma cidade inicial (atualmente `1`).
2. Escolhe a cidade nao visitada com menor custo a partir da cidade atual.
3. Repete ate visitar todas as cidades.
4. Retorna para a cidade inicial.

Arquivos principais:

- `src/main.py`: execucao do programa e calculo do gap para o otimo conhecido.
- `src/parser.py`: leitura da instancia `.tsp` com `tsplib95`.
- `src/heuristics.py`: implementacao da heuristica.

## Como rodar o projeto (simples)

### 1) Criar e ativar ambiente virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3) Executar

```bash
python src/main.py
```

## Dependencias

- Python 3.10+
- Pacotes em `requirements.txt` (principal: `tsplib95`)

## Resultados obtidos

Resultado de execucao com cidade inicial `1`:

- Instancia: `brazil58`
- Numero de cidades: `58`
- Custo total encontrado: `28429`
- Custo otimo conhecido: `25395`
- Gap: `11.95%`
- Tamanho da rota (com retorno): `59`

## Discussao sobre limitacoes e possiveis melhorias

Limitacoes:

- O resultado depende da cidade inicial.
- A heuristica e gulosa e pode ficar longe do otimo global.
- Nao ha etapa de refinamento da rota apos a construcao inicial.

Possiveis melhorias:

- Testar multiplas cidades iniciais e escolher o melhor resultado.


## Uso de IA generativa

Usei IA generativa como apoio para:

- revisar estrutura e clareza do README;
- discutir apresentacao da heuristica;
- revisar texto e organizacao da documentacao.

A implementacao do algoritmo, validacao da execucao e interpretacao dos resultados foram feitas manualmente.
