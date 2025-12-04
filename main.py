import random

def rolar(n_dados, faces):
    return [random.randint(1, faces) for _ in range(n_dados)]

def main():
    print("Digite rolagens no formato XdY (ex: 3d20, 2d6).")
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Rolagem: ").lower().strip()

        # saida do programa
        if entrada == "sair":
            print("Encerrando...")
            break  # sai do while

        # tenta pegar XdY
        try:
            n_dados, faces = entrada.split("d")
            n_dados = int(n_dados)
            faces = int(faces)
        except:
            print("Formato inválido! Use algo como 3d20 ou digite 'sair'.\n")
            continue  # volta ao inicio

        # rolagem
        resultado = rolar(n_dados, faces)

        # ordena do maior pro menor
        resultado_ordenado = sorted(resultado, reverse=True)

        soma = sum(resultado)
        maior = max(resultado)

        print(f"Rolando dados {n_dados}d{faces}...")
        print(f"Resultado: {resultado_ordenado}")
        print(f"Soma: {soma}")
        print(f"O maior valor é: {maior}")

if __name__ == "__main__":
    main()
