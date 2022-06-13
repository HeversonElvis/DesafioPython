import random
import sys
vencedor = ""

Propriedade1 = ""
Propriedade2 = ""
Propriedade3 = ""
Propriedade4 = ""
Propriedade5 = ""
Propriedade6 = ""
Propriedade7 = ""
Propriedade8 = ""
Propriedade9 = ""
Propriedade10 = ""
Propriedade11 = ""
Propriedade12 = ""
Propriedade13 = ""
Propriedade14 = ""
Propriedade15 = ""
Propriedade16 = ""
Propriedade17 = ""
Propriedade18 = ""
Propriedade19 = ""
Propriedade20 = ""

valorpropriedade1 = 70
valorpropriedade2 = 400
valorpropriedade3 = 250
valorpropriedade4 = 200
valorpropriedade5 = 150
valorpropriedade6 = 200
valorpropriedade7 = 310
valorpropriedade8 = 180
valorpropriedade9 = 350
valorpropriedade10 = 250
valorpropriedade11= 70
valorpropriedade12 = 500
valorpropriedade13 = 300
valorpropriedade14 = 150
valorpropriedade15 = 200
valorpropriedade16 = 330
valorpropriedade17 = 450
valorpropriedade18 = 260
valorpropriedade19 = 70
valorpropriedade20 = 180

AluguelPropriedade1 = 35
AluguelPropriedade2 = 80
AluguelPropriedade3 = 60
AluguelPropriedade4 = 80
AluguelPropriedade5 = 25
AluguelPropriedade6 = 30
AluguelPropriedade7 = 70
AluguelPropriedade8 = 30
AluguelPropriedade9 = 120
AluguelPropriedade10 = 55
AluguelPropriedade11 = 35
AluguelPropriedade12 = 170
AluguelPropriedade13 = 60
AluguelPropriedade14 = 25
AluguelPropriedade15 = 80
AluguelPropriedade16 = 45
AluguelPropriedade17 = 150
AluguelPropriedade18 = 40
AluguelPropriedade19 = 35
AluguelPropriedade20 = 30

# Dados Jogador 1
nomejog1 = "Jogador Impulsivo"
valorjogador1 = 300
posjog1 = 0
tentjog1 = 0
faliujog1 = False

# Dados Jogador 2
nomejog2 = "Jogador Exigente"
valorjogador2 = 300
posjog2 = 0
tentjog2 = 0
faliujog2 = False

# Dados Jogador 3
nomejog3 = "Jogador Cauteloso"
valorjogador3 = 300
posjog3 = 0
tentjog3 = 0
faliujog3 = False

# Dados Jogador 4
nomejog4 = "Jogador Aleatório"
valorjogador4 = 300
posjog4 = 0
tentjog4 = 0
faliujog4 = False

lista_de_faliu = []
lista_jog = []
lista_valores = []
turno = 0

# Loop de Jogadas
while int(not faliujog1) + int(not faliujog2) + int(not faliujog3) + int(not faliujog4) > 1:

    # Jogadas do Jogador 1 - Impulsivo
    if not faliujog1 and nomejog1 != "":
        print(str(nomejog1) + " você está na casa: " + str(posjog1))
        print(str(nomejog1) + " você possui em conta R$" + format(valorjogador1, '.2f'))
        dado = random.randint(1, 6)
        print("Valor do dado:", dado)
        posjog1 += dado

        # Verifica Posição no Tabuleiro
        if posjog1 > 20:
            dado = posjog1 - 20
            posjog1 = dado - 1
            valorjogador1 += 100
            print(nomejog1, "Você recebeu R$100,00 por atravessar todo o tabuleiro")

        if posjog1 == 1:
            if Propriedade1 == "":
                if valorjogador1 >= valorpropriedade1:
                    valorjogador1 -= valorpropriedade1
                    Propriedade1 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Pará ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Pará ")
            elif Propriedade1 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Pará ")
            else:
                if Propriedade1 == nomejog2:
                    valorjogador2 += AluguelPropriedade1
                    valorjogador1 -= AluguelPropriedade1
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade1 == nomejog3:
                    valorjogador3 += AluguelPropriedade1
                    valorjogador1 -= AluguelPropriedade1
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade1 == nomejog4:
                    valorjogador4 += AluguelPropriedade1
                    valorjogador1 -= AluguelPropriedade1
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 2:
            if Propriedade2 == "":
                if valorjogador1 >= valorpropriedade2:
                    valorjogador1 -= valorpropriedade2
                    Propriedade2 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Sergipe ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Sergipe ")
            elif Propriedade2 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Sergipe ")
            else:
                if Propriedade2 == nomejog2:
                    valorjogador2 += AluguelPropriedade2
                    valorjogador1 -= AluguelPropriedade2
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade2 == nomejog3:
                    valorjogador3 += AluguelPropriedade2
                    valorjogador1 -= AluguelPropriedade2
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade2 == nomejog4:
                    valorjogador4 += AluguelPropriedade2
                    valorjogador1 -= AluguelPropriedade2
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 3:
            if Propriedade3 == "":
                if valorjogador1 >= valorpropriedade3:
                    valorjogador1 -= valorpropriedade3
                    Propriedade3 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em Tocantins ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Tocantins")
            elif Propriedade3 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em Tocantins")
            else:
                if Propriedade3 == nomejog2:
                    valorjogador2 += AluguelPropriedade3
                    valorjogador1 -= AluguelPropriedade3
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade3 == nomejog3:
                    valorjogador3 += AluguelPropriedade3
                    valorjogador1 -= AluguelPropriedade3
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade3 == nomejog4:
                    valorjogador4 += AluguelPropriedade3
                    valorjogador1 -= AluguelPropriedade3
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 4:
            if Propriedade4 == "":
                if valorjogador1 >= valorpropriedade4:
                    valorjogador1 -= valorpropriedade4
                    Propriedade4 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em Goiás")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Goiás")
            elif Propriedade4 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em Goiás")
            else:
                if Propriedade4 == nomejog2:
                    valorjogador2 += AluguelPropriedade4
                    valorjogador1 -= AluguelPropriedade4
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade4 == nomejog3:
                    valorjogador3 += AluguelPropriedade4
                    valorjogador1 -= AluguelPropriedade4
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade4 == nomejog4:
                    valorjogador4 += AluguelPropriedade4
                    valorjogador1 -= AluguelPropriedade4
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 5:
            if Propriedade5 == "":
                if valorjogador1 >= valorpropriedade5:
                    valorjogador1 -= valorpropriedade5
                    Propriedade5 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Ceará")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Ceará")
            elif Propriedade5 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Ceará")
            else:
                if Propriedade5 == nomejog2:
                    valorjogador2 += AluguelPropriedade5
                    valorjogador1 -= AluguelPropriedade5
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade5 == nomejog3:
                    valorjogador3 += AluguelPropriedade5
                    valorjogador1 -= AluguelPropriedade5
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade5 == nomejog4:
                    valorjogador4 += AluguelPropriedade5
                    valorjogador1 -= AluguelPropriedade5
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 6:
            if Propriedade6 == "":
                if valorjogador1 >= valorpropriedade6:
                    valorjogador1 -= valorpropriedade6
                    Propriedade6 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade na Bahia ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade na Bahia ")
            elif Propriedade6 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade na Bahia ")
            else:
                if Propriedade6 == nomejog2:
                    valorjogador2 += AluguelPropriedade6
                    valorjogador1 -= AluguelPropriedade6
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade6 == nomejog3:
                    valorjogador3 += AluguelPropriedade6
                    valorjogador1 -= AluguelPropriedade6
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade6 == nomejog4:
                    valorjogador4 += AluguelPropriedade6
                    valorjogador1 -= AluguelPropriedade6
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 7:
            if Propriedade7 == "":
                if valorjogador1 >= valorpropriedade7:
                    valorjogador1 -= valorpropriedade7
                    Propriedade7 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade na Paraíba ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade na Paraíba ")
            elif Propriedade7 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade na Paraíba ")
            else:
                if Propriedade7 == nomejog2:
                    valorjogador2 += AluguelPropriedade7
                    valorjogador1 -= AluguelPropriedade7
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade7 == nomejog3:
                    valorjogador3 += AluguelPropriedade7
                    valorjogador1 -= AluguelPropriedade7
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade7 == nomejog4:
                    valorjogador4 += AluguelPropriedade7
                    valorjogador1 -= AluguelPropriedade7
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 8:
            if Propriedade8 == "":
                if valorjogador1 >= valorpropriedade8:
                    valorjogador1 -= valorpropriedade8
                    Propriedade8 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Amazonas ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Amazonas ")
            elif Propriedade8 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Amazonas ")
            else:
                if Propriedade8 == nomejog2:
                    valorjogador2 += 30
                    valorjogador1 -= 30
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$30,00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade8 == nomejog3:
                    valorjogador3 += 30
                    valorjogador1 -= 30
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$30,00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade8 == nomejog4:
                    valorjogador4 += 30
                    valorjogador1 -= 30
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$30,00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 9:
            if Propriedade9 == "":
                if valorjogador1 >= valorpropriedade9:
                    valorjogador1 -= valorpropriedade9
                    Propriedade9 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em Minas Gerais")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Minas Gerais")
            elif Propriedade9 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em Minas Gerais")
            else:
                if Propriedade9 == nomejog2:
                    valorjogador2 += AluguelPropriedade9
                    valorjogador1 -= AluguelPropriedade9
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade9 == nomejog3:
                    valorjogador3 += AluguelPropriedade9
                    valorjogador1 -= AluguelPropriedade9
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade9 == nomejog4:
                    valorjogador4 += AluguelPropriedade9
                    valorjogador1 -= AluguelPropriedade9
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 10:
            if Propriedade10 == "":
                if valorjogador1 >= valorpropriedade10:
                    valorjogador1 -= valorpropriedade10
                    Propriedade10 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em Santa Catarina")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Santa Catarina")
            elif Propriedade10 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em Santa Catarina")
            else:
                if Propriedade10 == nomejog2:
                    valorjogador2 += AluguelPropriedade10
                    valorjogador1 -= AluguelPropriedade10
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade10 == nomejog3:
                    valorjogador3 += AluguelPropriedade10
                    valorjogador1 -= AluguelPropriedade10
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade10 == nomejog4:
                    valorjogador4 += AluguelPropriedade10
                    valorjogador1 -= AluguelPropriedade10
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 11:
            if Propriedade11 == "":
                if valorjogador1 >= valorpropriedade11:
                    valorjogador1 -= valorpropriedade11
                    Propriedade11 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em Rondônia")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Rondônia")
            elif Propriedade11 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em Rondônia")
            else:
                if Propriedade11 == nomejog2:
                    valorjogador2 += AluguelPropriedade11
                    valorjogador1 -= AluguelPropriedade11
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade11 == nomejog3:
                    valorjogador3 += AluguelPropriedade11
                    valorjogador1 -= AluguelPropriedade11
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade11 == nomejog4:
                    valorjogador4 += AluguelPropriedade11
                    valorjogador1 -= AluguelPropriedade11
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 12:
            if Propriedade12 == "":
                if valorjogador1 >= valorpropriedade12:
                    valorjogador1 -= valorpropriedade12
                    Propriedade12 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Rio de Janeiro")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Rio de Janeiro")
            elif Propriedade12 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Rio de Janeiro")
            else:
                if Propriedade12 == nomejog2:
                    valorjogador2 += AluguelPropriedade12
                    valorjogador1 -= AluguelPropriedade12
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade12 == nomejog3:
                    valorjogador3 += AluguelPropriedade12
                    valorjogador1 -= AluguelPropriedade12
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade12 == nomejog4:
                    valorjogador4 += AluguelPropriedade12
                    valorjogador1 -= AluguelPropriedade12
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 13:
            if Propriedade13 == "":
                if valorjogador1 >= valorpropriedade13:
                    valorjogador1 -= valorpropriedade13
                    Propriedade13 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em Alagoas")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Alagoas")
            elif Propriedade13 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em Alagoas")
            else:
                if Propriedade13 == nomejog2:
                    valorjogador2 += AluguelPropriedade13
                    valorjogador1 -= AluguelPropriedade13
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade13 == nomejog3:
                    valorjogador3 += AluguelPropriedade13
                    valorjogador1 -= AluguelPropriedade13
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade13 == nomejog4:
                    valorjogador4 += AluguelPropriedade13
                    valorjogador1 -= AluguelPropriedade13
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 14:
            if Propriedade14 == "":
                if valorjogador1 >= valorpropriedade14:
                    valorjogador1 -= valorpropriedade14
                    Propriedade14 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Acre ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Acre ")
            elif Propriedade14 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Acre ")
            else:
                if Propriedade14 == nomejog2:
                    valorjogador2 += AluguelPropriedade14
                    valorjogador1 -= AluguelPropriedade14
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade14 == nomejog3:
                    valorjogador3 += AluguelPropriedade14
                    valorjogador1 -= AluguelPropriedade14
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade14 == nomejog4:
                    valorjogador4 += AluguelPropriedade14
                    valorjogador1 -= AluguelPropriedade14
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 15:
            if Propriedade15 == "":
                if valorjogador1 >= valorpropriedade15:
                    valorjogador1 -= valorpropriedade15
                    Propriedade15 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em São Paulo")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em São Paulo")
            elif Propriedade15 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em São Paulo")
            else:
                if Propriedade15 == nomejog2:
                    valorjogador2 += AluguelPropriedade15
                    valorjogador1 -= AluguelPropriedade15
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade15 == nomejog3:
                    valorjogador3 += AluguelPropriedade15
                    valorjogador1 -= AluguelPropriedade15
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade15 == nomejog4:
                    valorjogador4 += AluguelPropriedade15
                    valorjogador1 -= AluguelPropriedade15
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 16:
            if Propriedade16 == "":
                if valorjogador1 >= valorpropriedade16:
                    valorjogador1 -= valorpropriedade16
                    Propriedade16 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em Mato Grosso")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Mato Grosso")
            elif Propriedade16 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em Mato Grosso")
            else:
                if Propriedade16 == nomejog2:
                    valorjogador2 += AluguelPropriedade16
                    valorjogador1 -= AluguelPropriedade16
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade16 == nomejog3:
                    valorjogador3 += AluguelPropriedade16
                    valorjogador1 -= AluguelPropriedade16
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade16 == nomejog4:
                    valorjogador4 += AluguelPropriedade16
                    valorjogador1 -= AluguelPropriedade16
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 17:
            if Propriedade17 == "":
                if valorjogador1 >= valorpropriedade17:
                    valorjogador1 -= valorpropriedade17
                    Propriedade17 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Espirito Santo ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Espirito Santo ")
            elif Propriedade17 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Espirito Santo ")
            else:
                if Propriedade17 == nomejog2:
                    valorjogador2 += AluguelPropriedade17
                    valorjogador1 -= AluguelPropriedade17
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade17 == nomejog3:
                    valorjogador3 += AluguelPropriedade17
                    valorjogador1 -= AluguelPropriedade17
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade17 == nomejog4:
                    valorjogador4 += AluguelPropriedade17
                    valorjogador1 -= AluguelPropriedade17
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 18:
            if Propriedade18 == "":
                if valorjogador1 >= valorpropriedade18:
                    valorjogador1 -= valorpropriedade18
                    Propriedade18 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade em Roraima")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade em Roraima")
            elif Propriedade18 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade em Roraima")
            else:
                if Propriedade18 == nomejog2:
                    valorjogador2 += AluguelPropriedade18
                    valorjogador1 -= AluguelPropriedade18
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade18 == nomejog3:
                    valorjogador3 += AluguelPropriedade18
                    valorjogador1 -= AluguelPropriedade18
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade18 == nomejog4:
                    valorjogador4 += AluguelPropriedade18
                    valorjogador1 -= AluguelPropriedade18
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 19:
            if Propriedade19 == "":
                if valorjogador1 >= valorpropriedade19:
                    valorjogador1 -= valorpropriedade19
                    Propriedade19 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Maranhão")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Maranhão ")
            elif Propriedade19 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Maranhão ")
            else:
                if Propriedade19 == nomejog2:
                    valorjogador2 += AluguelPropriedade19
                    valorjogador1 -= AluguelPropriedade19
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade19 == nomejog3:
                    valorjogador3 += AluguelPropriedade19
                    valorjogador1 -= AluguelPropriedade19
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade19 == nomejog4:
                    valorjogador4 += AluguelPropriedade19
                    valorjogador1 -= AluguelPropriedade19
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        elif posjog1 == 20:
            if Propriedade20 == "":
                if valorjogador1 >= valorpropriedade20:
                    valorjogador1 -= valorpropriedade20
                    Propriedade20 = nomejog1
                    print(str(nomejog1) + " comprou a propriedade no Piauí ")
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                else:
                    print(str(nomejog1) + ", você não possui dinheiro para comprar a propriedade no Piauí ")
            elif Propriedade20 == nomejog1:
                print(str(nomejog1) + " você já possui a propriedade no Piauí ")
            else:
                if Propriedade20 == nomejog2:
                    valorjogador2 += AluguelPropriedade20
                    valorjogador1 -= AluguelPropriedade20
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog2)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade20 == nomejog3:
                    valorjogador3 += AluguelPropriedade20
                    valorjogador1 -= AluguelPropriedade20
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog3)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))
                elif Propriedade20 == nomejog4:
                    valorjogador4 += AluguelPropriedade20
                    valorjogador1 -= AluguelPropriedade20
                    print(str(nomejog1) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog4)
                    print(str(nomejog1) + " possui em conta R$", format(valorjogador1, '.2f'))

        # Verifica se Jogador Faliu
        if valorjogador1 < 0:
            if Propriedade1 == nomejog1:
                Propriedade1 = ""
            if Propriedade2 == nomejog1:
                Propriedade2 = ""
            if Propriedade3 == nomejog1:
                Propriedade3 = ""
            if Propriedade4 == nomejog1:
                Propriedade4 = ""
            if Propriedade5 == nomejog1:
                Propriedade5 = ""
            if Propriedade6 == nomejog1:
                Propriedade6 = ""
            if Propriedade7 == nomejog1:
                Propriedade7 = ""
            if Propriedade8 == nomejog1:
                Propriedade8 = ""
            if Propriedade9 == nomejog1:
                Propriedade9 = ""
            if Propriedade10 == nomejog1:
                Propriedade10 = ""
            if Propriedade11 == nomejog1:
                Propriedade11 = ""
            if Propriedade12 == nomejog1:
                Propriedade12 = ""
            if Propriedade13 == nomejog1:
                Propriedade13 = ""
            if Propriedade14 == nomejog1:
                Propriedade14 = ""
            if Propriedade15 == nomejog1:
                Propriedade15 = ""
            if Propriedade16 == nomejog1:
                Propriedade16 = ""
            if Propriedade17 == nomejog1:
                Propriedade17 = ""
            if Propriedade18 == nomejog1:
                Propriedade18 = ""
            if Propriedade19 == nomejog1:
                Propriedade19 = ""
            if Propriedade20 == nomejog1:
                Propriedade20 = ""
            print(str(nomejog1) + " faliu! XXX Está Fora do Jogo e Perdeu todas suas Propriedades XXX")
            faliujog1 = True
            lista_de_faliu.append(nomejog1)

    # Jogadas do Jogador 2 - Exigente
    if not faliujog2 and nomejog2 != "":
        print(str(nomejog2) + " você está na casa: " + str(posjog2))
        print(str(nomejog2) + " você possui em conta R$" + format(valorjogador2, '.2f'))
        dado = random.randint(1, 6)
        print("Valor do dado:", dado)
        posjog2 += dado

        # Verifica Posição no Tabuleiro
        if posjog2 > 20:
            dado = posjog2 - 20
            posjog2 = dado - 1
            valorjogador2 += 100
            print(nomejog2, "Você recebeu R$100,00 por atravessar todo o tabuleiro")

        if posjog2 == 1:
            if Propriedade1 == "":
                if valorjogador2 >= valorpropriedade1:
                    if AluguelPropriedade1 > 50:
                        valorjogador2 -= valorpropriedade1
                        Propriedade1 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade no Pará ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade no Pará inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Pará ")
            elif Propriedade1 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Pará ")
            else:
                if Propriedade1 == nomejog1:
                    valorjogador1 += AluguelPropriedade1
                    valorjogador2 -= AluguelPropriedade1
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade1 == nomejog3:
                    valorjogador3 += AluguelPropriedade1
                    valorjogador2 -= AluguelPropriedade1
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade1 == nomejog4:
                    valorjogador4 += AluguelPropriedade1
                    valorjogador2 -= AluguelPropriedade1
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 2:
            if Propriedade2 == "":
                if valorjogador2 >= valorpropriedade2:
                    if AluguelPropriedade2 > 50:
                        valorjogador2 -= valorpropriedade2
                        Propriedade2 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade no Sergipe ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade no Sergipe inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Sergipe ")
            elif Propriedade2 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Sergipe ")
            else:
                if Propriedade2 == nomejog1:
                    valorjogador1 += AluguelPropriedade2
                    valorjogador2 -= AluguelPropriedade2
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade2 == nomejog3:
                    valorjogador3 += AluguelPropriedade2
                    valorjogador2 -= AluguelPropriedade2
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade2 == nomejog4:
                    valorjogador4 += AluguelPropriedade2
                    valorjogador2 -= AluguelPropriedade2
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 3:
            if Propriedade3 == "":
                if valorjogador2 >= valorpropriedade3:
                    if AluguelPropriedade3 > 50:
                        valorjogador2 -= valorpropriedade3
                        Propriedade3 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em Tocantins ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade no Tocantins inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Tocantins")
            elif Propriedade3 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em Tocantins")
            else:
                if Propriedade3 == nomejog1:
                    valorjogador1 += AluguelPropriedade3
                    valorjogador2 -= AluguelPropriedade3
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade3 == nomejog3:
                    valorjogador3 += AluguelPropriedade3
                    valorjogador2 -= AluguelPropriedade3
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade3 == nomejog4:
                    valorjogador4 += AluguelPropriedade3
                    valorjogador2 -= AluguelPropriedade3
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 4:
            if Propriedade4 == "":
                if valorjogador2 >= valorpropriedade4:
                    if AluguelPropriedade4 > 50:
                        valorjogador2 -= valorpropriedade4
                        Propriedade4 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em Goiás")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade em Goiás inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Goiás")
            elif Propriedade4 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em Goiás")
            else:
                if Propriedade4 == nomejog1:
                    valorjogador1 += AluguelPropriedade4
                    valorjogador2 -= AluguelPropriedade4
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade4 == nomejog3:
                    valorjogador3 += AluguelPropriedade4
                    valorjogador2 -= AluguelPropriedade4
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade4 == nomejog4:
                    valorjogador4 += AluguelPropriedade4
                    valorjogador2 -= AluguelPropriedade4
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 5:
            if Propriedade5 == "":
                if valorjogador2 >= valorpropriedade5:
                    if AluguelPropriedade5 > 50:
                        valorjogador2 -= valorpropriedade5
                        Propriedade5 = nomejog1
                        print(str(nomejog2) + " comprou a propriedade no Ceará")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade no Ceará inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Ceará")
            elif Propriedade5 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Ceará")
            else:
                if Propriedade5 == nomejog1:
                    valorjogador1 += AluguelPropriedade5
                    valorjogador2 -= AluguelPropriedade5
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade5 == nomejog3:
                    valorjogador3 += AluguelPropriedade5
                    valorjogador2 -= AluguelPropriedade5
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade5 == nomejog4:
                    valorjogador4 += AluguelPropriedade5
                    valorjogador2 -= AluguelPropriedade5
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 6:
            if Propriedade6 == "":
                if valorjogador2 >= valorpropriedade6:
                    if AluguelPropriedade6 > 50:
                        valorjogador2 -= valorpropriedade6
                        Propriedade6 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade na Bahia ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade na Bahia inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade na Bahia ")
            elif Propriedade6 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade na Bahia ")
            else:
                if Propriedade6 == nomejog1:
                    valorjogador1 += AluguelPropriedade6
                    valorjogador2 -= AluguelPropriedade6
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade6 == nomejog3:
                    valorjogador3 += AluguelPropriedade6
                    valorjogador2 -= AluguelPropriedade6
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade6 == nomejog4:
                    valorjogador4 += AluguelPropriedade6
                    valorjogador2 -= AluguelPropriedade6
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 7:
            if Propriedade7 == "":
                if valorjogador2 >= valorpropriedade7:
                    if AluguelPropriedade7 > 50:
                        valorjogador2 -= valorpropriedade7
                        Propriedade7 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade na Paraíba ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade na Paraíba inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade na Paraíba ")
            elif Propriedade7 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade na Paraíba ")
            else:
                if Propriedade7 == nomejog1:
                    valorjogador1 += AluguelPropriedade7
                    valorjogador2 -= AluguelPropriedade7
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade7 == nomejog3:
                    valorjogador3 += AluguelPropriedade7
                    valorjogador2 -= AluguelPropriedade7
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade7 == nomejog4:
                    valorjogador4 += AluguelPropriedade7
                    valorjogador2 -= AluguelPropriedade7
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 8:
            if Propriedade8 == "":
                if valorjogador2 >= valorpropriedade8:
                    if AluguelPropriedade8 > 50:
                        valorjogador2 -= valorpropriedade8
                        Propriedade8 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade no Amazonas ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade no Amazonas inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Amazonas ")
            elif Propriedade8 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Amazonas ")
            else:
                if Propriedade8 == nomejog1:
                    valorjogador1 += 30
                    valorjogador2 -= 30
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$30,00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade8 == nomejog3:
                    valorjogador3 += 30
                    valorjogador2 -= 30
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$30,00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade8 == nomejog4:
                    valorjogador4 += 30
                    valorjogador2 -= 30
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$30,00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 9:
            if Propriedade9 == "":
                if valorjogador2 >= valorpropriedade9:
                    if AluguelPropriedade9 > 50:
                        valorjogador2 -= valorpropriedade9
                        Propriedade9 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em Minas Gerais")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade em Minas Gerais inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Minas Gerais")
            elif Propriedade9 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em Minas Gerais")
            else:
                if Propriedade9 == nomejog1:
                    valorjogador1 += AluguelPropriedade9
                    valorjogador2 -= AluguelPropriedade9
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade9 == nomejog3:
                    valorjogador3 += AluguelPropriedade9
                    valorjogador2 -= AluguelPropriedade9
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade9 == nomejog4:
                    valorjogador4 += AluguelPropriedade9
                    valorjogador2 -= AluguelPropriedade9
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 10:
            if Propriedade10 == "":
                if valorjogador2 >= valorpropriedade10:
                    if AluguelPropriedade10 > 50:
                        valorjogador2 -= valorpropriedade10
                        Propriedade10 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em Santa Catarina")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade em Santa Catarina inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Santa Catarina")
            elif Propriedade10 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em Santa Catarina")
            else:
                if Propriedade10 == nomejog1:
                    valorjogador1 += AluguelPropriedade10
                    valorjogador2 -= AluguelPropriedade10
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade10 == nomejog3:
                    valorjogador3 += AluguelPropriedade10
                    valorjogador2 -= AluguelPropriedade10
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade10 == nomejog4:
                    valorjogador4 += AluguelPropriedade10
                    valorjogador2 -= AluguelPropriedade10
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 11:
            if Propriedade11 == "":
                if valorjogador2 >= valorpropriedade11:
                    if AluguelPropriedade11 > 50:
                        valorjogador2 -= valorpropriedade11
                        Propriedade11 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em Rondônia")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade em Rondônia inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Rondônia")
            elif Propriedade11 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em Rondônia")
            else:
                if Propriedade11 == nomejog1:
                    valorjogador1 += AluguelPropriedade11
                    valorjogador2 -= AluguelPropriedade11
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade11 == nomejog3:
                    valorjogador3 += AluguelPropriedade11
                    valorjogador2 -= AluguelPropriedade11
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade11 == nomejog4:
                    valorjogador4 += AluguelPropriedade11
                    valorjogador2 -= AluguelPropriedade11
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 12:
            if Propriedade12 == "":
                if valorjogador2 >= valorpropriedade12:
                    if AluguelPropriedade12 > 50:
                        valorjogador2 -= valorpropriedade12
                        Propriedade12 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade no Rio de Janeiro")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade no Rio de Janeiro inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Rio de Janeiro")
            elif Propriedade12 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Rio de Janeiro")
            else:
                if Propriedade12 == nomejog1:
                    valorjogador1 += AluguelPropriedade12
                    valorjogador2 -= AluguelPropriedade12
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade12 == nomejog3:
                    valorjogador3 += AluguelPropriedade12
                    valorjogador2 -= AluguelPropriedade12
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade12 == nomejog4:
                    valorjogador4 += AluguelPropriedade12
                    valorjogador2 -= AluguelPropriedade12
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 13:
            if Propriedade13 == "":
                if valorjogador2 >= valorpropriedade13:
                    if AluguelPropriedade13 > 50:
                        valorjogador2 -= valorpropriedade13
                        Propriedade13 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em Alagoas")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade em Alagoas inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Alagoas")
            elif Propriedade13 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em Alagoas")
            else:
                if Propriedade13 == nomejog1:
                    valorjogador1 += AluguelPropriedade13
                    valorjogador2 -= AluguelPropriedade13
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade13 == nomejog3:
                    valorjogador3 += AluguelPropriedade13
                    valorjogador2 -= AluguelPropriedade13
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade13 == nomejog4:
                    valorjogador4 += AluguelPropriedade13
                    valorjogador2 -= AluguelPropriedade13
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 14:
            if Propriedade14 == "":
                if valorjogador2 >= valorpropriedade14:
                    if AluguelPropriedade14 > 50:
                        valorjogador2 -= valorpropriedade14
                        Propriedade14 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade no Acre ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", Aluguel da propriedade no Acre inferior a R$ 50,00")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Acre ")
            elif Propriedade14 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Acre ")
            else:
                if Propriedade14 == nomejog1:
                    valorjogador1 += AluguelPropriedade14
                    valorjogador2 -= AluguelPropriedade14
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade14 == nomejog3:
                    valorjogador3 += AluguelPropriedade14
                    valorjogador2 -= AluguelPropriedade14
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade14 == nomejog4:
                    valorjogador4 += AluguelPropriedade14
                    valorjogador2 -= AluguelPropriedade14
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 15:
            if Propriedade15 == "":
                if valorjogador2 >= valorpropriedade15:
                    if AluguelPropriedade15 > 50:
                        valorjogador2 -= valorpropriedade15
                        Propriedade15 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em São Paulo")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em São Paulo ")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em São Paulo")
            elif Propriedade15 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em São Paulo")
            else:
                if Propriedade15 == nomejog1:
                    valorjogador1 += AluguelPropriedade15
                    valorjogador2 -= AluguelPropriedade15
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade15 == nomejog3:
                    valorjogador3 += AluguelPropriedade15
                    valorjogador2 -= AluguelPropriedade15
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade15 == nomejog4:
                    valorjogador4 += AluguelPropriedade15
                    valorjogador2 -= AluguelPropriedade15
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 16:
            if Propriedade16 == "":
                if valorjogador2 >= valorpropriedade16:
                    if AluguelPropriedade16 > 50:
                        valorjogador2 -= valorpropriedade16
                        Propriedade16 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em Mato Grosso")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Mato Grosso")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Mato Grosso")
            elif Propriedade16 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em Mato Grosso")
            else:
                if Propriedade16 == nomejog1:
                    valorjogador1 += AluguelPropriedade16
                    valorjogador2 -= AluguelPropriedade16
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade16 == nomejog3:
                    valorjogador3 += AluguelPropriedade16
                    valorjogador2 -= AluguelPropriedade16
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade16 == nomejog4:
                    valorjogador4 += AluguelPropriedade16
                    valorjogador2 -= AluguelPropriedade16
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 17:
            if Propriedade17 == "":
                if valorjogador2 >= valorpropriedade17:
                    if AluguelPropriedade17 > 50:
                        valorjogador2 -= valorpropriedade17
                        Propriedade17 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade no Espirito Santo ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Espirito Santo")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Espirito Santo ")
            elif Propriedade17 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Espirito Santo ")
            else:
                if Propriedade17 == nomejog1:
                    valorjogador1 += AluguelPropriedade17
                    valorjogador2 -= AluguelPropriedade17
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade17 == nomejog3:
                    valorjogador3 += AluguelPropriedade17
                    valorjogador2 -= AluguelPropriedade17
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade17 == nomejog4:
                    valorjogador4 += AluguelPropriedade17
                    valorjogador2 -= AluguelPropriedade17
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 18:
            if Propriedade18 == "":
                if valorjogador2 >= valorpropriedade18:
                    if AluguelPropriedade18 > 50:
                        valorjogador2 -= valorpropriedade18
                        Propriedade18 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade em Roraima")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Roraima")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade em Roraima")
            elif Propriedade18 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade em Roraima")
            else:
                if Propriedade18 == nomejog1:
                    valorjogador1 += AluguelPropriedade18
                    valorjogador2 -= AluguelPropriedade18
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade18 == nomejog3:
                    valorjogador3 += AluguelPropriedade18
                    valorjogador2 -= AluguelPropriedade18
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade18 == nomejog4:
                    valorjogador4 += AluguelPropriedade18
                    valorjogador2 -= AluguelPropriedade18
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 19:
            if Propriedade19 == "":
                if valorjogador2 >= valorpropriedade19:
                    if AluguelPropriedade19 > 50:
                        valorjogador2 -= valorpropriedade19
                        Propriedade19 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade no Maranhão")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Maranhão")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Maranhão ")
            elif Propriedade19 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Maranhão ")
            else:
                if Propriedade19 == nomejog1:
                    valorjogador1 += AluguelPropriedade19
                    valorjogador2 -= AluguelPropriedade19
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade19 == nomejog3:
                    valorjogador3 += AluguelPropriedade19
                    valorjogador2 -= AluguelPropriedade19
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade19 == nomejog4:
                    valorjogador4 += AluguelPropriedade19
                    valorjogador2 -= AluguelPropriedade19
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        elif posjog2 == 20:
            if Propriedade20 == "":
                if valorjogador2 >= valorpropriedade20:
                    if AluguelPropriedade20 > 50:
                        valorjogador2 -= valorpropriedade20
                        Propriedade20 = nomejog2
                        print(str(nomejog2) + " comprou a propriedade no Piauí ")
                        print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                    else:
                        print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Piauí")
                else:
                    print(str(nomejog2) + ", você não possui dinheiro para comprar a propriedade no Piauí ")
            elif Propriedade20 == nomejog2:
                print(str(nomejog2) + " você já possui a propriedade no Piauí ")
            else:
                if Propriedade20 == nomejog1:
                    valorjogador1 += AluguelPropriedade20
                    valorjogador2 -= AluguelPropriedade20
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog1)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade20 == nomejog3:
                    valorjogador3 += AluguelPropriedade20
                    valorjogador2 -= AluguelPropriedade20
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog3)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))
                elif Propriedade20 == nomejog4:
                    valorjogador4 += AluguelPropriedade20
                    valorjogador2 -= AluguelPropriedade20
                    print(str(nomejog2) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog4)
                    print(str(nomejog2) + " possui em conta R$", format(valorjogador2, '.2f'))

        # Verifica se Jogador Faliu
        if valorjogador2 < 0:
            if Propriedade1 == nomejog2:
                Propriedade1 = ""
            if Propriedade2 == nomejog2:
                Propriedade2 = ""
            if Propriedade3 == nomejog2:
                Propriedade3 = ""
            if Propriedade4 == nomejog2:
                Propriedade4 = ""
            if Propriedade5 == nomejog2:
                Propriedade5 = ""
            if Propriedade6 == nomejog2:
                Propriedade6 = ""
            if Propriedade7 == nomejog2:
                Propriedade7 = ""
            if Propriedade8 == nomejog2:
                Propriedade8 = ""
            if Propriedade9 == nomejog2:
                Propriedade9 = ""
            if Propriedade10 == nomejog2:
                Propriedade10 = ""
            if Propriedade11 == nomejog2:
                Propriedade11 = ""
            if Propriedade12 == nomejog2:
                Propriedade12 = ""
            if Propriedade13 == nomejog2:
                Propriedade13 = ""
            if Propriedade14 == nomejog2:
                Propriedade14 = ""
            if Propriedade15 == nomejog2:
                Propriedade15 = ""
            if Propriedade16 == nomejog2:
                Propriedade16 = ""
            if Propriedade17 == nomejog2:
                Propriedade17 = ""
            if Propriedade18 == nomejog2:
                Propriedade18 = ""
            if Propriedade19 == nomejog2:
                Propriedade19 = ""
            if Propriedade20 == nomejog2:
                Propriedade20 = ""
            print(str(nomejog2) + " faliu! XXX Está Fora do Jogo e Perdeu todas suas Propriedades XXX")
            faliujog2 = True
            lista_de_faliu.append(nomejog2)

    # Jogadas do Jogador 3 - Cauteloso
    if not faliujog3 and nomejog3 != "":
        print(str(nomejog3) + " você está na casa: " + str(posjog3))
        print(str(nomejog3) + " você possui em conta R$" + format(valorjogador3, '.2f'))
        dado = random.randint(1, 6)
        print("Valor do dado:", dado)
        posjog3 += dado

        # Verifica Posição no Tabuleiro
        if posjog3 > 20:
            dado = posjog3 - 20
            posjog3 = dado - 1
            valorjogador3 += 100
            print(nomejog3, "Você recebeu R$100,00 por atravessar todo o tabuleiro")

        if posjog3 == 1:
            if Propriedade1 == "":
                if valorjogador3 >= valorpropriedade1 and (valorjogador3 - valorpropriedade1) >= 80:
                    valorjogador3 -= valorpropriedade1
                    Propriedade1 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Pará ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Pará ")
            elif Propriedade1 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Pará ")
            else:
                if Propriedade1 == nomejog1:
                    valorjogador1 += AluguelPropriedade1
                    valorjogador3 -= AluguelPropriedade1
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade1 == nomejog2:
                    valorjogador2 += AluguelPropriedade1
                    valorjogador3 -= AluguelPropriedade1
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade1 == nomejog4:
                    valorjogador4 += AluguelPropriedade1
                    valorjogador3 -= AluguelPropriedade1
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 2:
            if Propriedade2 == "":
                if valorjogador3 >= valorpropriedade2 and (valorjogador3 - valorpropriedade2) >= 80:
                    valorjogador3 -= valorpropriedade2
                    Propriedade2 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Sergipe ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Sergipe ")
            elif Propriedade2 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Sergipe ")
            else:
                if Propriedade2 == nomejog1:
                    valorjogador1 += AluguelPropriedade2
                    valorjogador3 -= AluguelPropriedade2
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade2 == nomejog2:
                    valorjogador2 += AluguelPropriedade2
                    valorjogador3 -= AluguelPropriedade2
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade2 == nomejog4:
                    valorjogador4 += AluguelPropriedade2
                    valorjogador3 -= AluguelPropriedade2
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 3:
            if Propriedade3 == "":
                if valorjogador3 >= valorpropriedade3 and (valorjogador3 - valorpropriedade3) >= 80:
                    valorjogador3 -= valorpropriedade3
                    Propriedade3 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Tocantins ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Tocantins")
            elif Propriedade3 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em Tocantins")
            else:
                if Propriedade3 == nomejog1:
                    valorjogador1 += AluguelPropriedade3
                    valorjogador3 -= AluguelPropriedade3
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade3 == nomejog2:
                    valorjogador2 += AluguelPropriedade3
                    valorjogador3 -= AluguelPropriedade3
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade3 == nomejog4:
                    valorjogador4 += AluguelPropriedade3
                    valorjogador3 -= AluguelPropriedade3
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 4:
            if Propriedade4 == "":
                if valorjogador3 >= valorpropriedade4 and (valorjogador3 - valorpropriedade4) >= 80:
                    valorjogador3 -= valorpropriedade4
                    Propriedade4 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade em Goiás ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Goiás")
            elif Propriedade4 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em Goiás")
            else:
                if Propriedade4 == nomejog1:
                    valorjogador1 += AluguelPropriedade4
                    valorjogador3 -= AluguelPropriedade4
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade4 == nomejog2:
                    valorjogador2 += AluguelPropriedade4
                    valorjogador3 -= AluguelPropriedade4
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade4 == nomejog4:
                    valorjogador4 += AluguelPropriedade4
                    valorjogador3 -= AluguelPropriedade4
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 5:
            if Propriedade5 == "":
                if valorjogador3 >= valorpropriedade5 and (valorjogador3 - valorpropriedade5) >= 80:
                    valorjogador3 -= valorpropriedade5
                    Propriedade5 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Ceará ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Ceará")
            elif Propriedade5 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Ceará")
            else:
                if Propriedade5 == nomejog1:
                    valorjogador1 += AluguelPropriedade5
                    valorjogador3 -= AluguelPropriedade5
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade5 == nomejog2:
                    valorjogador2 += AluguelPropriedade5
                    valorjogador3 -= AluguelPropriedade5
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade5 == nomejog4:
                    valorjogador4 += AluguelPropriedade5
                    valorjogador3 -= AluguelPropriedade5
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 6:
            if Propriedade6 == "":
                if valorjogador3 >= valorpropriedade6 and (valorjogador3 - valorpropriedade6) >= 80:
                    valorjogador3 -= valorpropriedade6
                    Propriedade6 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade na Bahia ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade na Bahia ")
            elif Propriedade6 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade na Bahia ")
            else:
                if Propriedade6 == nomejog1:
                    valorjogador1 += AluguelPropriedade6
                    valorjogador3 -= AluguelPropriedade6
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade6 == nomejog2:
                    valorjogador2 += AluguelPropriedade6
                    valorjogador3 -= AluguelPropriedade6
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade6 == nomejog4:
                    valorjogador4 += AluguelPropriedade6
                    valorjogador3 -= AluguelPropriedade6
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 7:
            if Propriedade7 == "":
                if valorjogador3 >= valorpropriedade7 and (valorjogador3 - valorpropriedade7) >= 80:
                    valorjogador3 -= valorpropriedade7
                    Propriedade7 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade na Paraíba ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade na Paraíba ")
            elif Propriedade7 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade na Paraíba ")
            else:
                if Propriedade7 == nomejog1:
                    valorjogador1 += AluguelPropriedade7
                    valorjogador3 -= AluguelPropriedade7
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade7 == nomejog2:
                    valorjogador2 += AluguelPropriedade7
                    valorjogador3 -= AluguelPropriedade7
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade7 == nomejog4:
                    valorjogador4 += AluguelPropriedade7
                    valorjogador3 -= AluguelPropriedade7
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 8:
            if Propriedade8 == "":
                if valorjogador3 >= valorpropriedade8 and (valorjogador3 - valorpropriedade8) >= 80:
                    valorjogador3 -= valorpropriedade8
                    Propriedade8 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Amazonas ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Amazonas ")
            elif Propriedade8 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Amazonas ")
            else:
                if Propriedade8 == nomejog1:
                    valorjogador1 += 30
                    valorjogador3 -= 30
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$30,00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade8 == nomejog2:
                    valorjogador2 += 30
                    valorjogador3 -= 30
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$30,00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade8 == nomejog4:
                    valorjogador4 += 30
                    valorjogador3 -= 30
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$30,00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 9:
            if Propriedade9 == "":
                if valorjogador3 >= valorpropriedade9 and (valorjogador3 - valorpropriedade9) >= 80:
                    valorjogador3 -= valorpropriedade9
                    Propriedade9 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade em Minas Gerais ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Minas Gerais")
            elif Propriedade9 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em Minas Gerais")
            else:
                if Propriedade9 == nomejog1:
                    valorjogador1 += AluguelPropriedade9
                    valorjogador3 -= AluguelPropriedade9
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade9 == nomejog2:
                    valorjogador2 += AluguelPropriedade9
                    valorjogador3 -= AluguelPropriedade9
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade9 == nomejog4:
                    valorjogador4 += AluguelPropriedade9
                    valorjogador3 -= AluguelPropriedade9
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 10:
            if Propriedade10 == "":
                if valorjogador3 >= valorpropriedade10 and (valorjogador3 - valorpropriedade10) >= 80:
                    valorjogador3 -= valorpropriedade10
                    Propriedade10 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade em Santa Catarina ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Santa Catarina")
            elif Propriedade10 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em Santa Catarina")
            else:
                if Propriedade10 == nomejog1:
                    valorjogador1 += AluguelPropriedade10
                    valorjogador3 -= AluguelPropriedade10
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade10 == nomejog2:
                    valorjogador2 += AluguelPropriedade10
                    valorjogador3 -= AluguelPropriedade10
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade10 == nomejog4:
                    valorjogador4 += AluguelPropriedade10
                    valorjogador3 -= AluguelPropriedade10
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 11:
            if Propriedade11 == "":
                if valorjogador3 >= valorpropriedade11 and (valorjogador3 - valorpropriedade11) >= 80:
                    valorjogador3 -= valorpropriedade11
                    Propriedade11 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade em Rondônia ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Rondônia")
            elif Propriedade11 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em Rondônia")
            else:
                if Propriedade11 == nomejog1:
                    valorjogador1 += AluguelPropriedade11
                    valorjogador3 -= AluguelPropriedade11
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade11 == nomejog2:
                    valorjogador2 += AluguelPropriedade11
                    valorjogador3 -= AluguelPropriedade11
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade11 == nomejog4:
                    valorjogador4 += AluguelPropriedade11
                    valorjogador3 -= AluguelPropriedade11
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 12:
            if Propriedade12 == "":
                if valorjogador3 >= valorpropriedade12 and (valorjogador3 - valorpropriedade12) >= 80:
                    valorjogador3 -= valorpropriedade12
                    Propriedade12 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Rio de Janeiro ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Rio de Janeiro")
            elif Propriedade12 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Rio de Janeiro")
            else:
                if Propriedade12 == nomejog1:
                    valorjogador1 += AluguelPropriedade12
                    valorjogador3 -= AluguelPropriedade12
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade12 == nomejog2:
                    valorjogador2 += AluguelPropriedade12
                    valorjogador3 -= AluguelPropriedade12
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade12 == nomejog4:
                    valorjogador4 += AluguelPropriedade12
                    valorjogador3 -= AluguelPropriedade12
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 13:
            if Propriedade13 == "":
                if valorjogador3 >= valorpropriedade13 and (valorjogador3 - valorpropriedade13) >= 80:
                    valorjogador3 -= valorpropriedade13
                    Propriedade13 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade em Alagoas ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Alagoas")
            elif Propriedade13 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em Alagoas")
            else:
                if Propriedade13 == nomejog1:
                    valorjogador1 += AluguelPropriedade13
                    valorjogador3 -= AluguelPropriedade13
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade13 == nomejog2:
                    valorjogador2 += AluguelPropriedade13
                    valorjogador3 -= AluguelPropriedade13
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade13 == nomejog4:
                    valorjogador4 += AluguelPropriedade13
                    valorjogador3 -= AluguelPropriedade13
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 14:
            if Propriedade14 == "":
                if valorjogador3 >= valorpropriedade14 and (valorjogador3 - valorpropriedade14) >= 80:
                    valorjogador3 -= valorpropriedade14
                    Propriedade14 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Acre ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Acre ")
            elif Propriedade14 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Acre ")
            else:
                if Propriedade14 == nomejog1:
                    valorjogador1 += AluguelPropriedade14
                    valorjogador3 -= AluguelPropriedade14
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade14 == nomejog2:
                    valorjogador2 += AluguelPropriedade14
                    valorjogador3 -= AluguelPropriedade14
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade14 == nomejog4:
                    valorjogador4 += AluguelPropriedade14
                    valorjogador3 -= AluguelPropriedade14
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 15:
            if Propriedade15 == "":
                if valorjogador3 >= valorpropriedade15 and (valorjogador3 - valorpropriedade15) >= 80:
                    valorjogador3 -= valorpropriedade15
                    Propriedade15 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade em São Paulo ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em São Paulo")
            elif Propriedade15 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em São Paulo")
            else:
                if Propriedade15 == nomejog1:
                    valorjogador1 += AluguelPropriedade15
                    valorjogador3 -= AluguelPropriedade15
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade15 == nomejog2:
                    valorjogador2 += AluguelPropriedade15
                    valorjogador3 -= AluguelPropriedade15
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade15 == nomejog4:
                    valorjogador4 += AluguelPropriedade15
                    valorjogador3 -= AluguelPropriedade15
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 16:
            if Propriedade16 == "":
                if valorjogador3 >= valorpropriedade16 and (valorjogador3 - valorpropriedade16) >= 80:
                    valorjogador3 -= valorpropriedade16
                    Propriedade16 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade em Mato Grosso ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Mato Grosso")
            elif Propriedade16 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em Mato Grosso")
            else:
                if Propriedade16 == nomejog1:
                    valorjogador1 += AluguelPropriedade16
                    valorjogador3 -= AluguelPropriedade16
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade16 == nomejog2:
                    valorjogador2 += AluguelPropriedade16
                    valorjogador3 -= AluguelPropriedade16
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade16 == nomejog4:
                    valorjogador4 += AluguelPropriedade16
                    valorjogador3 -= AluguelPropriedade16
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 17:
            if Propriedade17 == "":
                if valorjogador3 >= valorpropriedade17 and (valorjogador3 - valorpropriedade17) >= 80:
                    valorjogador3 -= valorpropriedade17
                    Propriedade17 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Espirito Santo ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Espirito Santo ")
            elif Propriedade17 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Espirito Santo ")
            else:
                if Propriedade17 == nomejog1:
                    valorjogador1 += AluguelPropriedade17
                    valorjogador3 -= AluguelPropriedade17
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade17 == nomejog2:
                    valorjogador2 += AluguelPropriedade17
                    valorjogador3 -= AluguelPropriedade17
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade17 == nomejog4:
                    valorjogador4 += AluguelPropriedade17
                    valorjogador3 -= AluguelPropriedade17
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 18:
            if Propriedade18 == "":
                if valorjogador3 >= valorpropriedade18 and (valorjogador3 - valorpropriedade18) >= 80:
                    valorjogador3 -= valorpropriedade18
                    Propriedade18 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade em Roraima ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade em Roraima")
            elif Propriedade18 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade em Roraima")
            else:
                if Propriedade18 == nomejog1:
                    valorjogador1 += AluguelPropriedade18
                    valorjogador3 -= AluguelPropriedade18
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade18 == nomejog2:
                    valorjogador2 += AluguelPropriedade18
                    valorjogador3 -= AluguelPropriedade18
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade18 == nomejog4:
                    valorjogador4 += AluguelPropriedade18
                    valorjogador3 -= AluguelPropriedade18
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 19:
            if Propriedade19 == "":
                if valorjogador3 >= valorpropriedade19 and (valorjogador3 - valorpropriedade19) >= 80:
                    valorjogador3 -= valorpropriedade19
                    Propriedade19 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Maranhão ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Maranhão ")
            elif Propriedade19 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Maranhão ")
            else:
                if Propriedade19 == nomejog1:
                    valorjogador1 += AluguelPropriedade19
                    valorjogador3 -= AluguelPropriedade19
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade19 == nomejog2:
                    valorjogador2 += AluguelPropriedade19
                    valorjogador3 -= AluguelPropriedade19
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade19 == nomejog4:
                    valorjogador4 += AluguelPropriedade19
                    valorjogador3 -= AluguelPropriedade19
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        elif posjog3 == 20:
            if Propriedade20 == "":
                if valorjogador3 >= valorpropriedade20 and (valorjogador3 - valorpropriedade20) >= 80:
                    valorjogador3 -= valorpropriedade20
                    Propriedade20 = nomejog3
                    print(str(nomejog3) + " comprou a propriedade no Piauí ")
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                else:
                    print(str(nomejog3) + ", você não possui dinheiro para comprar a propriedade no Piauí ")
            elif Propriedade20 == nomejog3:
                print(str(nomejog3) + " você já possui a propriedade no Piauí ")
            else:
                if Propriedade20 == nomejog1:
                    valorjogador1 += AluguelPropriedade20
                    valorjogador3 -= AluguelPropriedade20
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog1)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade20 == nomejog2:
                    valorjogador2 += AluguelPropriedade20
                    valorjogador3 -= AluguelPropriedade20
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog2)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))
                elif Propriedade20 == nomejog4:
                    valorjogador4 += AluguelPropriedade20
                    valorjogador3 -= AluguelPropriedade20
                    print(str(nomejog3) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog4)
                    print(str(nomejog3) + " possui em conta R$", format(valorjogador3, '.2f'))

        # Verifica se Jogador Faliu
        if valorjogador3 < 0:
            if Propriedade1 == nomejog3:
                Propriedade1 = ""
            if Propriedade2 == nomejog3:
                Propriedade2 = ""
            if Propriedade3 == nomejog3:
                Propriedade3 = ""
            if Propriedade4 == nomejog3:
                Propriedade4 = ""
            if Propriedade5 == nomejog3:
                Propriedade5 = ""
            if Propriedade6 == nomejog3:
                Propriedade6 = ""
            if Propriedade7 == nomejog3:
                Propriedade7 = ""
            if Propriedade8 == nomejog3:
                Propriedade8 = ""
            if Propriedade9 == nomejog3:
                Propriedade9 = ""
            if Propriedade10 == nomejog3:
                Propriedade10 = ""
            if Propriedade11 == nomejog3:
                Propriedade11 = ""
            if Propriedade12 == nomejog3:
                Propriedade12 = ""
            if Propriedade13 == nomejog3:
                Propriedade13 = ""
            if Propriedade14 == nomejog3:
                Propriedade14 = ""
            if Propriedade15 == nomejog3:
                Propriedade15 = ""
            if Propriedade16 == nomejog3:
                Propriedade16 = ""
            if Propriedade17 == nomejog3:
                Propriedade17 = ""
            if Propriedade18 == nomejog3:
                Propriedade18 = ""
            if Propriedade19 == nomejog3:
                Propriedade19 = ""
            if Propriedade20 == nomejog3:
                Propriedade20 = ""
            print(str(nomejog3) + " faliu! XXX Está Fora do Jogo e Perdeu todas suas Propriedades XXX")
            faliujog3 = True
            lista_de_faliu.append(nomejog3)

    # Jogadas do Jogador 4 - Aleatório
    if not faliujog4 and nomejog4 != "":
        print(str(nomejog4) + " você está na casa: " + str(posjog4))
        print(str(nomejog4) + " você possui em conta R$" + format(valorjogador4, '.2f'))
        dado = random.randint(1, 6)
        compra = random.randint(1, 2)
        print("Valor do dado:", dado)
        posjog4 += dado

        # Verifica Posição no Tabuleiro
        if posjog4 > 20:
            dado = posjog4 - 20
            posjog4 = dado - 1
            valorjogador4 += 100
            print(nomejog4, "Você recebeu R$100,00 por atravessar todo o tabuleiro")

        if posjog4 == 1:
            if Propriedade1 == "":
                if valorjogador4 >= valorpropriedade1:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade1
                        Propriedade1 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade no Pará ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Pará ")
            elif Propriedade1 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Pará ")
            else:
                if Propriedade1 == nomejog1:
                    valorjogador1 += AluguelPropriedade1
                    valorjogador4 -= AluguelPropriedade1
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade1 == nomejog2:
                    valorjogador2 += AluguelPropriedade1
                    valorjogador4 -= AluguelPropriedade1
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade1 == nomejog3:
                    valorjogador3 += AluguelPropriedade1
                    valorjogador4 -= AluguelPropriedade1
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade1) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 2:
            if Propriedade2 == "":
                if valorjogador4 >= valorpropriedade2:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade2
                        Propriedade2 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade no Sergipe ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Sergipe ")
            elif Propriedade2 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Sergipe ")
            else:
                if Propriedade2 == nomejog1:
                    valorjogador1 += AluguelPropriedade2
                    valorjogador4 -= AluguelPropriedade2
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade2 == nomejog2:
                    valorjogador2 += AluguelPropriedade2
                    valorjogador4 -= AluguelPropriedade2
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade2 == nomejog3:
                    valorjogador3 += AluguelPropriedade2
                    valorjogador4 -= AluguelPropriedade2
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade2) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 3:
            if Propriedade3 == "":
                if valorjogador4 >= valorpropriedade3:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade3
                        Propriedade3 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Tocantins ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Tocantins")
            elif Propriedade3 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em Tocantins")
            else:
                if Propriedade3 == nomejog1:
                    valorjogador1 += AluguelPropriedade3
                    valorjogador4 -= AluguelPropriedade3
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade3 == nomejog2:
                    valorjogador2 += AluguelPropriedade3
                    valorjogador4 -= AluguelPropriedade3
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade3 == nomejog3:
                    valorjogador3 += AluguelPropriedade3
                    valorjogador4 -= AluguelPropriedade3
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade3) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 4:
            if Propriedade4 == "":
                if valorjogador4 >= valorpropriedade4:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade4
                        Propriedade4 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Goiás ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Goiás")
            elif Propriedade4 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em Goiás")
            else:
                if Propriedade4 == nomejog1:
                    valorjogador1 += AluguelPropriedade4
                    valorjogador4 -= AluguelPropriedade4
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade4 == nomejog2:
                    valorjogador2 += AluguelPropriedade4
                    valorjogador4 -= AluguelPropriedade4
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade4 == nomejog3:
                    valorjogador3 += AluguelPropriedade4
                    valorjogador4 -= AluguelPropriedade4
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade4) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 5:
            if Propriedade5 == "":
                if valorjogador4 >= valorpropriedade5:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade5
                        Propriedade5 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Ceará ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Ceará")
            elif Propriedade5 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Ceará")
            else:
                if Propriedade5 == nomejog1:
                    valorjogador1 += AluguelPropriedade5
                    valorjogador4 -= AluguelPropriedade5
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade5 == nomejog2:
                    valorjogador2 += AluguelPropriedade5
                    valorjogador4 -= AluguelPropriedade5
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade5 == nomejog3:
                    valorjogador3 += AluguelPropriedade5
                    valorjogador4 -= AluguelPropriedade5
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade5) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 6:
            if Propriedade6 == "":
                if valorjogador4 >= valorpropriedade6:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade6
                        Propriedade6 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade na Bahia ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade na Bahia ")
            elif Propriedade6 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade na Bahia ")
            else:
                if Propriedade6 == nomejog1:
                    valorjogador1 += AluguelPropriedade6
                    valorjogador4 -= AluguelPropriedade6
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade6 == nomejog2:
                    valorjogador2 += AluguelPropriedade6
                    valorjogador4 -= AluguelPropriedade6
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade6 == nomejog3:
                    valorjogador3 += AluguelPropriedade6
                    valorjogador4 -= AluguelPropriedade6
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade6) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 7:
            if Propriedade7 == "":
                if valorjogador4 >= valorpropriedade7:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade7
                        Propriedade7 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade na Paraíba ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade na Paraíba ")
            elif Propriedade7 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade na Paraíba ")
            else:
                if Propriedade7 == nomejog1:
                    valorjogador1 += AluguelPropriedade7
                    valorjogador4 -= AluguelPropriedade7
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade7 == nomejog2:
                    valorjogador2 += AluguelPropriedade7
                    valorjogador4 -= AluguelPropriedade7
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade7 == nomejog3:
                    valorjogador3 += AluguelPropriedade7
                    valorjogador4 -= AluguelPropriedade7
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade7) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 8:
            if Propriedade8 == "":
                if valorjogador4 >= valorpropriedade8:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade8
                        Propriedade8 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade no Amazonas ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Amazonas ")
            elif Propriedade8 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Amazonas ")
            else:
                if Propriedade8 == nomejog1:
                    valorjogador1 += 30
                    valorjogador4 -= 30
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$30,00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade8 == nomejog2:
                    valorjogador2 += 30
                    valorjogador4 -= 30
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$30,00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade8 == nomejog3:
                    valorjogador3 += 30
                    valorjogador4 -= 30
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$30,00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 9:
            if Propriedade9 == "":
                if valorjogador4 >= valorpropriedade9:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade9
                        Propriedade9 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Minas Gerais ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Minas Gerais")
            elif Propriedade9 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em Minas Gerais")
            else:
                if Propriedade9 == nomejog1:
                    valorjogador1 += AluguelPropriedade9
                    valorjogador4 -= AluguelPropriedade9
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade9 == nomejog2:
                    valorjogador2 += AluguelPropriedade9
                    valorjogador4 -= AluguelPropriedade9
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade9 == nomejog3:
                    valorjogador3 += AluguelPropriedade9
                    valorjogador4 -= AluguelPropriedade9
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade9) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 10:
            if Propriedade10 == "":
                if valorjogador4 >= valorpropriedade10:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade10
                        Propriedade10 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Santa Catarina ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Santa Catarina")
            elif Propriedade10 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em Santa Catarina")
            else:
                if Propriedade10 == nomejog1:
                    valorjogador1 += AluguelPropriedade10
                    valorjogador4 -= AluguelPropriedade10
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade10 == nomejog2:
                    valorjogador2 += AluguelPropriedade10
                    valorjogador4 -= AluguelPropriedade10
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade10 == nomejog3:
                    valorjogador3 += AluguelPropriedade10
                    valorjogador4 -= AluguelPropriedade10
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade10) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 11:
            if Propriedade11 == "":
                if valorjogador4 >= valorpropriedade11:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade11
                        Propriedade11 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Rondônia ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Rondônia")
            elif Propriedade11 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em Rondônia")
            else:
                if Propriedade11 == nomejog1:
                    valorjogador1 += AluguelPropriedade11
                    valorjogador4 -= AluguelPropriedade11
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade11 == nomejog2:
                    valorjogador2 += AluguelPropriedade11
                    valorjogador4 -= AluguelPropriedade11
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade11 == nomejog3:
                    valorjogador3 += AluguelPropriedade11
                    valorjogador4 -= AluguelPropriedade11
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade11) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 12:
            if Propriedade12 == "":
                if valorjogador4 >= valorpropriedade12:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade12
                        Propriedade12 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade no Rio de Janeiro ")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Rio de Janeiro")
            elif Propriedade12 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Rio de Janeiro")
            else:
                if Propriedade12 == nomejog1:
                    valorjogador1 += AluguelPropriedade12
                    valorjogador4 -= AluguelPropriedade12
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade12 == nomejog2:
                    valorjogador2 += AluguelPropriedade12
                    valorjogador4 -= AluguelPropriedade12
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade12 == nomejog3:
                    valorjogador3 += AluguelPropriedade12
                    valorjogador4 -= AluguelPropriedade12
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade12) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 13:
            if Propriedade13 == "":
                if valorjogador4 >= valorpropriedade13:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade13
                        Propriedade13 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Alagoas")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Alagoas")
            elif Propriedade13 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em Alagoas")
            else:
                if Propriedade13 == nomejog1:
                    valorjogador1 += AluguelPropriedade13
                    valorjogador4 -= AluguelPropriedade13
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade13 == nomejog2:
                    valorjogador2 += AluguelPropriedade13
                    valorjogador4 -= AluguelPropriedade13
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade13 == nomejog3:
                    valorjogador3 += AluguelPropriedade13
                    valorjogador4 -= AluguelPropriedade13
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade13) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 14:
            if Propriedade14 == "":
                if valorjogador4 >= valorpropriedade14:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade14
                        Propriedade14 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade no Acre")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Acre ")
            elif Propriedade14 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Acre ")
            else:
                if Propriedade14 == nomejog1:
                    valorjogador1 += AluguelPropriedade14
                    valorjogador4 -= AluguelPropriedade14
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade14 == nomejog2:
                    valorjogador2 += AluguelPropriedade14
                    valorjogador4 -= AluguelPropriedade14
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade14 == nomejog3:
                    valorjogador3 += AluguelPropriedade14
                    valorjogador4 -= AluguelPropriedade14
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade14) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 15:
            if Propriedade15 == "":
                if valorjogador4 >= valorpropriedade15:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade15
                        Propriedade15 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em São Paulo")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em São Paulo")
            elif Propriedade15 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em São Paulo")
            else:
                if Propriedade15 == nomejog1:
                    valorjogador1 += AluguelPropriedade15
                    valorjogador4 -= AluguelPropriedade15
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade15 == nomejog2:
                    valorjogador2 += AluguelPropriedade15
                    valorjogador4 -= AluguelPropriedade15
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade15 == nomejog3:
                    valorjogador3 += AluguelPropriedade15
                    valorjogador4 -= AluguelPropriedade15
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade15) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 16:
            if Propriedade16 == "":
                if valorjogador4 >= valorpropriedade16:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade16
                        Propriedade16 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Mato Grosso")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Mato Grosso")
            elif Propriedade16 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em Mato Grosso")
            else:
                if Propriedade16 == nomejog1:
                    valorjogador1 += AluguelPropriedade16
                    valorjogador4 -= AluguelPropriedade16
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade16 == nomejog2:
                    valorjogador2 += AluguelPropriedade16
                    valorjogador4 -= AluguelPropriedade16
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade16 == nomejog3:
                    valorjogador3 += AluguelPropriedade16
                    valorjogador4 -= AluguelPropriedade16
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade16) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 17:
            if Propriedade17 == "":
                if valorjogador4 >= valorpropriedade17:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade17
                        Propriedade17 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade no Espirito Santo")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Espirito Santo ")
            elif Propriedade17 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Espirito Santo ")
            else:
                if Propriedade17 == nomejog1:
                    valorjogador1 += AluguelPropriedade17
                    valorjogador4 -= AluguelPropriedade17
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade17 == nomejog2:
                    valorjogador2 += AluguelPropriedade17
                    valorjogador4 -= AluguelPropriedade17
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade17 == nomejog3:
                    valorjogador3 += AluguelPropriedade17
                    valorjogador4 -= AluguelPropriedade17
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade17) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 18:
            if Propriedade18 == "":
                if valorjogador4 >= valorpropriedade18:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade18
                        Propriedade18 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade em Roraima")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade em Roraima")
            elif Propriedade18 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade em Roraima")
            else:
                if Propriedade18 == nomejog1:
                    valorjogador1 += AluguelPropriedade18
                    valorjogador4 -= AluguelPropriedade18
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade18 == nomejog2:
                    valorjogador2 += AluguelPropriedade18
                    valorjogador4 -= AluguelPropriedade18
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade18 == nomejog3:
                    valorjogador3 += AluguelPropriedade18
                    valorjogador4 -= AluguelPropriedade18
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade18) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 19:
            if Propriedade19 == "":
                if valorjogador4 >= valorpropriedade19:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade19
                        Propriedade19 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade no Maranhão")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Maranhão ")
            elif Propriedade19 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Maranhão ")
            else:
                if Propriedade19 == nomejog1:
                    valorjogador1 += AluguelPropriedade19
                    valorjogador4 -= AluguelPropriedade19
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade19 == nomejog2:
                    valorjogador2 += AluguelPropriedade19
                    valorjogador4 -= AluguelPropriedade19
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade19 == nomejog3:
                    valorjogador3 += AluguelPropriedade19
                    valorjogador4 -= AluguelPropriedade19
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade19) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        elif posjog4 == 20:
            if Propriedade20 == "":
                if valorjogador4 >= valorpropriedade20:
                    if compra == 1:
                        valorjogador4 -= valorpropriedade20
                        Propriedade20 = nomejog4
                        print(str(nomejog4) + " comprou a propriedade no Piauí")
                        print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                    else:
                        print(str(nomejog4) + " sua aleatóriedade não te permitiu comprar essa casa")
                else:
                    print(str(nomejog4) + ", você não possui dinheiro para comprar a propriedade no Piauí ")
            elif Propriedade20 == nomejog4:
                print(str(nomejog4) + " você já possui a propriedade no Piauí ")
            else:
                if Propriedade20 == nomejog1:
                    valorjogador1 += AluguelPropriedade20
                    valorjogador4 -= AluguelPropriedade20
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog1)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade20 == nomejog2:
                    valorjogador2 += AluguelPropriedade20
                    valorjogador4 -= AluguelPropriedade20
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog2)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))
                elif Propriedade20 == nomejog3:
                    valorjogador3 += AluguelPropriedade20
                    valorjogador4 -= AluguelPropriedade20
                    print(str(nomejog4) + " você teve que pagar o aluguel de R$"+ str(AluguelPropriedade20) +",00 para o", nomejog3)
                    print(str(nomejog4) + " possui em conta R$", format(valorjogador4, '.2f'))

        # Verifica se Jogador Faliu
        if valorjogador4 < 0:
            if Propriedade1 == nomejog4:
                Propriedade1 = ""
            if Propriedade2 == nomejog4:
                Propriedade2 = ""
            if Propriedade3 == nomejog4:
                Propriedade3 = ""
            if Propriedade4 == nomejog4:
                Propriedade4 = ""
            if Propriedade5 == nomejog4:
                Propriedade5 = ""
            if Propriedade6 == nomejog4:
                Propriedade6 = ""
            if Propriedade7 == nomejog4:
                Propriedade7 = ""
            if Propriedade8 == nomejog4:
                Propriedade8 = ""
            if Propriedade9 == nomejog4:
                Propriedade9 = ""
            if Propriedade10 == nomejog4:
                Propriedade10 = ""
            if Propriedade11 == nomejog4:
                Propriedade11 = ""
            if Propriedade12 == nomejog4:
                Propriedade12 = ""
            if Propriedade13 == nomejog4:
                Propriedade13 = ""
            if Propriedade14 == nomejog4:
                Propriedade14 = ""
            if Propriedade15 == nomejog4:
                Propriedade15 = ""
            if Propriedade16 == nomejog4:
                Propriedade16 = ""
            if Propriedade17 == nomejog4:
                Propriedade17 = ""
            if Propriedade18 == nomejog4:
                Propriedade18 = ""
            if Propriedade19 == nomejog4:
                Propriedade19 = ""
            if Propriedade20 == nomejog4:
                Propriedade20 = ""
            print(str(nomejog4) + " faliu! XXX Está Fora do Jogo e Perdeu todas suas Propriedades XXX")
            faliujog4 = True
            lista_de_faliu.append(nomejog4)

    # Encontra o Vencedor
    if not faliujog1:
        vencedor = nomejog1
    if not faliujog2:
        vencedor = nomejog2
    if not faliujog3:
        vencedor = nomejog3
    if not faliujog4:
        vencedor = nomejog4
    turno += 1
    if turno == 4:
        break
    print("--------------------------------------------------------------------------------------------")

mai = 0
print("\n")
if turno < 4:
    print("Numero de Rodadas: " + str(turno))
    print("🧠 --- VENCEDOR --- 🧠 ------> " + vencedor)
    print("☠  --- 2º Lugar --- ☠  ------> " + lista_de_faliu[2])
    print("☠  --- 3º Lugar --- ☠  ------> " + lista_de_faliu[1])
    print("☠  --- 4º Lugar --- ☠  ------> " + lista_de_faliu[0])
else:
    print("💣 Estourou por Time-Out 💣")
    print("Numero de Rodadas: " + str(turno))

    lista_jog = [nomejog1, nomejog2, nomejog3, nomejog4]
    lista_valores = [valorjogador1, valorjogador2, valorjogador3, valorjogador4]
    vencedor = lista_jog[lista_valores.index(max(lista_valores))]

    print("🧠 --- VENCEDOR --- 🧠 ------> " + vencedor)
