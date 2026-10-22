def calcular(
    primeiro_numero: float, segundo_numero: float, operacao: str
) -> float:
    """Executa uma operação aritmética entre dois números."""
    if operacao == "+":
        return primeiro_numero + segundo_numero
    if operacao == "-":
        return primeiro_numero - segundo_numero
    if operacao == "*":
        return primeiro_numero * segundo_numero
    if operacao == "/":
        if segundo_numero == 0:
            raise ValueError("Não é possível dividir por zero.")
        return primeiro_numero / segundo_numero
    raise ValueError("Operação inválida. Use +, -, * ou /.")


def main() -> None:
    print("Calculadora")
    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ").strip()
        segundo_numero = float(input("Digite o segundo número: "))
        resultado = calcular(primeiro_numero, segundo_numero, operacao)
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
