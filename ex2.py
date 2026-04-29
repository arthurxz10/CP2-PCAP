#▪ Faça um programa que leia 3 valores que representam os lados de um triângulo A, B e C e ordene-os
#em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o
#tipo de triângulo que estes três lados formam, com base nos seguintes casos:
#▪ Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
#▪ Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
#▪ Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
#▪ Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;
#▪ Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
#▪ Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;

#leitura dos lados
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

#Ordenação em ordem decrescente (A >= B >= C) sem funções prontas de ordenação
if lado1 >= lado2 and lado1 >= lado3:
    A = lado1
    if lado2 >= lado3:
        B = lado2
        C = lado3
    else:
        B = lado3
        C = lado2
elif lado2 >= lado1 and lado2 >= lado3:
    A = lado2
    if lado1 >= lado3:
        B = lado1
        C = lado3
    else:
        B = lado3
        C = lado1
else:
    A = lado3
    if lado1 >= lado2:
        B = lado1
        C = lado2
    else:
        B = lado2
        C = lado1

#Verifica se forma triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Verifica tipo por ângulo
    if (A ** 2) > (B ** 2) + (C ** 2):
        tipo_angulo = "TRIANGULO RETANGULO"
    elif (A ** 2) < (B ** 2) + (C ** 2):
        tipo_angulo = "TRIANGULO OBTUSANGULO"
    else:
        tipo_angulo = "TRIANGULO ACUTANGULO"

    # Verifica tipo por lados
    if A == B and B == C:
        tipo_lado = "TRIANGULO EQUILATERO"
    elif A == B or B == C or A == C:
        tipo_lado = "TRIANGULO ISOSCELES"
    else:
        tipo_lado = "TRIANGULO ESCALENO"

    print(tipo_angulo)
    print(tipo_lado)