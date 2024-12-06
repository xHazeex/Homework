def singl_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words)

    for i in range(len(words)):
         if words[i].lower() in root_word.lower() or root_word.lower() in words[i].lower():
            same_words.append(words[i])
    return(same_words)

result1 = singl_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = singl_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)