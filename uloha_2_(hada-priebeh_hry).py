fr = open('text/hada.txt', 'r')

fr_cely = fr.read()
poc = 0
for i in fr_cely:
    if i in '\n':
        poc += 1
print('pocet hier je:', poc)

fr.seek(0)
zoz = fr.readlines()
zoz.sort()
print(len(zoz[-1]))

fw = open('text/hada_write.txt', 'w')

for i in range(3):
    haha = ''
    pocitadlo = 1
    poradie = 0
    riadok = zoz[i]
    while poradie < len(riadok)-1:
        while riadok[poradie] == riadok[poradie+1]:
            pocitadlo += 1
            poradie += 1
        haha += riadok[poradie] + str(pocitadlo) + ' '
        pocitadlo = 1
        poradie += 1
    fw.write(haha)
    fw.write('\n')

