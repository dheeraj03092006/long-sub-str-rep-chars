def long_rep(s):
    sub_str_list = []
    for i in range(len(s)):
        new_str = ""
        for j in range(i, len(s)):
            if s[i] == s[j]:
                new_str += s[j]
            else:
                break
        if len(new_str) > 1:
            sub_str_list += [new_str]
    #print(sub_str_list)

    max_len = 0
    max_str = ""
    for elem in sub_str_list:
        if len(elem) > max_len:
            max_len = len(elem)
            max_str = elem
    print(max_str)
    print()


n_str= str(input("Enter the string to give longest repeated substring: "))

long_rep(n_str)
