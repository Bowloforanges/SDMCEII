from Bio import Entrez, SeqIO
import os


def NCBIDownload():
    db = "protein"
    term = "fixk"
    name = db + "_" + term + ".csv"
    nameQuery = name.replace(" ", "")
    nameF = db + "_" + term + ".fa"
    nameFasta = nameF.replace(" ", "")

    Entrez.email = "bio.eng.emmartin@outlook.com"  # required by NCBI
    handle = Entrez.esearch(db, term, retmax=99999)
    # Hace una consulta, la guarda en handle
    record = Entrez.read(handle)  # guarda en record los resultados de la búsqueda
    handle.close()  # Cierra el handle

    IDCount = int(record["Count"])
    IDs = record['IdList'];  # deposita el contenido en una lista
    IDsString = str(IDs).replace("['", "").replace("', '", ",\n").replace("']", "")  # Parsear Ids a un String

    csv_file = open(nameQuery, 'w')  # escribir .csv con los ID's
    csv_file.write(IDsString)
    csv_file.close()

    print("ID Counter is : ", IDCount)

    if (IDCount < 200):

        batch_size = 10  # download sequences in batches so NCBI doesn't time you out
        end = 0

        with open(nameFasta, 'w') as out_handle:
            for start in range(0, 200, batch_size):
                end = min(IDCount, start + batch_size)
                print("Downloading sequences %i to %i" % (start + 1, end))
                fetch_handle = Entrez.efetch(db=db, id=IDs, rettype="fasta", retmode="text",
                                             retstart=start, retmax=batch_size)
                data = fetch_handle.read()
                fetch_handle.close()
                out_handle.write(data)

        print("\nDownload completed")

    else:
        with open(nameFasta, 'w') as w:
                for id in IDs:
                    fetch_handle = Entrez.efetch(db=db, id=id, rettype="fasta", retmode="text")
                    fetch_record = SeqIO.read(fetch_handle, "fasta")
                    fetch_handle.close()
                    SeqIO.write(fetch_record, "current_seq.fasta", "fasta")
                    for line in open('current_seq.fasta'):
                        w.write(line)
        os.remove("current_seq.fasta")
        print("\nDownload completed")


NCBIDownload()

from Bio.Align.Applications import ClustalOmegaCommandline

in_file = "ALL_SEQ.fa"
out_file = "aligned.fa"
clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
print(clustalomega_cline)
