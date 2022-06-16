import random, os
os.system('cls')
deck=[]
#next, let's start building list holders so we can place our cards in there:
def create_DECK():
    global deck
    numberCards = []
    suits = ["♥️","♦️", "♣️", "♠️"]
    royals = ["J", "Q", "K", "A"]
    

    #now, let's start using loops to add our content:
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the royal faces to the cardbase

    
    for k in range(4):
        for l in range(13):
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make

    #now let's see the cards!
    counter=0
    for row in range(4):
        for col in range(13):
            # print(deck[counter], end=" ")
            counter +=1
        # print()
    #now let's shuffle our deck!
def playerCards():
    random.shuffle(deck)
    player1=[]
    player2=[]
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])
    # print("player1 ",player1)
    # print()
    # print("player2 ",player2)
    #I also want to see what the deck looks like before shuffling. We should have
        #done that a while ago... oh well!
    return player1, player2    
create_DECK()
decs = playerCards()
player1 = decs[0]
player2 = decs[1]

count = 1 
p1_deckcount = 0
p2_deckcount = 0
while count < 50: 
    if len(player1) == 0: 
        print("Player 1, YOU R A LOSER!!!")
        break
    if len(player2) == 0:
        print("Player 2 YOU R ALSO A LOSER!!!!!")
        break
    if p1_deckcount > len(player1)-2:
        p1_deckcount = 0
    if p2_deckcount > len(player2)-2:
        p2_deckcount = 0

    player1_card = player1[p1_deckcount]  
    player1_card = player1_card[0:len(player1_card)-3]  
    if player1_card == "J": 
        player1_card = 17
    if player1_card == "Q":
        player1_card = 12
    if player1_card == "K":
        player1_card = 16
    if player1_card == "A":
        player1_card = 13        

    player2_card = player2[p2_deckcount]  
    player2_card = player2_card[0:len(player2_card)-3]  
    if player2_card == "J":
        player2_card = 17
    if player2_card == "Q":
        player2_card = 12
    if player2_card == "K":
        player2_card = 16
    if player2_card == "A":
        player2_card = 13

    if int(player1_card) > int(player2_card):  
        player1.append(player2[p2_deckcount])
        player2.remove(player2[p2_deckcount])

    elif int(player2_card) > int(player1_card):
        player2.append(player1[p1_deckcount])
        player1.remove(player1[p1_deckcount])

    if count == 49:  
        print("Player 1 show your cards:",player1)
        print()
        print("Player 2 show your card:" , player2)
        print()
        if len(player1) > len(player2): 
            print("YAY!!!!!! PLAYER 1 IS DA WINNER")  
        elif len(player1) < len(player2):
            print("PLAYER 2 IS THE REAL WINNER YAY!!!!!") 
        else:
            print("YOU GUYS ARE BOTH LOSERS!!!!")        
    
    p1_deckcount +=1
    p2_deckcount +=1
    count +=1