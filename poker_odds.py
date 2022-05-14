def addCard():
  if (suit.get(), num.get()) in Odds.cards:
   updateActionTo(action["text"]+"\nPlease add a different card than before.")
  else:
    Odds.cards+=[(suit.get(),num.get())]; number=len(Odds.cards)
    if number==1: updateActionTo("Please add 2 more flop cards.")
    elif number==2: updateActionTo("Please add 1 more flop card.")
    elif number==3: flop(); updateActionTo("Please add a turn card.")
    elif number==4: turn(); updateActionTo("Please add a river card.")
    elif number==5: top(False); Odds.calculateAndPlot("River Card:"); end()
def flop():   top(False); Odds.calculateAndPlot("Flop Cards:"); top(True)
def turn():    top(False); Odds.calculateAndPlot("Turn Card:"); top(True)
def top(toggle):  win.attributes("-topmost", toggle)
def end():
  updateActionTo("Do you want to play another game?"); top(True); t="text"
  endButton[t]="No"; addButton["text"]="Yes"; addButton["command"] = reset
def reset():
  updateActionTo(""); Odds.__init__(); endButton["text"] = "Quit"
  addButton["text"] = "Start Hole Cards"; addButton["command"] = start
def updateActionTo(text):
  action["text"]=text; action["font"]=('Verdana',30); action["fg"]="blue"
def highCard(cards):
  sameSuit = Odds.sameSuits[-1] if Odds.sameSuits else 0
  sameNum = Odds.sameNums[-1] if Odds.sameNums else 0
  indexes=sorted([numbers.index(num) for num in [card[1] for card in cards]])
  isStraight = ( [index-indexes[0] for index in indexes] == [0,1,2,3,4] )
  return 10**(-6) if (sameSuit == 5 or sameNum > 1 or isStraight) else 100
def pair(key, cards):
  sameNum = Odds.sameNums[-1] if Odds.sameNums else 0
  return 100 if(sameNum==2) else (10**(-6) if(sameNum>2) else Odds.probs[key])
def twoPair(key, cards):
  sameNums = [0,0] if (Odds.sameNums == []) else Odds.sameNums[-2:]
  return 100 if (sameNums == [2,2]) else (10**(-6) if \
          (sameNums[0] > 2 or sameNums[1] > 2) else Odds.probs[key])
def threeOfAkind(key, cards):
  sameNum = Odds.sameNums[-1] if Odds.sameNums else 0
  return 100 if(sameNum==3) else (10**(-6) if(sameNum>3) else Odds.probs[key])
def straight(key, cards):
  indexes=sorted([numbers.index(num) for num in [card[1] for card in cards]])
  isStraight = ( [index-indexes[0] for index in indexes] == [0,1,2,3,4] )
  sameSuit = Odds.sameSuits[-1] if Odds.sameSuits else 0
  return 10**(-6) if(sameSuit==5)else (100 if isStraight else Odds.probs[key])
def flush(key, cards):
  indexes=sorted([numbers.index(num) for num in [card[1] for card in cards]])
  isStraight = ( [index-indexes[0] for index in indexes] == [0,1,2,3,4] )
  sameSuit = Odds.sameSuits[-1] if Odds.sameSuits else 0
  return 10**(-6) if (sameSuit==5 and isStraight) else 100 \
                                    if (sameSuit==5) else Odds.probs[key]
def fullHouse(key, cards):
  sameNums = [0,0] if (Odds.sameNums == []) else Odds.sameNums[-2:]
  return 100 if (sameNums == [2,3]) else (10**(-6) if \
          (sameNums[0] > 2 or sameNums[1] > 3) else Odds.probs[key])
def fourOfAkind(key, cards):
  sameNum = Odds.sameNums[-1] if Odds.sameNums else 0
  return 100 if (sameNum == 4) else Odds.probs[key]
def straightFlush(key, cards):
  royal="King"in[card[1]for card in cards]and"Ace"in[card[1]for card in cards]
  indexes=sorted([numbers.index(num) for num in [card[1] for card in cards]])
  isStraight = ( [index-indexes[0] for index in indexes] == [0,1,2,3,4] )
  sameSuit = Odds.sameSuits[-1] if Odds.sameSuits else 0; curr=Odds.probs[key]
  return 10**(-6) if royal else 100 if (sameSuit==5 and isStraight) else curr
def royalFlush(key, cards):
  royal="King"in[card[1]for card in cards]and"Ace"in[card[1]for card in cards]
  indexes=sorted([numbers.index(num) for num in [card[1] for card in cards]])
  isStraight = ( [index-indexes[0] for index in indexes] == [0,1,2,3,4] )
  sameSuit = Odds.sameSuits[-1] if Odds.sameSuits else 0
  return 100 if (sameSuit == 5 and isStraight and royal) else Odds.probs[key]
def total(cards): return 100
def pick(key, cards):
  if (key == " 1. High Card: "):    return highCard(cards)
  if (key == " 2. Pair: "):    return pair(key, cards)
  if (key == " 3. Two (2) Pair: "):    return twoPair(key, cards)
  if (key == " 4. Three (3) of a Kind: "):    return threeOfAkind(key,cards)
  if (key == " 5. Straight: "):    return straight(key, cards)
  if (key == " 6. Flush: "):    return flush(key, cards)
  if (key == " 7. Full House: "):    return fullHouse(key, cards)
  if (key == " 8. Four (4) of a Kind: "):    return fourOfAkind(key, cards)
  if (key == " 9. Straight Flush: "):    return straightFlush(key, cards)
  if (key == "10. Royal Flush: "):    return royalFlush(key, cards)
  if (key == "Total: "):    return total(cards)
class PokerOdds:
  def __init__(self):
    self.probs = { " 1. High Card: ": tot, " 2. Pair: ": 3 * 48 * 44 * \
        40 * 36 * 32, " 3. Two (2) Pair: ": 3 * 48 * 3 * 44 * 40 * 36, \
        " 4. Three (3) of a Kind: ": 6 * 48 * 44 * 40 * 36, " 5. St" + \
        "raight: ": 8 * 16 * 16 * 25 * 32 * 28, " 6. Flush: ": 12 * 11 \
        * 10 * 9 * 32 * 28, " 7. Full House: ": 3 * 2 * 48 * 3 * 44 * \
        40, " 8. Four (4) of a Kind: ": 3 * 2 * 1 * 48 * 44 * 40, \
        " 9. Straight Flush: ": 2 * 2 * 2 * 25 * 32 * 28, \
        "10. Royal Flush: ": 24 * 32 * 28, "Total: ": tot }
    self.probs.update((k, 100*v/tot) for k, v in self.probs.items())
    self.sameSuits=[]; self.sameNums=[]; self.cards=[]
  def calculateAndPlot(self, partOfRound):
    self.sameSuits=sorted([[c[0]for c in self.cards].count(s)for s in suits])
    self.sameNums=sorted([[c[1]for c in self.cards].count(n)for n in numbers])
    self.probs.update((k,pick(k,self.cards))for k,v in self.probs.items())
    self.probs[" 1. High Card: "] -= sum(list(self.probs.values())[1:-1])
    self.probs[" 1. High Card: "]=max(10**(-6),self.probs[" 1. High Card: "])
    y=list(self.probs.values())[:-1]; ax=plt.subplots(1,num="Poker Odds")[1]
    hands=[1,2,3,4,5,6,7,8,9,10]; ax.set_xticks(hands); ax.set_yscale("log")
    ax.scatter(hands, y); legend=""; ax.set_xlabel("Poker Hand",fontsize=8)
    for k,v in self.probs.items():  legend+=k+str(round(v,4))+"%\n"
    ax.plot(hands, y, label=legend[:-1]); ax.legend(fontsize=8)
    plt.get_current_fig_manager().window.setGeometry(0, 25, 1500, 480)
    plt.get_current_fig_manager().window.setWindowIcon(PyQt5.QtGui.QIcon(i))
    ax.set_ylabel("Probability",fontsize=8);ax.tick_params("both",labelsize=8)
    ax.set_title("Probabilities with "+partOfRound,fontsize=8+0.0); plt.show()
def start():
  updateActionTo("Please add 3 flop cards.");addButton["command"]=addCard;top\
  (F);Odds.calculateAndPlot("Hole Cards:");addButton["text"]="Add Card";top(T)
from tkinter import *; tot=51*50*49*48*47*46;win=Tk();import PyQt5; win.lift()
action = Label(win,text=""); suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
i="C:\\Users\David Colby\OneDrive\Documents\Tasks\Setup\Windows Software"+\
"\Poker Odds\Cards.ico";suit=StringVar();num=StringVar();win.option_add(\
"*Font",('Verdana',30)); addButton = Button(win,text="Start Hole Cards",\
command=start,fg="blue");win.iconbitmap(i);addButton.pack();action.pack()
top(True);win.title("Poker Odds:"); numbers=["2","3","4","5","6","7",\
"8","9","10","Jack","Queen","King","Ace"];endButton=Button(win,text=\
"Quit",command=win.quit,fg="red");Odds=PokerOdds();suit.set(suits[0])
import matplotlib, matplotlib.pyplot as plt; matplotlib.use("Qt5Agg")
Label(win, text="Suit:", fg="blue").pack(); num.set(numbers[0])
suitMenu=OptionMenu(win,suit,*suits); suitMenu.config(fg="green",\
activeforeground="black");suitMenu.pack();numMenu=OptionMenu(win,num,*numbers)
numMenu["menu"].config(fg="green",activeforeground="black");suitMenu["menu"].\
config(fg="green",activeforeground="black");numMenu.config(fg="green",\
activeforeground="black"); Label(win,text="Number",fg="blue").pack()
numMenu.pack(); endButton.pack(); T=True; F=False; win.mainloop()
