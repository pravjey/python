
def get_float(prompt):
    try:
        x = float(input(prompt))
        return x
    except ValueError:
        print('Invalid input - please type a number')
        return get_float(prompt)


#The putpose of this function is enable the program to state whether the lander is moving towards or away from the surface, rather than stating a negative velocity.
#For the player, a negative velocity would look unnatural
def get_direction(a,b):
    if a < b:
        c = "towards"
    else:
        c = "away from"
    return c


def game():

    #Starting values
    altitude = 1000.0  #Distance of lunar lander above the Moon's surface (metres)
    altitudeprev = altitude     #Previous altitude
    velocity = 0.0      #Velocity at which lunar lander is travelling (metres per second)
    fuelburn = 0.0        #Amount of fuel just burnt
    fuelleft = 1000.0   #Fuel left in in tank after each turn (litres) 
    timeperturn = 1.0     #Time taken per turn (seconds)

    #As long as the altitude is greater than zero, the lander still needs to land
    while altitude > 0.0:

        #Print current altitude and velocity of lander with fuel remaining
        print('Current status')
        print('==============')
        print('You are', altitude, 'metres from the Moon\'s surface.')
        print('You are moving at ' + str(abs(velocity)) + ' metres per second ' + get_direction(altitude, altitudeprev) + ' the surface.')
        print('You have', fuelleft, 'litres remaining in the lander\'s tank.')
        print('')

        #As long as there is fuel left in the tank, the player can choose how much fuel to burn, otherwise fuelburn is automatically set to zero
        if fuelleft > 0.0:
            fuelburn = get_float('How much fuel do you want to use? ')
        else:
            fuelburn = 0.0
        #If player inputs a negative value for fuel to burn, it is treated as if player input zero
        if fuelburn < 0.0: 
            fuelburn = 0.0

        #Velocity increases by 1.6 m/s due to gravity and decreases by an amount proportional to the fuel burnt. If fuelburn is zero, either at player's choice or because
        #there is no more fuel left, then velocity keeps increasing
        velocity = velocity + 1.6 - (0.15 * fuelburn)

        #Altitude (m) decreases by velocity (m/s) multiplied by time per turn (s)
        altitudeprev = altitude
        altitude = altitude - (velocity * timeperturn)

        #As long as there is enough fuel remaining, the fuel is reduced by the amount of fuel burnt, otherwise all the fuel is burnt and no fuel is left
        if fuelburn < fuelleft:
            fuelleft = fuelleft - fuelburn
        elif fuelburn >= fuelleft:
            fuelleft = 0.0

        #The main reason for this chunk is to allow user to view status when there is no more fuel - otherwise status will keep being printed until lander lands or crashes
        print(' ')
        input('Press any key and press Enter to continue')
        print(' ')

    #The program comes out of the loop once the altitude is less than or equal to zero. It checks the velocity to determine whether the landing was safe
    if velocity <= 10.0:
        safelanding = True
    elif velocity > 10.0:
        safelanding = False
    if safelanding == True:
        print('You have landed safely at a velocity of', velocity, 'with', fuelleft, 'litres of fuel remaining')
    elif safelanding == False:
        print('You hit the surface at a velocity of', velocity, 'and ended up in a crater of', abs(altitude), 'metres')


newgame = 'yes'
while newgame[0] == 'Y' or newgame[0] == 'y':
    game()
    print(' ')
    newgame = str(input('Do you want play again?'))
    if newgame[0] == 'n' or newgame[0] == 'N':
        break
    
    


