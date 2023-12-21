"""
Description: It is a one-player game, the player has to identify one alphabet that is common in the two given lists. 
"""
import string #to import alphabets
import random #to import random function
print("Hi there, let's play spotting")
print("You have to spot a letter that is present in both the list")
c=1 #for controlling the loop
while(c==1):  #loop starts here
    symbols=[] #preparing list to add letters
    symbols=list(string.ascii_letters) #all letter (lowercase and uppercase)  in one list
    card1=[0]*5 
    card2=[0]*5
    pos1=random.randint(0,4) #for choosing positions randomly for card 1
    pos2=random.randint(0,4) #for choosing positions randomly for card 2
#by the way pos1 and pos2 are same symbol position in card1 and card2
    samesymbol=random.choice(symbols) #randomly chosing letters from the list symbols
    symbols.remove(samesymbol) #to remove the letter from the list symbols 
    if(pos1==pos2): 
        card2[pos1]=samesymbol
        card1[pos1]=samesymbol
        # Change one of the positions (pos2 in this case)
        pos2 = (pos2 + 1) % 5  # taking modulo 5 to make sure it stays within range 0-4

        # Assign a different symbol to the changed position in card2
        card2[pos2] = random.choice(symbols)
        symbols.remove(card2[pos2])

    else: #if position of symbols are not same
        card1[pos1]=samesymbol #add chosen letter to the card1
        card2[pos2]=samesymbol   #add chosen letter to the card2
        card1[pos2]=random.choice(symbols) #adding different letter at random position stored in pos 2
        symbols.remove(card1[pos2])  #removing letter from the list each time, to avoid 
        card2[pos1]=random.choice(symbols) #adding different letter at random position stored in pos 1
        symbols.remove(card2[pos1]) 
    i=0 
    while(i<5):
        if(i!=pos1 and i!=pos2): #for filling rest of the position
            alphabet1=random.choice(symbols)
            symbols.remove(alphabet1)
            alphabet2=random.choice(symbols)
            symbols.remove(alphabet2)
            card1[i]=alphabet1
            card2[i]=alphabet2
        i=i+1
    print(card1)
    print(card2)
    ch=input("Enter the similar symbol: ")
    if (ch==samesymbol):
        print("Correct answer")
        c=int(input("Please 0 to quit and 1 to continue: "))
        if (c==0):
            print("Thank you for playing!")
            break
    else:
        print("You are wrong")
        
