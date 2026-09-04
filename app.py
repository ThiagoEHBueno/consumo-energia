nomeAparelho = input("Qual o nome do aparelho? ")
potencia = float(input("Qual a potência em watts? "))
horasDia = float(input("Qual o tempo médio de uso diário do aparelho? "))
valorKwh = 0.75
consumoMensal = (potencia * horasDia * 30) / 1000
valorEstimado = valorKwh * consumoMensal

print("Aparelho: ", nomeAparelho)
print(f"Consumo estimado: {consumoMensal:.2f}")
print(f"Valor estimado de acordo com R${valorKwh} hora:  {valorEstimado:.2f}")