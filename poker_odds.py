from os import system, path; import matplotlib.pyplot as plt, tkinter as t
main = t.Tk(); main.title("Poker Odds:"); main.geometry("800x600")
canvas = t.Canvas(main, width=600, height=400, bg="white")
canvas.pack(pady=20); circle = canvas.create_oval(300, 200, 320, 220)
def left(event):    canvas.move(circle, -10, 0)
def right(event):    canvas.move(circle, 10, 0)
def up(event):    canvas.move(circle, 0, -10)
def down(event):    canvas.move(circle, 0, 10)
def letter(event):
    x = -10 if event.char == "s" else (10 if event.char == "d" else 0)
    y = -10 if event.char == "e" else (10 if event.char == "x" else 0)
    canvas.move(circle, x, y)
main.bind("<Key>", letter); main.bind("<Left>", left)
main.bind("<Right>", right); main.bind("<Up>", up); main.bind("<Down>", down)
main.mainloop(); totalCombos = 51 * 50 * 49 * 48 * 47 * 46
def high_card(cards):
    return total(cards)
def pair(cards):
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
    match key:
        case [" 1. High Card: "]:    return high_card(cards)
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
def plot_probabilities(probs, title):
    hands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; L=""
    ax=plt.subplots(1,1,num=title,figsize=(10,10))[1]
    for k,v in probs.items(): L+=k+str(round(v,4))+"\n"
    ax.set_xticks(hands); ax.set_yscale("log")
    ax.plot(hands,list(probs.values())[:-1],label=L)
    ax.scatter(hands,list(probs.values())[:-1]); s=12
    ax.set_xlabel("Poker Hand",fontsize=s); ax.legend(fontsize=s)
    ax.set_ylabel("Probability",fontsize=s);ax.tick_params("both",labelsize=s)
    ax.set_title("Probabilities in Percent (%):", fontsize=s+0.00); plt.show()
class PokerOdds:
    def __init__(self):
        self.cards = []; self.probs = { " 1. High Card: ": totalCombos,\
                       " 2. Pair: ": 3 * 48 * 44 * 40 * 36 * 32,\
                       " 3. Two (2) Pair: ": 3 * 48 * 3 * 44 * 40 * 36,\
                       " 4. Three (3) of a Kind: ":3 * 2 * 48 * 44 * 40 * 36,\
                       " 5. Straight: ": 8 * 16 * 16 * 25 * 32 * 28,\
                       " 6. Flush: ": 12 * 11 * 10 * 9 * 32 * 28,\
                       " 7. Full House: ": 3 * 2 * 48 * 3 * 44 * 40,\
                       " 8. Four (4) of a Kind: ": 3 * 2 * 1 * 48 * 44 * 40,\
                       " 9. Straight Flush: ": 2 * 2 * 2 * 25 * 32 * 28,\
                       "10. Royal Flush: ": 24*32*28,"Total: ": totalCombos }
    def holeCards(self):
        self.probs.update((k,100*v/totalCombos) for k,v in self.probs.items())
        self.probs[" 1. High Card: "] -= sum(list(self.probs.values())[1:-1])
        plot_probabilities(self.probs, "Probabilities with Hole Cards:")
    def flop(self, flop_cards):
        self.cards += flop_cards; self.calc("Probabilities with Flop Cards:")
    def turn(self, turn_card):
        self.cards += [turn_card]; self.calc("Probabilities with Turn Card:")
    def river(self, river_card):
        self.cards += [river_card]; self.calc("Probablities with River Card")
    def calc(self, title):
        self.probs.update((k,pick(k,self.cards))for k,v in self.probs.items())
        self.probs[" 1. High Card: "] -= sum(list(self.probs.values())[1:-1])
        plot_probabilities(self.probs, title)
Odds = PokerOdds(); Odds.holeCards(); flopCard1 = ("Clubs", "10")
flopCard2 = ("Hearts", "Jack"); flopCard3 = ("Clubs", "Queen")
Odds.flop([flopCard1, flopCard2, flopCard3]); turnCard = ("Spades", "King")
Odds.turn(turnCard); riverCard = ("Hearts", "10"); Odds.river(riverCard)
system( 'rmdir /s /q "' + path.expanduser('~') + '\.matplotlib"' )
