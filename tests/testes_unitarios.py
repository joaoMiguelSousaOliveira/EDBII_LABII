"""Tests pytest para as árvores balanceadas.

Este único arquivo contém os testes automatizados (pytest) que valem
por ambos: verificação funcional da ArvoreRubroNegra e um sanity-check
condicional de desempenho que roda apenas se `ArvoreAVL` estiver
implementada em `src/arvore_avl.py`.
"""

import importlib
import pytest


def test_basico_rubro_negra():
    """Testa operações básicas de ArvoreRubroNegra (inserir, buscar, em_ordem, remover)."""
    rn_mod = importlib.import_module('src.arvore_rn')
    ArvoreRubroNegra = rn_mod.ArvoreRubroNegra

    arv = ArvoreRubroNegra()
    valores = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
    for v in valores:
        arv.inserir(v)

    # Verifica percurso em ordem
    assert arv.em_ordem() == [10, 20, 25, 30, 35, 40, 50, 60, 70, 80]

    # Busca valores presentes e ausentes
    assert arv.buscar(50)
    assert arv.buscar(25)
    assert not arv.buscar(90)
    assert arv.buscar(10)

    # Tamanho
    assert arv.obter_tamanho() == 10

    # Remoções
    assert arv.remover(20)
    assert arv.remover(30)
    assert arv.remover(50)

    assert arv.obter_tamanho() == 7
    assert arv.em_ordem() == [10, 25, 35, 40, 60, 70, 80]

    # imprimir não deve lançar
    arv.imprimir()


def test_desempenho_com_avl_ou_skip():
    """Roda um sanity-check de desempenho se `ArvoreAVL` existir; caso contrário pula o teste."""
    rn_mod = importlib.import_module('src.arvore_rn')
    ArvoreRubroNegra = rn_mod.ArvoreRubroNegra

    # Tenta importar AVL; se não existir, pula o teste
    try:
        avl_mod = importlib.import_module('src.arvore_avl')
        ArvoreAVL = getattr(avl_mod, 'ArvoreAVL')
    except Exception:
        pytest.skip('ArvoreAVL não implementada; pulando teste de desempenho')

    avl = ArvoreAVL()
    rn = ArvoreRubroNegra()

    # Teste de inserção simples como sanity-check de desempenho (pequeno)
    valores = list(range(1, 201))
    for v in valores:
        avl.inserir(v)
        rn.inserir(v)

    # Busca rápida
    for v in [1, 100, 200]:
        assert avl.buscar(v)
        assert rn.buscar(v)