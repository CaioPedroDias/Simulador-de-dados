import random

def rolar(n_dados, faces):
    return [random.randint(1, faces) for _ in range(n_dados)]

def main():
    print("Digite rolagens no formato XdY (ex: 3d20, 2d6, 4d6+7, 1d8-1).")
    print("Digite 'sair' para encerrar.\n")
    
    # input
    while True:
        entrada = input("Rolagem: ").lower().strip()

        if entrada == "sair":
            print("Encerrando...")
            break

        # modificador
        modificador = 0
        if "+" in entrada:
            parte_dado, mod = entrada.split("+")
            modificador = int(mod)
        elif "-" in entrada:
            parte_dado, mod = entrada.split("-")
            modificador = -int(mod)
        else:
            parte_dado = entrada

        # XdY
        try:
            n_dados, faces = parte_dado.split("d")
            n_dados = int(n_dados)
            faces = int(faces)
        except:
            print("Formato inválido! Use 3d20, 4d6+2, 1d8-1...\n")
            continue

        # roll
        resultado = rolar(n_dados, faces)
        resultado_ordenado = sorted(resultado, reverse=True)

        soma = sum(resultado)
        maior = max(resultado)
        soma_final = soma + modificador

        # print
        print(f"\nRolando {n_dados}d{faces} {'+' if modificador>=0 else ''}{modificador}...")
        print(f"Roll: {resultado_ordenado}\n")
        print(f"O maior valor é: {maior}")
        print(f"Soma dos dados: {soma}")
        if modificador != 0:
            print(f"Modificador: {modificador}")
        print(f"Soma final: {soma_final}\n")

if __name__ == "__main__":
    main()
