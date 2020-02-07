#!/bin/usr/python3

from robot import Robot

class RobotNG(Robot):
    def __init__(self,name, x = 0, y = 0, direction = "Est", modele = 'NG'):
        Robot.__init__(self,name, x = 0, y = 0, direction = "Est")
        self.modele = modele
        self.__turbo = "Off"
        
    def statut(self):
        print( "{} At your service, I am reborn as {} i am at {} going to {}, boost with me is {}" .format(self.name,self.modele,self.position,self.direction,(self.__turbo)))

    def left(self) :
        self._Robot__turn(turn_degres = -90)
        print("{}, turning left I face now the {}".format(self.name,self.direction))
    
    def turn_arround(self):
        self._Robot__turn(turn_degres = 90)
        self._Robot__turn(turn_degres = 90) ### solution a trouver pour le nord
        print("{}, turning arround I face now the {}".format(self.name,self.direction))

    
    def turbo(self):
        if self.__turbo == "Off" :
            self.__turbo = "On"
            print(" Let's ROCK !!! Let s sprint")
        else : 
            self.__turbo = "Off"
            print('yes ... tired guys mode activated')

    def forward(self, move=1, speed=1):
        if self.__turbo =="On" :
            return super().forward(move=3, speed=speed)
        else :
            return super().forward(move=move, speed=speed)

