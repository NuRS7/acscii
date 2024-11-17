import sys
def load_ascii_art(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.read().split('\n')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
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
def generate_ascii_art(text, symbol_dict):
    default_char_lines=symbol_dict.get(' ', [' '])
    line_count=len(next(iter(symbol_dict.values()), default_char_lines))

    lines=[''] * line_count
    for char in text:
        char_lines=symbol_dict.get(char, default_char_lines)
        char_lines=char_lines[:line_count] + [' ' * len(char_lines[0])] * (line_count - len(char_lines))

        for i in range(line_count):
            lines[i]+=char_lines[i] + ' '

    return lines
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [OPTION] [STRING] [BANNER]")
        print("EX: python3 main.py --output=<fileName.txt> something standard")
        sys.exit(1)

    option = sys.argv[1]
    if not option.startswith("--output="):
        print("Usage: python3 main.py [OPTION] [STRING] [BANNER]")
        print("EX: python3 main.py --output=<fileName.txt> something standard")
        sys.exit(1)

    output_file = option.split("=")[1]
    if len(sys.argv) < 4:
        print("Usage: python3 main.py [OPTION] [STRING] [BANNER]")
        print("EX: python3 main.py --output=<fileName.txt> something standard")
        sys.exit(1)

    text = sys.argv[2]
    banner = sys.argv[3]
    try:
        symbol_dict = load_ascii_art(f"{banner}.txt")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    ascii_art = generate_ascii_art(text, symbol_dict)

    try:
        with open(output_file, 'w') as file:
            for line in ascii_art:
                file.write(line + '\n')
        print(f"ASCII art written to {output_file}")
    except Exception as e:
        print(f"Error: Unable to write to file '{output_file}'. {e}")

if __name__ == "__main__":
    main()
