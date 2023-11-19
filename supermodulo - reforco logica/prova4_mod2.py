def calcular_media(lista_notas):
    soma = 0
    for nota in lista_notas:
        soma += nota
        media = soma/len(lista_notas)
    return media

def verificar_situacao(media):
    if media < 7:
        return f"A média é {media} e o aluno está REPROVADO."
    elif media >= 7 and media < 10:
        return f"A média é {media} e o aluno está APROVADO."
    else:
        return f"Parabéns, sua média é 10!"

notas_aluno = []


while True:
    menu = int(input("""
O que você deseja fazer?
                                   
0. Sair;
1. Incluir notas; 
2. Verificar média do aluno;
3. Verificar situação do aluno;

Digite um dos números: """))
    if menu == 0:
        print("Até logo!")
        break
    elif menu == 1:
        while True:
            # disciplina = str(input("Digite a disciplina | Caso não deseje incluir mais notas, digite FIM: ")).upper()
            # if disciplina == "FIM":
            #     break
            # else:
            nota = (input("digite a nota do aluno: "))
            if nota == 'fim':
                break
            else:
                nota = float(nota)
                if nota < 0 and nota > 10:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
                else:
                    notas_aluno.append(nota)
                print(notas_aluno)
    elif menu == 2:
        if notas_aluno == []:
            print("O aluno ainda não tem notas cadastradas.")
        else:
            media = calcular_media(notas_aluno)
            print(f"A média do aluno é {media}.")

    elif menu == 3:
        if notas_aluno == []:
            print("O aluno ainda não tem notas cadastradas.")
        else:
            media = calcular_media(notas_aluno)
            situacao = verificar_situacao(media)
            print(situacao)