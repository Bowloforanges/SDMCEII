import csv
import numpy

reader = csv.reader(open("CpxAR.csv", "r+"), delimiter=",")
x = list(reader)
matrixCpxAR = numpy.array(x)

reader = csv.reader(open("NarQP.csv", "r+"), delimiter=",")
x = list(reader)
matrixNarQP = numpy.array(x)

reader = csv.reader(open("PhoRB.csv", "r+"), delimiter=",")
x = list(reader)
matrixPhoRB = numpy.array(x)

reader = csv.reader(open("QseCB.csv", "r+"), delimiter=",")
x = list(reader)
matrixQseCB = numpy.array(x)

def GetList(matrix):
    listTF = matrix

    for i in range(0,len(listTF)):
                if matrix[i][2] != '':
                    listTF[i,2] = True

                    i+=1
                else:
                    listTF[i,2] = False

                    i+=1
    return listTF

listTF_matrixCpxAR = GetList(matrixCpxAR)
listTF_matrixNarQP = GetList(matrixNarQP)
listTF_matrixPhoRB = GetList(matrixPhoRB)
listTF_matrixQseCB = GetList(matrixQseCB)

#print(listTF_matrixCpxAR)

vec = listTF_matrixCpxAR
cont = 1


n= int(numpy.sqrt(len(vec)-1))
print(n)

for k in range(0,n):
    cont = 1
    for i in range(0,n):
        for j in range(0,2):
            if j == 0:
                vec[i+(n*k)][j] = k+1
            else:
                vec[i+(n*k)][j] = cont
                cont+=1


for l in range(0,n*n):
    print(vec[l][0],vec[l][1],vec[l][2])