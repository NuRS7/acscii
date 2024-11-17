import sys

def load_ascii_art(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
    symbol_dict = {}
    current_symbol = []
    current_symbol_code = 32
    for line in lines:
        if len(line) == 0:
            if current_symbol:
                symbol_dict[chr(current_symbol_code)] = current_symbol
                current_symbol = []
                current_symbol_code += 1
        else:
            current_symbol.append(line.rstrip('\n'))
    if current_symbol:
        symbol_dict[chr(current_symbol_code)] = current_symbol

    return symbol_dict
def print_ascii_art(text, symbol_dict):
    for lines in zip(*(symbol_dict.get(char, ['']) for char in text)):
        print(' '.join(lines))
def main():
    if len(sys.argv) != 2:
        print("Использование: python main.py <text>")
        sys.exit(1)
    text = sys.argv[1]
    symbol_dict = load_ascii_art('standard.txt')
    print_ascii_art(text, symbol_dict)

if __name__ == "__main__":
    main()
    input("\nШығу үшін любой кнопка...")


# terminal > python main.py "Hello, World!"