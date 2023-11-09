with open('working_on.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    print(text)
    s = []
    stig = ''
    for i in text:
        stig += i

        if i == '(':
            s.append(1)
        if i == '[':
            s.append(2)
        if i == '{':
            s.append(3)

        if i == ')':
            if s[len(s)-1] != 1:
                print('error in ()')
                break
            s = s[0:-1]

        if i == ']':
            if s[len(s)-1] != 2:
                print('error in []')
                break
            s = s[0:-1]

        if i == '}':
            if s[len(s)-1] != 3:
                print('error in {}')
                break
            s = s[0:-1]
    if s != []:
        print('errors')
    print(stig)
