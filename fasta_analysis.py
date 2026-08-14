from Bio import SeqIO

file_path = "sequences.fasta"

for record in SeqIO.parse(file_path, "fasta"):
    sequence = str(record.seq).upper()

    length = len(sequence)
    gc_content = (sequence.count("G") + sequence.count("C")) / length * 100

    print("Sequence ID:", record.id)
    print("Length:", length)
    print("GC Content:", round(gc_content, 2), "%")
    print("-" * 30)
