from random import randint
n = int (randint(1,9))
p = 0
while p != n:
    p = int(input("Seu palpite: "))
    if p == n:
        print("ACERTOU!!")
    elif p < n:
        print ("Chute um valor maior")
    else:
        print("Chute um valor menor")
print ("Fim do jogo")