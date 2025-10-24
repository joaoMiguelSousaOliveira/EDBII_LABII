# Implementação de Árvores Balanceadas: AVL e Rubro-Negra

Este projeto oferece uma implementação em Python das árvores de busca binária auto-balanceáveis AVL e Rubro-Negra, incluindo uma interface de linha de comando (CLI) para interagir com as estruturas de dados.

## 🌳 Estruturas de Dados

- **Árvore AVL:** Uma árvore de busca binária que se auto-balanceia. A diferença de altura entre as sub-árvores de qualquer nó (fator de balanceamento) é no máximo 1.
- **Árvore Rubro-Negra:** Outra árvore de busca binária auto-balanceável que utiliza cores (vermelho ou preto) nos nós para garantir que o caminho mais longo da raiz até uma folha não seja mais que o dobro do caminho mais curto.

Ambas as estruturas garantem que operações como inserção, remoção e busca tenham uma complexidade de tempo de **O(log n)** no pior caso.

## 🚀 Começando

Siga as instruções abaixo para executar o projeto localmente.

### Pré-requisitos

- Python 3.10+

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   # No Windows, use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Executando a Aplicação

Para iniciar a interface de linha de comando, execute o `main.py`:

```bash
python3 main.py
```

O programa solicitará que você escolha entre a Árvore AVL e a Árvore Rubro-Negra e, em seguida, apresentará um menu para realizar as seguintes operações:
- Inserir, remover e buscar elementos.
- Exibir a árvore e suas informações (tamanho, elementos em ordem, etc.).
- Limpar a árvore.

### Executando os Testes

O projeto utiliza `pytest` para testes unitários. Para executá-los, rode o seguinte comando na raiz do projeto:

```bash
pytest
```

Os testes validam a funcionalidade de inserção, busca, remoção e a integridade estrutural de ambas as árvores.

## 📁 Estrutura do Projeto

```
.
├── src/
│   ├── arvore_avl.py         # Implementação da Árvore AVL
│   └── arvore_rn.py          # Implementação da Árvore Rubro-Negra
├── tests/
│   └── test_arvores.py       # Testes unitários para as árvores
├── .gitignore
├── main.py                   # CLI para interagir com as árvores
├── README.md
└── requirements.txt
```