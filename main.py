import random

# Função que separa em duplas
def randomDoubles(names: list):
    duplas = []
    while len(names) != 0:
        amostra = random.sample(names, k=2)
        duplas.append(amostra)

        names.remove(amostra[0])
        names.remove(amostra[1])
    
    return duplas

# Coletando o numero de nomes
names = []
num_names = int(input('Digite o número de integrantes: '))
print()

# verificando se a quantidade é par
if not num_names % 2 == 0:
    choose = input('A quantidade de nomes é impar, Deseja continuar mesmo assim?[S/N] ').upper()
    while True:
        if choose == 'S':
            break

        elif choose == 'N':
            exit()

        else:
            choose = input('Desculpe não entendi sua resposta tecle "S" ou "N": ').upper()
print()

# coletando os nomes
for i in range(num_names):
    names.append(input(f'Digite o nome do {i+1}° integrante: '))

print()

# se for impar retira uma sobra
if num_names % 2 != 0:
    sobra = random.choice(names)
    names.remove(sobra)

# mostra no terminal os usuarios coletados
print('Nomes coletados:')
for i in range(num_names-1):
    print(f'- {names[i]}')
print()
print(f'Sobrou: {sobra}')
print()

#separa as duplas com a função feita anteriormente
duplas  = randomDoubles(names)

# mostra no terminal as duplas divididas
for i in range(len(duplas)):
    print(f'{i+1}° Dupla:')
    for ii in range(len(duplas[i])):
        print(f'- {duplas[i][ii]}')
