# def IMC(p, a):
#     indice = p / (a*a)
#     return indice

while True:
    nome = input("Digite seu nome: ")
    if nome == "sair":
        print("Até logo!")
        break
    else:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        imc = peso / (altura*altura)
        if imc >= 18.6 and imc <= 24.9:
            print(f"Olá, {nome}, parabéns! Seu IMC é {imc} e está dentro da faixa normal.")
        else:
            print(f"Olá, {nome}, ATENÇÃO! Seu IMC é {imc} e está fora da faixa de normalidade.")

