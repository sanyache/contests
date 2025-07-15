def repeating(s, sub):
    counter = 0
    word = sub
    while s.count(sub):
        sub += word
        counter += 1
    return counter


sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
print(repeating(sequence, word))