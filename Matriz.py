import csv
import os
from tkinter.filedialog import askdirectory

import numpy


def GetList(matrix, current_x):
    listTF = matrix

    for i in range(1, len(listTF)):
        if matrix[i][2] != '':
            listTF[i, 2] = current_x

            i += 1
        else:
            listTF[i, 2] = 0

            i += 1
    return listTF


def Ident(matrix):
    vec = matrix
    cont = 1
    n = int(numpy.sqrt(len(vec) - 1))
    for k in range(0, n):
        cont = 1
        for i in range(1, n + 1):
            for j in range(0, 2):
                if j == 0:
                    vec[i + (n * k)][j] = k + 1
                else:
                    vec[i + (n * k)][j] = cont
                    cont += 1

    return vec


def getFileList():
    list_matrix = []
    # Open a file
    path = askdirectory()
    # path = "C:\\Users\Soria\PycharmProjects\SDMCEII\matrices"

    dirs = os.listdir(path)
    # This would print all the files and directories
    print("Archivos en el directorio: ")
    for file in dirs:
        print(file)
    # print(type(dirs)) tipo de la lista de archivos
    i = 0
    todelete = []
    for file in dirs:
        if (str(file).find(".csv") == -1):  # Guarda en una lista los el id de los elementos MULTISPECIES a borrar
            todelete.append(i)

        i = i + 1
    i = 0
    for elemento in todelete:
        dirs.pop(elemento - i)  # Borra los elementos guardados en el for in anterior
        i = i + 1

    print("\nArchivos CSV a tomar. MATRICES:")
    if (len(dirs) != 0):
        countMatrix = 0
        for file in dirs:
            countMatrix = countMatrix + 1
            print(file)
            fopen = open(path + "/" + file)
            reader = csv.reader(fopen)
            x = list(reader)
            # x.remove(0)
            matrixTemp = numpy.array(x)
            matrix = Ident(GetList(matrixTemp, countMatrix))
            matrix = numpy.delete(matrix, (0), axis = 0)
            list_matrix.append(matrix)



    else:
        print("No elements met the required criterion.")

    print(countMatrix)

    # print(list_matrix[0][2599][2])
    # print("sdf65as4fa8f5asfa6f54a5f4e87r5")
    return list_matrix


# fopen= open("C:\\Users\Soria\PycharmProjects\SDMCEII\matrices\CpxAR1.csv", "r+")
def GenerateRecord(listaMatrices):
    MatrizHistorial = listaMatrices[0][:][:listaMatrices[0].__len__(), :2]  # Se genera una matriz con las 2 columnas de
    # la primera matriz, es decir una matriz de 2 columnas por 2601 renglones, esto es para el historial

    VectorVacio = [''] * listaMatrices[0].__len__()  # Generamos un vector vacio para guardar el historial

    MatrizHistorial = numpy.c_[MatrizHistorial, VectorVacio]  # numpy.c_ sirve para añadir una columna a una matriz

    for matriz in listaMatrices:  # Con este for recorremos cada matriz
        for i in range(0, len(matriz)):
            if (matriz[i][2] != '0' and (MatrizHistorial[i][
                                             2] != "MIp,")):  # comprobamos que se tiene un valor en la tercera es diferente de 0, si se cumple
                # se añade el valor al historial
                MatrizHistorial[i][2] = MatrizHistorial[i][2] + str(matriz[i][2]) + "."

    ShowRecords(MatrizHistorial)


def ShowRecords(MatrizHistorial):
    n = int(numpy.sqrt(len(MatrizHistorial)))
    Vector_Matriz = MatrizHistorial[:,
                    2]  # Seleccionamos la ultima columna de nuestra matriz de historial, las otras dos son del indice
    Matriz_resultante = numpy.reshape(Vector_Matriz, (
    n, n))  # reshape es una funcion de numpy permite convertir un vector en una matriz
    numpy.savetxt("Matriz de salida.csv", Matriz_resultante, delimiter = ",",
                  fmt = '%s')  # Guardamos la matriz en un csv
    print(Matriz_resultante)


listaMatrices = getFileList()
GenerateRecord(listaMatrices)
