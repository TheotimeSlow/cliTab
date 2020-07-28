import os
import re
from pyfiglet import Figlet
from pysine import sine
from time import sleep

os.system('clear')
f = Figlet(font='slant')
print(f.renderText('Tab'))

'''
sine(329, 0.1)
sine(349, 0.1)
sine(369, 0.1)
sine(391, 0.1)
sine(415, 0.1)
sine(440, 0.1)
sine(493, 0.1)
sine(523, 0.1)
'''

def menu(options):
    print("Please choose:")

    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))

    i = input("Enter number: ")
    
    try:
        if 0 < int(i) <= len(options):
            val = int(i)
            return val
    except:
        pass
    return None


def EADG(tab):

    #os.system('clear')

    f = Figlet(font='banner')
    print(f.renderText('EADG'))

    for row in tab:
        for elem in row:
            print(elem, end=' ')
        print()
    
    n = input('Enter position : ')


    if n == 'end' or n == 'END':
        return None



    eString = [41,44,46,49,52,55,58,62,65,69,73,78,82,87,92,98,104,110,117,123,131]

    if n =='play':
        print(tab[3])
        for val in tab[3][1:]:
            #print(tab[3].index(val))
            #print(val)

            if val != '- ':
                val = int(val)
                #print('eString')
                print(eString[val])
            else:
                sleep(0.5)



    if len(n) == 3 :
        note = n[1] + n[2]
    else:
        note = n[1] + ' '


    if len(n) < 2 or len(n) > 3:
        #print(len(n))
        print('too much/few info')
        EADG(tab)


    if n[0] == 'E' or n[0] == 'e':        
        print('E string')
        tab[3].insert(len(tab[3]), note)
        tab[2].insert(len(tab[2]), '- ')
        tab[1].insert(len(tab[1]), '- ')
        tab[0].insert(len(tab[0]), '- ')


    elif n[0] == 'A' or n[0] == 'a':
        print('A string')
        tab[3].insert(len(tab[3]), '- ')
        tab[2].insert(len(tab[2]), note)
        tab[1].insert(len(tab[1]), '- ')
        tab[0].insert(len(tab[0]), '- ')


    elif n[0] == 'D' or n[0] == 'd':
        print('D string')
        tab[3].insert(len(tab[3]), '- ')
        tab[2].insert(len(tab[2]), '- ')
        tab[1].insert(len(tab[1]), note)
        tab[0].insert(len(tab[0]), '- ')


    elif n[0] == 'G' or n[0] == 'g':
        print('G string')
        tab[3].insert(len(tab[3]), '- ')
        tab[2].insert(len(tab[2]), '- ')
        tab[1].insert(len(tab[1]), '- ')
        tab[0].insert(len(tab[0]), note)


    else:
        print('Not valid string')
        EADG(tab)

    EADG(tab)



#exec
options = ['BASS', 'UKULELE(wip)']
val = menu(options)
print(val)

if val == 1:
    os.system('clear')
    f = Figlet(font='slant')
    print(f.renderText('Bass tunings'))

    tunings = ['EADG', 'DADG(wip)', 'BEADG(wip)', 'EADGC(wip)', 'BEADGC(wip)']
    tuning = menu(tunings)

    if tuning == 1:
        os.system('clear')
        tab = [['G-'], ['D-'], ['A-'], ['E-']]
        EADG(tab)