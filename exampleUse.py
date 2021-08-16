
from ConsoleGameEngine import *
app = App("ExampleGame", "TheFireFlyer"
)

#=========================declarations=======================================
currentLoc = Area()
#rooms
exampleArea1 = Area("Example area 1", "You enter into a large empty room with marble floors and white plaster walls")
exampleArea2 = Area("Example area 2", "You enter a small wooden cabin")
exampleArea3 = Area("Example area 3", "You enter a large uninspiring room")

#characters
Jack = Character("Hello there, my name is Jack")

#=======================================init connections======================
exampleArea1.connections = [exampleArea2, 0,0,0]
exampleArea2.connections = [0,exampleArea1, 0,0]
exampleArea3.connections = [0,0,0,exampleArea1]

#====================================init interactions for rooms=================
exampleArea1.interactions = {
    "look around":"not much to look at"
    }
exampleArea2.interactions = {
    "talk to jack":Jack.talkTo
    }
exampleArea3.interactions = {

}


#=======================================character functions==============================
def test_movement_system(inp, scene):
    scene.talking = False
    exampleArea3.enter()
    return exampleArea3



#===================================inits interactions for characters====================
Jack.interactionsC = {
    "do you like coffee or tea":"tea",
    "do you like potatoes":"duh",
    "where do you live?":test_movement_system
    }


app.start(exampleArea1)

"""
#start of the game=============================================================
currentLoc = exampleArea1
currentLoc.enter()
running = True
while running:
    #main game loop
    inp = input("what do you do?")
    inp.lower()
    if inp != "q" and inp != "quit":
        currentLoc = currentLoc.process(inp, currentLoc)
    else:
        running = False

print("quitting")
quit()
"""
