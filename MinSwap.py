# Minimum Swaps required to group all 1’s together
t = int(input())
for _ in range(t):
    n = int(input())
    bina = input().split()
    ones = []
    if '1' not in bina:
        print("-1")
    else:
        aux = ""
        for  i in bina:
            if i == '1':
                aux += '1'
        #print(bina[1:4+1])
        maycont = 1000000000000000
        cont = 0
        for j in range(len(bina)):
            if j + len(aux) < len(bina) + 1:
                auxx = bina[j:len(aux)+j]
                for i in range(len(aux)):
                    if aux[i] != auxx[i]:
                        cont += 1
                if cont < maycont:
                    maycont = cont
                cont = 0
        print(maycont)
