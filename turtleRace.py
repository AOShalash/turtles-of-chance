from turtle import *
from random import *
import time

class Game():
    def __init__(self, numPlayers, seed):
        self.numPlayers = numPlayers
        self.seed = seed
        self.turtleList = []
        self.colorList = ["red", "blue", "green", "yellow", "pink", "purple", "orange", "brown", "black", "cyan", "olive", "gray", "magenta", "violet", "lightblue", "wheat", "goldenrod", "plum", "orchid", "beige", "dark green", "deep sky blue", "gainsboro", "gray", "light sea green", "turquoise"]
        screensize(canvwidth=1000,canvheight=1000)
        speed(10)
        penup()
        goto(-350, 350)

        for step in range(7):
            write(step, align='center')
            right(90)
            for num in range(numPlayers):
                penup()
                forward(20)
                pendown()
                forward(20)
            penup()
            backward(numPlayers * 40)
            left(90)
            forward(100)

    def initGame(self):
        genIter = 0

        for i in range(0, self.numPlayers):
            self.turtleList.append(Turtle())

        for turtle in self.turtleList:
            turtle.color(self.colorList[genIter])
            genIter += 1
            turtle.shape("turtle")

        for i in range(0, self.numPlayers):
            self.turtleList[i].penup()
            self.turtleList[i].goto(-400, 310 - 40)
            self.turtleList[i].pendown()

        for iter in range(250):
                for i in range(0, self.numPlayers):
                    self.turtleList[i].forward(randint(1,5))
                    if (self.turtleList[i].xcor() >= 350):
                        print('The winner is %s!' % self.colorList[i])
                        time.sleep(5)
                        exit()










def main():

    numPlayers = 0
    while numPlayers <= 0:
        numPlayers = int(input("How many people were nominated today? "))
        if numPlayers <= 0:
            print("Something went wrong, please try again.")

    inputSeed = 0
    while (inputSeed <= 0) or (inputSeed > 10000):
        inputSeed = int(input("Give me a random number in the range 1-10,000: "))
        if (inputSeed < 1) or (inputSeed > 10000):
            print("Something went wrong, please try again.")

    nominationRace = Game(numPlayers=numPlayers, seed=inputSeed)
    nominationRace.initGame()

if __name__ == "__main__":
    main()


