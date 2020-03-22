# Game #Black_Jack
#

import random
import tkinter


# to input the card images in the GUI


def load_images(card_images):
    suits = ['heart', 'spade', 'diamond', 'club']
    face_cards = ['king', 'queen', 'jack']
    # file used as your version of tkinter is 8.6 we use png other wise if we have older version we have to use ppg
    extention = 'png'
#     each suits have to retrive from he card folder
    for suit in suits:
        # the suit for number cards
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(card, suit, extention)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # the suit for face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(card, suit, extention)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


# this function takesout the card from the deck
def deal_card(fram):
    next_card = deck.pop(0)
    # below line is add becoz to prevent from run out of cards
    deck.append(next_card)
    tkinter.Label(fram, image=next_card[1], relief='raised').pack(side="left")
    return next_card


def hand_card(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


# this function is for dealer_button
def deal_dealer():
    dealer_score = hand_card(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_fram))
        dealer_score = hand_card(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = hand_card(player_hand)
    if dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins")
    elif player_score > 21:
        result_text.set("Dealer wins")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("Match Draw no one wins")


# this function is for player_button
def deal_player():
    player_hand.append(deal_card(player_card_fram))
    player_score = hand_card(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")


def restart():
    global dealer_card_fram
    global player_card_fram
    global player_hand
    global dealer_hand
    dealer_card_fram.destroy()
    player_card_fram.destroy()
    dealer_card_fram = tkinter.Frame(card_fram, bg="green")
    dealer_card_fram.grid(row=0, column=1, sticky="ensw", rowspan=2)
    player_card_fram = tkinter.Frame(card_fram, bg="green")
    player_card_fram.grid(row=2, column=1, sticky="ensw", rowspan=2)

    result_text.set("")

    dealer_hand = []
    player_hand = []
    deal_player()
    dealer_hand.append(deal_card(dealer_card_fram))
    dealer_score_label.set(hand_card(dealer_hand))
    deal_player()


root = tkinter.Tk()
root.title("Black Jack")
root.geometry("600x400")
root.configure(bg="green")

# Result (who is winner)
result_text = tkinter.StringVar()                                       # .stringvar() function help to take the outcome
result = tkinter.Label(root, textvariable=result_text, fg="white", bg="green")
result.grid(row=0, column=0, columnspan=3)

# Fram of the game
card_fram = tkinter.Frame(root, bg="green", relief="raised", border=3)
card_fram.grid(row=1, column=0, rowspan=2, columnspan=3, sticky="nsew")

# setting the score of the dealer
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_fram, text="Dealer", bg="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_fram, textvariable=dealer_score_label, bg="green", fg="white").grid(row=1, column=0)

# Fram of the dealer cards
dealer_card_fram = tkinter.Frame(card_fram, bg="green")
dealer_card_fram.grid(row=0, column=1, sticky="ensw", rowspan=2)

# setting the score of the player
player_score_label = tkinter.IntVar()
tkinter.Label(card_fram, text="Player", bg="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_fram, textvariable=player_score_label, bg="green", fg="white").grid(row=3, column=0)

# Frame of the player cards
player_card_fram = tkinter.Frame(card_fram, bg="green")
player_card_fram.grid(row=2, column=1, sticky="ensw", rowspan=2)

# buttons for the dealer and player
button_fram = tkinter.Frame(root)
button_fram.grid(row=3, column=0, columnspan=3, sticky="w")

button_dealer = tkinter.Button(button_fram, text="Dealer", command=deal_dealer)
button_dealer.grid(row=0, column=0, sticky="e")

button_player = tkinter.Button(button_fram, text="player", command=deal_player)
button_player.grid(row=0, column=1, sticky="w")


# restart button
button_restart = tkinter.Button(root, relief="raised", borderwidth=3, text="Restart", command=restart)
button_restart.grid(row=4, column=4, sticky="ew")

# loading cards
cards = []
load_images(cards)


# making a list to shuffel the deck of cards
deck = list(cards)
random.shuffle(deck)

# cards in the hands of the dealer and player
dealer_hand = []
player_hand = []

restart()
# deal_player()
# dealer_hand.append(deal_card(dealer_card_fram))
# dealer_score_label.set(hand_card(dealer_hand))
# deal_player()

tkinter.mainloop()
