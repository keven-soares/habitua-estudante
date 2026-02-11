cadastro = input('voce possui cadastro n / s: ')
if cadastro == 'n':
    print ('---cadastro de usuarios---')
    tipo_conta = input('estudante / empresa: ')
    if tipo_conta == 'estudante':
        nome_completo = input('digite seu nome completo: ')
        curso = input('qual é seu curso: ')
        universidade = input('digite o nome da sua universidade: ')
        email_estudante = input('digite o seu melhor e-mail: ')
        senha_estudante = input('digite sua senha: ')

        print('cadastro efetuado com sucesso!')

    elif tipo_conta == 'empresa':
        nome_empresa = input('digite o nome da emprese: ')
        nome_responsavel = input('digite o nome do responsável: ')
        email_empresa = input('digite o email da empresa: ')
        senha_empresa = input('digite sua senha: ')

        print('Empresa cadastrada com sucesso!')

    elif cadastro == 's':
        print('---login---')
        email_login = input('digite seu email: ')
        senha_login = input('digite sua senha: ')
        if email_estudante == email_login and senha_estudante == senha_login:
            print('OK')




