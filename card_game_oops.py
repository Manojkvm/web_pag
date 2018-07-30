from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class deck():

    def __init__(self):
        print("creating cards!...")
        self.allcards = [(s,r) for s in suite for r in ranks]

    def shuffle(self):
        print("shuffling cards now!..")
        shuffle(self.allcards)

    def split_half(self):
        print("splitting cards!...")
        return (self.allcards[:26],self.allcards[26:])

class hand():

    def __init__(self,cards):
        self.cards = cards

    def __str__(self,cards):
        return ("deck contains {} cards".format(len(self.cards))

    def added(self,add_card):
        self.cards.extend(add_card)

    def remove(self):
         return self.cards.pop()

class player():

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print("palyer {} has palced: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 2:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def still_has_cards(self):
        """
        returns true if player still has war_cards

        """
        return len(self.hand.cards) != 0

print("lets do war!")

d = deck()
d.shuffle()
half1,half2 = d.split_half()

comp = palyer("computer",hand(half1))

name = input("enter your name to play")
user = player(name,hand(half2))

war_count = 0
total_rounds = 0

while user.still_has_cards() and comp.still_has_cards():

    total_rounds+=1
    print("time for a new round")
    print("here are the currents standings")
    print("user has {} cards".format(str(len(user.hand.cards))))
    print("computer has {} cards".format(str(len(comp.hand.cards))))
    print("play a card!")
    print("\n")

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count+=1
        print("war! ")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.added(table_cards)
        else:
            comp.hand.added(table_cards)
    else:
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.added(table_cards)
        else:
            comp.hand.added(table_cards)

print("number of rounds"+str(total_rounds))
print("A war happened"+str(war_count)+"times")
