import os, matplotlib.pyplot as plt; from tkinter import *
import matplotlib; matplotlib.use("Qt5Agg"); tot=51*50*49*48*47*46; cards=[]
def addCard():
    cards += [(suit.get(), num.get())]
    if len(cards) ==  3:  Odds.calculate("Flop Cards:")
    elif len(cards) == 4: Odds.calculate("Turn Card:")
    elif len(cards) == 5: Odds.calculate("River Card:"); cards = []; end()
    else:  action = Label(window, text="Please add another flop card.").pack()
def end():
    action = Label(window, text="Do you want to play another game?").pack()
    addCardButton = Button(window, text="Yes", command=reset)
    endButton = Button(window, text="No", command=os.exit)
def reset(): action = Label(window, text="Please add another flop card.").pack()
def highCard(cards):   return total(cards)
def pair(cards):
    numbers = [card[1] for card in cards]
    for index, number in enumerate(numbers):
        if (index >= 1 and number in numbers[:index-1]):   return 100
    return 0
def twoPair(cards):
    return 0
def threeOfAkind(cards):
    return 0
def straight(cards):
    return 0
def flush(cards):
    return 0
def fullHouse(cards):
    return 0
def fourOfAkind(cards):
    return 0
def straightFlush(cards):
    return 0
def royalFlush(cards):
    return 0
def total(cards):
    return 100
def pick(key, cards):
    if (key == " 1. High Card: "):    return highCard(cards)
    if (key == " 2. Pair: "):    return pair(cards)
    if (key == " 3. Two (2) Pair: "):    return twoPair(cards)
    if (key == " 4. Three (3) of a Kind: "):    return threeOfAkind(cards)
    if (key == " 5. Straight: "):    return straight(cards)
    if (key == " 6. Flush: "):    return flush(cards)
    if (key == " 7. Full House: "):    return fullHouse(cards)
    if (key == " 8. Four (4) of a Kind: "):    return fourOfAkind(cards)
    if (key == " 9. Straight Flush: "):    return straightFlush(cards)
    if (key == "10. Royal Flush: "):    return royalFlush(cards)
    if (key == "Total: "):    return total(cards)
def plotProbabilities(probs, part):
    hands=[1,2,3,4,5,6,7,8,9,10]; L=""
    ax=plt.subplots(1,1,num="Poker Odds")[1]
    ax.set_xticks(hands); ax.set_yscale("log")
    ax.scatter(hands, list(probs.values())[:-1])
    for k,v in probs.items(): L+=k+str(round(v,4))+"%\n"
    ax.plot(hands, list(probs.values())[:-1], label=L[:-1])
    ax.set_xlabel("Poker Hand",fontsize=f); ax.legend(fontsize=f)
    plt.get_current_fig_manager().window.setGeometry(0, 25, 1500, 480)
    ax.set_ylabel("Probability",fontsize=f);ax.tick_params("both",labelsize=f)
    ax.set_title("Probabilities with " + part, fontsize=f + 0.000); plt.show()
    os.system( ' rmdir /s /q "' + os.path.expanduser('~') + '\.matplotlib" ' )
class PokerOdds:
    def __init__(self):
        self.probs = { " 1. High Card: ": tot, \
                       " 2. Pair: ": 3 * 48 * 44 * 40 * 36 * 32, \
                       " 3. Two (2) Pair: ": 3 * 48 * 3 * 44 * 40 * 36, \
                       " 4. Three (3) of a Kind: ": 6 * 48 * 44 * 40 * 36, \
                       " 5. Straight: ": 8 * 16 * 16 * 25 * 32 * 28, \
                       " 6. Flush: ": 12 * 11 * 10 * 9 * 32 * 28, \
                       " 7. Full House: ": 3 * 2 * 48 * 3 * 44 * 40, \
                       " 8. Four (4) of a Kind: ": 3 * 2 * 1 * 48 * 44 * 40, \
                       " 9. Straight Flush: ": 2 * 2 * 2 * 25 * 32 * 28, \
                       "10. Royal Flush: ": 24 * 32 * 28, "Total: ": tot }
        self.calculate("Hole Cards:")
    def calculate(self, part):
        self.probs.update((k,  100*v / tot) for k, v in self.probs.items())
        self.probs.update((k,  pick(k, cards))for k,v in self.probs.items())
        self.probs[" 1. High Card: "] -= sum(list(self.probs.values())[1:-1])
        self.probs[" 1. High Card: "] = max(0, self.probs[" 1. High Card: "])
        plotProbabilities(self.probs, part)
window = Tk(); window.lift(); window.attributes("-topmost", True)
window.title( "Poker Odds:" ); window.geometry( "900x450" ); f = 10
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]; Odds = PokerOdds()
window.iconbitmap("C:\Program Files\Microsoft Games\Multiplayer\Spades\shvlzm.exe")
suit=StringVar(); suit.set(suits[0]);  OptionMenu(window, suit, *suits).pack()
numbers = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
num=StringVar(); num.set(numbers[0]); OptionMenu(window,num,*numbers).pack()
addCardButton = Button(window,text="Add Card:",command=addCard); window.mainloop()