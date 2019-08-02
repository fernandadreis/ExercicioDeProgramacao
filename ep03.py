# -*- coding: utf-8 -*-

#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
import random

#####################################################################
# CONSTANTES
# Constantes definem variáveis cujos valores NÃO DEVEM ser 
# alterados durante a execução do programa. Assim você deve
# escolher bem esses valores ANTES de executar o programa.
#
# O uso de constantes é um boa prática de programação
# pois constantes ajudam a melhorar a legibilidade
# de seus programas. Por convenção, para identificar
# as constantes em um programa, vamos usar nomes com todas 
# as letras maiúsculas.
#
# As constantes abaixo são fornecidas como exemplo. Você
# pode utilizar, ou não, qualquer uma delas e ainda criar 
# outras constantes se desejar.
#
DEBUG = True       # se True, pede para digitar a semente e mostra a senha
MENOR_VALOR = 0    # menor número sorteado
MAIOR_VALOR = 1000 # limite superior para o maior número sorteado (mais 1)
MAX_TENTATIVAS = 5 # número máximos de chutes permitidos
NUM_DIGITOS  = 3   # número de dígitos da senha

#####################################################################
def main():
    '''(None) -> None 
    Vamos criar uma versão bem simplificada do jogo, onde o programa sorteia 
    um número de até 3 dígitos, que vamos chamar de senha, e o jogador tem 5 
    chances para acertar a senha sorteada.
    
    Escreva um programa ( main() ) que sorteia um inteiro senha entre 0 e 999, 
    e pergunte ao jogador que ele chute um número tentando descobrir qual o 
    número sorteado.
    
    Seu programa deve permitir ao jogador que chute até 5 vezes e, a cada 
    chute, indicar apenas se o jogador acertou a senha ou não. Caso o jogador
    adivinhar a senha, o programa deve parar e dar os parabéns. Ao final do 
    número máximo de tentativas, o programa deve se despedir do jogador.
 
    '''

    print("Bem vindo ao MASTER BIME!!")
    # as linhas abaixo vão ajudar durante o desenvolvimento e depuração 
    # para deixar de executá-las, basta modificar a constante DEBUG para 
    # False. 
    if DEBUG:
        semente = int(input("Digite o valor da semente: "))
        random.seed(semente)
        senha = random.randrange(MENOR_VALOR, MAIOR_VALOR)
        print("Número sorteado: ", senha)
    else:
        senha = random.randrange(MENOR_VALOR, MAIOR_VALOR)
   # escreva seu programa a seguir
    n = 1
    chute=0
    while n<6 and chute!=senha:
     chute = int(input('Digite seu chute: '))
     if chute!=senha:
      print('Chute',n,'/ 5 : errado!')
      n=n+1
     if n==6:
         print('Ha ha, você perdeu!')
     if chute==senha:
      print('Chute',n,'/ 5 : certo!')   
      print('Parabéns, você acertou!')   
      
    print("Fim do jogo.")

    # fim da main()

if __name__ == "__main__":
    main()