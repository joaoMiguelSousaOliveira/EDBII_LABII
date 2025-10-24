import os
import sys

# Adiciona o diretório raiz ao path para permitir importações diretas de 'src'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.arvore_avl import ArvoreAVL
from src.arvore_rn import ArvoreRubroNegra


class TerminalUI:
    """Classe para gerenciar a estética da interface no terminal"""
    
    # Cores ANSI
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    AMARELO = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    @staticmethod
    def limpar_tela():
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def header(texto: str):
        """Exibe um cabeçalho formatado"""
        TerminalUI.limpar_tela()
        print(f"{TerminalUI.AZUL}{TerminalUI.BOLD}╔{"═" * (len(texto) + 2)}╗{TerminalUI.RESET}")
        print(f"{TerminalUI.AZUL}{TerminalUI.BOLD}║ {texto} ║{TerminalUI.RESET}")
        print(f"{TerminalUI.AZUL}{TerminalUI.BOLD}╚{"═" * (len(texto) + 2)}╝{TerminalUI.RESET}")

    @staticmethod
    def prompt(texto: str) -> str:
        """Exibe um prompt de entrada formatado"""
        return input(f"{TerminalUI.AMARELO}► {texto}{TerminalUI.RESET}")

    @staticmethod
    def sucesso(texto: str):
        """Exibe uma mensagem de sucesso"""
        print(f"{TerminalUI.VERDE}✓ {texto}{TerminalUI.RESET}")

    @staticmethod
    def erro(texto: str):
        """Exibe uma mensagem de erro"""
        print(f"{TerminalUI.VERMELHO}✗ {texto}{TerminalUI.RESET}")


def obter_valor_int(prompt: str) -> int | None:
    """Solicita um valor inteiro ao usuário e trata exceções"""
    try:
        return int(TerminalUI.prompt(prompt))
    except (ValueError, TypeError):
        TerminalUI.erro("Por favor, digite um número inteiro válido")
        return None

def inserir_elemento(arvore):
    """Lida com a inserção de um elemento na árvore"""
    valor = obter_valor_int("Digite o valor a ser inserido: ")
    if valor is not None:
        arvore.inserir(valor)
        TerminalUI.sucesso(f"Valor {valor} inserido na árvore")

def remover_elemento(arvore):
    """Lida com a remoção de um elemento da árvore"""
    valor = obter_valor_int("Digite o valor a ser removido: ")
    if valor is not None:
        if arvore.remover(valor):
            TerminalUI.sucesso(f"Valor {valor} removido da árvore")
        else:
            TerminalUI.erro(f"Valor {valor} não encontrado")

def buscar_elemento(arvore):
    """Lida com a busca de um elemento na árvore"""
    valor = obter_valor_int("Digite o valor a ser buscado: ")
    if valor is not None:
        if arvore.buscar(valor):
            TerminalUI.sucesso(f"Valor {valor} encontrado na árvore")
        else:
            TerminalUI.erro(f"Valor {valor} não encontrado")

def mostrar_arvore(arvore, tipo_nome):
    """Exibe a estrutura da árvore de forma mais estética"""
    TerminalUI.header(f"ESTRUTURA DA {tipo_nome}")
    arvore.imprimir()
    input(f"\n{TerminalUI.AMARELO}Pressione Enter para continuar...{TerminalUI.RESET}")

def mostrar_informacoes(arvore):
    """Exibe informações detalhadas sobre a árvore"""
    TerminalUI.header("INFORMAÇÕES DA ÁRVORE")
    tamanho = arvore.obter_tamanho()
    print(f"- Quantidade de nós: {tamanho}")
    print(f"- Árvore está vazia: {'Sim' if tamanho == 0 else 'Não'}")
    if tamanho > 0:
        elementos = arvore.em_ordem()
        print(f"- Elementos (em ordem): {elementos}")
    input(f"\n{TerminalUI.AMARELO}Pressione Enter para continuar...{TerminalUI.RESET}")

def limpar_arvore(arvore, tipo):
    """Recria a árvore, efetivamente limpando-a"""
    confirmacao = TerminalUI.prompt("Tem certeza que deseja limpar a árvore? (s/n): ").lower()
    if confirmacao == 's':
        TerminalUI.sucesso("Árvore limpa")
        return ArvoreAVL() if tipo == "1" else ArvoreRubroNegra()
    else:
        TerminalUI.erro("Operação cancelada")
        return arvore

def escolher_arvore():
    """Permite ao usuário escolher o tipo de árvore a ser usada"""
    TerminalUI.header("IMPLEMENTAÇÃO DE ÁRVORES BALANCEADAS")
    print("1. Árvore AVL")
    print("2. Árvore Rubro-Negra")
    
    while True:
        tipo = TerminalUI.prompt("Escolha o tipo de árvore (1 ou 2): ")
        if tipo in ["1", "2"]:
            return (ArvoreAVL(), "ÁRVORE AVL") if tipo == "1" else (ArvoreRubroNegra(), "ÁRVORE RUBRO-NEGRA")
        TerminalUI.erro("Opção inválida! Tente novamente")

def main():
    """Função principal que gerencia o menu e a interação com o usuário"""
    arvore, tipo_nome = escolher_arvore()
    
    # Mapeamento de opções para funções
    acoes = {
        "1": lambda: inserir_elemento(arvore),
        "2": lambda: remover_elemento(arvore),
        "3": lambda: buscar_elemento(arvore),
        "4": lambda: mostrar_arvore(arvore, tipo_nome),
        "5": lambda: mostrar_informacoes(arvore),
    }

    while True:
        TerminalUI.header(f"MENU PRINCIPAL - {tipo_nome}")
        print("1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Buscar elemento")
        print("4. Mostrar árvore")
        print("5. Mostrar informações")
        print("6. Limpar árvore")
        print("0. Sair")
        
        opcao = TerminalUI.prompt("Escolha uma opção: ")

        if opcao == "0":
            print("\nSaindo do programa. Até mais!")
            break
        
        acao = acoes.get(opcao)
        if acao:
            acao()
        elif opcao == "6":
            arvore = limpar_arvore(arvore, "1" if isinstance(arvore, ArvoreAVL) else "2")
        else:
            TerminalUI.erro("Opção inválida!")
        
        if opcao in ["1", "2", "3", "6"]:
            input(f"\n{TerminalUI.AMARELO}Pressione Enter para continuar...{TerminalUI.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperação interrompida pelo usuário. Saindo...")