import pygame

#alakzatok+szinek
#palya=12*22

fekete=(0,0,0)
piros = (255, 49, 49)
lila=(128, 0, 128)
cian=(0, 254, 252)
narancs=(255, 165, 0)
kek = (31, 81, 255)
sarga = (255, 234, 0)
zold=(57,255,20)
feher=(255,255,255)

Lbetu = [
    [1, 0],
    [1, 0],
    [1, 1]
]
Jbetu = [
    [0, 1],
    [0, 1],
    [1, 1]
]

Tbetu = [
    [1, 1, 1],
    [0, 1, 0]
]

Ibetu = [
    [1, 1, 1, 1]
]

Obetu = [
    [1, 1],
    [1, 1]
]

Zbetu = [
    [1, 1, 0],
    [0, 1, 1]
]

Sbetu = [
    [0, 1, 1],
    [1, 1, 0]
]

lbet=Lbetu,narancs
jbet=Jbetu,kek
ibet=Ibetu,cian
obet=Obetu,sarga
sbet=Sbetu,zold
tbet=Tbetu,lila
zbet=Zbetu,piros
ablak=pygame.display.set_mode((900,650))

def alakzatrajz(alakzat, szin, x, y):
    cella = 25
    for i in range(len(alakzat)):
        for j in range(len(alakzat[i])):
            if alakzat[i][j] == 1:
                pygame.draw.rect(ablak, szin, (x + j * cella, y + i * cella, cella, cella))

def balraforgatas(betu):
    balraforg=list(map(list,zip(*betu[::-1])))
    return balraforg

def jobbraforgatas(betu):
    jobbraforg = list(map(list, zip(*betu)))[::-1]
    return jobbraforg



