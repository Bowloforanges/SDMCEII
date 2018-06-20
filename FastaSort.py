from Bio import SeqIO

deprecate = "MULTISPECIES"

countantes = 0
countdespues = 0



def SortedFasta():



    F1string = [""] #Lista donde se van a guardar los individuos
    Organism = [""] #Sublista donde se van a guardar los atributos

    for record in SeqIO.parse('protein_qsebANDRefSeq[filter].fa', 'fasta'):
        descstr = str(record.description)

        seq= str(record.seq)
        id = descstr[0:12]
        desc = descstr[15:descstr.index("[")-1]
        name = descstr[descstr.index("[")+1:descstr.index("]")]


        Organism = [id, desc, name, seq]
        F1string.append(Organism)

    F1string.pop(0)  #Borrar elemento con el que se inicializa la lista
    # countantes = len(F1string)


    for record in SeqIO.parse('protein_qsecANDRefSeq[filter].fa', 'fasta'):
        descstr = str(record.description)

        seq= str(record.seq)
        id = descstr[0:12]
        desc = descstr[15:descstr.index("[")-1]
        name = descstr[descstr.index("[")+1:descstr.index("]")]


        Organism = [id, desc, name, seq]
        F1string.append(Organism)

    # countdespues = len(F1string)

    i = 0
    F1string.pop(4905)

    for org in F1string:
        if(str(org[1]).find(deprecate) != -1):
            print("putoelquelolea")             #
            todelete = i                        # AQUI SE LE SIGUE: intentar borrar el elemento
                                                # multispecies
            F1string.pop(todelete)              #

        print(i)
        print(str(org[1]))
        i = i+1



    # print(countantes)
    # print(countdespues)


    # for organismo in F1string:
    #
    #     if(str(organismo).find(deprecate) != -1):
    #         F1string.remove(organismo)
    #
    # for organismo in F1string:
    #     countdespues+=1
    #
    #
    # print(type(F1string))
    #
    # print("putoelquelolea")
    #
    # # tempfile = open("tempfile.txt", 'w')  # escribir .csv con los ID's
    # # tempfile.write(str(F1string))
    # # tempfile.close()
    #
    # # for organismo in F1string:
    # #
    # #     print('\n'.join(organismo))
    # #
    # # print(type(F1string))
    # print(str(F1string[1]))
    # print(countantes)
    # print(countdespues)
    # with open("protein_qsecANDRefSeq[filter].fa", "r") as F1:
    #
    #     F1string.append(F1.read().split(">"))
    # F1.close()
    #
    # with open("protein_qsebANDRefSeq[filter].fa", "r") as F2:
    #     F1string.append(F2.read().split(">"))
    # F2.close()
    #
    # #countantes = len(F1string)
    #
    # for organismo in F1string:
    #     countantes+=1
    #
SortedFasta()

# Guardar listas dentro de la lista. usar replace