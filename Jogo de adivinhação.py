import random

while True:
  numero_sorteado = random.randint(0, 100)
  print("Novo jogo iniciado! Tente adivinhar o número.")
  
  while True:
    palpite = input("Informe um número de 0 a 100: ")
    palpite = int(palpite)
    
    print(f"Seu palpite foi {palpite}")

    if numero_sorteado == palpite:
      print("Acertou, parabéns!")
      break
    elif numero_sorteado > palpite:
      print("Muito pouco")
    elif numero_sorteado < palpite:
      print("Passou demais")

  nova_tentativa = input("Você quer jogar novamente? Digite s para sim e n para não: ").lower()
  if nova_tentativa == "n":
    print("Jogo finalizado!")
    break