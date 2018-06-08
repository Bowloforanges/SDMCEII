

def SortedFasta():

    F1string = [""]
    FastaDataset = [""]

    with open("protein_qsecANDRefSeq[filter].fa", "r") as F1:
        F1string.append(F1.read().split(">"))
    F1.close()

    with open("protein_qsebANDRefSeq[filter].fa", "r") as F2:
        F1string.append(F2.read().split(">"))
    F2.close()

    print("putoelquelolea")

    # tempfile = open("tempfile.txt", 'w')  # escribir .csv con los ID's
    # tempfile.write(str(F1string))
    # tempfile.close()

    # for organismo in F1string:
    #
    #     print('\n'.join(organismo))
    #
    # print(type(F1string))



SortedFasta()

# Guardar listas dentro de la lista. usar replace