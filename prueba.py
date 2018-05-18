from Bio import Entrez, SeqIO
import os



Entrez.email = "bio.eng.emmartin@outlook.com"
handle = Entrez.esearch(db="protein", retmax=100000, term="fixk")
record = Entrez.read(handle)
handle.close()

with open("ALL_SEQ2.fa", 'w') as w:
    for id in record["IdList"]:
        fetch_handle = Entrez.efetch(db = "protein", id = id, rettype = "fasta", retmode="text")
        fetch_record = SeqIO.read(fetch_handle, "fasta")
        fetch_handle.close()
        SeqIO.write(fetch_record, "current_seq.fasta", "fasta")
        for line in open('current_seq.fasta'):
            w.write(line)
os.remove("current_seq.fasta")