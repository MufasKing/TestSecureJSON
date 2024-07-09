import json

def process_bp(bp_string):
    # Divide la stringa in elementi separati da virgola
    elements = bp_string.split(',')
    # Rimuove i punti finali e spazi bianchi extra dagli elementi
    processed_elements = [element.strip().rstrip('.') for element in elements]
    return processed_elements

def convert_bp_in_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            record = json.loads(line)
            if 'BP' in record:
                record['BP'] = process_bp(record['BP'])
            outfile.write(json.dumps(record) + '\n')

# Specifica il percorso del file di input e di output
input_file = 'SecureCatalogue.jsonl'
output_file = 'SecureCatalogue2.jsonl'

# Esegui la conversione
convert_bp_in_jsonl(input_file, output_file)
