estudante = []
empresa = []
imovel = []
estagio = []

while True:
    print('---- bem vindo ao habitua estudante ----')
    print('1- cadastre-se')
    print('2- login')
    print('0- sair do programa')

    op = input('digite a opção desejada: ')

    # ----------- CADASTRO -------------- #

    if op == '1':
        print('\n---- cadastro -----')
        tipo_conta = input('voçê é empresa ou estudante: ')

        if tipo_conta == 'estudante':
            info_estudante = {
                'nome' : input('nome completo: '),
                'curso' : input('curso: '),
                'universidade' : input('universidade: '), 
                'email' : input('seu melhor email: '),
                'senha' : input('senha: ')
            }
            estudante.append(info_estudante)
            print('Estudante cadastrado com sucesso!')
        
        elif tipo_conta == 'empresa':
            info_empresa = {
                'nome' : input('nome da empresa: '),
                'responsável' : input('nome do responsável pela empresa: '),
                'email' : input('email: '),
                'senha' : input('senha: ')
            }
            empresa.append(info_empresa)
            print('empresa cadastrada com sucesso!')
        
        else:
            print('Tipo de conta inválido.')


    # ------------ LOGIN -------------- #

    elif op == '2':
        print('\n----- login -----')
        email_login = input('Email: ')
        senha_login = input('Senha: ')

        logado = False

        # Login estudante
        for est in estudante:
            if est['email'] == email_login and est['senha'] == senha_login:
                print('Login de estudante realizado com sucesso!')
                logado = True

                while logado:
                    print('Bem vindo à sua nova cidade!')
                    print('1- imovéis para alugar')
                    print('2- repúblicas e quartos')
                    print('3- vagas de estágio')
                    print('4- anunciar república ou quarto')
                    print('0- sair do programa')

                    op = input('digite a opção desejada: ')

                    if op == '1':
                        print('---opções de imoveis para alugar---')
                        if len(imovel) < 1:
                            print('nenhum imóvel disponível')
                        else:
                            for imov in imovel:
                                for chave, valor in imov.items():
                                    print(f'{chave}: {valor}')
                                    print('-' * 30)

                    elif op == '2':
                        print('--- opções de repúblicas e quartos ---')
                        if len(imovel) < 1:  # Aqui você está usando imovel, mas deveria ter uma lista separada
                            print('nenhuma república ou quarto disponível')
                        else:
                            for rep in imovel:
                                for chave, valor in rep.items():
                                    print(f'{chave}: {valor}')
                                    print('-' * 30)

                    elif op == '3':
                        print('--- vagas de estágio ---')
                        if len(estagio) < 1:
                            print('nenhuma vaga de estágio disponível')
                        else:
                            for vaga in estagio:
                                for chave, valor in vaga.items():
                                    print(f'{chave}: {valor}')
                                    print('-' * 30)
                                        
                    elif op == '4':
                        print('--- anunciar república ou quarto ---')
                        info_quarto = {
                            'titulo' : input('titulo do anúncio: '),
                            'tipo' : input('tipo do imóvel (apartamento, casa...): '),
                            'preco' : input('preço mensal: '),
                            'endereco' : input('nome da rua, número e bairro: '),
                            'distancia' : float(input('qual a distancia ate a universidade mais proxima: ')),
                            'quartos' : int(input('possui quantos quartos: ')),
                            'banheiros' : int(input('possui quantos banheiros: ')),
                            'area' : float(input('tamanho do imóvel (m*2): ')),
                            'descricao' : input('descreva o imóvel (comodidades, características...) : '),
                            'contato' : input('digite seu numero para contato: ')
                        }
                        imovel.append(info_quarto)  # Aqui você adiciona na lista imovel
                        print('quarto / república cadastrado(a) com sucesso!')
                        
                    elif op == '0':
                        logado = False

        # Login empresa
        for emp in empresa:
            if emp['email'] == email_login and emp['senha'] == senha_login:
                print('Login de empresa realizado com sucesso!')
                logado = True

                while logado:
                    print('bem vindo, esperamos que consiga alugar seu imóvel ou uma nova contratação para sua empresa!')
                    print('1- alugar imóvel')
                    print('2- contratação')
                    print('0- sair do programa')

                    op = input('digite a opção desejada: ')

                    if op == '1':
                        print('--- anunciar imóvel ---')
                        info_imovel = {
                            'titulo' : input('titulo do anúncio: '),
                            'tipo' : input('tipo do imóvel (apartamento, casa...): '),
                            'preco' : input('preço mensal: '),
                            'endereco' : input('nome da rua, número e bairro: '),
                            'distancia' : float(input('qual a distancia ate a universidade mais proxima: ')),
                            'quartos' : int(input('possui quantos quartos: ')),
                            'banheiros' : int(input('possui quantos banheiros: ')),
                            'area' : float(input('tamanho do imóvel (m*2): ')),
                            'descricao' : input('descreva o imóvel (comodidades, características...) : '),
                            'contato' : input('digite seu numero para contato: ')
                        }
                        imovel.append(info_imovel)
                        print('Imóvel cadastrado com sucesso!')

                    elif op == '2':
                        print('--- anunciar vagas de estágio ---')
                        info_estagio = {
                            'titulo' : input('título da vaga: '),   
                            'area' : input('área: '),
                            'tipo' : input('tipo (presencial, remoto, híbrido): '),
                            'endereco' : input('nome da rua, número e bairro: '),
                            'carga_horaria' : input('carga horária: '),
                            'bolsa_auxilio' : input('bolsa auxílio: '),
                            'descricao' : input('descrição: '),
                            'requisitos': input('requisitos (um por linha): ')
                        }
                        estagio.append(info_estagio)
                        print('Vaga de estágio cadastrada com sucesso!')
                    
                    elif op == '0':
                        logado = False

        if not logado:
            print('Email ou senha incorretos!')

    # ---------- SAIR ---------- #
    elif op == '0':
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida.')