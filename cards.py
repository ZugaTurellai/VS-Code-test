from os import readlink
from xml.etree.ElementTree import ProcessingInstruction
""" 
class Player:
    def __init__(self, id, deck_skin):
        self.points = 0 # for keeping track of points for losing the game
        self.hand = Hand() # a instance of the hand class, presumably starts empty
        self.lead = 0 # this would be a flag that could be used to keep track of who leads each trick (places first card)
        self.id = id # this would be for account and server side idefication
        self.skin = deck_skin # this is so that when drawing the cards it can look at the player deck skin selected
        self.score = 0 # keeps track of this players score


    def Round_of_Slobberhanes(self, other_players):
        self.hand.deal() # a function that would deal cards to all players, 8 when a four player game
        self.Trick_of_Slobberhanes(other_players, True, False) #first trick of a round
        while (self.hand != 1): # this would run a trick for every card in the hand
            self.Trick_of_Slobberhanes(other_players, False, False)
        self.Trick_of_Slobberhanes(other_players, False, True) # last trick of a round
        if (self.score >= 10 or other_players.score >= 10):
            pass # vitory or lose screen
        else:
            self.Round_of_Slobberhanes(other_players) # the game keeps going till someone goes over ten points during the tricks


    def Trick_of_Slobberhanes(self, other_players, first_trick, last_trick):
        if (self.lead == 1): # this is if the player this is running on is the lead
            c1 = self.play_card() # play_card should return the card played, that way we can pass it to outranks()
            c2 = other_players.play_card() # another option is we could make a table object that would keep track of such things
        else:
            c1 = other_players.play_card() # not sure how this would work with server stuff
            c2 = self.play_card()
        winner = c1.outranks(c2) # there would of course be more than c2 played cards, but this is just for planning
        if (winner == True):
            self.lead = 1 # leads next trick
            #if (c1.rank == queen and c1.suit == clubs or c2.rank == queen and c2.suit == clubs):
             #   self.score += 1 # if the player wins and the took the queen of clubs they gain a point
            if (first_trick == True or last_trick == True):
                self.score += 1 # if the player wins the first or last trick of hand they gain a point
 """
        
###########################################################################################################################


class Card:
    def __init__(self, rank, suit, skin):
        self.rank = rank
        self.suit = suit
        self.skin = skin # this would be for the card image so that we can use self.skin to draw the cards 
                         # with the players deck skin

    def draw(self):
        pass # this would likely be used by the hand class to draw all the cards in the hand

    def outranks(self, c2, c3, c4, lead_suit):
        c1 = self
        if c1.suit != lead_suit:
            return False    # this means that the starting card does not have a chance of winning as it is not of the lead suit

        if c2.suit == lead_suit and c1.rank < c2.rank: # these will compare the cards on the table and if the self (card played by you)
            return False                        # is not the highest it will return false

        if c3.suit == lead_suit and c1.rank < c3.rank: 
            return False

        if c4.suit == lead_suit and c1.rank < c4.rank:
            return False

        else:   # this returns true when it is the highest card on the board, i assume that this will later be used by a Trick function
            return True # I imagine the Trick function would handle most board play, and if outranks returns true it would allocate points
        