

#driver.py
#the main file where the code is run
from executive import Executive

def main():
    #It wasn't required, but I don't like seeing red text
        #...wait a second.
    i = 0
    while i == 0:
        try:
            file_name = input('Enter the name of the input file: ')
            my_exec = Executive(file_name)
            i = 1
        except:
            i = 0

if __name__ == '__main__':
    main()
