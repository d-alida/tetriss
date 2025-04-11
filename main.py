import sys
import pygame
import gomb
import alakzatok
import random
import dicsoseglista

pygame.init()
ablak=pygame.display.set_mode((900,650))
pygame.display.set_caption('menő tetris!')

egyikszin=(168, 50, 145)
font = pygame.font.SysFont("comic sans", 30)

kezdokep=pygame.image.load("start.png").convert_alpha()
kilepes=pygame.image.load("kilep.png").convert_alpha()
dicsoseglistaa=pygame.image.load("dicsoseglista.png").convert_alpha()

startgomb=gomb.Gomb(340,150,kezdokep)
kilepgomb=gomb.Gomb(340,350,kilepes)
dicsoseglistagomb=gomb.Gomb(270,250,dicsoseglistaa)

def gameoverkinezet(pontok):
    dicsoseghez=False
    hatter()
    kirajzolas("game over!",font,(255,255,255),300,300)
    potokstr = str(pontok)
    if dicsoseghez==False:
        dicsoseglista.hozzaad_pontszam("Játékos", pontok)
        dicsoseghez=True
    kirajzolas(potokstr, font, alakzatok.feher, 465, 300)

    pygame.display.update()

def gameover(pontok):
    run = True
    while run:
        gameoverkinezet(pontok)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # ha vmi le van nyomva akkor...
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.QUIT:
                run = False
leesett_alazatok=[]

def utkozesellenorzes(palya, alak, x, y):
    for i in range(len(alak)):
        for j in range(len(alak[i])):
            if alak[i][j] == 1:
                if palya[(y-50)//25 + i][(x-200)//25 + j] == 1:
                    return True  #utkozes
    return False  #nincs utkozes

def tetjatekkinezet():
    hatter()
    fekete = (0, 0, 0)
    szurke=(20,20,20)
    piros = (255, 49, 49)
    kek = (31, 81, 255)
    sarga = (255, 234, 0)
    palya = (200, 50, 300, 550)
    palyakorvonalsarga=(197,47,306,556)
    alakzathelye = (600, 300, 200, 200)
    pontszamhelye = (600, 150, 200, 100)

    pygame.draw.rect(ablak, fekete, palya)
    #megrajzoljuk a kockas palyat
    cella=25

    for x in range(palya[0],palya[2] + palya[0],cella):
        pygame.draw.line(ablak,szurke, (x,palya[1]),(x,palya[3]+palya[1]),1)
    for x in range(palya[1], palya[3] + palya[1], cella):
        pygame.draw.line(ablak, szurke, (palya[0], x), (palya[2] + palya[0], x), 1)

    pygame.draw.rect(ablak, sarga, palyakorvonalsarga, 3)

    for adatok in leesett_alazatok:
        alak, szin, x, y = adatok
        alakzatok.alakzatrajz(alak, szin, x, y)

    pygame.draw.rect(ablak, fekete, alakzathelye)
    pygame.draw.rect(ablak, piros, alakzathelye, 3)


    pygame.draw.rect(ablak, fekete, pontszamhelye)
    pygame.draw.rect(ablak, kek, pontszamhelye, 3)
    kirajzolas("Pontszám:", font, piros, 630, 150)
    pygame.display.update()

def hatter():
    kephatter = pygame.image.load("tetrishez.jpg")
    ablak.fill((0, 0, 0))
    ablak.blit(kephatter, (0, 0))

def frissit_palya(palya, alak, x, y):
    for i in range(len(alak)):
        for j in range(len(alak[i])):

            if alak[i][j] == 1:
                palya[(y-50) // 25 + i][(x-200)//25+j] = 1

def dicsoseglistakinezet():
    hatter()
    fekete=(0,0,0)
    alakzathelye=(100,100,700,500)
    betualatt=(100,50,300,50)
    pygame.draw.rect(ablak,fekete,betualatt)
    pygame.draw.rect(ablak, (31, 81, 255), betualatt,3)
    kirajzolas("A kockák csarnoka:",font,(255, 234, 0),110,50)
    pygame.draw.rect(ablak,fekete,alakzathelye)
    pygame.draw.rect(ablak, (255, 49, 49), alakzathelye,3)
    pygame.display.update()

def zene(neve):
    pygame.mixer_music.load(neve)
    pygame.mixer_music.play()

def alakzatrajz(alakzat, szin, x, y):
    cella = 25
    for i in range(len(alakzat)):
        for j in range(len(alakzat[i])):
            if alakzat[i][j] == 1:
                pygame.draw.rect(ablak, szin, (x + j * cella, y + i * cella, cella, cella))

def spaceszoveg():
    hatter()
    kirajzolas("Megallt a jatek te ", font, egyikszin, 300, 300)
    kirajzolas("Nyomj spacet a visszatereshez", font, egyikszin, 260, 350)
    afk = "afkzene.ogg"
    #zene(afk)#?
    pygame.display.update()


hang=pygame.mixer.Sound("gombnyomasra.ogg")

def kirajzolas(szoveg,betutipus,szin,x,y):
    megjelenitendo=betutipus.render(szoveg,True,szin)
    ablak.blit(megjelenitendo,(x,y))


def ujpalya():
    palya = []

    for i in range(22): #(12*22 a palya merete)
        sor = []
        for j in range(12):
            sor.append(0)
        palya.append(sor)

    return palya

def utkozesifugg(palya,alak,x,y,szin):
    if not utkozesellenorzes(palya, alak, x, y + 25):
        y += 25  # Lefele mozgas
    else:
        leesett_alazatok.append((alak, szin, x, y))
        frissit_palya(palya, alak, x, y)
        y = 50  # Kozepfentre állítás
        x = 300
        ujalakzat = True

def sor_torles(palya, leesett_alazatok):
    torolt_sorok = 0
    for i in range(len(palya) - 1, -1, -1):
        if sum(palya[i]) == len(palya[i]):
            del palya[i]
            torolt_sorok += 1
            leesett_alazatok = [(alak, szin, x, y - 25) if y > 50 else (alak, szin, x, y) for alak, szin, x, y in
                                leesett_alazatok]

    for i in range(torolt_sorok):
        uj_sor = [0 for i in range(12)]  # Új üres sor hozzáadása
        palya.insert(0, uj_sor)

    return torolt_sorok




def tetrisjatek():
    global pontszam
    pontszam=0
    jatekmegall = False
    run = True

    x, y = 300, 50  # Kiindulási pozíció
    esesszamalalo = 0
    esesisebes = 30  # Idő (milliszekundum), amikor az alakzat automatikusan lefelé mozdul
    ujalakzat=False
    betu = random.choice([alakzatok.lbet, alakzatok.sbet, alakzatok.zbet, alakzatok.ibet, alakzatok.jbet, alakzatok.lbet, alakzatok.obet, alakzatok.tbet])
    palya = ujpalya()
    betu=alakzatok.ibet
    kovibetu=random.choice([alakzatok.lbet, alakzatok.sbet, alakzatok.zbet, alakzatok.ibet, alakzatok.jbet, alakzatok.lbet, alakzatok.obet, alakzatok.tbet])
    kovetkezoalak,koviszine=kovibetu
    alak,szin=betu
    while run:
        hatter()

        if jatekmegall == True:
            spaceszoveg()
        else:

            pontokstringben=str(pontszam)

            tetjatekkinezet()
            alakzatok.alakzatrajz(kovetkezoalak, koviszine, 660, 360)
            kirajzolas(pontokstringben, font, alakzatok.feher, 670, 200)
            if ujalakzat==True:
                alak=kovetkezoalak
                szin=koviszine
                kovibetu = random.choice([alakzatok.lbet, alakzatok.sbet, alakzatok.zbet, alakzatok.ibet, alakzatok.jbet, alakzatok.lbet,  alakzatok.obet, alakzatok.tbet])
                ujalakzat=False
                kovetkezoalak, koviszine = kovibetu

            alakzatok.alakzatrajz(alak,szin, x, y)

            for i in range(len(palya[0])):
                if palya[0][i]==1:
                    gameoverkinezet(pontszam)
                    pygame.display.update()
                    return pontszam

            esesszamalalo += 1
            if esesszamalalo >= esesisebes:
                if not utkozesellenorzes(palya,alak,x,y+25):
                    y += 25  # Lefele mozgas
                else:
                    leesett_alazatok.append((alak, szin, x, y))
                    frissit_palya(palya, alak, x, y)
                    torolt_sorok = sor_torles(palya, leesett_alazatok)
                    pontszam += torolt_sorok * 25
                    pontszam += sum(sum(alak) for alak in alak)
                    x,y=300,50
                    ujalakzat = True


                    pygame.display.update()
                esesszamalalo = 0


            # Palya aljat elerte e
            if y + len(alak) * 25 >= 600:
                leesett_alazatok.append((alak,szin,x,y))
                frissit_palya(palya, alak, x, y)
                torolt_sorok = sor_torles(palya, leesett_alazatok)
                pontszam += torolt_sorok * 25
                pontszam += sum(sum(alak) for alak in alak)
                x,y=300,50

                ujalakzat=True

                pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if jatekmegall == False:
                        jatekmegall = True
                    else:
                        jatekmegall = False
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_RIGHT:
                    if not utkozesellenorzes(palya, alak, x + 25, y):
                        x += 25
                    if x > 500 - len(alak[0]) * 25:
                        x = 500 - len(alak[0]) * 25
                if event.key == pygame.K_LEFT:
                    if not utkozesellenorzes(palya, alak, x - 25, y):
                        x -= 25

                    if x < 200:
                        x = 200
                if event.key == pygame.K_DOWN:
                    if not utkozesellenorzes(palya, alak, x, y + 25):
                        y += 25  # Lefele mozgas
                    else:
                        leesett_alazatok.append((alak, szin, x, y))
                        frissit_palya(palya, alak, x, y)
                        torolt_sorok = sor_torles(palya, leesett_alazatok)
                        pontszam += torolt_sorok * 25
                        pontszam += sum(sum(alak) for alak in alak)
                        y = 50  # Kozepfentre állítás
                        x = 300
                        ujalakzat = True

                if event.key ==pygame.K_a:
                    alak=alakzatok.balraforgatas(alak)

                if event.key ==pygame.K_d:
                    ideiglenesalak = alakzatok.balraforgatas(alak)
                    if x > 500 - len(ideiglenesalak[0]) * 25:
                        pass
                    else:
                        alak = ideiglenesalak

            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()
    return pontszam
def dicsoseglistaa():
    run=True
    while run:
        dicsoseglistakinezet()


        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:#ha vmi le van nyomva akkor...
                if event.key==pygame.K_ESCAPE:
                    run=False
            if event.type ==pygame.QUIT:
                run=False
def main():
    jatekmegall = False
    run=True
    while run:
        hatter()
        if startgomb.rajz(ablak) == True:
            hang.play()
            pontok=tetrisjatek()
            gameover(pontok)
            dicsoseglistaa()

        if kilepgomb.rajz(ablak) == True:
            hang.play()
            run = False

        if dicsoseglistagomb.rajz(ablak) == True:
            hang.play()
            dicsoseglistaa()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:#ha vmi le van nyomva akkor...
                if event.key==pygame.K_ESCAPE:
                    run=False
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
                run=False
        pygame.display.update()

    pygame.quit()

main()

