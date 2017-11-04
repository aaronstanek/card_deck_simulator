import random

val_to_num = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}

class card:
    def __init__(self,val,suit):
        self.val = val
        self.suit = suit
    def __str__(self):
        return self.val+self.suit
    def same_value(self,other):
        if self.val==other.val:
            return True
        return False
    def same_suit(self,other):
        if self.suit==other.suit:
            return True
        return False
    def __eq__(self,other):
        if self.same_value(other)==False:
            return False
        if self.same_suit(other)==False:
            return False
        return True
    def __ne__(self,other):
        if self==other:
            return False
        return True
    def __lt__(self,other):
        if val_to_num[self.val]<val_to_num[other.val]:
            return True
        return False
    def __ge__(self,other):
        if self<other:
            return False
        return True
    def __gt__(self,other):
        if val_to_num[self.val]>val_to_num[other.val]:
            return True
        return False
    def __le__(self,other):
        if self>other:
            return False
        return True

def initial_fill():
    global hold
    hold = []
    for val in list(val_to_num):
        for suit in ["c","d","h","s"]:
            hold.append(card(val,suit))

initial_fill()

class deck:
    def __init__(self):
        self.cards = []
    def __len__(self):
        return len(self.cards)
    def __contains__(self,c):
        if c in self.cards:
            return True
        return False
    def sort(self):
        self.cards.sort()
    def sort_inverse(self):
        self.cards.sort()
        self.cards = self.cards[::-1]
    def __getitem__(self,index):
        return self.cards[index]
    def __setitem__(self,index,value):
        self.cards[index] = value
    def initialize(self):
        self.cards = hold[:]
    def shuffle(self):
        b = len(self)*1000
        assoc = dict()
        order = []
        for i in range(len(self.cards)):
            while True:
                g = random.randint(0,b)
                if g not in assoc:
                    assoc[g] = self[i]
                    order.append(g)
                    break
        order.sort()
        for i in range(len(order)):
            order[i] = assoc[order[i]]
        self.cards = order[:]
    def add_to_bottom(self,c):
        self.cards = [c] + self.cards
    def pop_bottom(self):
        return self.cards.pop(0)
    def add_to_top(self,c):
        self.cards.append(c)
    def pop_top(self):
        return self.cards.pop()
    def duplicate(self):
        n = deck()
        n.cards = self.cards[:]
        return n
    def move_cards_to(self,other):
        other.cards = other.cards + self.cards[:]
        self.cards = []

def deal(d,hands,cph):
    #cph is cards per hand (int)
    #hands is the number of hands to deal(int)
    ou = []
    for i in range(hands):
        ou.append(deck())
    for i in range(cph):
        for j in range(hands):
            if len(d)==0:
                return ou
            c = d.pop_top()
            ou[j].add_to_top(c)
    return ou
