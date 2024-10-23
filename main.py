import string


def prelucrare_text(text_articol):
    # Împarte șirul în două părți egale
    index_mijloc = len(text_articol) // 2
    prima_parte = text_articol[:index_mijloc]
    a_doua_parte = text_articol[index_mijloc:]

    # Prelucrarea primei părți: majuscule și eliminarea spațiilor de la început și final
    prima_parte = prima_parte.upper().strip()

    # Prelucrarea celei de-a doua părți: inversarea șirului, majusculă la început, eliminarea punctuației
    a_doua_parte = a_doua_parte[::-1]  # Inversare șir
    a_doua_parte = a_doua_parte.capitalize()  # Prima literă în majusculă

    # Eliminarea caracterelor de punctuație din a doua parte
    a_doua_parte = ''.join(caracter for caracter in a_doua_parte if caracter not in string.punctuation)

    # Combinarea celor două părți
    text_prelucrat = prima_parte + a_doua_parte
    return text_prelucrat


# Exemplu de utilizare
text_articol = """Acesta este un exemplu de articol copiat de pe internet. Este doar un text de test pentru exemplificare!"""
text_final = prelucrare_text(text_articol)
print(text_final)
