'''
                            [SNAKE WATER GUN {SWG}] Game
                        Programming language used --> Python  
'''
def swg():                              # Main/Head function
    import random
                         
    def game(c,p):
        if c == p:                      # c --> Computer & p --> Player
            return None
        elif c == 's':                  # s --> Snake , w --> Water & g --> Gun
                if p == 'w':
                    return False
                elif p == 'g':
                    return True
        elif c == 'w':
                if p == 'g':
                    return False
                elif p == 's':
                    return True
        elif c == 'g':
                if p == 's':
                    return False
                elif p == 'w':
                    return True

# Computer's turn !!

    print("\n")
    print(input('''
    Computer's turn ---> ---> ---> Computer choosed !! 
    Press enter or any key for your turn
    ''' ))
    
    rn = random.randint(1,3)                     
    '''print(rn)       # --> print the number choosen by the computer i.e 1,2 or 3'''
    if rn == 1:                 
        c = 's'
    elif rn == 2:
        c = 'w'
    elif rn == 3:
        c = 'g'

# Player's turn !!

    print("\n")
    p = input('''
    Your's turn ---> Please enter your choice !!                     
    Press ---> [s] for SNAKE [w] for WATER [g] for GUN : 
    ''' )

# If correct option is choosed by the Player !!

    if (p=='s' or p=='w' or p=='g'):

# Options choosed by both the players i.e {Computer as well as Player} is ? !! 

        print('''
        Computer choosed ---> ''',c)
        print('''
        Player choosed   ---> ''',p)

# Declaration of Winner !!

        print("\n")
        if game(c,p)== True:
            print('''
            Congratulations !! 
            You WIN
            ''')
        elif game(c,p) == None:
            print('''
            Ooopsss !! 
            Game TIE
            ''')
        else:
            print('''
            Better Luck Next Time !! 
            You LOOSE
            ''')

# Want to Continue or Exit ?

        ec = input('''
        Want to Play again ?? ---> Press 1
        Want to E X I T ?? ---> Press any key except 1
        ''')
        if ec == "1":
            swg()                   # Main function Call
        else:
            exit()                 # exit function Call

# If wrong option is choosed by the player !!

    else:
        print(''' 
        E R R O R !! E R R O R !! E R R O R !! E R R O R !! E R R O R !! 
        Please choose 
        [s] for SNAKE
        [w] for WATER
        [g] for GUN 
        only !!
        ''')

        ce = input('''
        --> Press 1 to C O N T I N U E

        --> Press any key except 1 to E X I T
        ''')
        if ce == "1":
            swg()
        else:
            exit()

# Main function Call 

swg()

'''********************END OF THE CODE********************'''