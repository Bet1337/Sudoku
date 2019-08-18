# -*- coding: utf-8 -*-

# Kastro e Bet
# SUDOKU
import sys
import random
div = (1,2,3,4,5,6,7,8,9)
jorge=[
    [' ', ' ', random.choice(div), ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', random.choice(div), ' ', ' ', random.choice(div)],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', random.choice(div), ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', random.choice(div), ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', random.choice(div), ' ', ' '],
    [' ', ' ', ' ', ' ', random.choice(div), ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', random.choice(div), ' '],
    [random.choice(div),' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
def tab():
    print('''+-----------------------+
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
|-------+-------+-------|
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} | 
|-------+-------+-------|
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
+-----------------------+'''.format(jorge[0][0], jorge[0][1], jorge[0][2], jorge[0][3], jorge[0][4], jorge[0][5],
                                    jorge[0][6], jorge[0][7], jorge[0][8],
                                    jorge[1][0], jorge[1][1], jorge[1][2], jorge[1][3], jorge[1][4], jorge[1][5],
                                    jorge[1][6], jorge[1][7], jorge[1][8],
                                    jorge[2][0], jorge[2][1], jorge[2][2], jorge[2][3], jorge[2][4], jorge[2][5],
                                    jorge[2][6], jorge[2][7], jorge[2][8],
                                    jorge[3][0], jorge[3][1], jorge[3][2], jorge[3][3], jorge[3][4], jorge[3][5],
                                    jorge[3][6], jorge[3][7], jorge[3][8],
                                    jorge[4][0], jorge[4][1], jorge[4][2], jorge[4][3], jorge[4][4], jorge[4][5],
                                    jorge[4][6], jorge[4][7], jorge[4][8],
                                    jorge[5][0], jorge[5][1], jorge[5][2], jorge[5][3], jorge[5][4], jorge[5][5],
                                    jorge[5][6], jorge[5][7], jorge[5][8],
                                    jorge[6][0], jorge[6][1], jorge[6][2], jorge[6][3], jorge[6][4], jorge[6][5],
                                    jorge[6][6], jorge[6][7], jorge[6][8],
                                    jorge[7][0], jorge[7][1], jorge[7][2], jorge[7][3], jorge[7][4], jorge[7][5],
                                    jorge[7][6], jorge[7][7], jorge[7][8],
                                    jorge[8][0], jorge[8][1], jorge[8][2], jorge[8][3], jorge[8][4], jorge[8][5],
                                    jorge[8][6], jorge[8][7], jorge[8][8]))

linha = []
colun = [[], [], [], [], [], [], [], [], []]
block = [[], [], [], [], [], [], [], [], []]
venceu = 0
verf = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
while True:

    def win():
        global linha
        cont = 0
        venceu = 0
        for t in range(0,9):
            for j in range(0,9):
                if jorge[t][j] in div:
                    jorge [t][j] = str(jorge[t][j])

        for linha in jorge:
            coluna = [l[cont] for l in jorge]
            msn = (cont // 3) * 3
            cont += 1
            square = [jorge[j][i] for j in range(msn, msn + 3) for i in range(msn, msn + 3)]
            if set(square) == verf and set(coluna) == verf and set(linha) == verf:
                venceu+=1
        if venceu == 9:
            print("PARABÉNS VC GANHOU!!!!!")
            sys.exit()
        else:
            for t in range(0,9):
                for j in range(0,9):
                    if jorge[t][j] in div:
                        jorge [t][j] = int(jorge[t][j])
            return True


    for i in jorge:
        if ' ' in i or ' ' not in i:
            tab()
            fila = input("Em qual fila vc quer colocar o número:")
            coluna = input("Em qual coluna vc quer colocar o número:")
            num = input("Qual número vc deseja colocar no lugar:")
            while fila not in verf or coluna not in verf or num not in verf or jorge[int(fila)-1][int(coluna)-1] in div:
                fila = input("Digite uma fila válida:")
                coluna = input("Digite uma coluna válida:")
                num = input("Digite um número válido de 1 a 9:")
            jorge[int(fila)-1][int(coluna)-1] = num
            win()





'''[
    ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ['3', '4', '5', '2', '8', '6', '1', '7', '9']
] '''



