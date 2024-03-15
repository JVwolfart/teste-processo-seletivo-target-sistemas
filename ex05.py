"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

string = input("Digite uma frase: ")

def inverte_string(s):
    reverso = ""
    for i in range(len(s)-1, -1, -1):
        reverso += s[i]
    return reverso

print("\n\n")
print(inverte_string(string))