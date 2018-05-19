from Bio import Entrez


# handle = Entrez.esearch(db="nucleotide", retmax=10, term="opuntia[ORGN] accD", idtype="acc")
# handle = Entrez.efetch(db="nucleotide", id=IDs, rettype="fasta", retmode="text")
# fetch_handle = Entrez.efetch(db="protein", id=IDs, rettype="fasta", retmode="text", retstart=start, retmax=batch_size)

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

    if (IDCount >= 200):

        batch_size = 10  # download sequences in batches so NCBI doesn't time you out
        end = 0

        with open(nameFasta, "w") as out_handle:
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

        print("jaja al chile")


NCBIDownload()

from Bio.Align.Applications import ClustalOmegaCommandline

in_file = "ALL_SEQ.fa"
out_file = "aligned.fa"
clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
print(clustalomega_cline)












# search_handle = Entrez.esearch(db="nucleotide", term=search_term, usehistory="y", property='complete genome')
# search_results = Entrez.read(search_handle)
# search_handle.close()

# from Bio import Entrez
#
# search_term = raw_input("Organism name: ")
#
# Entrez.email = "your_email@isp.com"   # required by NCBI
# search_handle = Entrez.esearch(db="nucleotide", term=search_term, usehistory="y", property='complete genome')
# search_results = Entrez.read(search_handle)
# search_handle.close()
#
# gi_list = search_results["IdList"]
# count = int(search_results["Count"])
# webenv = search_results["WebEnv"]
# query_key = search_results["QueryKey"]
#
# batch_size = 5    # download sequences in batches so NCBI doesn't time you out
#
# with open("ALL_SEQ.fasta", "w") as out_handle:
#     for start in range(0, count, batch_size):
#         end = min(count, start+batch_size)
#         print "Going to download record %i to %i" % (start+1, end)
#         fetch_handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text",retstart=start, retmax=batch_size, webenv=webenv, query_key=query_key)
#         data = fetch_handle.read()
#         fetch_handle.close()
#         out_handle.write(data)
#
# print ("\nDownload completed")