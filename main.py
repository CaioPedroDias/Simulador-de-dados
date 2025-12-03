import random
import time

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
        print(f"Rolando {n_dados}d{faces}...")
        time.sleep(0.5)
        print(f"Resultado: {resultado} -> soma = {sum(resultado)}\n")

if __name__ == "__main__":
    main()
