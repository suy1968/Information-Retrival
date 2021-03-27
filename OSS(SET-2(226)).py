def deletion(non_word,real_word):
    if(len(non_word) <= len(real_word)):
        return -1
    for i in range(len(real_word)):
        previous_part = real_word[:i]
        after_part = real_word[i + 1:]
        now_word = previous_part + real_word[i] + after_part
        if(now_word == non_word):
            return i
    return -1

def insertion(non_word,real_word):
    if(len(non_word) >= len(real_word)):
        return -1
    for i in range(len(real_word)):
        previous_part = real_word[:i]
        after_part = real_word[i + 1:]
        now_word = previous_part + after_part
        if(now_word == non_word):
            return i
    return -1

def transpose(non_word,real_word):
    if(len(non_word) != len(real_word)):
        return -1
    for i in range(len(real_word) - 1):
        copy_real = list(real_word)
        copy_real[i],copy_real[i + 1] = copy_real[i + 1],copy_real[i]
        now_word = ''
        for j in copy_real:
            now_word += j
        if(now_word == non_word):
            return i
    return -1

def substitution(non_word,real_word):
    if(len(non_word) != len(real_word)):
        return -1
    for i in range(len(real_word)):
        previous_part = real_word[:i]
        after_part = real_word[i + 1:]
        now_word = previous_part + non_word[i] + after_part
        if(now_word == non_word):
            return i
    return -1

real_words = ['actress','across','caress']
non_word = 'acress'
for i in real_words:
    real_word = i
    if(insertion(non_word,real_word) > -1):
        print('Insert at position : ' + (str)(insertion(non_word,real_word)))
    elif(deletion(non_word,real_word) > -1):
        print('Delete at position : ' + (str)(deletion(non_word,real_word)))
    elif(transpose(non_word,real_word) > -1):
        print('Transpose at position : ' + (str)(transpose(non_word,real_word)))
    elif(substitution(non_word,real_word) > -1):
        print('Substitute at position : ' + (str)(substitution(non_word,real_word)))
