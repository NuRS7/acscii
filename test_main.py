import pytest
from main import load_ascii_art, print_ascii_art



def test_load_ascii_art_empty_file(tmp_path):
    ascii_art_file = tmp_path / 'standard.txt'
    ascii_art_file.write_text('')

    symbol_dict = load_ascii_art(ascii_art_file)

    assert symbol_dict == {}

def test_print_ascii_art(capsys):
    symbol_dict = {'H': ['####', '#  #', '#  #', '####'], 'e': ['#####', '#   #', '#   #', '#####']}

    print_ascii_art('He', symbol_dict)

    captured = capsys.readouterr()
    assert captured.out == '#### #####\n#  # #   #\n#  # #   #\n#### #####\n'

