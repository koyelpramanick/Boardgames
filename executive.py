#executive.py
#the factory where the sausage gets made--
    #in charge of most of the user end interactions
from boardgame import BoardGame

class Executive:
    def __init__(self, name):
        self._file = open(name, 'r')
        self._data = self.data_consolidation()
        print('Welcome to Dr. Gibbon\'s Board Game Library!')
        self.menu()

#Goes through the file, organizes each line into a game object,
        #and returns list of game objects
    def data_consolidation(self):
        game_list = []
        for line in self._file:
            line = line.strip()
            data_list = line.split('\t') 
            try:
                game = BoardGame(data_list)
                game_list.append(game)
            except:
                None
        return game_list
        
#Function goes through the if-elif block and returns correct output
    #for each choice
#Each choice then goes back to the menu (unless choice 6 is input)
    def simulation(self, num):
        if num == 1:
            sort_list = [self._data[0]]
            for game in range(1, len(self._data)):
                for index in range(len(sort_list)):
                    if self._data[game] >= sort_list[index]:
                        sort_list.insert(index, self._data[game])
                        break
                #if a game does not trump or match any other in rating it's
                    #added to the bottom
                else:
                    sort_list.append(self._data[game])
            for game in sort_list:
                print(game)
            self.menu()
        elif num == 2:
            #The next 11 lines of code are going to be a recurring theme
            #They act as a good-input determiner.
            #Future blocks will be denoted GOODINPUT
            i = 0
            while i == 0:
                try:
                    #ironically I needed to grab a float to gurantee an int
                    #after all there's no such year as 2023.7
                    year = float(input('What year?: '))
                    if (year - int(year)) != 0:
                        raise
                    else:
                        year = int(year)
                        i = 1
                except:
                    i = 0
            j = 0
            for game in self._data:
                if year == int(game.yearpublished):
                    print(game)
                    j = 1
            if j == 0:
                print('No games found.')
            self.menu()
        elif num == 3:
            #GOODINPUT
            i = 0
            while i == 0:
                try:
                    weight = float(input('Pick a weight?: '))
                    if 0 <= weight <= 5:
                        i = 1
                    else:
                        raise
                except:
                    i = 0
            for game in self._data:
                if game.avgweight <= weight:
                    print(game)
            self.menu()
        elif num == 4:
            #GOODINPUT
            i = 0
            while i == 0:
                try:
                    deficit = float(input('Choose a deficit: '))
                    if 0 <= deficit <= 10:
                        i = 1
                    else:
                        raise
                except:
                    i = 0
            print('Dr Gibbons and the masses had a rating deficit of', deficit, 'or higher on the following games:')
            for game in self._data:
                if game.deficit >= deficit:
                    print(game)
            self.menu()
        elif num == 5:
            #GOODINPUT
            i = 0
            while i == 0:
                try:
                    players = float(input('How many players?: '))
                    if (players - int(players)) != 0:
                        raise
                    else:
                        players = int(players)
                        i = 1
                except:
                    i = 0
            for game in self._data:
                try:
                    if type(game.bggbestplayers) == list:
                        if players in game.bggbestplayers:
                            print(game)
                    else:
                        game.bggbestplayers = int(game.bggbestplayers)
                        if players == game.bggbestplayers:
                            print(game)
                except: #I'm especially proud of this metaphor
                    problem_children = game.bggbestplayers
                    problem_daycare = problem_children.split(',')
                    for index in range(len(problem_daycare)):
                        problem_daycare[index] = int(problem_daycare[index])
                    game.bggbestplayers = problem_daycare
                    if players in game.bggbestplayers:
                        print(game)
            self.menu()
        else:
            print('Goodbye.')

#Creates menu and obtains valid choice
    def menu(self):
        i = 0
        print('='*15)
        print('1. Print all games highest Gibbons rating to lowest\n2. Print all games from a year\n3. Print all games with a weight equal or lower than a provided weight\n4. The People VS Dr. Gibbons\n5. Print based on player count\n6. Exit the program')
        print('='*15)
        #GOODINPUT
        while i == 0:
            try:
                choice = int(input('Choose an option (1-6): '))
                if 0 < choice < 7:
                    i = 1
                else:
                    raise
            except:
                i = 0
        self.simulation(choice)
                
