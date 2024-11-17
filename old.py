file = open('standard.txt')
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
text = input()

for lines in zip(*(symbol_dict.get(char, ['']) for char in text)):
    print(' '.join(lines))

if __name__ == "__main__":
    main()
    input("\nШығу үшін любой кнопка...")
