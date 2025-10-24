class NoAVL:
    """Nó da árvore AVL com valor, altura e referências"""
    
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None  # Referência ao filho esquerdo
        self.direita = None   # Referência ao filho direito
        self.altura = 1       # Altura do nó (para balanceamento)

class ArvoreAVL_Principal:
    """Implementação de árvore AVL com balanceamento automático"""

    def __init__(self):
        self.raiz = None
        
    def altura(self, no):
        """Retorna a altura do nó ou 0 se for None"""
        return 0 if no is None else no.altura
    
    def fator_balanceamento(self, no):
        """Calcula o fator de balanceamento do nó"""
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)
    
    def rotacao_direita(self, no_desbalanceado):
        """Executa rotação simples à direita"""
        if no_desbalanceado is None or no_desbalanceado.esquerda is None:
            return no_desbalanceado
            
        novo_pai = no_desbalanceado.esquerda
        subarvore_movida = novo_pai.direita

        novo_pai.direita = no_desbalanceado
        no_desbalanceado.esquerda = subarvore_movida

        # Atualiza alturas
        no_desbalanceado.altura = 1 + max(
            self.altura(no_desbalanceado.esquerda),
            self.altura(no_desbalanceado.direita)
        )
        novo_pai.altura = 1 + max(
            self.altura(novo_pai.esquerda),
            self.altura(novo_pai.direita)
        )

        return novo_pai

    def rotacao_esquerda(self, no_desbalanceado):
        """Executa rotação simples à esquerda"""
        if no_desbalanceado is None or no_desbalanceado.direita is None:
            return no_desbalanceado
            
        novo_pai = no_desbalanceado.direita
        subarvore_movida = novo_pai.esquerda

        novo_pai.esquerda = no_desbalanceado
        no_desbalanceado.direita = subarvore_movida

        # Atualiza alturas
        no_desbalanceado.altura = 1 + max(
            self.altura(no_desbalanceado.esquerda),
            self.altura(no_desbalanceado.direita)
        )
        novo_pai.altura = 1 + max(
            self.altura(novo_pai.esquerda),
            self.altura(novo_pai.direita)
        )

        return novo_pai

    # Interface: inserir(raiz, valor) -> retorna (sub)raiz
    def inserir(self, raiz, valor):
        if raiz is None:
            return NoAVL(valor)
        if valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.inserir(raiz.direita, valor)
        else:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        fb = self.fator_balanceamento(raiz)

        # LL
        if fb > 1 and raiz.esquerda is not None and valor < raiz.esquerda.valor:
            return self.rotacao_direita(raiz)
        # RR
        if fb < -1 and raiz.direita is not None and valor > raiz.direita.valor:
            return self.rotacao_esquerda(raiz)
        # LR
        if fb > 1 and raiz.esquerda is not None and valor > raiz.esquerda.valor:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        # RL
        if fb < -1 and raiz.direita is not None and valor < raiz.direita.valor:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def buscar(self, raiz, chave):
        if raiz is None:
            return None
        if chave == raiz.valor:
            return raiz
        if chave < raiz.valor:
            return self.buscar(raiz.esquerda, chave)
        return self.buscar(raiz.direita, chave)

    def mostrar_arvore(self, no, prefixo="", is_esq=True):
        if no is not None:
            print(prefixo + ("└── " if is_esq else "┌── ") + str(no.valor))
            if no.esquerda is not None or no.direita is not None:
                novo_prefixo = prefixo + ("    " if is_esq else "│   ")
                self.mostrar_arvore(no.direita, novo_prefixo, False)
                self.mostrar_arvore(no.esquerda, novo_prefixo, True)

    def minimo_no(self, nodo):
        atual = nodo
        while atual is not None and atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def remover(self, raiz, valor):
        if raiz is None:
            return None

        if valor < raiz.valor:
            raiz.esquerda = self.remover(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.remover(raiz.direita, valor)
        else:
            # nó com 0 ou 1 filho
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda
            # nó com 2 filhos: pega sucessor (mínimo da direita)
            temp = self.minimo_no(raiz.direita)
            raiz.valor = temp.valor
            raiz.direita = self.remover(raiz.direita, temp.valor)

        # se sub-árvore ficou vazia
        if raiz is None:
            return None

        # atualizar altura e rebalancear
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        fb = self.fator_balanceamento(raiz)

        # LL
        if fb > 1 and self.fator_balanceamento(raiz.esquerda) >= 0:
            return self.rotacao_direita(raiz)
        # LR
        if fb > 1 and self.fator_balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        # RR
        if fb < -1 and self.fator_balanceamento(raiz.direita) <= 0:
            return self.rotacao_esquerda(raiz)
        # RL
        if fb < -1 and self.fator_balanceamento(raiz.direita) > 0:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

class ArvoreAVL:
    """Implementação AVL com API esperada pelos testes"""
    def __init__(self):
        self.root = None
        self._avl = ArvoreAVL_Principal()

    def inserir(self, valor):
        self.root = self._avl.inserir(self.root, valor)

    def remover(self, valor):
        if self.buscar(valor) is None:
            return False
        self.root = self._avl.remover(self.root, valor)
        return True

    def buscar(self, valor):
        return self._avl.buscar(self.root, valor)

    def em_ordem(self):
        resultado = []
        def _in_order(no):
            if no:
                _in_order(no.esquerda)
                resultado.append(no.valor)
                _in_order(no.direita)
        _in_order(self.root)
        return resultado

    def imprimir(self):
        self._avl.mostrar_arvore(self.root)

    def obter_tamanho(self):
        return len(self.em_ordem())

    def esta_vazia(self):
        return self.root is None


