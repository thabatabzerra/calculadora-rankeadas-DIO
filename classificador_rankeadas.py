def classificar_jogador(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas  # Calcular o saldo de vitórias
    
    # Classificação do jogador com base no número de vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    # Exibe a mensagem final
    print(f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}")

# Exemplo de uso
vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))
classificar_jogador(vitorias, derrotas)
