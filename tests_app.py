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


@pytest.mark.parametrize(
    "entradas, esperado",
    [
        (["3", " + ", "2"], "Resultado: 5.0"),
        (["1", "/", "0"], "Erro: Não é possível dividir por zero."),
        (["1", "%", "2"], "Erro: Operação inválida"),
        (["abc"], "Erro:"),
    ],
)
def test_interface(monkeypatch, capsys, entradas, esperado):
    from app import main

    respostas = iter(entradas)
    monkeypatch.setattr("builtins.input", lambda _: next(respostas))

    main()

    assert esperado in capsys.readouterr().out


def test_execucao_como_script(monkeypatch, capsys):
    import runpy

    respostas = iter(["6", "/", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(respostas))

    runpy.run_module("app", run_name="__main__")

    assert "Resultado: 3.0" in capsys.readouterr().out
