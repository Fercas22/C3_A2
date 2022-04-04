import csv
import random
from tokenize import String

from numpy import double


aux = []
valor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    data = [['LLEGADA', 'ESPERA']]
    for i in range(0, 500):
        # Random de la hora de llegada
        horaL = random.randint(13, 21)
        minutoL = random.randint(0, 59)
        # Random del tiempo de espera
        horaE = random.randint(0,50)
        minutoE = random.randint(0,50)
        
        if minutoL > 9:
            datoH = str(horaL) + '.' + str(minutoL)
            # print('random', minutoE)
            if minutoE > 9:
                datoE = str(minutoE)
                # print('Hora de llegada', datoH, 'Tiempo de espera:', datoE)
            else:
                datoE = minutosMenores(minutoE)
                # print('Hora de llegada', datoH, 'Tiempo de espera:', datoE)
            # print('Datos', datoH, datoE)
            data.append([float(datoH), int(datoE)])
        else:
            concaM = minutosMenores(minutoL)
            datoH = str(horaL) + '.' + concaM
            # print(datoH)
            if minutoE > 9:
                datoE = str(minutoE)
                # print('Hora de llegada', datoH, 'Tiempo de espera:', datoE)
            else:
                concaM = minutosMenores(minutoE)
                # print('Hora de llegada', datoH, 'Tiempo de espera:', concaM)
            # print('Datos', datoH, datoE)
            data.append([float(datoH), int(datoE)])   
    print(data)
    escribirCsv(data)

def minutosMenores(m):
    for j in range(len(valor)):
        if m == valor[j]:
            numero = str(m)
            concatenar = '0' + numero
            # print('Minutos concatenado', concatenar)
            return concatenar

def escribirCsv(data):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)
# HORA DE LLEGADA A LA FILA Y TIEMPO FORMADO EN LA FILA
# 17.30, 30

main()