classificacao = (
    "Time A", "Time B", "Time C", "Time D", "Time E", 
    "Time F", "Time G", "Time H", "Time I", "Time J"
)

print("Os três primeiros colocados são:", classificacao[:3])

print("Os três últimos colocados são:", classificacao[-3:])

print("Times em ordem alfabética:", sorted(classificacao))

time_usuario = input("Digite o nome de um time para ver sua posição: ")
if time_usuario in classificacao:
    print(f"O time {time_usuario} está na posição {classificacao.index(time_usuario) + 1}.")
else:
    print("Time não encontrado na classificação.")
