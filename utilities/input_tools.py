def str_input(print_text):
    user_input = raw_input(print_text)
    if user_input != '':
        output = u'"' + user_input.decode("utf-8") + u'"'
    else:
        output = u'NULL'
    return output


def int_input(print_text):
    user_input = raw_input(print_text)
    if user_input == '':
        output = u'NULL'
    else:
        output = unicode(user_input)
    return output
