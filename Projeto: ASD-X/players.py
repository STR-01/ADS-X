import gameSystem

class Players:
    
    def __init__(self, nome):
        self.__name = nome
        self.__health = 100
        self.__damageMod = 0
        self.__moves = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        update = self.__health + value
        if update <= 0:
            update = 0
        if update >= 100:
            update = 100
        self.__health = update

    @property
    def damageMod(self):
        return self.__damageMod
    
    @damageMod.setter
    def damageMod(self, value):
        self.__damageMod = value
    
    @property
    def moves(self):
        return self.__moves
    
    @moves.setter
    def moves(self, moves):
        self.__moves = moves


        
class Bot(Players):
    
    def __init__(self, nome, bot=False):
        super().__init__(nome)
        self.__bot = bot
        


class User(Players):

    def __init__(self, nome):
        super().__init__(nome)
        self.__points = 0
        self.__pointsMod = 1

    @property
    def points(self):
        return self.__points
    
    @points.setter
    def points(self, value):
        if value == 0:
            self.__points = 0
        else:
            self.__points += (value * self.__pointsMod)

    @property
    def pointsMod(self):
        return self.__pointsMod

    @pointsMod.setter
    def pointsMod(self, value):

        verif = self.__pointsMod + value

        if value == 0:
            self.__pointsMod = 1
        elif verif >= 2:
            self.__pointsMod = 2
        else:
            self.__pointsMod = verif
        