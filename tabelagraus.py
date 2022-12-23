#Exercício 10. Crie um programa que pede ao usuário dois ângulos, em graus, e gera uma tabela bem formatada.

#Importação
import math

#Interação com o usuário
print("Insira dois ângulos (em graus): \n")
angulo1 = eval(input("Ângulo 1: "))
angulo2 = eval(input("Ângulo 2: "))
print(" ")

#Tabela - Parte 1
print(43 * "*")
theta = "\u03b8"
sen = "sen(\u03b8)"
cos = "cos(\u03b8)"
tan = "tg(\u03b8)"
print(theta.center(10), sen.center(10), cos.center(10), tan.center(10))
print(43 * "*")

#Para o ângulo 1
a1 = angulo1 * (math.pi / 180.0)
sen1 = math.sin(a1)
cos1 = math.cos(a1)
tan1 = math.tan(a1)

#Para o ângulo 2
a2 = angulo2 * (math.pi / 180.0)
sen2 = math.sin(a2)
cos2 = math.cos(a2)
tan2 = math.tan(a2)

#Tabela - Parte 2
print(str(angulo1).center(10), str(round(sen1, 3)).center(10), str(round(cos1, 3)).center(10), str(round(tan1, 3)).center(10))
print(str(angulo2).center(10), str(round(sen2, 3)).center(10), str(round(cos2, 3)).center(10), str(round(tan2, 3)).center(10))
print(43 * "*")