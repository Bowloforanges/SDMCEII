from Bio import SeqIO
from operator import itemgetter
import textwrap

deprecate = "MULTISPECIES"
OrganismName = ""

comma = ", "

RawList = [""]  # Lista donde se van a guardar los individuos
Organism = [""]  # Sublista donde se van a guardar los atributos
SortedList = [""] # Lista con los individuos ordenados, sin los Multispecies


def DeprecateFasta():


    for record in SeqIO.parse('protein_qsebANDRefSeq[filter].fa', 'fasta'):
        descstr = str(record.description)

        seq= str(record.seq)
        id = descstr[0:descstr.index(".")]
        desc = descstr[descstr.index(".")+2:descstr.index("[")-1]
        name = descstr[descstr.index("[")+1:descstr.index("]")]


        Organism = [id, desc, name, seq]
        RawList.append(Organism)

    RawList.pop(0)  #Borrar elemento con el que se inicializa la lista


    for record in SeqIO.parse('protein_qsecANDRefSeq[filter].fa', 'fasta'):
        descstr = str(record.description)

        seq= str(record.seq)
        id = descstr[0:descstr.index(".")]
        desc = descstr[descstr.index(".")+2:descstr.index("[")-1]
        name = descstr[descstr.index("[")+1:descstr.index("]")]


        Organism = [id, desc, name, seq]
        RawList.append(Organism)

    i = 0
    todelete = []



    for org in RawList:
        if(str(org[1]).find(deprecate) != -1):  #Guarda en una lista los el id de los elementos MULTISPECIES a borrar
            todelete.append(i)

        i = i+1

    i = 0
    for elemento in todelete:
        RawList.pop(elemento - i)  #Borra los elementos guardados en el for in anterior
        i = i+1



def PrintRawList():

    i = 0
    for org in RawList:        #imprime los organismos restantes
        print(i)
        print(str(org[0]))
        i = i+1

def PrintSortedList(SortedList):

    i = 0
    for org in SortedList:        #imprime los organismos restantes
        print(str(org[0]), comma, str(org[2]), comma, str(org[1]))
        i = i+1

def SortFasta():

    STuple = RawList
    SL_set=set(map(tuple, STuple))                      #Pasar la lista a tuplas para eliminar duplicados
    FinalList = map(list,SL_set)
    SortedList=sorted(FinalList, key = itemgetter(2, 0))#Sort de la lista por id y nombre
    PrintSortedList(SortedList)

    file = open("SweetFasta.fa", "w")

    for organism in SortedList:

        #https://docs.python.org/3/library/textwrap.html

        sequencestr = str(organism[3])

        sequencepar = textwrap.wrap(sequencestr, width = 60)


        file.write(">")
        file.write(organism[0])
        file.write(" ")
        file.write(organism[1])
        file.write(" [")
        file.write(organism[2])
        file.write("]\n")
        for line in sequencepar:
            file.write(line)
            file.write("\n")

    file.close()







# SIGUE:


DeprecateFasta()
SortFasta()
