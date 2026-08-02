def translate(text):
    palabras_traducidas = []
    
    # Separamos la frase en palabras individuales
    for word in text.split():
        
        # 1. Regla 1: Vocal inicial, 'xr' o 'yt'
        if word[0] in "aeiou" or word.startswith("xr") or word.startswith("yt"):
            palabras_traducidas.append(word + "ay")
            
        # 2. Regla 3: Consonantes seguidas de 'qu' (ej: "quick", "square")
        # Si 'qu' está en la palabra y todo lo anterior a 'qu' son consonantes
        elif "qu" in word and all(c not in "aeiou" for c in word[:word.index("qu")]):
            i = word.index("qu") + 2  # Cortamos DESPUÉS de 'qu'
            palabras_traducidas.append(word[i:] + word[:i] + "ay")
            
        # 3. Regla 4: Consonantes seguidas de 'y' (ej: "my", "rhythm")
        # Si 'y' está en la palabra, no es la primera letra, y antes solo hay consonantes
        elif "y" in word and word.index("y") > 0 and all(c not in "aeiou" for c in word[:word.index("y")]):
            i = word.index("y")  # Cortamos JUSTO EN la 'y'
            palabras_traducidas.append(word[i:] + word[:i] + "ay")
            
        # 4. Regla 2: Consonantes normales (ej: "pig", "chair", "thrush")
        else:
            # Buscamos el índice de la primera vocal
            i = 0
            while i < len(word) and word[i] not in "aeiou":
                i += 1
            palabras_traducidas.append(word[i:] + word[:i] + "ay")

    # Unimos todas las palabras traducidas con un espacio
    return " ".join(palabras_traducidas)