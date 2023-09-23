from Bio import SeqIO
import sys

input_file_path = sys.argv[1]

total_nt_count = 0
a_count = 0
t_count = 0
g_count = 0
c_count = 0

result = ""

for record in SeqIO.parse(input_file_path, "fasta"):
    total_nt_count += len(record.seq)
    a_count += record.seq.count('A')
    t_count += record.seq.count('T')
    g_count += record.seq.count('G')
    c_count += record.seq.count('C')

    sequence_name = '_'.join(record.description.split(' ')[1:])
    result += f"Sequence name: {sequence_name}\n"
    result += f"Sequence Detail: {sequence_name}\n\n"

result += f"Total No. Nucleotides: {total_nt_count}\n\n"
result += f"A: {a_count}\n"
result += f"T: {t_count}\n"
result += f"G: {g_count}\n"
result += f"C: {c_count}\n"

at_count = a_count + t_count
gc_count = g_count + c_count

result += f"AT Count : {at_count}\n"
result += f"GC Count : {gc_count}\n"

AT_percentage = (at_count / total_nt_count) * 100
rounded_AT = round(AT_percentage, 2)

GC_percentage = (gc_count / total_nt_count) * 100
rounded_GC = round(GC_percentage, 2)

result += f"AT Percentage : {rounded_AT}\n"
result += f"GC Percentage : {rounded_GC}\n"

# Print the result to standard output (stdout)
print(result)
