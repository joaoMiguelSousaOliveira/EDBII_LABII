from abc import ABC, abstractmethod

# Interface

class InterfaceArvore(ABC):
    @abstractmethod
    def inserir(self, chave):
        """Insere um elemento na árvore."""
        raise NotImplementedError()
    
    @abstractmethod
    def corrigir_insercao(self, novo_no):
        """Corrige violações após inserção"""
        raise NotImplementedError()
    
    @abstractmethod
    def remover_no(self, no):
        """Remove um nó e rebalanceia a árvore"""
        raise NotImplementedError()
    
    @abstractmethod
    def corrigir_remocao(self, no):
        """Corrige violações após remoção"""
        raise NotImplementedError()

    @abstractmethod
    def remover(self, chave):
        """Remove um elemento da árvore.""" 
        raise NotImplementedError()

    @abstractmethod
    def buscar(self, chave):
        """Busca um elemento na árvore e retorna True/False.""" 
        raise NotImplementedError()

    @abstractmethod
    def imprimir(self):
        """Imprime ou visualiza a estrutura da árvore."""
        raise NotImplementedError()

    @abstractmethod
    def em_ordem(self):
        """Retorna lista com valores em ordem"""
        raise NotImplementedError()

    @abstractmethod
    def obter_tamanho(self):
        """Retorna o número de elementos na árvore"""
        raise NotImplementedError()

    @abstractmethod
    def esta_vazia(self):
        """Verifica se a árvore está vazia"""
        raise NotImplementedError()