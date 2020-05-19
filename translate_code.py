def translate(buffer):
    '''Функция, переводящая код'''
    from src_for_trcode import print_comment, var_func, alg_func, ad_for, ad_while, ad_if

    buffer2 = []                                                    # в этом списке будет код на Python
    for i in buffer:
        if 'алг' in i:                                              # если есть слово "алг" в строке
            print_comment(buffer2, i)                               # то вызываем функцию print_comment()

        if ('цел' in i) or ('вещ' in i) or ('сим' in i) or ('лит' in i) or ('лог' in i) or ('таб' in i):  # если есть слова для объявления переменных
            var_func(buffer2, i)                                    # то вызываем функцию var_func()

        if 'ввод' in i:                             # если в строке есть служебное слово ввод,
            buffer2.extend([i[5:-1], 'input()\n'])  # то добавляем переменные и функцию input()

        if 'вывод' in i:                                # если в строке есть служебное слово вывод,
            buffer2.extend(['print(', i[6:-1], ')\n'])  # то составляем строку print(<что выводим>)

        if ('+' in i or '-' in i or '*' in i or '/' in i or '%' in i or '//' in i or '**' in i) and 'вывод' not in i:  # если в строке присутствуют алгебраические операции
            alg_func(buffer2, i)

        if 'нц' in i:                                # если в строке есть слкжебное слово нц, означающее начало цикла,
            if 'для' in i:                           # то проверяем какой это цикл ("для" - for, "пока" - while)
                ad_for(buffer2, i)
            if 'пока' in i:
                ad_while(buffer2, i)
        if 'если' in i:                              # проверка, есть ли ветвление в коде (есть ли служебное слово если)
            ad_if(buffer2, i)
        if 'иначе' in i:
            buffer2.append('else:\n\t')
    return buffer2
