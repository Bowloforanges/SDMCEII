from Bio import Entrez

Entrez.email = "bio.eng.emmartin@outlook.com"   # required by NCBI
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

list1 = record['IdList']; #deposita el contenido en una lista

for ID in list1:
    print (ID)

file = open('test.txt', 'w') #crea un txt de la lista por linea
for item in record['IdList']:
    file.write("%s\n" % item)
file.closed

print (file)

search_term = list1

handle = Entrez.efetch(db="nucleotide", id=list1, rettype="fasta", retmode="text") #regresa la información de la list1 en fasta
print(handle.read()) # no puede leer el archivo txt como referencia

gi_list = search_results["IdList"]
count = int(search_results["Count"])
webenv = search_results["WebEnv"]
query_key = search_results["QueryKey"]

batch_size = 5    # download sequences in batches so NCBI doesn't time you out

with open("ALL_SEQ.fasta", "w") as out_handle:
     for start in range(0, count, batch_size):
         end = min(count, start+batch_size)
         print ("Going to download record %i to %i" % (start+1, end))
         fetch_handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text",retstart=start, retmax=batch_size, webenv=webenv, query_key=query_key)
         data = fetch_handle.read()
         fetch_handle.close()
         out_handle.write(data)
print ("\nDownload completed")
#ASopotamadre



















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