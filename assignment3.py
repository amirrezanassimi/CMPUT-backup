# Assignment 3
# Amirreza Nassimi 
# 1513904


import random as rand



class Queue:
    
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception ('Error: Invalid capacity')
        self.items = []
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self,item):
        if self.count == self.capacity:
            raise Exception('Error: Queue is full')
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.tail]=item
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        
    def dequeue(self):
        if self.count == 0:
            raise Exception('Error: Queue is empty')
        item = self.items[self.head]
        self.items[self.head] = None
        self.count -= 1
        self.head = (self.head + 1) % self.capacity
        
        return item
    
    def peek(self):
        if self.count == 0:
            raise Exception('Error: Queue is empty')
        return self.items[self.head]
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.capacity     

    def size(self):
        return self.count
    
    def capacity(self):
        return self.capacity
        
    def clear(self):
        self.items = []
        self.head = 0
        self.tail = 0
        self.count = 0
        
    def __str__(self):
        str_exp = ']'
        j = self.head
        for j in range(self.count):
            str_exp += str(self.items[j])+' '
            j = (j+1) % self.capacity
        return str_exp + "]"
 
    def __repr__(self):
        return str(self.items)+" H = "+str(self.head)+" T = "+str(self.tail) + str(self.count) + '/' + str(self.capacity) + '/'


class War:
    
    def __init__(self):
        self.player1 = Queue(52)
        self.player2 = Queue(52)
        self.suits=["D", "C", "H", "S"]
        self.ranks=["2","3","4","5","6","7","8","9","0","J", "Q", "K", "A"]    
        self.value = {}
        for j in range(len(self.ranks)):
            self.value[self.ranks[j]]=j            
        self.deck = self.Loading()
        self.TestDeck(self.deck)
        self.ChosePlayer(self.deck)

        while True:
            try:
                self.warNum = int(input("How many cards for war /(1,2,3)? "))
                assert self.warNum in [1,2,3]
            except Exception:
                print('That is not a valid number') 
                print('Please pick a number between 1,2 or 3')
            else:
                break
            
        self.endGame = False
        
    def Loading(self):
        while True:
            try:
                file = input('What is the file name for the shuffled deck? ')
                deckFile = open(file, 'r')
                deck = [j.strip().upper() for j in deckFile]
            except Exception as e:
                print(e)
            else:
                deckFile.close()
                print('Deck loading complete')
                return deck
 
    
    def TestDeck(self,deck): 
        
        assert len(deck) == 52, "Deck doesn't have enough cards"
        
        for rank in self.ranks:
            for suit in self.suits:
                assert rank+suit in deck, "Deck check: Failed\n{} not in the deck" \
                                           .format(rank+suit)
        print('Deck check complete')

    
    def ChosePlayer(self,deck):
        player = rand.choice([1,-1])
        for j in range(52):
            self.DistributionCards(player, deck.pop())
            player = player * -1

            
    def DistributionCards(self, player, card):
        if player == 1:
            hand = self.player1
        else:
            hand = self.player2   
        hand.enqueue(card)
    
               
    def winner(self):
        if self.player1.isEmpty():
            return 2
        elif self.player2.isEmpty():
            return 1
        else:
            return False
                   
    def comparing(self,player1,player2):

        if self.value[player1[0]] == self.value[player2[0]]:
            return 0
        elif self.value[player1[0]] > self.value[player2[0]]:
            return 1
        else:
            return -1
        
        
    def getCard(self,player):

        try:
            if player == 1:
                return self.player1.dequeue()
            else:
                return self.player2.dequeue()
        except:
            return 0
        
        
    def __repr__(self):

        str_exp = 'Player1: {} cards\nPlayer2: {} cards'.format(
                  self.player1.size(), self.player2.size())
        return str_exp


class OnTable:
    def __init__(self):
        self.__cards = []
        self.__faceUp = []

        
    def place(self,player,card,hidden):
        if player == 1:
            self.__cards.insert(0,card)
            self.__faceUp.insert(0,not hidden)
        if player == -1:
            self.__cards.append(card)
            self.__faceUp.append(not hidden)
            
        
    def updTable(self):
        p = self.__cards
        self.cleanTable()
        return p
    
    
    def cleanTable(self):
        self.__cards = []
        self.__faceUp = []
          
        
    def __str__(self):
        str_exp = "["
        for j in range(len(self.__cards)):
            if j == 0:
                str_exp += self.__cards[j]   
            else:
                if self.__faceUp[j]:
                    str_exp += ", "+self.__cards[j]
                else:
                    str_exp += ", XX"
        str_exp += "]"
        return str_exp

def main():
    war = War()
    table = OnTable()

    while not war.endGame:
        faceUp1 = war.getCard(1)
        table.place(1,faceUp1,False)
        faceUp2 = war.getCard(-1)
        table.place(-1,faceUp2,False)
        print(table)
        print(repr(war))
        input('Press enter to continue:\n')
        
        win = war.comparing(faceUp1, faceUp2)
        if win:
            for j in table.updTable():
                war.DistributionCards(win,j)
        
        else:
            for player in [1,-1]:
                for j in range(war.warNum):
                    fdown = war.getCard(player)
                    if fdown:
                        table.place(player, fdown, True)
                    else:
                        for j in table.updTable():
                            war.DistributionCards(player*-1, j)
                            war.endGame = player
       
        war.endGame = war.winner()

    print("Player {} wins the War!".format(war.endGame))  
              
main()






## I Got some help in  few parts