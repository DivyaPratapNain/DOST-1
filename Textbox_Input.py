def count_nucleotides(sequence, sequence_name=None, sequence_detail=None):
    nucleotide_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    total_count = 0
    at_count = 0
    gc_count = 0

    for nucleotide in sequence:
        nucleotide_upper = nucleotide.upper()
        if nucleotide_upper in nucleotide_count:
            nucleotide_count[nucleotide_upper] += 1
            total_count += 1

    at_count = nucleotide_count['A'] + nucleotide_count['T']
    gc_count = nucleotide_count['G'] + nucleotide_count['C']

    nucleotide_count['Total Nucleotides'] = total_count
    nucleotide_count['AT Count'] = at_count
    nucleotide_count['GC Count'] = gc_count
    nucleotide_count['AT Percentage'] = (at_count / total_count) * 100
    nucleotide_count['GC Percentage'] = (gc_count / total_count) * 100

    # Format the result
    formatted_result = []
    if sequence_name:
        formatted_result.append("Sequence name: " + sequence_name)
    if sequence_detail:
        formatted_result.append("Sequence Detail: " + sequence_detail)

    formatted_result.append("\nTotal No. Nucleotides: " + str(nucleotide_count['Total Nucleotides']))
    formatted_result.append("A: " + str(nucleotide_count['A']))
    formatted_result.append("T: " + str(nucleotide_count['T']))
    formatted_result.append("G: " + str(nucleotide_count['G']))
    formatted_result.append("C: " + str(nucleotide_count['C']))
    formatted_result.append("\nAT Count: " + str(nucleotide_count['AT Count']))
    formatted_result.append("GC Count: " + str(nucleotide_count['GC Count']))
    formatted_result.append("\nAT Percentage: " + str(nucleotide_count['AT Percentage']))
    formatted_result.append("GC Percentage: " + str(nucleotide_count['GC Percentage']))

    return "\n".join(formatted_result)