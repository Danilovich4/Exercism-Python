def is_pangram(sentence):
# Convertimos a minúsculas y filtramos solo los caracteres que son letras del alfabeto
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters_in_sentence = set(c.lower() for c in sentence if c.isalpha())
    
    # Comprobamos si el alfabeto está contenido en las letras de la frase
    return alphabet.issubset(letters_in_sentence)