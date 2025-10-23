from .interface_arvore import InterfaceArvore
class NoRN:
    """Nó da Árvore Rubro-Negra"""
    def __init__(self, valor):
        self.valor = valor
        self.cor = 'VERMELHO'  # Novos nós sempre começam vermelhos
        self.esquerda = None
        self.direita = None
        self.pai = None


class ArvoreRubroNegra(InterfaceArvore):
    """
    Implementação de Árvore Rubro-Negra com operações de inserção, remoção e busca.
    
    Propriedades mantidas:
    1. Todo nó é vermelho ou preto
    2. A raiz é sempre preta
    3. Todas as folhas (None) são consideradas pretas
    4. Se um nó é vermelho, seus filhos devem ser pretos
    5. Todos os caminhos de um nó até suas folhas contêm o mesmo número de nós pretos
    """
    
    def __init__(self):
        self.raiz = None
        self.tamanho = 0
    
    def inserir(self, valor):
        """Insere um valor na árvore e rebalanceia"""
        novo_no = NoRN(valor)
        self.tamanho += 1
        
        # Inserção padrão BST
        if self.raiz is None:
            self.raiz = novo_no
            self.raiz.cor = 'PRETO'  # Raiz sempre é preta
            return
        
        atual = self.raiz
        while True:
            if valor < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = novo_no
                    novo_no.pai = atual
                    break
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo_no
                    novo_no.pai = atual
                    break
                atual = atual.direita
        
        # Corrigir violações das propriedades
        self.corrigir_insercao(novo_no)
    
    def corrigir_insercao(self, no):
        """Corrige violações após inserção"""
        while no != self.raiz and no.pai.cor == 'VERMELHO':
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita
                
                # Caso 1: Tio é vermelho
                if tio and tio.cor == 'VERMELHO':
                    no.pai.cor = 'PRETO'
                    tio.cor = 'PRETO'
                    no.pai.pai.cor = 'VERMELHO'
                    no = no.pai.pai
                else:
                    # Caso 2: Tio é preto e nó é filho direito
                    if no == no.pai.direita:
                        no = no.pai
                        self._rotacao_esquerda(no)
                    
                    # Caso 3: Tio é preto e nó é filho esquerdo
                    no.pai.cor = 'PRETO'
                    no.pai.pai.cor = 'VERMELHO'
                    self._rotacao_direita(no.pai.pai)
            else:
                tio = no.pai.pai.esquerda
                
                # Caso 1: Tio é vermelho
                if tio and tio.cor == 'VERMELHO':
                    no.pai.cor = 'PRETO'
                    tio.cor = 'PRETO'
                    no.pai.pai.cor = 'VERMELHO'
                    no = no.pai.pai
                else:
                    # Caso 2: Tio é preto e nó é filho esquerdo
                    if no == no.pai.esquerda:
                        no = no.pai
                        self._rotacao_direita(no)
                    
                    # Caso 3: Tio é preto e nó é filho direito
                    no.pai.cor = 'PRETO'
                    no.pai.pai.cor = 'VERMELHO'
                    self._rotacao_esquerda(no.pai.pai)
        
        self.raiz.cor = 'PRETO'
    
    def remover(self, valor):
        """Remove um elemento da árvore"""
        no = self._buscar_no(valor)
        if no is None:
            return False
        
        self.tamanho -= 1
        self.remover_no(no)
        return True
    
    def remover_no(self, no):
        """Remove um nó e rebalanceia a árvore"""
        # Encontrar o nó a ser removido e seu substituto
        if no.esquerda and no.direita:
            # Nó com dois filhos: encontrar sucessor
            sucessor = self._minimo(no.direita)
            no.valor = sucessor.valor
            no = sucessor
        
        # Nó tem no máximo um filho
        filho = no.esquerda if no.esquerda else no.direita
        
        if no.cor == 'PRETO':
            no.cor = filho.cor if filho else 'PRETO'
            self.corrigir_remocao(no)
        
        self._substituir_no(no, filho)
    
    def corrigir_remocao(self, no):
        """Corrige violações após remoção"""
        while no != self.raiz and (no is None or no.cor == 'PRETO'):
            if no == no.pai.esquerda:
                irmao = no.pai.direita
                
                # Caso 1: Irmão é vermelho
                if irmao and irmao.cor == 'VERMELHO':
                    irmao.cor = 'PRETO'
                    no.pai.cor = 'VERMELHO'
                    self._rotacao_esquerda(no.pai)
                    irmao = no.pai.direita
                
                # Caso 2: Irmão é preto e ambos os filhos são pretos
                if irmao and (not irmao.esquerda or irmao.esquerda.cor == 'PRETO') and \
                   (not irmao.direita or irmao.direita.cor == 'PRETO'):
                    irmao.cor = 'VERMELHO'
                    no = no.pai
                else:
                    # Caso 3: Irmão é preto, filho esquerdo vermelho, direito preto
                    if irmao and (not irmao.direita or irmao.direita.cor == 'PRETO'):
                        if irmao.esquerda:
                            irmao.esquerda.cor = 'PRETO'
                        irmao.cor = 'VERMELHO'
                        self._rotacao_direita(irmao)
                        irmao = no.pai.direita
                    
                    # Caso 4: Irmão é preto e filho direito é vermelho
                    if irmao:
                        irmao.cor = no.pai.cor
                        no.pai.cor = 'PRETO'
                        if irmao.direita:
                            irmao.direita.cor = 'PRETO'
                        self._rotacao_esquerda(no.pai)
                    no = self.raiz
            else:
                irmao = no.pai.esquerda
                
                # Caso 1: Irmão é vermelho
                if irmao and irmao.cor == 'VERMELHO':
                    irmao.cor = 'PRETO'
                    no.pai.cor = 'VERMELHO'
                    self._rotacao_direita(no.pai)
                    irmao = no.pai.esquerda
                
                # Caso 2: Irmão é preto e ambos os filhos são pretos
                if irmao and (not irmao.direita or irmao.direita.cor == 'PRETO') and \
                   (not irmao.esquerda or irmao.esquerda.cor == 'PRETO'):
                    irmao.cor = 'VERMELHO'
                    no = no.pai
                else:
                    # Caso 3: Irmão é preto, filho direito vermelho, esquerdo preto
                    if irmao and (not irmao.esquerda or irmao.esquerda.cor == 'PRETO'):
                        if irmao.direita:
                            irmao.direita.cor = 'PRETO'
                        irmao.cor = 'VERMELHO'
                        self._rotacao_esquerda(irmao)
                        irmao = no.pai.esquerda
                    
                    # Caso 4: Irmão é preto e filho esquerdo é vermelho
                    if irmao:
                        irmao.cor = no.pai.cor
                        no.pai.cor = 'PRETO'
                        if irmao.esquerda:
                            irmao.esquerda.cor = 'PRETO'
                        self._rotacao_direita(no.pai)
                    no = self.raiz
        
        if no:
            no.cor = 'PRETO'
    
    def _substituir_no(self, no, filho):
        """Substitui um nó por seu filho"""
        if no.pai is None:
            self.raiz = filho
        elif no == no.pai.esquerda:
            no.pai.esquerda = filho
        else:
            no.pai.direita = filho
        
        if filho:
            filho.pai = no.pai
    
    def _rotacao_esquerda(self, no):
        """Realiza rotação à esquerda"""
        direita = no.direita
        no.direita = direita.esquerda
        
        if direita.esquerda:
            direita.esquerda.pai = no
        
        direita.pai = no.pai
        
        if no.pai is None:
            self.raiz = direita
        elif no == no.pai.esquerda:
            no.pai.esquerda = direita
        else:
            no.pai.direita = direita
        
        direita.esquerda = no
        no.pai = direita
    
    def _rotacao_direita(self, no):
        """Realiza rotação à direita"""
        esquerda = no.esquerda
        no.esquerda = esquerda.direita
        
        if esquerda.direita:
            esquerda.direita.pai = no
        
        esquerda.pai = no.pai
        
        if no.pai is None:
            self.raiz = esquerda
        elif no == no.pai.direita:
            no.pai.direita = esquerda
        else:
            no.pai.esquerda = esquerda
        
        esquerda.direita = no
        no.pai = esquerda
    
    def buscar(self, valor):
        """Busca um valor na árvore"""
        return self._buscar_no(valor) is not None
    
    def _buscar_no(self, valor):
        """Busca e retorna o nó com o valor especificado"""
        atual = self.raiz
        while atual:
            if valor == atual.valor:
                return atual
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None
    
    def _minimo(self, no):
        """Encontra o nó com menor valor a partir de um nó"""
        while no.esquerda:
            no = no.esquerda
        return no
    
    def imprimir(self):
        """Imprime a árvore de forma visual"""
        if self.raiz is None:
            print("Árvore vazia")
            return
        
        print("\n=== Estrutura da Árvore Rubro-Negra ===")
        self._imprimir_recursivo(self.raiz, "", True)
        print()
    
    def _imprimir_recursivo(self, no, prefixo, eh_direita):
        """Imprime a árvore recursivamente"""
        if no is None:
            return
        
        print(prefixo + ("└── " if eh_direita else "┌── ") + 
              f"{no.valor} ({no.cor[0]})")
        
        if no.esquerda or no.direita:
            if no.direita:
                self._imprimir_recursivo(no.direita, 
                    prefixo + ("    " if eh_direita else "│   "), True)
            if no.esquerda:
                self._imprimir_recursivo(no.esquerda, 
                    prefixo + ("    " if eh_direita else "│   "), False)
    
    def em_ordem(self):
        """Retorna lista com valores em ordem"""
        resultado = []
        self._em_ordem_recursivo(self.raiz, resultado)
        return resultado
    
    def _em_ordem_recursivo(self, no, resultado):
        """Percurso em ordem recursivo"""
        if no:
            self._em_ordem_recursivo(no.esquerda, resultado)
            resultado.append(no.valor)
            self._em_ordem_recursivo(no.direita, resultado)
    
    def obter_tamanho(self):
        """Retorna o número de elementos na árvore"""
        return self.tamanho
    
    def esta_vazia(self):
        """Verifica se a árvore está vazia"""
        return self.raiz is None