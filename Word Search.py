# STEP 1
# DIALOGUES (D)
dialogues = (
['Type in your word. Do not use capitals.', 'which row is the first letter?', 'which column is the first letter?',
 '+1 POINT', 'YOU WIN!'])
print('select difficulty')
print('"fine()", "boring()", "chore()"')


# D END

# STEP 2
# SCOREBOARD (B)
def scoreboard():
    f = open('scoreboard.txt', 'w')
    f.write('WORDSEARCH SCOREBOARD\n')
    f.close()


# B END

# STEP 3
# WORDSEARCHES (W)

# FINE
def fine():
    print('  C 1 2 3 4 5 6 7')
    print('R')
    print('1   a l o s m p v')
    print('2   m i u d o c g')
    print('3   z n z e l d a')
    print('4   y k s c j i n')
    print('5   h j u r e n o')
    print('6   y e u r y a n')
    print('7   m j c x e q w')
    print('WORDS: Link, Zelda, Ganon, Din, Nayru\n')
    print(dialogues[0])

    f = open('scoreboard.txt', 'a')
    search = ''
    while (search != 'x'):
        print("Enter 'x' to exit")
        search = input()
        # LINK
        if search == 'link':
            print(dialogues[1])
            row = input()
            if row == '1':
                print(dialogues[2])
                column = input()
                if column == '2':
                    print(dialogues[3])
                    f.write('point\n')
        # ZELDA
        if search == 'zelda':
            print(dialogues[1])
            row = input()
            if row == '3':
                print(dialogues[2])
                column = input()
                if column == '3':
                    print(dialogues[3])
                    f.write('point\n')
        # GANON
        if search == 'ganon':
            print(dialogues[1])
            row = input()
            if row == '2':
                print(dialogues[2])
                column = input()
                if column == '7':
                    print(dialogues[3])
                    f.write('point\n')
        # DIN
        if search == 'din':
            print(dialogues[1])
            row = input()
            if row == '3':
                print(dialogues[2])
                column = input()
                if column == '6':
                    print(dialogues[3])
                    f.write('point\n')
        # NAYRU
        if search == 'nayru':
            print(dialogues[1])
            row = input()
            if row == '6':
                print(dialogues[2])
                column = input()
                if column == '7':
                    print(dialogues[3])
                    f.write('point\n')
    f.close()

    sum = 0
    with open('scoreboard.txt') as openfile:
        for line in openfile:
            for part in line.split():
                if "point" in part:
                    sum = sum + 1
        if sum >= 5:
            print("You win!")


# BORING
def boring():
    print('  C 1 2 3 4 5 6 7 8 9')
    print('R')
    print('1   m a l l e r b m u')
    print('2   r c b i r k i n c')
    print('3   x v u x r e i x l')
    print('4   l e o n s n g b a')
    print('5   h u n k e n v u i')
    print('6   r e d f i e l d r')
    print('7   u m m r r d l a e')
    print('8   s h e r r y x j n')
    print('9   s t v i r u s i k')
    print('WORDS: Leon, Kennedy, Claire, Redfield, Sherry, Birkin, Mr X, Hunk, T Virus, Umbrella')

    f = open('scoreboard.txt', 'a')
    search = ''
    while (search != 'x'):
        print("Enter 'x' to exit")
        search = input()
        # LEON
        if search == 'leon':
            print(dialogues[1])
            row = input()
            if row == '4':
                print(dialogues[2])
                column = input()
                if column == '1':
                    print(dialogues[3])
                    f.write('point\n')
        # KENNEDY
        if search == 'kennedy':
            print(dialogues[1])
            row = input()
            if row == '2':
                print(dialogues[2])
                column = input()
                if column == '6':
                    print(dialogues[3])
                    f.write('point\n')
        # CLAIRE
        if search == 'claire':
            print(dialogues[1])
            row = input()
            if row == '2':
                print(dialogues[2])
                column = input()
                if column == '2':
                    print(dialogues[3])
                    f.write('point\n')
        # REDFIELD
        if search == 'redfield':
            print(dialogues[1])
            row = input()
            if row == '6':
                print(dialogues[2])
                column = input()
                if column == '1':
                    print(dialogues[3])
                    f.write('point\n')
        # SHERRY
        if search == 'sherry':
            print(dialogues[1])
            row = input()
            if row == '8':
                print(dialogues[2])
                column = input()
                if column == '1':
                    print(dialogues[3])
                    f.write('point\n')
        # BIRKIN
        if search == 'birkin':
            print(dialogues[1])
            row = input()
            if row == '1':
                print(dialogues[2])
                column = input()
                if column == '7':
                    print(dialogues[3])
                    f.write('point\n')
        # MR X
        if search == 'mr x':
            print(dialogues[1])
            row = input()
            if row == '1':
                print(dialogues[2])
                column = input()
                if column == '1':
                    print(dialogues[3])
                    f.write('point\n')
        # HUNK
        if search == 'hunk':
            print(dialogues[1])
            row = input()
            if row == '5':
                print(dialogues[2])
                column = input()
                if column == '1':
                    print(dialogues[3])
                    f.write('point\n')
        # T VIRUS
        if search == 't virus':
            print(dialogues[1])
            row = input()
            if row == '9':
                print(dialogues[2])
                column = input()
                if column == '8':
                    print(dialogues[2])
                    f.write('point\n')
        # UMBRELLA
        if search == 'umbrella':
            print(dialogues[1])
            row = input()
            if row == '1':
                print(dialogues[2])
                column = input()
                if column == '9':
                    print(dialogues[3])
                    f.write('point\n')
    f.close()

    sum = 0
    with open('scoreboard.txt') as openfile:
        for line in openfile:
            for part in line.split():
                if "point" in part:
                    sum = sum + 1
        if sum >= 10:
            print("You win!")


# CHORE
def chore():
    print('  C 1 2 3 4 5 6 7 8 9 10 11 12 13')
    print('R')
    print('1   a r a i d e n i c a  s  w  v')
    print('2   m c u d o c x j n e  n  d  e')
    print('3   s v f a r m k p q u  i  e  t')
    print('4   o f s c j h g k i r  p  w  a')
    print('5   l i q u i d v t c x  e  g  s')
    print('6   i e t c v e n o m v  n  i  s')
    print('7   d j o x e k w l l q  w  z  o')
    print('8   a c x o f a e e u g  o  j  b')
    print('9   o i e q s n z c r e  l  v  g')
    print('10  i t c q v r p o j h  f  v  i')
    print('11  d d o g i n e k a n  s  z  b')
    print('12  k l e w o r r o s y  y  o  j')
    print(
        'WORDS: Snake, Solid, Liquid, Naked, Venom, Big Boss, Raiden, Ocelot, Sniper Wolf, Quiet, Joy, Sorrow, End, Fox, D Dog')

    f = open('scoreboard.txt', 'a')
    search = ''
    while (search != 'x'):
        print("Enter 'x' to exit")
        search = input()
        # SNAKE
        if search == 'snake':
            print(dialogues[1])
            row = input()
            if row == '11':
                print(dialogues[2])
                column = input()
                if column == '11':
                    print(dialogues[3])
                    f.write('point\n')
        # SOLID
        if search == 'solid':
            print(dialogues[1])
            row = input()
            if row == '1':
                print(dialogues[2])
                column = input()
                if column == '3':
                    print(dialogues[3])
                    f.write('point\n')
        # LIQUID
        if search == 'liquid':
            print(dialogues[1])
            row = input()
            if row == '5':
                print(dialogues[2])
                column = input()
                if column == '1':
                    print(dialogues[3])
                    f.write('point\n')
        # NAKED
        if search == 'naked':
            print(dialogues[1])
            row = input()
            if row == '9':
                print(dialogues[2])
                column = input()
                if column == '6':
                    print(dialogues[3])
                    f.write('point\n')
        # VENOM
        if search == 'venom':
            print(dialogues[1])
            row = input()
            if row == '6':
                print(dialogues[2])
                column = input()
                if column == '5':
                    print(dialogues[3])
                    f.write('point\n')
        # BIG BOSS
        if search == 'big boss':
            print(dialogues[1])
            row = input()
            if row == '11':
                print(dialogues[2])
                column = input()
                if column == '13':
                    print(dialogues[3])
                    f.write('point\n')
        # RAIDEN
        if search == 'raiden':
            print(dialogues[1])
            row = input()
            if row == '1':
                print(dialogues[2])
                column = input()
                if column == '2':
                    print(dialogues[3])
                    f.write('point\n')
        # OCELOT
        if search == 'ocelot':
            print(dialogues[1])
            row = input()
            if row == '10':
                print(dialogues[2])
                column = input()
                if column == '8':
                    print(dialogues[3])
                    f.write('point\n')
        # SNIPDER WOLF
        if search == 'sniper wolf':
            print(dialogues[1])
            row = input()
            if row == '1':
                print(dialogues[2])
                column = input()
                if column == '11':
                    print(dialogues[3])
                    f.write('point\n')
        # QUIET
        if search == 'quiet':
            print(dialogues[1])
            row = input()
            if row == '3':
                print(dialogues[2])
                column = input()
                if column == '9':
                    print(dialogues[3])
                    f.write('point\n')
        # JOY
        if search == 'joy':
            print(dialogues[1])
            row = input()
            if row == '12':
                print(dialogues[2])
                column = input()
                if column == '13':
                    print(dialogues[3])
                    f.write('point\n')
        # SORROW
        if search == 'sorrow':
            print(dialogues[1])
            row = input()
            if row == '12':
                print(dialogues[2])
                column = input()
                if column == '9':
                    print(dialogues[3])
                    f.write('point\n')
        # END
        if search == 'end':
            print(dialogues[1])
            row = input()
            if row == '2':
                print(dialogues[2])
                column = input()
                if column == '10':
                    print(dialogues[3])
                    f.write('point\n')
        # FOX
        if search == 'fox':
            print(dialogues[1])
            row = input()
            if row == '7':
                print(dialogues[2])
                column = input()
                if column == '5':
                    print(dialogues[3])
                    f.write('point\n')
        # D DOG
        if search == 'd dog':
            print(dialogues[1])
            row = input()
            if row == '11':
                print(dialogues[2])
                column = input()
                if column == '1':
                    print(dialogues[3])
                    f.write('point\n')
    f.close()

    sum = 0
    with open('scoreboard.txt') as openfile:
        for line in openfile:
            for part in line.split():
                if "point" in part:
                    sum = sum + 1
        if sum >= 15:
            print("You win!")


# W END

# STEP 4
# PLAY (P)
difficulty = input()
if difficulty == 'fine':
    fine()
elif difficulty == 'boring':
    boring()
# else difficulty == 'chore':
#     chore()
'''cannot figure out why this else statement won't cooperate'''
# P END