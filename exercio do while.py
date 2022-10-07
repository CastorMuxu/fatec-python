# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:44:55 2022

@author: lab54
"""
"""execercicio 2
fim_contagem = int(input("\digite o valor do contador = "))
x = 1
while x <= fim_contagem:
    print(x,"\n")
    x = x + 1
"""

"""exercicio 3
limite = int(input("entrar com o valor limite da contagem dos números pares = "))
contador = 0
while contador <= limite:
    if contador % 2 == 0: #resto de contador dividido por 2 = 0 ?
        print(contador, "\n")
    contador = contador + 1
""" 
"""exercicio 4
comando = "continuar"
n = 0
while comando != "parar": # != -> diferente
    comando = input("entrar com o comando de continuar ou parar: \t")
    n = n + 1
    print(n,"\t", comando)      

""" 
"""execercicio 5
senha = "abc"
n = 1
while n <= 3:
    entrada_usuario = input("enrtrar com sua senha\t")
    if entrada_usuario == senha:
            print("senha correta")
            break #break = sai do laço
    else:
        n = n + 1
        print("senha errada")
"""

"""execercicio 6
b = int(input("quantos numero ira somar ??? "))
n = 1
soma = 0
while n <= b:
    a = int(input("entra com a valor do nª a somar: "))
    soma = soma + a
    n = n + 1
print("valor da soma = ", soma)
"""

"""execercicio 7
a = int(input("entrar com a variavel 'a' : "))
b = int(input("entrar com a variavel 'b': "))   
n = 0
c = 0
while n < b:
    c = c + a
    n = n + 1
    print("c=", c)
    print("n=", n)
print("valor da multiplicação de a x b = ", c)    
"""
















"""execercicio 9
b = int(input("quantos numeros ira somar ??? "))
n = 1
soma = 0
while n <= b:
    a = int(input("entrar com valor do nª a somar: "))
    if a == 0:
        break
    soma += a
    n = n + 1
print("valor da soma = ", soma)
"""

        