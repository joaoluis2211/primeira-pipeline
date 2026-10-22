import pytest

from app import calcular


def test_soma():
    assert calcular(3, 2, "+") == 5


def test_subtracao():
    assert calcular(3, 2, "-") == 1


def test_multiplicacao():
    assert calcular(3, 2, "*") == 6


def test_divisao():
    assert calcular(6, 2, "/") == 3


def test_divisao_por_zero():
    with pytest.raises(ValueError, match="Não é possível dividir por zero."):
        calcular(1, 0, "/")


def test_operacao_invalida():
    with pytest.raises(ValueError, match="Operação inválida"):
        calcular(1, 2, "%")