# Imports:
from os import system, path
import matplotlib.pyplot as plt, tkinter as t
# Start graphical application:
main = t.Tk(); main.title('Codemy.com')
main.geometry("800x600"); w = 600; h = 400
canvas=t.Canvas(main,width=w,height=h,bg="white")
canvas.pack(pady=20); x = w/2; y = h/2
circle = canvas.create_oval(x, y, x+20, y+20)
def left(event):
    x = -10; y = 0; canvas.move(circle, x, y)
def right(event):
    x = 10; y = 0; canvas.move(circle, x, y)
def up(event):
    x = 0; y = -10; canvas.move(circle, x, y)
def down(event):
    x = 0; y = 10; canvas.move(circle, x, y)
def pressing(event):
    x = 0; y = 0
    if event.char == "a": x = -10
    if event.char == "d": x = 10
    if event.char == "r": y = -10
    if event.char == "x": y = 10
    canvas.move(circle, x, y)
main.bind("<Key>", pressing)
main.bind("<Left>", left)
main.bind("<Right>", right)
main.bind("<Up>", up)
main.bind("<Down>", down)
main.mainloop()
# Calculate the probability of a Pair:
def pair(cards):
    totalCards = 13 * [0]
    for card in cards.values():
        totalCards += card
    same = max(totalCards)
    print(totalCards)
    print(same)
    print(cards)
    print(len(cards))
    if (same == 1):
        if (len(cards) == 3):
            return 100 * 40 * 36 * 32 * 18 / 49 * 48 * 47 * 46
        if (len(cards) == 4):
            return 100 * 36 * 32 * 18  / 48 * 47 * 46
        if (len(cards) == 5):
            return 100 * 32 * 18 / 47 * 46
    elif (same == 2):
        return 100
    return 0
# Calculate the probability of a Two (2) Pair:
def two_pair(cards):
    return 0
# Calculate the probability of a Three (3) of a Kind:
def three_of_a_kind(cards):
    return 0
# Calculate the probability of a Straight:
def straight(cards):
    return 0
# Calculate the probability of a Flush:
def flush(cards):
    return 0
def full_house(cards):
    return 0
# Calculate the probability of a Four (4) of a Kind:
def four_of_a_kind(cards):
    return 0
# Calculate the probability of a Straight Flush:
def straight_flush(cards):
    return 0
# Calculate the probability of a Royal Flush:
def royal_flush(cards):
    return 0
# Chooses the function to calculate the probability of each poker hand:
def choose(key, cards):
    if (key == ' 2. Pair: '):
        return pair(cards)
    if (key == ' 3. Two (2) Pair: '):
        return two_pair(cards)
    if (key == ' 4. Three (3) of a Kind: '):
        return three_of_a_kind(cards)
    if (key == ' 5. Straight: '):
        return straight(cards)
    if (key == ' 6. Flush: '):
        return flush(cards)
    if (key == ' 7. Full House: '):
        return full_house(cards)
    if (key == ' 8. Four (4) of a Kind: '):
        return four_of_a_kind(cards)
    if (key == ' 9. Straight Flush: '):
        return straight_flush(cards)
    if (key == '10. Royal Flush: '):
        return royal_flush(cards)
    return 100
# Plot probabilities:
def plot_probabilities(probabilities):
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    hands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    LEGEND = ''
    for k, v in probabilities.items():
        LEGEND += k + str(v) + 'n'
    ax.plot(hands, list(probabilities.values())[:-1], label=LEGEND)
    ax.set_title('Probabilities in %:', fontsize=15)
    ax.set_xlabel('Poker Hand', fontsize=15)
    ax.set_ylabel('Probability', fontsize=15)
    ax.tick_params('both', labelsize=12)
    ax.legend(fontsize=15); plt.show()
    system( 'rmdir /s /q "' + path.expanduser('~') + '\.matplotlib"' )
# Class for assigning each card of the flop, turn, and river.
class Card:
    def __init__(self, cardSuit, cardNumber):
        self.suit = cardSuit
        self.numbers = ['2', '3', '4', '5', '6', '7', '8', '9', \
                              '10', 'Jack', 'Queen', 'King', 'Ace']
        self.numberCode = 13 * [0]
        for index, number in enumerate(self.numbers):
            if (number == cardNumber):
                self.numberCode[index] = 1
# Class for calculating probabilities:
class PokerOdds:
    # Assign initial variables:
    def __init__(self):
        self.totalCombos = 52 * 51 * 50 * 49 * 48 * 47 * 46
        self.probs = { ' 1. High Card: ': self.totalCombos, \
                       ' 2. Pair: ': 52 * 3 * 48 * 44 * 40, \
                       ' 3. Two (2) Pair: ': 52 * 3 * 48 * 3 * 44, \
                       ' 4. Three (3) of a Kind: ': 52*3*2*48*44, \
                       ' 5. Straight: ': 4*9*4*4*4*3*4*2*3*1, \
                       ' 6. Flush: ': 52 * 12 * 11 * 10 * 8, \
                       ' 7. Full House: ': 52 * 3 * 2 * 48 * 3, \
                       ' 8. Four (4) of a Kind: ': 52*3*2*48, \
                       ' 9. Straight Flush: ': 4 * 9 * 4 * 3 * 2, \
                       '10. Royal Flush: ': (4 * 5) * 4 * 3 * 2, \
                       'Total: ': self.totalCombos \
                     }
    # Plot and give initial probabilities before flop:
    def holeCards(self):
        self.probs.update((k, 100*v/self.totalCombos) \
                                for k, v in self.probs.items())
        self.probs[' 1. High Card: ']-=sum(list(\
                                    self.probs.values())[1:-1])
        plot_probabilities(self.probs)
    # Calculate probabilities after flop:
    def flop(self, card1, card2, card3):
        # Update cards:
        suit1, suit2, suit3 = card1.suit, card2.suit, card3.suit
        num1, num2, num3 = card1.numberCode, card2.numberCode, \
                                                   card3.numberCode
        self.cards = {suit1: num1, suit2: num2, suit3: num3}
        print(self.cards)
        if (suit1 == suit2):    num2 += num1
        self.cards.update((suit2, num2))
        if (suit2 == suit3):    num3 += num2
        if (suit1 == suit3):    num3 += num1
        self.cards.update((suit3, num3))
        print(self.cards)
        # Update probabilities:
        self.probs.update((k,choose(k,self.cards)) \
                                for k,v in self.probs.items())
        highCardOdds = 100 - sum(list(self.probs.values())[1:-1])
        self.probabilities[' 1. High Card: '] = max(0, highCardOdds)
        plot_probabilities(self.probs)
    # Calculate probabilities after turn:
    def turn(self, turn_card):
        self.cards.update(turn_card)
        self.probs.update((k, choose(k, self.cards)) \
                            for k, v in self.probs.items())
        highCardOdds = 100 - sum(list(self.probs.values())[1:-1])
        self.probabilities[' 1. High Card: '] = max(0, highCardOdds)
        plot_probabilities(self.probabilities)
    # Calculate probabilities after river:
    def river(self, river_card):
        self.cards.update(river_card)
        self.probs.update((k, choose(k, self.cards)) \
                                for k, v in self.probs.items())
        highCardOdds = 100 - sum(list(self.probs.values())[1:-1])
        self.probs[' 1. High Card: '] = max(0, highCardOdds)
        plot_probabilities(self.probs)
# Test our code for some cards:
Odds = PokerOdds(); Odds.holeCards(); flopCard1 = Card('Clubs', '10')
flopCard2 = Card('Hearts', 'Jack'); flopCard3 = Card('Clubs', 'Queen')
Odds.flop(flopCard1, flopCard2, flopCard3)
turnCard = Card('Spades', 'King'); Odds.turn(turnCard)
riverCard = Card('Hearts', '10'); Odds.river(riverCard)
