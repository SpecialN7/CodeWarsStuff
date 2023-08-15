def first_non_repeating_letter(s):
    dictionary = []
    for letter in s:
        if letter.lower() in dictionary:
            dictionary.remove(letter.lower())
        elif letter.upper() in dictionary:
            dictionary.remove(letter.upper())
        else:
            dictionary.append(letter)
    if len(dictionary) == 0:
        return ""
    else:
        return dictionary [0]
    pass 
