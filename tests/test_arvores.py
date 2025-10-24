"""Testes automatizados para árvores balanceadas.

Este módulo contém testes pytest para validar:
1. Funcionalidade básica da Árvore Rubro-Negra
2. Funcionalidade básica da Árvore AVL 
3. Comparação de desempenho entre as implementações
"""

import os
import sys
import pytest
from typing import List, Type, Any

# Adiciona diretório raiz ao path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.arvore_rn import ArvoreRubroNegra
from src.arvore_avl import ArvoreAVL

def criar_arvore_teste(tipo_arvore: Type[Any], valores: List[int]):
    """Função auxiliar para criar e popular uma árvore com valores"""
    arvore = tipo_arvore()
    for valor in valores:
        arvore.inserir(valor)
    return arvore

@pytest.fixture
def valores_teste() -> List[int]:
    """Fixture com conjunto de valores para teste"""
    return [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]

@pytest.fixture
def arvore_rn(valores_teste) -> ArvoreRubroNegra:
    """Fixture que fornece uma árvore rubro-negra populada para testes"""
    return criar_arvore_teste(ArvoreRubroNegra, valores_teste)

class TesteArvoreRubroNegra:
    """Testes específicos para a implementação Rubro-Negra"""

    def test_insercao_basica(self, arvore_rn, valores_teste):
        """Testa se a inserção mantém a ordem correta"""
        assert arvore_rn.em_ordem() == sorted(valores_teste)

    def test_busca(self, arvore_rn):
        """Testa operações de busca."""
        assert arvore_rn.buscar(50) is not None
        assert arvore_rn.buscar(10) is not None
        assert arvore_rn.buscar(90) is None
        assert arvore_rn.buscar(-1) is None

    def test_remocao(self, arvore_rn, valores_teste):
        """Testa operações de remoção"""
        arvore_rn.remover(10)
        assert arvore_rn.buscar(10) is None

        arvore_rn.remover(20)
        assert arvore_rn.buscar(20) is None

        arvore_rn.remover(30)
        assert arvore_rn.buscar(30) is None

        # Tenta remover valor inexistente
        tamanho_antes = arvore_rn.obter_tamanho()
        arvore_rn.remover(999)
        assert arvore_rn.obter_tamanho() == tamanho_antes


    def test_tamanho(self, arvore_rn, valores_teste):
        """Testa controle de tamanho da árvore"""
        assert arvore_rn.obter_tamanho() == len(valores_teste)
        arvore_rn.remover(50)
        assert arvore_rn.obter_tamanho() == len(valores_teste) - 1

class TesteArvoreAVL:
    """Testes específicos para a implementação AVL"""

    @pytest.fixture
    def arvore_avl(self, valores_teste) -> ArvoreAVL:
        """Fixture que fornece uma árvore AVL populada para testes"""
        return criar_arvore_teste(ArvoreAVL, valores_teste)

    def test_insercao_e_ordem(self, arvore_avl, valores_teste):
        """Testa se a inserção mantém a ordem correta na árvore AVL"""
        assert arvore_avl.em_ordem() == sorted(valores_teste)

    def test_busca_avl(self, arvore_avl):
        """Testa operações de busca na árvore AVL"""
        assert arvore_avl.buscar(50) is not None
        assert arvore_avl.buscar(25) is not None
        assert arvore_avl.buscar(999) is None
        assert arvore_avl.buscar(-1) is None

    def test_remocao_simples(self, arvore_avl, valores_teste):
        """Testa a remoção de elementos e a manutenção da ordem"""
        # Remove um nó folha
        arvore_avl.remover(10)
        assert arvore_avl.buscar(10) is None
        
        # Remove um nó com um filho
        arvore_avl.remover(80)
        assert arvore_avl.buscar(80) is None

        # Remove um nó com dois filhos
        arvore_avl.remover(50)
        assert arvore_avl.buscar(50) is None
        
        elementos_restantes = valores_teste[:]
        elementos_restantes.remove(10)
        elementos_restantes.remove(80)
        elementos_restantes.remove(50)
        
        assert arvore_avl.em_ordem() == sorted(elementos_restantes)

    def test_integridade_estrutural_apos_insercao(self):
        """Testa a integridade estrutural da árvore AVL após várias inserções"""
        arvore = ArvoreAVL()
        valores = [10, 20, 30, 40, 50, 25]
        for v in valores:
            arvore.inserir(v)
        
        assert self._verificar_balanceamento(arvore.root, arvore._avl)

    def test_integridade_estrutural_apos_remocao(self, arvore_avl):
        """Testa a integridade estrutural da árvore AVL após várias remoções"""
        arvore_avl.remover(10)
        arvore_avl.remover(30)
        arvore_avl.remover(50)
        
        assert self._verificar_balanceamento(arvore_avl.root, arvore_avl._avl)

    def _verificar_balanceamento(self, no, avl_principal):
        if no is None:
            return True
        
        fator = avl_principal.fator_balanceamento(no)
        if not (-1 <= fator <= 1):
            return False
            
        return (self._verificar_balanceamento(no.esquerda, avl_principal) and 
                self._verificar_balanceamento(no.direita, avl_principal))

    def test_casos_especiais(self, arvore_avl, valores_teste):
        """Testa casos especiais de manipulação da árvore"""
        # Tenta inserir elemento duplicado
        tamanho_inicial = arvore_avl.obter_tamanho()
        arvore_avl.inserir(50)  # 50 já existe
        assert arvore_avl.obter_tamanho() == tamanho_inicial
        
        # Tenta remover de árvore vazia
        arvore_vazia = ArvoreAVL()
        tamanho_vazia = arvore_vazia.obter_tamanho()
        arvore_vazia.remover(10)
        assert arvore_vazia.obter_tamanho() == tamanho_vazia

if __name__ == '__main__':
    pytest.main(['-v', __file__])
