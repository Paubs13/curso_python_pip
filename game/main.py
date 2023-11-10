import random

options = ('rock', 'paper', 'scissors')

#declaramos el enfrentamiento como una funcion para no agregar otro bodoque de texto al codigo
def battle (a, b):
    
    if ((a == 'rock' and b == 'scissors') or (a == 'scissors' and b == 'rock')):
        winner = 'rock'
        return winner
    elif ((a == 'paper' and b == 'scissors') or (a == 'scissors' and b == 'paper')):
        winner = 'scissors'
        return winner
    else:
        winner = 'paper'
        return winner

#declaracion de variables que usaremos dentro del loop
user_choice = 'none'
user_win = 0
computer_win = 0

print ('\nThis is THE rock paper and scissors game\n')

#loop principal
while (user_choice != 'quit'):
    #adentro de este if esta la logica del juego, saldremos de esta rama una vez uno llegue a 3 victorias
    if (computer_win < 3 and user_win < 3):
        print('The one who gets to three wins first will win the game \n\nThe score right now is: \nComputer =', computer_win, '\nUser =', user_win, '\n')
        user_choice = input('Type rock, paper or scissors. If you want to quit, type quit: ')
        computer_choice = random.choice(options)
        user_choice = user_choice.lower()

        if (user_choice == 'quit'):
            print ("\nYOU HAVE QUITTED")
            #al declarar el user_choice como quit el programa automaticamente terminara
        else:
            print ('\nYour choice ==> ', user_choice)
            print ("Computer's choice ==> ", computer_choice)
            
            if (computer_choice == user_choice):
                print("\nIt's a TIE!\n")
            elif (not user_choice in options):
                print ("\nYou didn't type a valid option\n")
            else:
                #aca invocamos la funcion que preparamos antes, haciendo las cosas mas simples.
                if (battle (user_choice, computer_choice) == user_choice):
                    print ('\nUser wins this round\n')
                    user_win +=1
                else:
                    print ('\nComputer wins this round\n')
                    computer_win +=1
    #Cuando uno llegue a 3 victorias, el programa pasara a esta instancia dando un score final y dandole la posibilidad al usuario de jugar de nuevo.
    else:
        while (user_win == 3 or computer_win == 3):
            replay = 'not chose yet'
            print('FINAL SCORE:\n COMPUTER ==>', computer_win, '\n USER     ==>', user_win)
            if (user_win == 3):
                print('\nUSER WON')
            else:
                print('\nCOMPUTER WON')
            replay = input('\nDo you want to play again? y/n: ')
            if (replay == 'y'):
                user_win = 0
                computer_win = 0
                #seteamos todos los scores a 0 para volver al juego
                continue
            elif (replay == 'n'):
                user_choice = 'quit'
                #aca rompemos el sub-ciclo while con un break y el ciclo while que engloba todo mediante el quit
                break
            else:
                print("\nYou didn't type a valid option!\n")
                #gracias al ciclo while si el usuario no escribe algo correcto, podra volver a intentarlo
                continue