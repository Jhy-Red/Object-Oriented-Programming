#!/bin/usr/python3

# - 1) 
class Robot : 

    def __init__(self,name, x = 0, y = 0, direction = "Est"):
        self.name = str(name)
        self.position = int(x),int(y)
        self.direction = direction
        self.__turbo = False

    def statut(self):
        print( "{} At your service, i am at {} going to {}" .format(self.name,self.position,self.direction))


    def __turn(self, turn_degres = 0):
        if self.direction in ["Nord","Ouest","Sud","Est"] :
            if self.direction == "Est" :
                degres = 0
            elif self.direction == "Sud" :
                degres = 90
            elif self.direction == "Ouest" :
                degres = 180
            elif self.direction == "Nord" :
                degres = 270
        
            degres = degres + turn_degres

            if degres == 0 or degres == 360:
                self.direction = "Est"
            elif degres == 90 or degres == -270:
                self.direction = "Sud"
            elif degres == 180 or degres == -180 :
                self.direction = "Ouest" 
            elif degres == 270 or degres == -90 :
                self.direction = "Nord"
            

    def right(self):
        self.__turn(turn_degres = 90)
        print("{}, turning right I face now the {}".format(self.name,self.direction))

            
        
    def left(self):
        print("I can't do that !")
        return
        
    def forward(self, move = 1 , speed = 1):
        y = self.position[1]
        x = self.position[0]

        if self.direction == "Est" :
            x += (move * speed)
        elif self.direction == "Nord" :
            y += (move * speed)
        elif self.direction == "Ouest" :
            x += (-move * speed)
        elif self.direction == "Sud" :
            y += (-move * speed)
        
        print('Moving Forward !')
        self.position = x,y
            