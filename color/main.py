import sys

ANSI_COLORS={
    "red": "\033[31m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "white": "\033[37m",
    "reset": "\033[0m",
}


def load_ascii_art(filename):
    with open(filename, 'r') as file:
        lines=file.read().split('\n')
    symbol_dict={}
    current_symbol=[]
    current_symbol_code=32
    for line in lines:
        if len(line) == 0:
            if current_symbol:
                symbol_dict[chr(current_symbol_code)]=current_symbol
                current_symbol=[]
                current_symbol_code+=1
        else:
            current_symbol.append(line.rstrip('\n'))
    if current_symbol:
        symbol_dict[chr(current_symbol_code)]=current_symbol

    return symbol_dict


def colorize(text, color):
    if color in ANSI_COLORS:
        return f"{ANSI_COLORS[color]}{text}{ANSI_COLORS['reset']}"
    return text


def print_ascii_art(text, symbol_dict, color=None, letters_to_color=None):
    for lines in zip(*(symbol_dict.get(char, ['']) for char in text)):
        line=' '.join(lines)
        if color and letters_to_color:
            line=''.join(colorize(char, color) if char in letters_to_color else char for char in line)
        elif color:
            line=colorize(line, color)
        print(line)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [OPTION] [STRING]")
        print("\nEX: python3 main.py --color=<color> <letters to be colored> \"something\"")
        sys.exit(1)

    option=sys.argv[1]
    if option.startswith("--color="):
        color=option.split("=")[1]
        if len(sys.argv) < 4:
            print("Usage: python3 main.py [OPTION] [STRING]")
            print("\nEX: python3 main.py --color=<color> <letters to be colored> \"something\"")
            sys.exit(1)

        letters_to_color=sys.argv[2]
        text=sys.argv[3]
    else:
        color=None
        letters_to_color=None
        text=sys.argv[1]

    symbol_dict=load_ascii_art('sometext.txt')

    print_ascii_art(text, symbol_dict, color=color, letters_to_color=letters_to_color)


if __name__ == "__main__":
    main()
    input("\nPress any key to continue...")


#  python main.py --color=blue "H" "Hello, World!"