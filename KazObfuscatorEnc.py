import random
import getpass


password = getpass.getpass("Enter Password : ")
digit = int(getpass.getpass("Enter Extra Digit (Min 8) : "))
random.seed(password)


characters_list = []

for i in range(1114111):
    characters_list.append(chr(i))


def extrachar(value):
        for i in value:
            if i not in characters_list:
                characters_list.append(i)

extrachar(['\r','\n','️'])

min,max = int('1'*digit),int('9'*digit)
random_values = random.sample(range(min, max), len(characters_list))


kamus = {char: str(val) for char, val in zip(characters_list, random_values)}

def encode(file):
    code = file
    try:
        encode = ''.join([kamus[i] for i in code.decode()])
    except:
        raise Exception('''Karakter Tidak Ditemukan, Tambahkan Menggunakan extrachar() atau tambahkan manual kedalam module,
Kombinasi ExtraChar harus sama persis untuk mendapatkan Result yang sama''')
    tobyte = encode.encode()
    return tobyte


def decode(file):
    tostr = file.decode()
    splitdecode = [tostr[i:i+digit] for i in range(0, len(tostr),digit)]
    decode = ''.join([find(i) for i in splitdecode])
    return decode.encode()
    
def find(value):
    for u,i in kamus.items():
        if i == value:
            return str(u)
        
def write(path, content):
    head = f'''import requests;req = requests.get('https://raw.githubusercontent.com/KazamaReinjector/KazObfuscator/main/KazObfuscatorEnc.py');exec(req.content);exec(decode({content}))'''
    with open(path, 'w') as file:
        file.write(head)
