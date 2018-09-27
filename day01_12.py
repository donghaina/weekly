def text_create(name, msg):
    path = name + '.txt'
    file = open(path, 'w')
    file.write(msg, )
    file.close()
    print('Done')


def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)

def censord_text_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)

censord_text_create('Try', 'lame!lame!lame!')
