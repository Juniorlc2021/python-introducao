import random

numero_secreto = int(93.90659198739872293)
print(numero_secreto) # 94

#random gera um número decimal entre 0 e 1, por isso multiplicamos por 100
numero_secreto = int(random.random() * 100)
print(numero_secreto)

numero_secreto = random.randrange(0,101)
print(numero_secreto)

numero_secreto = random.randint(0,100)
print(numero_secreto)

