import random

#playerlVariables
playerTotalMoney = 200.0
winCount = 0.0


#this value will increase as you win more.
betMultiplier = 1.5


print("*****Welcome to SimpleBlackJack******")
print("It's not similar to the real black jack, because here we are no counting on the suits, here we are only playing with numbers")
print("Also the minimun bet value is 5$, so if you go below this money amount, you can't play anymore\n")

def GameWonSequence():
    
    global playerTotalMoney
    global betMultiplier
    global betMoney
    global winCount
    
    print("YOU WON !!!, here's you money: " + str(betMoney * betMultiplier))
    playerTotalMoney += betMoney * betMultiplier
    winCount += 1
    print("The multiplier was increased to " + str(betMultiplier + (winCount / 10)))
    
def GameOverSequence():
    print("You lose, more luck next time!")
    
    
while playerTotalMoney >= 5:
    
    #PlayerVariables2
    playerHand = 0
    playerHasAndAce = False
    betMoney = 0
    
    #ComputerVariables2
    dealerHand = 0
    dealerHasAnAce = False
    
    print("*** Player Stats ***")
    print("Money: " + str(playerTotalMoney) + "$")
    option = ""
    print("Do you want to play S BlackJack? (y/n)")
    option = input(">")
    if(option.lower() == "y"):
        print("How much money do you want to bet? ")
        betMoney = int(input(">"))
        if(betMoney > playerTotalMoney):
            betMoney = playerTotalMoney
            playerTotalMoney -= betMoney
        elif(betMoney < 5):
            betMoney = 5
            playerTotalMoney -= betMoney
        else:
            playerTotalMoney -= betMoney
    else:
        break;
    print("Shuffling the cards...")
    print("DealingTheFirstHand: ")
    playerHand += random.randint(2,11)
    dealerHand += random.randint(2,11)
    print("PlayerHand: " + str(playerHand))
    print("DealerHand: " + str(dealerHand))
    while playerHand <= 21:
        print("Do you whant to (h)it or (s)tay? ")
        playerDecision = input(">")
        if(playerDecision.lower() == "h"):
            cardValue = random.randint(2,11)
            if(cardValue == 11 and playerHand >= 11 and playerHasAndAce == False):
                cardValue = 1
                playerHasAndAce = True
                playerHand += cardValue
            elif(cardValue <= 11):
                playerHand += cardValue
            print("PlayerHand: " + str(playerHand))
            print("DealerHand: " + str(dealerHand))
        else:
            print("DealerTime")
            break
            
    while dealerHand < 17:
        cardValue = random.randint(2,11)
        if(cardValue == 11 and dealerHand >= 11 and dealerHasAnAce == False):
            cardValue = 1
            dealerHasAnAce = True
            dealerHand += cardValue
        elif(cardValue <= 11):
            dealerHand += cardValue
        flag = input("Press anything to continue")
        print("PlayerHand: " + str(playerHand))
        print("DealerHand: " + str(dealerHand))
    
    if(dealerHand > 21 and playerHand <= 21):
        GameWonSequence()
    elif(playerHand <= 21 and dealerHand <= 21 and playerHand > dealerHand):
        GameWonSequence()
    elif(playerHand <= 21 and dealerHand <= 21 and dealerHand > playerHand):
        GameOverSequence()
    elif(playerHand > 21 and dealerHand <= 21):
        GameOverSequence()
    elif(playerHand == dealerHand):
        print("That's a tie, here is your money back")
        playerTotalMoney += betMoney
    elif(playerHand > 21 and dealerHand > 21):
        print("Since both blew up, here are 1/5 of what you bet")
        playerTotalMoney += betMoney * 0.50

print("Thanks for playing S BlackJack")
print("Final money: " + str(playerTotalMoney) + "$")


