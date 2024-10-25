#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo 
# #valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 
# 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que 
# desejar onde, informado um número, ele calcule a sequência de 
# Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.
'''
# Função que gera a sequencia Finonacci
def seq_fibonacci(n):
    
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
    # Retorna True se n pertence à sequência

# Entrada do usuário
num = int(input("Informe um número: "))

# Verificação e saída
if seq_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
'''''''''  

#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, 
# além de informar a quantidade de vezes em que ela ocorre.
#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;


# Função  que converte a string para minúsculas e conta quantas vezes tem o 'a'

''''''''''
def contar_a(string):
    
    quantidade = string.lower().count('a')
    
    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vezes.")
    else:
        print("A letra 'a' não aparece.")

# Entrada do usuário
texto = input("Digite uma palavra ou uma frase: ")

# Verificação
contar_a(texto)
'''''''''


# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1;
# SOMA = SOMA + K; } imprimir(SOMA); Ao final do processamento, qual será o valor da variável SOMA?
'''''
indice= 12
soma= 0 
k=1

while k< indice:
    k = k+1
    soma= soma+k
    
print(soma)
# Resposta: 77
'''''

#4) Descubra a lógica e complete o próximo elemento:
#a) 1, 3, 5, 7, ___
#b) 2, 4, 8, 16, 32, 64, ____
#c) 0, 1, 4, 9, 16, 25, 36, ____
#d) 4, 16, 36, 64, ____
#e) 1, 1, 2, 3, 5, 8, ____
#f) 2,10, 12, 16, 17, 18, 19, ____

'''''
# Função da letra 'a' Sequência de números ímpares
def completar_a():
    
    return 9

# Função da letra 'b' Sequência que dobra a cada passo
def completar_b():
    
    return 128

# Função da letra 'c' Quadrados perfeitos
def completar_c():
    
    return 49  # 7^2

# Função da letra 'd' Quadrados perfeitos pares
def completar_d():
    
    return 100  # 10^2

# Função letra 'e' Sequência de Fibonacci
def completar_e():
    
    return 13

# Função letra 'f' Sequência de números com exclusão do 11 e múltiplos de 5
def completar_f():
    
    return 20

# Imprimir os próximos elementos
print("a) 1, 3, 5, 7,", completar_a())
print("b) 2, 4, 8, 16, 32, 64,", completar_b())
print("c) 0, 1, 4, 9, 16, 25, 36,", completar_c())
print("d) 4, 16, 36, 64,", completar_d())
print("e) 1, 1, 2, 3, 5, 8,", completar_e())
print("f) 2, 10, 12, 16, 17, 18, 19,", completar_f())
'''''

#5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você 
# não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
# Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas
# duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

'''''
import time

# Simulando o estado das lâmpadas
def descobrir_interruptores():
    
    lampadas = {"lampada1": "fria", "lampada2": "fria", "lampada3": "fria"}
    
    # Simulando o tempo em que o interruptor 1 foi ligado
    print("Ligando o interruptor 1 por um tempo...")
    lampadas["lampada1"] = "quente"  
    time.sleep(2)  
    
    # Agora desligando o interruptor 1 e ligando o interruptor 2
    print("Desligando o interruptor 1 e ligando o interruptor 2...")
    lampadas["lampada1"] = "quente, apagada"  
    lampadas["lampada2"] = "acesa" 
    
    # Lâmpada 3 continua fria e apagada porque o interruptor 3 nunca foi ligado
    lampadas["lampada3"] = "fria, apagada"
    
    # Simulação da ida até a sala das lâmpadas
    print("\nVocê vai até a sala das lâmpadas para verificar o estado delas:")
    for lampada, estado in lampadas.items():
        print(f"{lampada}: {estado}")

    # Determinando qual interruptor controla qual lâmpada
    if lampadas["lampada1"] == "quente, apagada":
        print("\nO interruptor 1 controla a lampada1 (quente, mas apagada).")
    if lampadas["lampada2"] == "acesa":
        print("O interruptor 2 controla a lampada2 (ligada e acesa).")
    if lampadas["lampada3"] == "fria, apagada":
        print("O interruptor 3 controla a lampada3 (fria e apagada).")

# Chamada da função para resolver o problema
descobrir_interruptores()
'''''