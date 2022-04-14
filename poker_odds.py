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
main.mainloop(); total = 51 * 50 * 49 * 48 * 47 * 46
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
def pick(key, cards):
    if (key == " 2. Pair: "):    return pair(cards)
    if (key == " 3. Two (2) Pair: "):    return two_pair(cards)
    if (key == " 4. Three (3) of a Kind: "):    return three_of_a_kind(cards)
    if (key == " 5. Straight: "):    return straight(cards)
    if (key == " 6. Flush: "):    return flush(cards)
    if (key == " 7. Full House: "):    return full_house(cards)
    if (key == " 8. Four (4) of a Kind: "):    return four_of_a_kind(cards)
    if (key == " 9. Straight Flush: "):    return straight_flush(cards)
    if (key == "10. Royal Flush: "):    return royal_flush(cards)
    return 100
def plot_probs(probs, title):
    ax = plt.subplots(1,1,num=title,figsize=(10,10))[1]
    hands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; legend = ""
    for k, v in probs.items():    legend += k+str(v)+"\n"
    ax.plot(hands, list(probs.values())[:-1], label=legend)
    ax.set_ylabel("Probability", fontsize=12); ax.legend(fontsize=12); s=12
    ax.set_xlabel("Poker Hand",fontsize=12);ax.tick_params("both",labelsize=s)
    ax.set_title("Probabilities in Percent (%):", fontsize=12); plt.show()
class PokerOdds:
    def __init__(self):
        self.cards = []; self.probs = { " 1. High Card: ": total, \
                       " 2. Pair: ": 3 * 48 * 44 * 40 * 36 * 32, \
                       " 3. Two (2) Pair: ": 3 * 48 * 3 * 44 * 40 * 36, \
                       " 4. Three (3) of a Kind: ":3 * 2 * 48 * 44 * 40 * 36,\
                       " 5. Straight: ": 8 * 16 * 16 * 25 * 32 * 28, \
                       " 6. Flush: ": 12 * 11 * 10 * 9 * 32 * 28, \
                       " 7. Full House: ": 3 * 2 * 48 * 3 * 44 * 40, \
                       " 8. Four (4) of a Kind: ": 3 * 2 * 1 * 48 * 44 * 40, \
                       " 9. Straight Flush: ": 2 * 2 * 2 * 25 * 32 * 28, \
                       "10. Royal Flush: ": 4*3*2*32*28, "Total: ": total }
    def holeCards(self):
        self.probs.update((k,100*v/total) for k,v in self.probs.items())
        self.probs[" 1. High Card: "] -= sum(list(self.probs.values())[1:-1])
        plot_probs(self.probs, "Poker Odds Hole Cards Plot:")
    def flop(self, flop_cards):
        self.cards+=flop_cards; self.calculate("Poker Odds Flop Cards Plot:")
    def turn(self, turn_card):
        self.cards+=[turn_card]; self.calculate("Poker Odds Turn Card Plot:")
    def river(self, river_card):
        self.cards+=[river_card]; self.calculate("Poker Odds River Card Plot")
    def calculate(self, title):
        self.probs.update((k,pick(k,self.cards))for k,v in self.probs.items())
        highCard = 100 - sum(list(self.probs.values())[1:-1])
        self.probs[" 1. High Card: "] = highCard; plot_probs(self.probs,title)
Odds = PokerOdds(); Odds.holeCards(); flopCard1 = ("Clubs", "10")
flopCard2 = ("Hearts", "Jack"); flopCard3 = ("Clubs", "Queen")
Odds.flop([flopCard1, flopCard2, flopCard3]); turnCard = ("Spades", "King")
Odds.turn(turnCard); riverCard = ("Hearts", "10"); Odds.river(riverCard)
system( 'rmdir /s /q "' + path.expanduser('~') + '\.matplotlib"' )
