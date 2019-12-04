#Ryan Moses
#CSCI 101 - Section C
#Create Project - Text Adventure Game
#https://github.com/HellosesImMoses/CSCI-101-Create-Response

#global variables
end_list = []
playcount = 0

#functions
def decision():             #prompts the player which of the decisions given they would like to choose
    print('')
    print('What do you wish to do?')
    choice = int(input('CHOICE> '))
    print('---------------------------------------------------------')
    return choice

def read_file(file):        #function to read each set of choices and exposition
    with open(file, 'r') as text:
        for i in text:
            output = i.strip('\n')
            print(output)

def write_file(ending):      #function to give an output showcasing all decisions made during game
    with open('output.txt', 'a') as text:
        text.write(ending)
        text.write('\n')

def initialize_output():
    with open('output.txt', 'w') as file:
        file.write('')

def write_output(end_list, ending):
    if ending in end_list:
        return False
    else:
        write_file(ending)
        return True
    
def ready():
    output = str(input('Are you ready to play? (yes/no)\n'))
    if output == 'no':
        print('Too bad! Maybe next time!')
    elif output == 'yes':
        print("Great! Let's begin!\n")
    return output

def welcome():
    read_file('welcome.txt')
        

def Start():                #begins the game
    read_file('start.txt')
    option = decision()
    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    else:
        option_4()

def option_1():                 #Take her bowling
    read_file('option_1.txt')
    option = decision()
    if option == 1:
        option_1_1()
    elif option == 2:
        option_1_2()

def option_2():                 #Go see a movie
    read_file('option_2.txt')
    option = decision()
    if option == 1:
        option_2_1()
    elif option == 2:
        option_2_2()
    elif option == 3:
        option_2_3()

def option_3():                 #Go to a coffee shop
    read_file('option_3.txt')
    if write_output(end_list, 'Cold Coffee') is True:
        end_list.append('Cold Coffee')
    #fail

def option_4():                 #Take her out for dinner
    read_file('option_4.txt')
    option = decision()
    if option == 1:
        option_4_1()
    elif option == 2:
        option_4_2()
    elif option == 3:
        option_4_3()

def option_1_1():               #Crush her, I never lose
    read_file('option_1.1.txt')
    if write_output(end_list, 'Wait that Worked?') is True:
        end_list.append('Wait that Worked?')
    #success (somehow)

def option_1_2():               #Be nice and let her win
    read_file('option_1.2.txt')
    if write_output(end_list, 'Bad Bowlers Can Still Win') is True:
        end_list.append('Bad Bowlers Can Still Win')
    #success

def option_2_1():               #Joker
    read_file('option_2.1.txt')
    option = decision()
    if option == 1:
        option_2_1_1()
    elif option == 2:
        option_2_1_2()

def option_2_2():               #Charlie's Angels
    read_file('option_2.2.txt')
    if write_output(end_list, 'Bad Movies = Bad Dates') is True:
        end_list.append('Bad Movies = Bad Dates')
    #fail (like the movie)

def option_2_3():               #Frozen II
    read_file('option_2.3.txt')
    if write_output(end_list, 'Disney Always Wins') is True:
        end_list.append('Disney Always Wins')
    #success

def option_4_1():               #pizza
    read_file('option_4.1.txt')
    if write_output(end_list, 'Nolstagia') is True:
        end_list.append('Nolstalgia')
    #success

def option_4_2():               #fast food
    read_file('option_4.2.txt')
    option = decision()
    if option == 1:
        option_4_2_1()
    elif option == 2:
        option_4_2_2()

def option_4_3():               #fancy food
    read_file('option_4.3.txt')
    if write_output(end_list, 'Better to Start Small') is True:
        end_list.append('Better to Start Small')
    #fail

def option_2_1_1():             #ask if she's ok
    read_file('option_2.1.1.txt')
    option = decision()
    if option == 1:
        option_2_1_1_1()
    elif option == 2:
        option_2_1_1_2()

def option_2_1_2():             #she'll be fine
    read_file('option_2.1.2.txt')
    if write_output(end_list, 'Killer Clowns') is True:
        end_list.append('Killer Clowns')
    #fail

def option_2_1_1_1():           #pfft no way
    read_file('option_2.1.1.1.txt')
    if write_output(end_list, 'We Live in a Society') is True:
        end_list.append('We Live in a Society')
    #fail

def option_2_1_1_2():           #walk her out
    read_file('option_2.1.1.2.txt')
    if write_output(end_list, 'Try Again Next Time') is True:
        end_list.append('Try Again Next Time')
    #success (kind of)

def option_4_2_1():
    read_file('option_4.2.1.txt')
    if write_output(end_list, 'Make the First Move') is True:
        end_list.append('Make the First Move')
    #success

def option_4_2_2():
    read_file('option_4.2.2.txt')
    if write_output(end_list, 'Safe and Not Sorry') is True:
        end_list.append('Safe and Not Sorry')
    #success

#running game
welcome()
initialize_output()
again = ready()
while again == 'yes':
    Start()
    print('')
    print('The endings you have earned so far are:')
    read_file('output.txt')
    print('')
    playcount += 1
    print('You have played {} time(s) this session!'. format(playcount))
    print('---------------------------------------------------------')
    again = input('Would you like to play again? (yes/no)\n').lower().strip()
    if again == 'yes':
        print("Great Let's Start Again!")
    else:
        print('Too Bad! See ya next time!')
    print('---------------------------------------------------------\n')
