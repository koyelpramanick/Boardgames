
#boardgame.py
#This class defines the properties of a single boardgame object.
class BoardGame:
    def __init__(self, data):
        data_list = data
        self.name = data_list[0]
        self.gibbonsrating = float(data_list[1])
        self.baverage = float(data_list[2])
        self.avgweight = float(data_list[3])
        self.yearpublished = int(data_list[4])
        self.bggbestplayers = data_list[5]
        self.deficit = float(self.gibbonsrating - self.baverage)
        #grabs abs value of deficit
        if self.deficit < 0:
            self.deficit = self.deficit*-1

    #Formats the games accordingly
    def __str__(self):
        if type(self.bggbestplayers) != list:
            output = ('='* 12) + '\nName: ' + str(self.name) + '\nGibbons\' Rating: ' + str(self.gibbonsrating) + '\nBAverage: ' + str(self.baverage) + '\nAvgWeight: ' + str(self.avgweight) + '\nYear Published: ' + str(self.yearpublished) + '\nBGG Best Player Count: ' + str(self.bggbestplayers) + '\n' + ('='*12)
        else:
            #after the problem_daycare block in executive.py,
                #self.bggbestplayers must turn back
                    #into a string to be printed properly
            for index in range(len(self.bggbestplayers)):
                self.bggbestplayers[index] = str(self.bggbestplayers[index])
            self.bggbestplayers = ','.join(self.bggbestplayers)
            output = ('='* 12) + '\n' + str(self.name) + '\n' + str(self.gibbonsrating) + '\n' + str(self.baverage) + '\n' + str(self.avgweight) + '\n' + str(self.yearpublished) + '\n' + str(self.bggbestplayers) + '\n' + ('='*12)
        return output

    #handy for sorting the titles by rating
    def __ge__(self, other):
        if self.gibbonsrating >= other.gibbonsrating:
            return True
        else:
            return False
