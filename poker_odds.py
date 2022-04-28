import os, matplotlib.pyplot as plt; from tkinter import *
main = Tk(); main.lift(); main.attributes("-topmost", True)
main.title( "Poker Odds:" ); main.geometry( "900x450" ); f = 10
main.iconbitmap("C:\Program Files\Microsoft Games\Solitaire\Solitaire.exe")
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
def show(): Label(main, text=suit.get()).pack()
suit = StringVar(); suit.set(suits[0]); OptionMenu(main, suit, *suits).pack()
Button(main, text="Suit:", command=show).pack()
import matplotlib; matplotlib.use("Qt5Agg"); main.mainloop(); t = 1296681120
def high_card(cards):
    return total(cards)
def pair(cards):
    numbers = [card[1] for card in cards]
    for index, number in enumerate(numbers):
        if (index >= 1 and number in numbers[:index-1]):   return 100
    return 0
def two_pair(cards):
    return 0
def three_of_a_kind(cards):
    return 0
def straight(cards):
    return 0
def flush(cards):
    return 0
def full_house(cards):
    return 0
def four_of_a_kind(cards):
    return 0
def straight_flush(cards):
    return 0
def royal_flush(cards):
    return 0
def total(cards):
    return 100
def pick(key, cards):
    if (key == " 1. High Card: "):    return high_card(cards)
    if (key == " 2. Pair: "):    return pair(cards)
    if (key == " 3. Two (2) Pair: "):    return two_pair(cards)
    if (key == " 4. Three (3) of a Kind: "):    return three_of_a_kind(cards)
    if (key == " 5. Straight: "):    return straight(cards)
    if (key == " 6. Flush: "):    return flush(cards)
    if (key == " 7. Full House: "):    return full_house(cards)
    if (key == " 8. Four (4) of a Kind: "):    return four_of_a_kind(cards)
    if (key == " 9. Straight Flush: "):    return straight_flush(cards)
    if (key == "10. Royal Flush: "):    return royal_flush(cards)
    if (key == "Total: "):    return total(cards)
def plot_probabilities(probs, part):
    hands=[1,2,3,4,5,6,7,8,9,10]; L=""
    ax=plt.subplots(1,1,num="Poker Odds")[1]
    ax.set_xticks(hands); ax.set_yscale("log")
    ax.scatter(hands, list(probs.values())[:-1])
    for k,v in probs.items(): L+=k+str(round(v,4))+"%\n"
    ax.plot(hands, list(probs.values())[:-1], label=L[:-1])
    ax.set_xlabel("Poker Hand",fontsize=f); ax.legend(fontsize=f)
    plt.get_current_fig_manager().window.setGeometry(0,25,1500,480)
    ax.set_ylabel("Probability",fontsize=f);ax.tick_params("both",labelsize=f)
    ax.set_title("Probabilities with " + part, fontsize=f+0.0000); plt.show()
    os.system( 'rmdir /s /q "' + os.path.expanduser('~') + '\.matplotlib"' )
class PokerOdds:
    def __init__(self):
        self.cards = []; self.probs = { " 1. High Card: ": t,\
                       " 2. Pair: ": 3 * 48 * 44 * 40 * 36 * 32,\
                       " 3. Two (2) Pair: ": 3 * 48 * 3 * 44 * 40 * 36,\
                       " 4. Three (3) of a Kind: ": 6 * 48 * 44 * 40 * 36,\
                       " 5. Straight: ": 8 * 16 * 16 * 25 * 32 * 28,\
                       " 6. Flush: ": 12 * 11 * 10 * 9 * 32 * 28,\
                       " 7. Full House: ": 3 * 2 * 48 * 3 * 44 * 40,\
                       " 8. Four (4) of a Kind: ": 3 * 2 * 1 * 48 * 44 * 40,\
                       " 9. Straight Flush: ": 2 * 2 * 2 * 25 * 32 * 28,\
                       "10. Royal Flush: ": 2 * 2 * 6 * 32 * 28, "Total: ": t}
    def holeCards(self):
        self.probs.update((k,100*v/t) for k,v in self.probs.items())
        self.probs[" 1. High Card: "] -= sum(list(self.probs.values())[1:-1])
        plot_probabilities(self.probs, "Hole Cards:")
    def flop(self, flop_cards):
        self.cards += flop_cards; self.calc("Flop Cards:")
    def turn(self, turn_card):
        self.cards += [turn_card]; self.calc("Turn Card:")
    def river(self, river_card):
        self.cards += [river_card]; self.calc("River Card")
    def calc(self, part):
        self.probs.update((k,pick(k,self.cards))for k,v in self.probs.items())
        self.probs[" 1. High Card: "] -= sum(list(self.probs.values())[1:-1])
        self.probs[" 1. High Card: "] = max(0, self.probs[" 1. High Card: "])
        plot_probabilities(self.probs, part)
Odds = PokerOdds(); Odds.holeCards(); flopCard1 = ("Clubs", "10")
flopCard2 = ("Hearts", "Jack"); flopCard3 = ("Clubs", "Queen")
Odds.flop([flopCard1, flopCard2, flopCard3]); turnCard = ("Spades", "King")
Odds.turn(turnCard); riverCard = ("Hearts", "10"); Odds.river(riverCard)
