def response(hey_bob):
    saludo =hey_bob.strip()

    if saludo == "":
        return "Fine. Be that way!"
    elif saludo.endswith("?") and saludo.isupper():
        return "Calm down, I know what I'm doing!"
    elif saludo.isupper():
        return "Whoa, chill out!"
    elif saludo.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
    
