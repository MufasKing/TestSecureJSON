import json
import os


def read_code_from_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Il file '{file_path}' non esiste.")
    with open(file_path, 'r') as file:
        code = file.read()
    return code


def format_code_for_json(code):
    # Sostituisce i ritorni a capo con \r\n e rimuove eventuali spazi alla fine delle righe
    code = code.replace("\n", "\\r\\n")
    return code


def save_to_jsonl(text, bp, code, output_file):
    # Rimuove i caratteri '#' dal testo
    text = text.replace("#", "")
    # Rimuove i ritorni a capo dal testo
    text = text.replace("\n", " ")
    bp = bp.replace("\n", " ")

    # Crea un dizionario con i campi "text", "bp" e "code"
    json_content = {"text": text, "BP": bp, "code": code}

    # Scrive il contenuto JSONL nel file di output
    with open(output_file, 'a') as file:
        file.write(json.dumps(json_content) + "\n")


def main_interactive():
    # Modalità interattiva
    print("Modalità interattiva:")
    print("1. Inserisci testo e codice separati")
    print("2. Leggi codice da un file")

    choice = input("Seleziona un'opzione (1 o 2): ").strip()

    if choice == "1":
        text = get_multiline_input("Inserisci il testo normale (termina con 'EOF' su una nuova riga):")
        bp = get_multiline_input("Inserisci Best Practices (termina con 'EOF' su una nuova riga):")
        code = get_multiline_input("Inserisci il codice Python:")
        #output_file = input(
        #    "Inserisci il nome del file di output (default: formatted_code.jsonl): ").strip() or "formatted_code.jsonl"
        output_file = './SecureCatalogue.jsonl'   
    elif choice == "2":
        file_path = input("Inserisci il percorso del file contenente il codice: ").strip()
        #output_file = input(
           # "Inserisci il nome del file di output (default: formatted_code.jsonl): ").strip() or "formatted_code.jsonl"
        output_file = '/SecureCatalogue.jsonl'
        text = get_multiline_input("Inserisci il testo normale (termina con 'EOF' su una nuova riga):")
        bp = get_multiline_input("Inserisci Best Practices (termina con 'EOF' su una nuova riga):")
        code = read_code_from_file(file_path)
    else:
        print("Scelta non valida.")
        return

    formatted_code = format_code_for_json(code)

    # Salva nel formato JSONL
    save_to_jsonl(text, bp, formatted_code, output_file)
    print(f"Dati salvati in formato JSONL nel file '{output_file}'")


def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    main_interactive()
