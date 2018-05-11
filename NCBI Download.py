from Bio import Entrez

Entrez.email = "george.soriano.plus@gmail.com"   # required by NCBI
handle = Entrez.esearch(db="nucleotide", retmax=10, term="opuntia[ORGN] accD", idtype="acc") # Hace una consulta, la guarda en handle
record = Entrez.read(handle) #guarda en record los resultados de la búsqueda
handle.close() #Cierra el handle
if int(record["Count"]) >= 4:
    print('hay 4 o más registros')
else:
    print('hay menos de 4 registros')

# for IdList in record
#     print (IdList[])

print (record['IdList']) # regresa la información del diccionario IdList en record

print(record)

print(type(record))



















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