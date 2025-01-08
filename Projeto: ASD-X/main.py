from gameSystem import *
from players import *
from jsonVerification import *

import pygame
from pygame.locals import *
from sys import exit
from time import sleep

pygame.init()

#Iniciando a Tela:

sWidth = 700
sHeight = 500
screen = pygame.display.set_mode((sWidth, sHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("ASD-X")

#Importando imagens e soms:

gameBg = pygame.image.load('assets/img/gameScreen.png').convert_alpha()
menuBg = pygame.image.load('assets/img/menuScreen.png').convert_alpha()
nameBg = pygame.image.load('assets/img/nameScreen.png').convert_alpha()
helpBg = pygame.image.load('assets/img/helpScreen.png').convert_alpha()
winBg = pygame.image.load('assets/img/winScreen.png').convert_alpha()
defeatBg = pygame.image.load('assets/img/defeatScreen.png').convert_alpha()
drawBg = pygame.image.load('assets/img/drawScreen.png').convert_alpha()

startImage = pygame.image.load('assets/img/playButton.png').convert_alpha()
helpImage = pygame.image.load('assets/img/helpButton.png').convert_alpha()
quitImage = pygame.image.load('assets/img/quitButton.png').convert_alpha()
goImage = pygame.image.load('assets/img/goButton.png').convert_alpha()
confirmImage = pygame.image.load('assets/img/confirmButton.png').convert_alpha()
returnImage = pygame.image.load('assets/img/returnButton.png').convert_alpha()
continueImage = pygame.image.load('assets/img/continueButton.png').convert_alpha()
leftImage = pygame.image.load('assets/img/left.png').convert_alpha()
rightImage = pygame.image.load('assets/img/right.png').convert_alpha()
exitImage = pygame.image.load('assets/img/exit.png').convert_alpha()
menuImage = pygame.image.load('assets/img/menuButton.png').convert_alpha()

attackImage = pygame.image.load('assets/img/attack.png').convert_alpha()
defenseImage = pygame.image.load('assets/img/defense.png').convert_alpha()
magicImage = pygame.image.load('assets/img/magic.png').convert_alpha()
randomImage = pygame.image.load('assets/img/random.png').convert_alpha()
noneImage = pygame.image.load('assets/img/none.png').convert_alpha()

lKey = pygame.image.load('assets/img/leftKey.png').convert_alpha()
rKey = pygame.image.load('assets/img/rightKey.png').convert_alpha()
uKey = pygame.image.load('assets/img/upKey.png').convert_alpha()
dKey = pygame.image.load('assets/img/downKey.png').convert_alpha()

attackSfx = pygame.mixer.Sound('assets/sfx/attack.mp3')
defenseSfx = pygame.mixer.Sound('assets/sfx/defense.mp3')
magicSfx = pygame.mixer.Sound('assets/sfx/magic.mp3')

selectSfx = pygame.mixer.Sound('assets/sfx/select.mp3')
wrongSfx = pygame.mixer.Sound('assets/sfx/wrong.mp3')
confirmSfx = pygame.mixer.Sound('assets/sfx/button1.mp3')
buttonSfx = pygame.mixer.Sound('assets/sfx/button2.mp3')
startSfx = pygame.mixer.Sound('assets/sfx/start.mp3')

gameOverSfx = pygame.mixer.Sound('assets/sfx/gameover.mp3')
winSfx = pygame.mixer.Sound('assets/sfx/win.mp3')
defeatSfx = pygame.mixer.Sound('assets/sfx/defeat.mp3')
drawSfx = pygame.mixer.Sound('assets/sfx/draw.mp3')


user = players.User('')
bot = players.Bot('Adversário', True)

class Button():
    
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.__image = pygame.transform.scale(image, (int(width * scale), int(height*scale)))
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = (x, y)
        self.__clicked = False
    
    def draw(self):

        action = False
        pos = pygame.mouse.get_pos()

        if self.__rect.collidepoint(pos):

            if pygame.mouse.get_pressed()[0] == 1 and self.__clicked == False:
                self.__clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.__clicked = False

        screen.blit(self.__image, (self.__rect.x, self.__rect.y))

        return action
    
class InterfaceElements():
    
    def drawText (text, font, color, surface, x, y):
        textObj = font.render(text, 1, color)
        textRect = textObj.get_rect()
        textRect.topleft = (x, y)
        surface.blit(textObj, textRect)

    def getFont(font, size):
        return pygame.font.Font(font, size)
    
    def botPhase1MovesDraw(moves, x, y):
        
        movePos = moves[3]
        moveShown = moves[int(movePos)-1]
        moveIndex = ''

        if moveShown == 'a':
            moveIndex = attackImage
        if moveShown == 'd':
            moveIndex = defenseImage
        if moveShown == 'm':
            moveIndex = magicImage


        if movePos == '1':
            screen.blit(moveIndex, (x, y))
            screen.blit(randomImage, (x+107, y))
            screen.blit(randomImage, (x+214, y))
        if movePos == '2':
            screen.blit(randomImage, (x, y))
            screen.blit(moveIndex, (x+107, y))
            screen.blit(randomImage, (x+214, y))
        if movePos == '3':
            screen.blit(randomImage, (x, y))
            screen.blit(randomImage, (x+107, y))
            screen.blit(moveIndex, (x+214, y))

    def userMovesDraw(moves, x, y):

        screen.blit(noneImage, (x, y))
        screen.blit(noneImage, (x+107, y))
        screen.blit(noneImage, (x+214, y))
        if len(moves) >= 1:

            if moves[0] == 'a':
                screen.blit(attackImage, (x, y))
            elif moves[0] == 'd':
                screen.blit(defenseImage, (x, y))
            else:
                screen.blit(magicImage, (x, y))
            
            if len(moves) >= 2:

                if moves[1] == 'a':
                    screen.blit(attackImage, (x+107, y))
                elif moves[1] == 'd':
                    screen.blit(defenseImage, (x+107, y))
                else:
                    screen.blit(magicImage, (x+107, y))

                if len(moves) == 3:

                    if moves[2] == 'a':
                        screen.blit(attackImage, (x+214, y))
                    elif moves[2] == 'd':
                        screen.blit(defenseImage, (x+214, y))
                    else:
                        screen.blit(magicImage, (x+214, y))

    def botPhase2MovesDraw(moves, x, y):

        screen.blit(noneImage, (x, y))
        screen.blit(noneImage, (x+107, y))
        screen.blit(noneImage, (x+214, y))
        
        if moves[0] == 'a':
            screen.blit(attackImage, (x, y))
        elif moves[0] == 'd':
            screen.blit(defenseImage, (x, y))
        else:
            screen.blit(magicImage, (x, y))

        if moves[1] == 'a':
            screen.blit(attackImage, (x+107, y))
        elif moves[1] == 'd':
            screen.blit(defenseImage, (x+107, y))
        else:
            screen.blit(magicImage, (x+107, y))

        if moves[2] == 'a':
            screen.blit(attackImage, (x+214, y))
        elif moves[2] == 'd':
            screen.blit(defenseImage, (x+214, y))
        else:
            screen.blit(magicImage, (x+214, y))

class HealthBar():

    def __init__(self, hp):
        
        self.__maxHp = 100
        self.__hpBar = 300
        self.__hpRatio = self.__maxHp / self.__hpBar
        self.__targetHp = 0

    def drawHpBar(self, health, surface, x, y, bot = False):

        self.__targetHp = health

        color = ((0, 255, 0))
        if bot:
            color = ((255, 0, 0))


        pygame.draw.rect(surface, (0,0,0), (x, y, self.__hpBar, 25))
        pygame.draw.rect(surface, color, (x, y, self.__targetHp/self.__hpRatio, 25))
        pygame.draw.rect(surface, (255, 255, 255), (x, y, self.__hpBar, 25), 4)

class RoundVerification():

    def statusIndicator(i, uDmg, bDmg):
        roundResult = GameSystem.turnVerif(user.moves, bot.moves)
        
        dmgValueU = ''
        dmgValueB = ''
        healValueU = ''
        healValueB = ''
        modValueU = ''
        modValueB = ''

        winner = GameSystem.winnerVerif(roundResult, i)
        attackType = GameSystem.moveTypeVerif(roundResult, i)
        if winner == 'n':
            if attackType == 'a':
                dmgValueU = str(GameSystem.attackResult('a', bDmg))
                dmgValueB = str(GameSystem.attackResult('a', uDmg))
            if attackType == 'm':
                healValueU = '+10'
                modValueU = '-8'
            if attackType == 'd':
                modValueB = '0'
                modValueU = '0'
        if winner == 'u':
            if attackType == 'a':
                dmgValueB = str(GameSystem.attackResult('m', uDmg))
            if attackType == 'm':
                healValueU = '+15'
                modValueU = '+3'
            if attackType == 'd':
                modValueU = '+5'
                modValueB = '-5'
        if winner == 'b':
            if attackType == 'a':
                dmgValueU = str(GameSystem.attackResult('m', bDmg))
            if attackType == 'm':
                healValueB = '+5'
                modValueU = '-15'
            if attackType == 'd':
                modValueB = '+5'
                dmgValueU = '-5'

        result = [dmgValueU, dmgValueB, healValueU, healValueB, modValueU, modValueB]
        return result

    def movesResults(i):

        roundResult = GameSystem.turnVerif(user.moves, bot.moves)

        if user.health > 0 and bot.health > 0:
            winner = GameSystem.winnerVerif(roundResult, i)
            attackType = GameSystem.moveTypeVerif(roundResult, i)
            if winner == 'n':
                if attackType == 'a':
                    user.health = GameSystem.attackResult('a', bot.damageMod)
                    bot.health = GameSystem.attackResult('a', user.damageMod)
                    user.damageMod = 0
                    bot.damageMod = 0
                    user.points = 50
                if attackType == 'm':
                    user.health = GameSystem.magicResult('m')
                    user.damageMod += GameSystem.damageModVerif('m', 'm', True)
                    user.points = 50
                if attackType == 'd':
                    user.points = 50
            if winner == 'u':
                if attackType == 'a':
                    bot.health = GameSystem.attackResult('m', user.damageMod)
                    user.damageMod = 0
                    user.pointsMod = 0.1
                    user.points = 100
                if attackType == 'm':
                    user.health = GameSystem.magicResult('d')
                    user.damageMod += GameSystem.damageModVerif('d', 'm')
                    user.pointsMod = 0.1
                    user.points = 100
                if attackType == 'd':
                    user.damageMod += GameSystem.damageModVerif('a', 'd')
                    bot.damageMod = GameSystem.botDefended(bot.damageMod)
                    user.pointsMod = 0.1
                    user.points = 100
            if winner == 'b':
                if attackType == 'a':
                    user.health = GameSystem.attackResult('m', bot.damageMod)
                    bot.damageMod = 0
                    user.pointsMod = 0
                if attackType == 'm':
                    bot.health = GameSystem.magicResult('d', True)
                    user.damageMod += GameSystem.damageModVerif('d', 'm', True)
                    user.pointsMod = 0
                if attackType == 'd':
                    bot.damageMod += GameSystem.damageModVerif('a', 'd')
                    user.health = -5
                    user.damageMod = 0
                    user.pointsMod = 0

            if user.damageMod < -8:
                user.damageMod = -8
            sleep(0.5)

#Criando Fontes:

nameFont = InterfaceElements.getFont('assets/superpixel.ttf', 24)
statusFont = InterfaceElements.getFont('assets/mj.ttf', 16)
battleFont = InterfaceElements.getFont('assets/superpixel.ttf', 20)
dmgFont = InterfaceElements.getFont('assets/mj.ttf', 20)
scoreFont = InterfaceElements.getFont('assets/mj.ttf', 24)
helpFont = InterfaceElements.getFont('assets/superpixel.ttf', 18)
helpTitleFont = InterfaceElements.getFont('assets/superpixel.ttf', 25)

class Window():

    menuCheck = False
    check = False
    turn = 1

    def startMenu():

        while True:

            screen.blit(menuBg, (0,0))

            if btnStart.draw() and Window.menuCheck:
                buttonSfx.play()
                Window.menuCheck = False
                Window.nameMenu()

            if btnHelp.draw() and Window.menuCheck:
                buttonSfx.play()
                Window.menuCheck = False
                Window.helpMenu()

            if btnQuit.draw() and Window.menuCheck:
                wrongSfx.play()
                Window.menuCheck = False
                pygame.quit
                exit()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()

            if not Window.menuCheck:
                sleep(0.2)
                Window.menuCheck = True

            pygame.display.update()
            clock.tick(60)

    def helpMenu():

        page = 0

        run = True
        while run:

            screen.blit(helpBg, (0,0))

            if page < 6:
                if btnRight.draw():
                    buttonSfx.play()
                    page += 1

            if page > 0:
                if btnLeft.draw():
                    buttonSfx.play()
                    page -= 1

            if btnExit.draw():
                buttonSfx.play()
                run = False

            if page == 0:
                InterfaceElements.drawText("Introdução", helpTitleFont, (0,0,0), screen, 245, 75)

                InterfaceElements.drawText("ASD-X é um jogo estilo pedra, papel e tessoura", helpFont, (0,0,0), screen, 15, 120)
                InterfaceElements.drawText("jogado em turnos contra um computador, onde", helpFont, (0,0,0), screen, 15, 120+28+10)
                InterfaceElements.drawText("cada jogador realiza três movimentos por turno.", helpFont, (0,0,0), screen, 15, 148+28+10)
                InterfaceElements.drawText("Cada tipo de movimento possui uma fraqueza,", helpFont, (0,0,0), screen, 15, 20+148+28*2)
                InterfaceElements.drawText("e seus efeitos variam entre o jogador e oponente.", helpFont, (0,0,0), screen, 15, 25+148+28*3)

                screen.blit(randomImage, (350, 300))
                screen.blit(randomImage, (250, 300))
                screen.blit(randomImage, (450, 300))
                screen.blit(noneImage, (250, 400))
                screen.blit(noneImage, (350, 400))
                screen.blit(noneImage, (450, 400))

                InterfaceElements.drawText("Oponente ->", helpFont, (100,0,0), screen, 95, 330)
                InterfaceElements.drawText("Você ->", helpFont, (0,100,0), screen, 150, 420)

            if page == 1:
                InterfaceElements.drawText("Controles", helpTitleFont, (0,0,0), screen, 260, 80)

                InterfaceElements.drawText("Você pode user as teclas de seta prar selecionar", helpFont, (0,0,0), screen, 15, 120)
                InterfaceElements.drawText("seus movimentos da esquerda para direita:", helpFont, (0,0,0), screen, 15, 120+38)
                InterfaceElements.drawText("esquerda é ataque, cima é defesa, direita é especial.", helpFont, (0,0,0), screen, 15, 120+28*2 + 10)
                InterfaceElements.drawText("Você pode usar a seta para baixou ou backspace", helpFont, (0,0,0), screen, 15, 120+28*3 + 15)
                InterfaceElements.drawText("para cancelar um ataque, antes de enviar.", helpFont, (0,0,0), screen, 15, 120+28*4 + 25)
                InterfaceElements.drawText("Aperte no botão 'go' para começar o round.", helpFont, (0,0,0), screen, 15, 120+28*5 + 25)

                screen.blit(attackImage, (80, 360))
                screen.blit(lKey, (160, 360))

                screen.blit(defenseImage, (280, 360))
                screen.blit(uKey, (350, 360))

                screen.blit(magicImage, (460, 360))
                screen.blit(rKey, (540, 360))

            if page == 2:
                InterfaceElements.drawText("Movimentos", helpTitleFont, (0,0,0), screen, 260, 80)

                InterfaceElements.drawText("Cada tipo de movimento é forte contra outro tipo.", helpFont, (0,0,0), screen, 15, 120)
                InterfaceElements.drawText("Seus efeitos dependem de quem ganhou o round.", helpFont, (0,0,0), screen, 15, 120+38)

                screen.blit(attackImage, (230, 200))
                screen.blit(magicImage, (400, 200))
                screen.blit(rKey, (315, 200))

                screen.blit(magicImage, (230, 300))
                screen.blit(defenseImage, (400, 300))
                screen.blit(rKey, (315, 300))

                screen.blit(defenseImage, (230, 400))
                screen.blit(attackImage, (400, 400))
                screen.blit(rKey, (315, 400))

            if page == 3:
                InterfaceElements.drawText("Attack", helpTitleFont, (0,0,0), screen, 280, 80)

                InterfaceElements.drawText("O ataque tira parte da vida do inimigo. Este", helpFont, (0,0,0), screen, 15, 120)
                InterfaceElements.drawText("movimento possui o mesmo efeito para os dois", helpFont, (0,0,0), screen, 15, 120+28)
                InterfaceElements.drawText("jogadores. Possui o dano base de dez, e consome", helpFont, (0,0,0), screen, 15, 120+28*2)
                InterfaceElements.drawText("o damage mod do jogador para dar mais", helpFont, (0,0,0), screen, 15, 120+28*3)
                InterfaceElements.drawText("dano. Caso usado contra um movimento especial,", helpFont, (0,0,0), screen, 15, 120+28*4)
                InterfaceElements.drawText("o dano base aumenta para quinze.", helpFont, (0,0,0), screen, 15, 120+28*5)

                screen.blit(attackImage, (300, 400))

            if page == 4:
                InterfaceElements.drawText("Special", helpTitleFont, (0,0,0), screen, 280, 80)

                InterfaceElements.drawText("O especial é um movimento de suporte. Ele pode", helpFont, (0,0,0), screen, 15, 120-3)
                InterfaceElements.drawText("variar dependendo de quem usa:", helpFont, (0,0,0), screen, 15, 120+28)

                InterfaceElements.drawText("Quando o jogador usa o especial, recupera vida.", helpFont, (0,0,0), screen, 15, 120+28*2)
                InterfaceElements.drawText("Caso usado contra um movimento defesa, ele", helpFont, (0,0,0), screen, 15, 120+28*3)
                InterfaceElements.drawText("recupera mais vida e aumenta o damage mod.", helpFont, (0,0,0), screen, 15, 120+28*4)
                InterfaceElements.drawText("Quando o adversário usa o especial, ele reduz", helpFont, (0,0,0), screen, 15, 120+28*5 -4)
                InterfaceElements.drawText("o damage mod do jogador. Caso usado contra", helpFont, (0,0,0), screen, 15, 120+28*6 -2)
                InterfaceElements.drawText("um movimento defesa, recupera vida", helpFont, (0,0,0), screen, 15, 120+28*7 -2)

                screen.blit(magicImage, (300, 400))

            if page == 5:
                InterfaceElements.drawText("Defense", helpTitleFont, (0,0,0), screen, 280, 80)

                InterfaceElements.drawText("A defesa é um movimento que bloqueia o dano", helpFont, (0,0,0), screen, 15, 120-3)
                InterfaceElements.drawText("do movimento de ataque. Alguns efeitos variam", helpFont, (0,0,0), screen, 15, 120+28)
                InterfaceElements.drawText("dependendo de quem usa:", helpFont, (0,0,0), screen, 15, 120+28*2)

                InterfaceElements.drawText("Quando o jogador defende um movimento de", helpFont, (0,0,0), screen, 15, 120+28*3)
                InterfaceElements.drawText("ataque, aumenta seu damage mod e diminui o do", helpFont, (0,0,0), screen, 15, 120+28*4)
                InterfaceElements.drawText("oponente. Quando o adversário defende um", helpFont, (0,0,0), screen, 15, 120+28*5-4)
                InterfaceElements.drawText("movimento de ataque, reflete dano, aumenta seu", helpFont, (0,0,0), screen, 15, 120+28*6-2)
                InterfaceElements.drawText("damage mod e zera o do jogador.", helpFont, (0,0,0), screen, 15, 120+28*7-2)

                screen.blit(defenseImage, (300, 400))

            if page == 6:
                InterfaceElements.drawText("Mais informações", helpTitleFont, (0,0,0), screen, 200, 80-5)

                InterfaceElements.drawText("Você podera ver um movimento do oponente", helpFont, (0,0,0), screen, 15, 120-3)
                InterfaceElements.drawText("antes de confirmar os movimentos. Os outros", helpFont, (0,0,0), screen, 15, 120+28)
                InterfaceElements.drawText("dois seram revelados após a confirmação.", helpFont, (0,0,0), screen, 15, 120+28*2-4)
                InterfaceElements.drawText("O jogo acaba quando a vida de pelo menos", helpFont, (0,0,0), screen, 15, 120+28*3-2)
                InterfaceElements.drawText("um jogador chege a zero.", helpFont, (0,0,0), screen, 15, 120+28*4-2)
                InterfaceElements.drawText("Sua pontuação será salva no computador.", helpFont, (0,0,0), screen, 15, 120+28*5-8)
                InterfaceElements.drawText("O damage mod o jogador pode diminuir até", helpFont, (0,0,0), screen, 15, 120+28*6-10)
                InterfaceElements.drawText("menos oito, enquanto do oponente pode diminuir", helpFont, (0,0,0), screen, 15, 120+28*7-8)
                InterfaceElements.drawText("até zero.", helpFont, (0,0,0), screen, 15, 120+28*8-12)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        buttonSfx.play()
                        run = False
                    if event.key == K_LEFT:
                        if page > 0:
                            buttonSfx.play()
                            page -= 1
                    if event.key == K_RIGHT:
                        if page < 6:
                            buttonSfx.play()
                            page += 1

            pygame.display.update()
            clock.tick(60)

    def nameMenu():

        name: str = ''
        inputBar = pygame.Rect(90, 281, 140, 32)

        colorSelected = pygame.Color('gray90')
        colorUnselected = pygame.Color('gray50')
        barActive = False

        run = True
        while run:

            screen.blit(nameBg, (0,0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if inputBar.collidepoint(event.pos):
                        barActive = True
                    else:
                        barActive = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                    if event.key == K_RETURN and len(name) != 0:
                        user.name = name
                        startSfx.play()
                        Window.gameWindow()
                    else:
                        if barActive == True:
                            if event.key == pygame.K_BACKSPACE:
                                name = name[0:-1]
                            elif len(name) < 20:
                                name += event.unicode

            color = colorUnselected
            if barActive == True:
                color = colorSelected
            else:
                color = colorUnselected

            if btnReturn.draw():
                buttonSfx.play()
                run = False

            if btnContinue.draw():
                if len(name) != 0:
                    user.name = name
                    startSfx.play()
                    Window.gameWindow()
                else:
                    wrongSfx.play()

            pygame.draw.rect(screen, color, inputBar)
            nameText = nameFont.render(name, True, (0, 0, 0))
            screen.blit(nameText, (inputBar.x + 5, inputBar.y + 8))

            inputBar.w = 512 #max(200, nameText.get_width() + 10)
            inputBar.h = nameText.get_height() + 10
            

            pygame.display.update()
            clock.tick(60)

    def gameWindow():

        user.health = 100
        bot.health = 100
        Window.turn = 1
        user.points = 0
        user.pointsMod = 0

        userMoves = []
        botMoves = []

        while True:

            screen.blit(gameBg, (0,0))
            
            userHp = HealthBar(user.health)
            botHp = HealthBar(bot.health)

            if Window.check:
                userMoves = []
                botMoves = []
                Window.check = False

            if len(botMoves) == 0:
                botMoves = gameSystem.GameSystem.pickMoves(bot.moves)
                bot.moves = botMoves
            

            InterfaceElements.drawText("Damage MOD: " + str(bot.damageMod), dmgFont, (255, 255, 255), screen, 20, 15)
            InterfaceElements.drawText(bot.name, battleFont, (255, 255, 255), screen, 510, 42)
            InterfaceElements.drawText("Damage MOD: " + str(user.damageMod), dmgFont, (255, 255, 255), screen, 465, 465)
            InterfaceElements.drawText(user.name, battleFont, (255, 255, 255), screen, 20, 433)

            userHp.drawHpBar(user.health, screen, 20, 463)
            botHp.drawHpBar(bot.health, screen, 380, 12, True)

            InterfaceElements.botPhase1MovesDraw(botMoves, 88, 148)
            InterfaceElements.userMovesDraw(userMoves, 88, 276)

            if btnGo.draw():
                if len(userMoves) == 3:
                    user.moves = userMoves
                    confirmSfx.play()
                    Window.moveWindow()
                else:
                    wrongSfx.play()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT and len(userMoves) < 3:
                        userMoves.append('a')
                        selectSfx.play()
                    if event.key == K_UP and len(userMoves) < 3:
                        userMoves.append('d')
                        selectSfx.play()
                    if event.key == K_RIGHT and len(userMoves) < 3:
                        userMoves.append('m')
                        selectSfx.play()
                    if (event.key == K_BACKSPACE or event.key == K_DOWN) and len(userMoves) > 0:
                        userMoves.pop()
                        selectSfx.play()
                        
                    if event.key == K_RETURN:
                        if len(userMoves) == 3:
                            user.moves = userMoves
                            confirmSfx.play()
                            Window.moveWindow()
                        else:
                            wrongSfx.play()

            pygame.display.update()
            clock.tick(60)
    
    def moveWindow():

        userHp = HealthBar(user.health)
        botHp = HealthBar(bot.health)

        result1 = []
        result2 = []
        result3 = []

        roundResult = GameSystem.turnVerif(user.moves, bot.moves)
        attackType = ''
        statusControl = 0
        soundCheck = True

        wait = 0

        run = True
        while run:

            screen.blit(gameBg, (0,0))

            uDmg = user.damageMod
            bDmg = bot.damageMod

            if wait == 1 and bot.health != 0 and user.health != 0:
                result1 = RoundVerification.statusIndicator(wait-1, uDmg, bDmg)
                statusControl += 1
            if wait == 2 and bot.health != 0 and user.health != 0:
                result2 = RoundVerification.statusIndicator(wait-1, uDmg, bDmg)
                statusControl += 1
            if wait == 3 and bot.health != 0 and user.health != 0:
                result3 = RoundVerification.statusIndicator(wait-1, uDmg, bDmg)
                statusControl += 1

            if wait <= 3 and wait > 0:
                attackType = GameSystem.moveTypeVerif(roundResult, wait-1)
                if bot.health != 0 and user.health != 0:
                    RoundVerification.movesResults(wait-1)
                    sleep(0.3)

            userHp.drawHpBar(user.health, screen, 20, 463)
            botHp.drawHpBar(bot.health, screen, 380, 12, True)

            InterfaceElements.botPhase2MovesDraw(bot.moves, 88, 148)
            InterfaceElements.userMovesDraw(user.moves, 88, 276)
            
            InterfaceElements.drawText("Damage MOD: " + str(bot.damageMod), dmgFont, (255, 255, 255), screen, 20, 15)
            InterfaceElements.drawText(bot.name, battleFont, (255, 255, 255), screen, 510, 42)
            InterfaceElements.drawText("Damage MOD: " + str(user.damageMod), dmgFont, (255, 255, 255), screen, 465, 465)
            InterfaceElements.drawText(user.name, battleFont, (255, 255, 255), screen, 20, 433)
            
            if result1 and statusControl > 0:
                InterfaceElements.drawText(result1[0], statusFont, (255, 80, 80), screen, 105, 260)
                InterfaceElements.drawText(result1[1], statusFont, (255, 80, 80), screen, 105, 225)

                InterfaceElements.drawText(result1[2], statusFont, (80, 255, 80), screen, 85, 260)
                InterfaceElements.drawText(result1[3], statusFont, (80, 255, 80), screen, 85, 225)

                InterfaceElements.drawText(result1[4], statusFont, (80, 80, 255), screen, 135, 260)
                InterfaceElements.drawText(result1[5], statusFont, (80, 80, 255), screen, 135, 225)

            if result2 and statusControl > 1:
                InterfaceElements.drawText(result2[0], statusFont, (255, 80, 80), screen, 105+107, 260)
                InterfaceElements.drawText(result2[1], statusFont, (255, 80, 80), screen, 105+107, 225)

                InterfaceElements.drawText(result2[2], statusFont, (80, 255, 80), screen, 85+107, 260)
                InterfaceElements.drawText(result2[3], statusFont, (80, 255, 80), screen, 85+107, 225)

                InterfaceElements.drawText(result2[4], statusFont, (80, 80, 255), screen, 135+107, 260)
                InterfaceElements.drawText(result2[5], statusFont, (80, 80, 255), screen, 135+107, 225)

            if result3 and statusControl > 2:
                InterfaceElements.drawText(result3[0], statusFont, (255, 80, 80), screen, 105+214, 260)
                InterfaceElements.drawText(result3[1], statusFont, (255, 80, 80), screen, 105+214, 225)

                InterfaceElements.drawText(result3[2], statusFont, (80, 255, 80), screen, 85+214, 260)
                InterfaceElements.drawText(result3[3], statusFont, (80, 255, 80), screen, 85+214, 225)

                InterfaceElements.drawText(result3[4], statusFont, (80, 80, 255), screen, 135+214, 260)
                InterfaceElements.drawText(result3[5], statusFont, (80, 80, 255), screen, 135+214, 225)

            if wait > 0 and wait < 4 and user.health > 0 and bot.health > 0:
                if attackType == 'a':
                    attackSfx.play()
                if attackType == 'm':
                    magicSfx.play()
                if attackType == 'd':
                    defenseSfx.play()

            if btnConfirm.draw():
                if wait >= 4:
                    Window.check = True
                    user.moves = []
                    bot.moves = []

                    if bot.health == 0 or user.health == 0:
                        Window.gameOverWindow()
                    else:
                        Window.turn += 1
                        confirmSfx.play()
                        run = False
                
            
            if bot.health == 0 or user.health == 0:
                if soundCheck:
                    gameOverSfx.play()
                    soundCheck = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        if wait >= 4:
                            Window.check = True
                            user.moves = []
                            bot.moves = []

                            if bot.health == 0 or user.health == 0:
                                Window.gameOverWindow()
                            else:
                                Window.turn += 1
                                confirmSfx.play()
                                run = False
                        

            if wait < 4:
                wait += 1

            pygame.display.update()
            clock.tick(60)

    def gameOverWindow():

        jsonCheck = True

        user.pointsMod = 0

        if Window.turn < 7:
            user.points = 1000
        elif Window.turn >= 7 and Window.turn < 13:
            user.points = 500

        if bot.health == 0 and user.health == 0:
            drawSfx.play()
        elif bot.health == 0:
            winSfx.play()
        else:
            defeatSfx.play()


        while True:

            if bot.health == 0 and user.health == 0:
                screen.blit(drawBg, (0,0))
            elif bot.health == 0:
                screen.blit(winBg, (0,0))
            else:
                screen.blit(defeatBg, (0,0))

            if jsonCheck:
                if bot.health == 0 and user.health != 0:
                    scores = JsonVerification.jsonDict(user.name, int(user.points), Window.turn, True)
                    JsonVerification.jsonSave(scores)
                else:
                    scores = JsonVerification.jsonDict(user.name, int(user.points), Window.turn, False)
                    JsonVerification.jsonSave(scores)
                jsonCheck = False

            InterfaceElements.drawText('Recorde: ' + str(JsonVerification.jsonHighScore()), scoreFont, (0, 0, 0), screen, 135, 290)
            InterfaceElements.drawText('Pontos: ' + str(int(user.points)), scoreFont, (0, 0, 0), screen, 135, 241)
            InterfaceElements.drawText('Turnos: ' + str(Window.turn), scoreFont, (0, 0, 0), screen, 395, 241)

            if btnMenu.draw():
                buttonSfx.play()
                Window.startMenu()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        buttonSfx.play()
                        Window.startMenu()
                    if event.key == K_RETURN:
                        buttonSfx.play()
                        Window.startMenu()
            pygame.display.update()
            clock.tick(60)

#Criando botões:

btnStart = Button(215, 237, startImage, 1)
btnHelp = Button(215, 321, helpImage, 1)
btnQuit = Button(215, 405, quitImage, 1)
btnGo = Button(482, 182, goImage, 1)
btnConfirm = Button(482, 182, confirmImage, 1)
btnContinue = Button(387, 360, continueImage, 1)
btnReturn = Button(153, 360, returnImage, 1)
btnLeft = Button(2, 66, leftImage, 1)
btnRight = Button(650, 66, rightImage, 1)
btnExit = Button(4, 464, exitImage, 1)
btnMenu = Button(252, 382, menuImage, 1)

resultados = JsonVerification.jsonScores()
Window.startMenu()
