
print('Made with C.G.E')


class App:

    current_scene = None

    def __init__(self, name, author):

        print("==="+name+"===")
        print("by "+author+"\n\n")
        
    def start(self, starting_scene):
        
        print("press q to quit or end a converstation and press n, s, w, e for the directions of the corresponding intial")
        print("GAME START\n")
        
        self.current_scene = starting_scene
        self.current_scene.enter()
        
        running = True
        while running:
            #main game loop
            inp = input("what do you do?")
            inp = inp.lower()
            print(inp)
            if inp != "q" and inp != "quit":
                #print(self.current_scene)
                self.current_scene = self.current_scene.process(inp, self.current_scene)
            else:
                running = False
    



class Area:
    connections = [
     0, 0, 0, 0]
    initText = ''
    interactions = {}
    name = ''

    def __init__(self, name='untitled district', text='empty area'):
        self.initText = text
        self.name = name



    def enter(self):
        print(self.name.upper())
        print(self.initText)
        print('\nIt connects to the following:')
        direcs = ['n', 's', 'w', 'e']
        for direc in range(0, 4):
            if self.connections[direc] != 0:
                print(direcs[direc] + ' to ' + self.connections[direc].name)
        else:
            print('\nYou can do the followng:')

        for act in list(self.interactions):
            print(act)
        else:
            print('')

    def process(self, text, currentL):
        direcs = [
         'n', 's', 'w', 'e']
        for direc in range(0, 4):
            if text == direcs[direc]:
                if self.connections[direc] != 0:
                    self.connections[direc].enter()
                    return self.connections[direc]
                print('hmm, that wall looks rather solid')
                break
        for act in list(self.interactions):
            if text in act or act in text:
            
                if type(self.interactions[act]) is str:
                    print(self.interactions[act])
                else:
                    try:
                        return self.interactions[act](text, self)
                    except:
                        return self.interactions[act]()
                break

        return self


class Character(Area):
    initText = ''
    interactionsC = {}

    def __init__(self, initText):
        self.initText = initText

    def talkTo(self, text, state):
        print('')
        print('"' + self.initText + '"')
        print('\nYou can say the following:')
        for act in self.interactionsC:
            print(act)
        
        self.talking = True
        while self.talking:
            inp = input('What would you like to say?')
            inp.lower()
            if inp != 'q' and inp != 'bye':
                state = self.processC(inp, state)
            else:
                self.talking = False
        
        return state

    def processC(self, text, state):
        for act in list(self.interactionsC):
            if text in act or act in text:
                if type(self.interactionsC[act]) is str:
                    print('"' + self.interactionsC[act] + '"')
                else:
                    try:
                        return self.interactionsC[act](text, self)
                    except:
                        return self.interactionsC[act]()
                break
        return self