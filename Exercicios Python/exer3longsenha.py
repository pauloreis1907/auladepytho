def t (asd,qwe):
    senha = 'asd'
    login = 'qwe'
    return senha == asd and login == qwe
login = str (input('digite sua senha:'))
senha = str (input('digite seu login:'))

print(t(login,senha))