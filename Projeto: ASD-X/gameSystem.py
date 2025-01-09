import random
import players

class GameSystem:

    @staticmethod
    def __randomAttack():
        listA = ['a', 'd', 'm']
        return random.choice(listA)
    
    @staticmethod
    def __randomPosition():
        listP = ['1', '2', '3']
        return random.choice(listP)
    
    def pickMoves(moves):

        size = len(moves)

        if size != 4:
            move1 = GameSystem.__randomAttack()
            move2 = GameSystem.__randomAttack()
            move3 = GameSystem.__randomAttack()

            position = GameSystem.__randomPosition()

            finalMoves = [move1, move2, move3, position]

            return finalMoves

    def turnVerif(userM, botM):
        
        movesResult = []
        i = 0

        for x in userM:
        
            if x == 'a':
                
                if botM[i] == 'a':
                    movesResult.append('nA')
                if botM[i] == 'd':
                    movesResult.append('bD')
                if botM[i] == 'm':
                    movesResult.append('uA')
            
            if x == 'd':
                
                if botM[i] == 'a':
                    movesResult.append('uD')
                if botM[i] == 'd':
                    movesResult.append('nD')
                if botM[i] == 'm':
                    movesResult.append('bM')

            if x == 'm':
                
                if botM[i] == 'a':
                    movesResult.append('bA')
                if botM[i] == 'd':
                    movesResult.append('uM')
                if botM[i] == 'm':
                    movesResult.append('nM')
            
            i += 1

        return movesResult
    
    def winnerVerif(turnMoves, turn):

        result = turnMoves[turn]
        winner = result[0]

        if winner == 'u':
            return 'u'
        elif winner == 'b':
            return 'b'
        else:
            return 'n'
        
    def moveTypeVerif(turnMoves, turn):

        result = turnMoves[turn]
        winner = result[1]

        if winner == 'A':
            return 'a'
        elif winner == 'D':
            return 'd'
        else:
            return 'm'
        
    
    def attackResult(enemyResult, damageMod):

        damage: int
        if enemyResult == 'm':
            damage = 0 - (15 + damageMod)
        else:
            damage = 0 - (10 + damageMod)
        return damage
    
    def magicResult(enemyResult, bot=False):
        
        heal: int

        if enemyResult == 'd' and bot == True:
            heal = 5
        elif enemyResult == 'd':
            heal = 15
        else:
            heal = 10
        
        return heal
    
    def damageModVerif(enemyResult, playerResult, bot=False):
        if playerResult == 'm' and enemyResult == 'd' and bot == False:
            return 3
        if playerResult == 'd' and enemyResult == 'a':
            return 5
        if playerResult == 'm' and enemyResult == 'd' and bot == True:
            return -15
        if playerResult == 'm' and enemyResult == 'm' and bot == True:
            return -8
        return 0

    def botDefended(dmgMod):
        dmg = dmgMod - 5
        if dmg < 0:
            return 0
        else:
            return dmg

