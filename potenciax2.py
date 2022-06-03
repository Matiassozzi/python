limite=1000
contador=0
potencia=2**contador
while potencia < limite:
    print('2 elevado a ' +str(contador)+' es igual a '+str(potencia))
    contador+=1
    potencia= 2**contador
print('fin del programa :s')
