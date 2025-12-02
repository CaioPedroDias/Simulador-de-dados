import random

def rolar(n_dados, faces):
    return [random.randint(1, faces) for _ in range(n_dados)]

def main():
    try:
        n_dados = int(input("Quantos dados? : "))
        faces = int(input("Quantas faces? : "))
        vezes = int(input("Quantas vezes quer rolar? : "))

    except ValueError:
        print("Entrada inválida. Use números inteiros.")
        return

    for i in range(vezes):
        resultado = rolar(n_dados, faces)
        print(f"Rolada {i+1}: {resultado} -> soma = {sum(resultado)}")

if __name__ == "__main__":
    main()