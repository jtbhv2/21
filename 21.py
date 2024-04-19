import random
import statistics



def gameSetUp():
    hardMode = 0
    print('21! Closest to 21 without going over wins. Each player shares one deck of cards 1-11 inclusive, no repeats.')
    if input('Would you like to enable Hard Mode? y/n: ') == 'y':
        hardMode = 1
    while True:
        mainGame(hardMode)
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            break

def handValue(hand):
    total = 0
    total = total + sum(hand)
    return total

def drawCard(deck):
    return deck.pop()
    
def mainGame(hardMode):
    deck = [1,2,3,4,5,6,7,8,9,10,11]
    random.shuffle(deck)
    myCards = [deck.pop(), deck.pop()]
    opponentCards = [deck.pop(), deck.pop()]

    playerTurn = True
    superDrawCount = 0

    while True: #player's turn
        if playerTurn:
            print(f'Opponent is showing {opponentCards[1:]}')
            print(f'Your cards are {myCards} ({handValue(myCards)})')
            choice = input('Enter H for hit, or S for stay: ')
            possibleBreak = 0 #game ends when both players stay in a row. which means if you stay, then they hit, you have the option to hit again
            if choice == 'S':
                possibleBreak += 1
                playerTurn = False
            elif choice == 'H':
                myCards.append(deck.pop())
                playerTurn = False #whether you hit or stay, it then becomes their turn
            else:
                print("Invalid choice. Please enter 'H' for hit or 'S' for stay.")
        else:
            if handValue(opponentCards) < 21:
                superCard = 21 - handValue(opponentCards)
                superDrawCount += 1
                superCardInDeck = False
                for card in deck:
                    if superCard == card:
                        superCardInDeck = True
                        break
                if superDrawCount == 1 and superCardInDeck == True and hardMode == 1: #I like the idea of the computer cheating
                    superCardIndex = deck.index(superCard)
                    opponentCards.append(deck.pop(superCardIndex))
                    playerTurn = True
                elif handValue(opponentCards) <= statistics.mean(deck):
                    opponentCards.append(deck.pop()) #computer checks to see if numbers are in their favor, and if so, this is a hit
                    playerTurn = True
                else:
                    possibleBreak += 1
                    playerTurn = True # they say odds are against them, so they stay
            else: #They have either 21 or greater, so they stay
                possibleBreak += 1
                playerTurn = True
        if possibleBreak >= 2:
            break
 
    playerScore = handValue(myCards)
    opponentScore = handValue(opponentCards)
    print(f'Opponent hand was {opponentCards}')
    print(f'Opponent Score was: {opponentScore}')
    print(f'Your score was: {playerScore}')
    if playerScore > 21 and opponentScore > 21:
        if playerScore <= opponentScore:
            print('Really? Both busted? Well, yours was lower...or tied... so... You Win!')
        else:
            print('Really? Both busted? Well, yours was higher so... You Double Lose!')
    elif opponentScore > 21:
        print('You win! That dude busted. He was a punk anyways')
    elif playerScore > 21:
        print('You went over 21. That is... not great. You lose :(')
    elif playerScore > opponentScore:
        if hardMode == 1:
            print('Damn!! You beat this jerk even when it is cheating. You are truly the King of Games!')
        else:
            print('You win! You sure did beat a computer... on easy mode...')
    elif opponentScore > playerScore:
        print('Blimey. Losing to a computer is... well... gg anyways.')
    elif playerScore == opponentScore:
        print('Tie game. Boooooo')

if __name__ == "__main__":
    gameSetUp()
