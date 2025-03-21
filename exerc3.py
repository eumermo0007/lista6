cores_arco_iris = ("Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta")

num = int(input("Digite um número de 1 a 7 para ver a cor correspondente do arco-íris: "))

if 1 <= num <= 7:
    print(f"A cor correspondente é {cores_arco_iris[num - 1]}.")
else:
    print("Número inválido! Digite um valor entre 1 e 7.")
