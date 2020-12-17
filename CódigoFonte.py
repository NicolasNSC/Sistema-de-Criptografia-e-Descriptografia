from time import sleep
from tqdm import tqdm, trange
import getpass

# Membros do Grupo com RA e Turma
'''
Letícia Coutinho da Silva - N5752E4
Lucas Vinícius Mercadante - N6535E7
Nicolas Castanha - N618BJ2
Mateus Teixeira Dos Santos - F31AHD0
Monique Santos Mota - F182843
Lucas Gabriel Paiva - F2417A3
Rafael Silvestre dos Santos – G162641
Turma: CC2A41
'''

print("="*180)
print("\033[4;33mEmail Confidencial - Com Cifra de Cesar\033[m".center(180))

usuario = None
senha = None





def criptografar():
    cripto = ''
    mensagem = '''
    Caro amigo, Dudu Pazuello. Venho de imediato lhe informar uma situação deliciada, cujo problema ocorre no navio. Gostaria de ter suas instruções para me ajudar com o ocorrido.
    Lembra-se daquele vírus que havia sido descoberto na América do Norte? Receio que ele tenha chegado à região da Baixada Santista, pois um dos tripulantes foi encontrado morto com os mesmos sintomas de E-bow. Me encontro desesperado sem saber o que fazer, porque os passageiros estão no ápice de entrar em pânico. Cerca de cinquenta da tripulação apresentam os sintomas deste vírus, e estão em isolamento, para que o mesmo não se espalhe entre eles, assim precavendo  mais mortalidades. Pude avaliar a melhor maneira para qual o vírus não se alastre para fora do navio, deixando todos os tripulantes, de quarentena. Tem alguma objeção conquanto a isso?
    '''
    chave = 13

    for i in mensagem:
        if 'A' <= i <= 'Z':
            if ord(i) - chave < ord('A'):
                cripto += chr(ord('Z') - (chave - (ord(i)+1 - ord('A'))))
            else:
                cripto += chr(ord(i) - chave)
        elif 'a' <= i <= 'z':
            if ord(i) - chave < ord('a'):
                cripto += chr(ord('z') - (chave - (ord(i)+1 - ord('a'))))
            else:
                cripto += chr(ord(i) - chave)
        else:
            cripto += i 
    return cripto

def resposta_usuario(mensagem):
    cripto = ''
    chave = 13
    for i in mensagem:
        if 'A' <= i <= 'Z':
            if ord(i) - chave < ord('A'):
                cripto += chr(ord('Z') - (chave - (ord(i)+1 - ord('A'))))
            else:
                cripto += chr(ord(i) - chave)
        elif 'a' <= i <= 'z':
            if ord(i) - chave < ord('a'):
                cripto += chr(ord('z') - (chave - (ord(i)+1 - ord('a'))))
            else:
                cripto += chr(ord(i) - chave)
        else:
            cripto += i 
    return cripto

def descriptografar():
    cripto = ''
    mensagem = criptografar()
    chave = 13

    for i in mensagem:
        if 'A' <= i <= 'Z':
            if ord(i) + chave > ord('Z'):
                cripto += chr((ord('A') + chave - (ord('Z')+1 - ord(i))))
            else:
                cripto += chr(ord(i) + chave)
        elif 'a' <= i <= 'z':
            if ord(i) + chave > ord('z'):
                cripto += chr((ord('a') + chave - (ord('z')+1 - ord(i))))
            else:
                cripto += chr(ord(i) + chave)
        else:
            cripto += i
    return cripto
    


while(usuario != 'DUDUPAZUELLO' and senha != 'TOMPERODETERERE'):
    print("")
    print("Por favor, faça o seu login.")
    print("")
    usuario = input("Digite o usuario: ").upper()
    senha = getpass.getpass("Digite a senha: ").upper()
    print("")
    for i in trange(5):
        sleep(0.1)
        pass
    print("="*180)

    if (usuario == 'DUDUPAZUELLO' and senha == 'TOMPERODETERERE'):
        print("\033[1;34mVocê recebeu uma mensagem criptografada!\033[m".center(180))
        
        opcao = None

        while(opcao != 4):
            print("="*180)
            print("Escolha uma opção abaixo:")
            print("")
            print("[1] Visualizar a mensagem")
            print("[2] Descriptografar a mensagem")
            print("[3] Responder a mensagem")
            print("[4] Sair do programa")
            print("")
            opcao = int(input("Digite a opção: "))
            print("")

            if(opcao == 1):
                for i in trange(5):
                    sleep(0.1)
                    pass
                print("="*180)
                print("")
                print("MENSAGEM CRIPTOGRAFADA".center(180))
                print("")
                print(criptografar())
            elif(opcao == 2):
                for i in trange(5):
                    sleep(0.1)
                    pass
                print("="*180)
                print("")
                print("MENSAGEM DESCRIPTOGRAFADA".center(180))
                print("")
                print(descriptografar())
            elif(opcao == 3):
                print("="*180)
                print()
                mensagem = input("Digite a sua resposta: ")
                print("")
                print("Por favor, aguarde...")
                print()
                for i in trange(5):
                    sleep(0.1)
                    pass
                print("")
                print("Resposta Criptografada: ",resposta_usuario(mensagem))
                print("")
                print("\033[32mMensagem enviada com sucesso!\033[m".center(180))
                print("")
            elif(opcao == 4):
                print("Por favor aguarde, estamos fechando o programa...")
                for i in trange(5):
                    sleep(0.1)
                    pass
                print("")
                print("Fim do Programa! Volte sempre.".center(170))
                print("")
                print("\033[1;35mRealizado pelo Grupo STONKS ❤\033[m".center(180))
                print("")
                print("\033[1;35mLetícia Coutinho\033[m".center(180))
                print("\033[1;35mLucas Mercadante\033[m".center(180))
                print("\033[1;35mNicolas Castanha\033[m".center(180))
                print("\033[1;35mMateus Teixeira\033[m".center(180))    
                print("\033[1;35mMonique Santos\033[m".center(180))
                print("\033[1;35mLucas Paiva\033[m".center(180))
                print("\033[1;35mRafael Silvestre\033[m".center(180))
                print("="*180)
            else:
                print("="*180)
                print("\033[1;31mOpção Inválida! Tente novamente.\033[m".center(180))
    else:
        print("\033[1;31mErro no usuario ou senha! Tente novamente.\033[m".center(180))
        print("="*180)