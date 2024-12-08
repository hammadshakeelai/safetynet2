spades_cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
clubs_cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
daimonds_cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
hearts_cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
import random
color=random.randint(0,1)
if color==0:#red
    flavour=random.randint(0,1)
    if flavour==0:
        card=random.choice(spades_cards)
        Type='spades_cards'
    else:
        card=random.choice(clubs_cards)
        Type='clubs_cards'

else:#black
    flavour=random.randint(0,1)
    if flavour==0:
        card=random.choice(daimonds_cards)
        Type='daimonds_cards'

    else:
        card=random.choice(hearts_cards)
        Type='hearts_cards'

print(card+" of "+Type)

