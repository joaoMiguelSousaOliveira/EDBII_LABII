class NoRubroNegro:
    """Nó da árvore Rubro-Negra com valor, cor e referências"""
    
    __slots__ = ("valor", "cor", "esquerda", "direita", "pai")
    
    def __init__(self, valor=None, cor='PRETO', esquerda=None, direita=None, pai=None):
        self.valor = valor
        self.cor = cor       # 'PRETO' ou 'VERMELHO'
        self.esquerda = esquerda
        self.direita = direita
        self.pai = pai

class ArvoreRubroNegra:
    """Implementação de árvore Rubro-Negra com recoloração e rotações"""

    def __init__(self):
        self.NIL = NoRubroNegro(cor='PRETO')  # Nó sentinela
        self.raiz = self.NIL
        self._tamanho = 0

    def rotacao_esquerda(self, no):
        """Executa rotação à esquerda mantendo propriedades RN"""
        y = no.direita
        no.direita = y.esquerda
        if y.esquerda is not self.NIL:
            y.esquerda.pai = no
        y.pai = no.pai
        if no.pai is self.NIL:
            self.raiz = y
        elif no is no.pai.esquerda:
            no.pai.esquerda = y
        else:
            no.pai.direita = y
        y.esquerda = no
        no.pai = y

    def rotacao_direita(self, y):
        """Executa rotação à direita mantendo propriedades RN"""
        x = y.esquerda
        y.esquerda = x.direita
        if x.direita is not self.NIL:
            x.direita.pai = y
        x.pai = y.pai
        if y.pai is self.NIL:
            self.raiz = x
        elif y is y.pai.direita:
            y.pai.direita = x
        else:
            y.pai.esquerda = x
        x.direita = y
        y.pai = x

    def _fixar_insercao(self, z):
        """Restaura propriedades da árvore Rubro-Negra após inserção"""
        while z.pai is not self.NIL and z.pai.cor == 'VERMELHO':
            if z.pai is z.pai.pai.esquerda:
                y = z.pai.pai.direita
                if y is not self.NIL and y.cor == 'VERMELHO':
                    z.pai.cor = 'PRETO'
                    y.cor = 'PRETO'
                    z.pai.pai.cor = 'VERMELHO'
                    z = z.pai.pai
                else:
                    if z is z.pai.direita:
                        z = z.pai
                        self.rotacao_esquerda(z)
                    z.pai.cor = 'PRETO'
                    z.pai.pai.cor = 'VERMELHO'
                    self.rotacao_direita(z.pai.pai)
            else:
                y = z.pai.pai.esquerda
                if y is not self.NIL and y.cor == 'VERMELHO':
                    z.pai.cor = 'PRETO'
                    y.cor = 'PRETO'
                    z.pai.pai.cor = 'VERMELHO'
                    z = z.pai.pai
                else:
                    if z is z.pai.esquerda:
                        z = z.pai
                        self.rotacao_direita(z)
                    z.pai.cor = 'PRETO'
                    z.pai.pai.cor = 'VERMELHO'
                    self.rotacao_esquerda(z.pai.pai)
        self.raiz.cor = 'PRETO'

    def _transplantar(self, u, v):
        """Substitui um subtree pela outra"""
        if u.pai is self.NIL:
            self.raiz = v
        elif u is u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai

    def _minimo(self, x):
        """Retorna o nó com o menor valor em uma árvore"""
        while x.esquerda is not self.NIL:
            x = x.esquerda
        return x

    def _fixar_remocao(self, x):
        """Restaura propriedades da árvore Rubro-Negra após remoção"""
        while x is not self.raiz and x.cor == 'PRETO':
            if x is x.pai.esquerda:
                w = x.pai.direita
                if w.cor == 'VERMELHO':
                    w.cor = 'PRETO'
                    x.pai.cor = 'VERMELHO'
                    self.rotacao_esquerda(x.pai)
                    w = x.pai.direita
                if w.esquerda.cor == 'PRETO' and w.direita.cor == 'PRETO':
                    w.cor = 'VERMELHO'
                    x = x.pai
                else:
                    if w.direita.cor == 'PRETO':
                        w.esquerda.cor = 'PRETO'
                        w.cor = 'VERMELHO'
                        self.rotacao_direita(w)
                        w = x.pai.direita
                    w.cor = x.pai.cor
                    x.pai.cor = 'PRETO'
                    w.direita.cor = 'PRETO'
                    self.rotacao_esquerda(x.pai)
                    x = self.raiz
            else:
                w = x.pai.esquerda
                if w.cor == 'VERMELHO':
                    w.cor = 'PRETO'
                    x.pai.cor = 'VERMELHO'
                    self.rotacao_direita(x.pai)
                    w = x.pai.esquerda
                if w.direita.cor == 'PRETO' and w.esquerda.cor == 'PRETO':
                    w.cor = 'VERMELHO'
                    x = x.pai
                else:
                    if w.esquerda.cor == 'PRETO':
                        w.direita.cor = 'PRETO'
                        w.cor = 'VERMELHO'
                        self.rotacao_esquerda(w)
                        w = x.pai.esquerda
                    w.cor = x.pai.cor
                    x.pai.cor = 'PRETO'
                    w.esquerda.cor = 'PRETO'
                    self.rotacao_direita(x.pai)
                    x = self.raiz
        x.cor = 'PRETO'

    # --- API pública esperada pelos testes ---
    def inserir(self, valor):
        novo = NoRubroNegro(valor, cor='VERMELHO', esquerda=self.NIL, direita=self.NIL, pai=self.NIL)
        y = self.NIL
        x = self.raiz
        while x is not self.NIL:
            y = x
            if novo.valor < x.valor:
                x = x.esquerda
            elif novo.valor > x.valor:
                x = x.direita
            else:
                return  # não insere duplicatas
        novo.pai = y
        if y is self.NIL:
            self.raiz = novo
        elif novo.valor < y.valor:
            y.esquerda = novo
        else:
            y.direita = novo
        self._fixar_insercao(novo)
        self._tamanho += 1

    def _buscar_no(self, node, valor):
        x = node
        while x is not self.NIL:
            if valor == x.valor:
                return x
            if valor < x.valor:
                x = x.esquerda
            else:
                x = x.direita
        return self.NIL

    def buscar(self, valor):
        node = self._buscar_no(self.raiz, valor)
        return None if node is self.NIL else node

    def em_ordem(self):
        out = []
        def _inorder(n):
            if n is self.NIL:
                return
            _inorder(n.esquerda)
            out.append(n.valor)
            _inorder(n.direita)
        _inorder(self.raiz)
        return out

    def imprimir(self):
        self.mostrar_arvore(self.raiz)

    def mostrar_arvore(self, no, prefixo="", is_esq=True):
        if no is not self.NIL:
            cor = '\033[91m' if no.cor == 'VERMELHO' else '\033[90m' # Vermelho ou Cinza para Preto
            reset = '\033[0m'
            print(prefixo + ("└── " if is_esq else "┌── ") + f"{cor}{no.valor} ({no.cor}){reset}")
            if no.esquerda is not self.NIL or no.direita is not self.NIL:
                novo_prefixo = prefixo + ("    " if is_esq else "│   ")
                self.mostrar_arvore(no.direita, novo_prefixo, False)
                self.mostrar_arvore(no.esquerda, novo_prefixo, True)

    def obter_tamanho(self):
        return self._tamanho

    def remover(self, valor):
        z = self._buscar_no(self.raiz, valor)
        if z is self.NIL:
            return False
        y = z
        y_original_color = y.cor
        if z.esquerda is self.NIL:
            x = z.direita
            self._transplantar(z, z.direita)
        elif z.direita is self.NIL:
            x = z.esquerda
            self._transplantar(z, z.esquerda)
        else:
            y = self._minimo(z.direita)
            y_original_color = y.cor
            x = y.direita
            if y.pai is z:
                x.pai = y
            else:
                self._transplantar(y, y.direita)
                y.direita = z.direita
                y.direita.pai = y
            self._transplantar(z, y)
            y.esquerda = z.esquerda
            y.esquerda.pai = y
            y.cor = z.cor
        if y_original_color == 'PRETO':
            # x pode ser self.NIL; _fixar_remocao trata sentinel corretamente
            self._fixar_remocao(x)
        self._tamanho -= 1
        return True

    def esta_vazia(self):
        return self.raiz is self.NIL
