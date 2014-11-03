import random

class Deck(object):

    def __init__(self):
        self.reset()

    def reset(self):
        # 13 cards in each of 4 suits
        self.PDF = [4]*13
        self.num_cards = 52

    def cards_left(self):
        return self.num_cards

    def draw_card(self):

        if self.num_cards == 0:
            print("No cards left to draw!")
            return
        
        # calculate CDF by summing
        # over all bins of the PDF
        # from bin 0 to bin i
        CDF = [0]*13
        for i in range(len(self.PDF)):
            for j in range(i+1):
                CDF[i] = CDF[i] + self.PDF[j]

        card = 0

        # generate random number and
        # sample inverse CDF
        cum_prob = random.randint(1,self.num_cards)
        
        # lookup corresponding index
        for card in range(len(CDF)):
            if CDF[card] >= cum_prob:
                break               

        # update the PDF for next time
        self.PDF[card] -= 1
        self.num_cards -= 1

        return card
