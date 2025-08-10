def longest(words, groups):
    rez = []
    flag = not (True if groups[0] else False)
    for word, group in zip(words, groups):
        curr_flag = True if group else False
        if curr_flag != flag:
            rez.append(word)
            flag = not flag
    return rez

words = ["a","b","c","d"]
groups = [1,0,1,1]
print(longest(words, groups))