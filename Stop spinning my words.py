def spin_words(sentence):
    stringReturn = ""
    word = ""
    for i in range(len(sentence)):
        if i == len(sentence) - 1:
            if sentence[i] != " ":
                word += sentence[i]
            if len(word) >= 5:
                word = word[::-1]
                stringReturn += word + " "
                word = ""
            else:
                stringReturn += word + " "
                word = ""
        elif sentence[i] != " ":
            word += sentence[i]
        else:
            if len(word) >= 5:
                word = word[::-1]
                stringReturn += word + " "
                word = ""
            else:
                stringReturn += word + " "
                word = ""
    return stringReturn.strip()

sentence = " hi there Welcome Friends hi"
print(spin_words(sentence))