def single_root_words(root_word, *other_words):
    same_words = []
    ROOT_WORD = (root_word.upper())
    OTHER_WORDS = (list(b.upper() for b in other_words))
    other_words_str = [str(element) for element in OTHER_WORDS]
    for i in range(len(other_words_str)):
        a = other_words_str[i].find(ROOT_WORD)
        if a != -1:
            same_words.append(other_words[i])
        elif a == -1:
            continue
    for j in range(len(OTHER_WORDS)):
        b = ROOT_WORD.find(other_words_str[j])
        if b != -1:
            same_words.append(other_words[j])
        elif b == -1:
            continue
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
