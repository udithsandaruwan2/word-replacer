def word_replacement():
    str = input("Paragraph / Sentense or Etc : \n")
    print("\n")
    want_to_replace = input("The word you want to replace : ")
    word_replacement = input("The Replacement word : ")
    print("\n")
    outcome = str.replace(want_to_replace, word_replacement)
    return outcome

print(word_replacement())