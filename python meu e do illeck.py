# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:57:50 2022

@author: lab54
"""
"""
quantidade = int(input("qual a quantidade  de peças de roupa irá comprar ?\t"))
if quantidade <= 30 and quantidade >= 20:
    preco_unidade = 28.00
if quantidade < 20:
    preco_unidade = 35.00
if quantidade > 30:
    preco_unidade = 20.00
print("\quantidade de  peças de roupa = \t", quantidade)
print("\preço por unidade de acordo com  a quantidade = R$ ", preco_unidade)
print(f"\npreço da compra =: R$ {preco_unidade*quantidade:8.2f}")
print("quantidade <= 30 and quantidade >= 20: ", quantidade <= 30 and quantidade >= 20)
print("quantidade < 20: ", quantidade < 20)
print("quantidade > 30: ", quantidade < 30)
"""

"""

quantidade = int(input("qual a quantidade de peças de roupa irá comprar?\t"))
if quantidade < 20:
    preco_unidade = 35.00
else:
    if quantidade <=30:
        preco_unidade = 28.00
    else:
        preco_unidade = 20.00
print("\nquantidade de peças de roupa = \t", quantidade)
print("\npreço por unidade de acordo com a quantidade = R$", preco_unidade) 
print(f"\npreço de compra =: R$ {preco_unidade*quantidade: 8.2f}")
       
"""

#tabela - código preço
#         1       13.30
#         2       1.40
#         3       19.00
#         4       123.79
#         5       44.33

"""

código = int(input("digitar o código do produto\t"))
if código == 1:
    preco_produto = 13.30
else:
    if código == 2:
        preco_produto = 1.40
    else:
        if código == 3:
            preco_produto = 19.00
        else:
            if código == 4:
                preco_produto = 123.79
            else: 
                if código == 5:
                    preco_produto == 44.33
                else:
                    print("\ndigitar código do produto entre 1 e 5: código ->", código, "não é válido")
                    preco_produto = 0.00
print("\ncódigo do produtp = \t\t\t\t\t\t\t\t", código)
print(f"\npreço do produto de acordo com o código = R$ {preco_produto:4.2f}") 

"""


"""

#tabela - código preço
#         1       13.30
#         2       1.40
#         3       19.00
#         4       123.79
#         5       44.33

código = int(input("digitar o código do produto\t"))
if código == 1:
    preco_produto = 130.30
elif código == 2:
     preco_produto = 1.40
elif código == 3:
     preco_produto = 19.00
elif código == 4:
     preco_produto = 123.79
elif código == 5:
     preco_produto = 44.33
else:
    print("\ndigitar o código do produto entre 1 e 5: código ->", código, "não é válido!")
    preco_produto = 0.00
print("\ncódigo do produto = \t\t\t\t\t\t\t\t", código)
print(f"\npreço do produto de acordo com o código = R$ {preco_produto:4.2f}") 
   
"""


"""
clima = int(input("digite a temperatura: ")) 

if clima >= 16 and  clima <= 30:
    print("Agradavel")
else:
    if clima > 30:
        print("Calor")
    else:
        if clima < 16:
            print("Frio")
            
"""


estacao = input("Qual estação do ano: ")

if estacao == 'verão' or estacao == 'Verão':
    print("janeiro")
    print("fevereiro")
    print("março")
    print("dezembro")
if estacao == 'inverno' or estacao == 'inverno':
     print("Junho") 
     print("Juhlo")
     print("Agosto")
     print("Setembro")
if estacao == 'outono' or estacao == 'outono':
    print("abril")
    print("maio")
    print("outubro")
    print("Novembro")    