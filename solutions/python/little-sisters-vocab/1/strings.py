"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """

    finalword = "un" + word
    return finalword

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words."""
    
    # 1. Sacamos el prefijo (ej: 'en')
    prefix = vocab_words[0]
    
    # 2. Preparamos una lista donde el primer elemento es solo el prefijo
    resultado = [prefix]
    
    # 3. Recorremos las palabras (sáltandonos la primera con [1:])
    for word in vocab_words[1:]:
        # Le pegamos el prefijo y lo añadimos a la lista
        palabra_con_prefijo = prefix + word
        resultado.append(palabra_con_prefijo)
    
    # En este punto, 'resultado' vale: ['en', 'enclose', 'enjoy', 'enlighten']
    
    # 4. Unimos toda la lista con ' :: '
    return ' :: '.join(resultado)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """

    raiz = word [:-4]

    if raiz [-1] == "i":
        raiz = raiz [:-1] + "y"

    return raiz


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """
    words = sentence.split()

    adv = words [index]

    clean = adv.strip(".")

    return clean + "en"
