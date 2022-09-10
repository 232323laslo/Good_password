def is_password_good(password):
    flag = False
    i = 0
    lst = []
    s1 = ' '.join(txt)
    s2 = s1.split()

    if len(s2) > 7:
        lst.append(1)
    while flag == False and i == 0:
        for i in range(len(s2)):
            if s2[i].isupper():
                lst.append(1)
                flag = True
                break

    flag = False
    i = 0

    while flag == False and i == 0:
        for i in range(len(s2)):
            if s2[i].islower():
                lst.append(1)
                flag = True
                break

    flag = False
    i = 0

    while flag == False and i == 0:
        for i in range(len(s2)):
            if s2[i] in '0123456789':
                lst.append(1)
                flag = True
                break

    if len(lst) == 4:
        return 'Your password is safe!'
    else:
        return 'Your password is not safe!:('


txt = input('Password: ')

print(is_password_good(txt))