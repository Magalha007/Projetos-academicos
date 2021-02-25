print('======== Bem vindo ========')
print('OBS: O diretorio deve ter esse formato C:/Users/[nome do usuário]/Desktop/')
diret = input('Digite o diretório onde serão salvos os arquivos gerados pelo programa:\n')
pergunta = input('Deseja fazer a criptografia ou descriptografia?\n(Use apenas letras minúsculas)\n')
resposta1 = 'criptografia'
resposta2 = 'descriptografia'
while pergunta == '':
    pergunta = input('Deseja fazer a criptografia ou descriptografia?: ')
    resposta1 = 'criptografia'
    resposta2 = 'descriptografia'
if pergunta == resposta1:
    senha = input('Digite uma senha de 8 caracteres ou mais para a criptografia: ')
    while len(senha) <= 7:
        senha = input("Digite uma senha de 8 caracteres ou mais.")
    def key_crypt():
        key = []
        lista = []
        for x in senha:
            key.append(ord(x))
        for z in key:
            lista.append(str(z + 5))
        return lista
    conver = (','.join(key_crypt()).replace(',', ''))
    with open(diret+"key.txt", "w") as ff:
        ff.write(conver)
    frase = input('Digite sua mensagem:\n ')
    while len(frase) >= 129:
        print("Digite uma mensagem de até 128 caracteres.")
        frase = input('Digite sua mensagem:\n ')
    def crypt_frase():
        crfrase = []
        codefrase = []
        for x in frase:
            crfrase.append(ord(x))
        for c in crfrase:
            codefrase.append(str(c + 7))
        resultfrase = '§'.join(codefrase).replace('§', '31')
        return resultfrase
    with open(diret+'mensagem.txt', 'w') as ff:
        ff.write(crypt_frase())
    print('Sua mensagem foi criptografada em um arquivo de texto criado no diretorio escolhido!\nPara descriptografar a mensagem, reinicie o programa.')
elif pergunta == resposta2:
    def prockey():
        try:
            with open(diret+"key.txt", 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False
    def procarquivo():
        try:
            with open(diret + "mensagem.txt", 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False
    if prockey() and procarquivo() == True:
        def decrypt_frase():
            with open(diret+'mensagem.txt', 'r') as ff:
                decrypt = ff.read()
            dec = decrypt.replace('31', ' ')
            declist = dec.split()
            declistint = []
            subdec = []
            for d in declist:
                declistint.append(int(d))
            for r in declistint:
                subdec.append(chr(r - 7))
            resultdec = '§'.join(subdec).replace('§', '')
            return resultdec
        token = input('Digite a key gerada em key.txt, no diretório que optou: ')
        with open(diret+'key.txt', 'r') as ff:
            teste3 = ff.read()
        while token != teste3:
            print('A senha está errada.')
            token = input('Digite a mesma key para descriptografar a mensagem: ')
        with open(diret+'descriptografia.txt', 'w') as ff:
            ff.write(decrypt_frase())
        print('Descriptografia finalizada e salva no diretorio escolhido!')
    else:
        print('Para fazer a descriptografia é necessário que você tenha os arquivos da senha (key.txt) e mensagem (mensagem.txt) no local especificado.')
else:
    print('Por favor inicie o programa novamente e escolha uma das opcões apresentadas.')
