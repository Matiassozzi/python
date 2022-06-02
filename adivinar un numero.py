import random
num_aleatorio= random.randint(1,100)
num_user=int(input('Ingresa un numero del 1 al 100 :'))
while num_aleatorio != num_user:
    if num_aleatorio < num_user:
        print('😒 intenta con un numero mas bajo ')
    else :
        print(' 😒 intenta con un numero mas alto ')
    num_user=int(input('Elegi otro numero :'))

print( 'Acertaste 😊😊')