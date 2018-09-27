# 字符串格式化符
print('{} a word she can get what she {} for.'.format('With', 'came'))

print('{preposition} a word she can get what she {verb} for.'.format(preposition = 'With',verb='came'))

print('{0} a word she can get what she {1} for.'.format('With','came'))


city = input('write down the name of city')
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

print(url)