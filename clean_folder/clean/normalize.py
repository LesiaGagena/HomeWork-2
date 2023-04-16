import re

cyrilic_simbol = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєії'
translation = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", 'i', "ji", "g")
TRANS = {}

for c, l in zip(cyrilic_simbol, translation):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W\.', '_', t_name)
    return t_name
