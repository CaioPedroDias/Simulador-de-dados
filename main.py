import random
import time

def rolar(n_dados, faces):
    return [random.randint(1, faces) for _ in range(n_dados)]

def main():
    entrada = input("Digite a rolagem (ex: 3d20): ").lower()

    # divide na letra 'd'
    try:
        n_dados, faces = entrada.split("d")
        n_dados = int(n_dados)
        faces = int(faces)
    except:
        print("Formato inválido! Use algo como 3d20, 2d6, 1d100...")
        return

    resultado = rolar(n_dados, faces)
    print(f"Rolando {n_dados}d{faces}...")
    time.sleep(0.5)
    print(f"Resultados: {resultado} -> soma = {sum(resultado)}")

if __name__ == "__main__":
    main()