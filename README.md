## Para rodar testes

Instalar pytest (se necessário)
```
python3 -m pip install pytest
```

Rodar todos os testes
```
python3 -m pytest -q
```

Rodar um teste específico (ex.: testar Rubro-Negra)
```
python3 -m pytest tests/test_arvores.py::test_basico_rn -q
```
