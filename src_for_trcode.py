def ad_to_buffer(string, buffer2):
    string2 = ''
    for j in string:
        string2 += j
    buffer2.append(string2)
    buffer2.append(':')
    buffer2.append('\n\t')


def ad_if(buffer2, i):
    buffer2.append('if')
    if ' и ' in i:
        string = [j for j in i[4:-1]]
        string[string.index('и')] = 'and'
        ad_to_buffer(string, buffer2)
    elif 'или' in i:
        string = [j for j in i[4:-1]]
        string[string.index('и'):string.index('и') + 3] = 'or'
        ad_to_buffer(string, buffer2)
    elif 'не' in i:
        string = [j for j in i[4:-1]]
        ad_to_buffer(string, buffer2)
    if '=' in i:
        string = [j for j in i[4:-1]]
        string[string.index('=')] = '=='
        ad_to_buffer(string, buffer2)
    else:
        buffer2.append(i[4:-1])
        buffer2.append(':\n\t')


def ad_while(buffer2, i):
    buffer2.append('while')
    if ' и ' in i:  # проверяем, есть ли в условии служебные слова И, ИЛИ, НЕ
        string = [j for j in i[7:-1]]
        string[string.index('и')] = 'and'
        ad_to_buffer(string, buffer2)
    elif 'или' in i:
        string = [j for j in i[7:-1]]
        string[string.index('и'):string.index('и') + 3] = 'or'
        ad_to_buffer(string, buffer2)
    elif 'не' in i:
        string = [j for j in i[7:-1]]
        string[string.index('е') - 1:string.index('е') + 1] = '!='
        ad_to_buffer(string, buffer2)
    else:
        buffer2.append(i[7:-1])
        buffer2.append(':')
        buffer2.append('\n\t')


def ad_for(buffer2, i):
    buffer2.append('for ')
    buffer2.append(i[7:i.index('от')])
    buffer2.append('in range(')
    buffer2.append(i[i.index(' до ')+4:-1])
    buffer2.append('):\n\t')


def print_comment(buffer2, i):
    buffer2.append('#')  # то пишем комментарий
    buffer2.append(i[4:])


def var_func(buffer2, i):
    if '=' in i:  # если переменная определена, то присваиваем ему значение
        buffer2.append(i[4:i.index('=') - 1])
        buffer2.append(i[i.index('='):])
    else:  # если нет определения, то присваиваем значение None
        buffer2.append(i[4:])
        buffer2.append('=')
        buffer2.append('None')


def alg_func(buffer2, i):
    st = 'float('  # то составляем выражение, где все переменные приводятся к типу float
    buffer2.append(i[:i.index('=') - 1])
    buffer2.append('=')
    for j in i[i.index('=') + 1:]:
        if j != '*' and j != '+' and j != '-' and j != '/' and j != '%' and j != '**':
            st += j
        if j == '*':
            st += ')'
            buffer2.append(st)
            buffer2.append('*')
            st = 'float('
        if j == '+':
            st += ')'
            buffer2.append(st)
            buffer2.append('+')
            st = 'float('
        if j == '-':
            st += ')'
            buffer2.append(st)
            buffer2.append('-')
            st = 'float('
        if j == '/':
            st += ')'
            buffer2.append(st)
            buffer2.append('/')
            st = 'float('
        if j == '**':
            st += ')'
            buffer2.append(st)
            buffer2.append('**')
            st = 'float('
        if j == i[-1]:
            st += ')'
            buffer2.append(st)
