#Imports
from random import shuffle

#Variables
game = True
cards = {"KoS":10,"QoS":10,"JoS":10,"10oS":10,
        "9oS":9,"8oS":8,"7oS":7,"6oS":6,"5oS":5,"4oS":4,"3oS":3,"2oS":2,"AoS":1,
        "KoH":10,"QoH":10,"JoH":10,"10oH":10,
        "9oH":9,"8oH":8,"7oH":7,"6oH":6,"5oH":5,"4oH":4,"3oH":3,"2oH":2,"AoH":1,
        "KoC":10,"QoC":10,"JoC":10,"10oC":10,
        "9oC":9,"8oC":8,"7oC":7,"6oC":6,"5oC":5,"4oC":4,"3oC":3,"2oC":2,"AoC":1,
        "KoD":10,"QoD":10,"JoD":10,"10oD":10,
        "9oD":9,"8oD":8,"7oD":7,"6oD":6,"5oD":5,"4oD":4,"3oD":3,"2oD":2,"AoD":1}
players_stay = []

#Fonctions
class Player(object):
    def __init__(self, player_num, player_name):
        self.player_num = player_num
        self.hand = [ ]
        self.score = 0
        self.name = player_name
        self.ingame = True
        self.eliminer = False

    def stay(self):
        InGame = False
        players_stay.append([self,self.score])


    def card(self):

        carte = deck.pop()
        self.hand.append(carte)
        self.score = self.score + cards[carte]
        if self.score > 21:
            self.ingame = False
            self.eliminer = True
        print(self.hand, self.score)

class House(object):
    def __init__(self, list_player):
        self.ingame = list_player
        self.card_deck = cards
        self.hand = []

    def Start_game(self):
        global deck
        game = True
        deck = [c for c in cards.keys()]
        shuffle(deck)

    def card(self):
        carte = deck.pop()
        self.hand.append(carte)
        b = 0
        for i in range(len(self.hand)):
            a = cards[i]
            b = b + a
        if b >= 17 :
            game = False

    def Check(self):
        if len(self.ingame) != len(players_stay):
            print("Il y a encore des joueurs")
        else:
            print("le jeu est terminer")
            print("Le gagnant est:")
            if len(players_stay) != 1:
                a = [players_stay[i][1] for i in range(len(players_stay)) if players_stay[i][0].eliminer == False]
                p = max(a)
                for i in range(len(players_stay)):
                    if players_stay[i][1] == p:
                        b = players_stay[i][0]
                print("joueur ", b.player_num, " avec ", p, " points")
            else:
                b = players_stay[0][0]
                print("joueur ",b.plyer_num," avec ", players_stay[0][1], " points")



#Game
#Initialisation des joueurs
nb_joueur = int(input("combien de joueur? Maximum 5 joueur "))
if nb_joueur == 1:
    j1 = Player(1,input("Quel est votre nom? "))
    Banque = House([j1.name])

if nb_joueur == 2:
    j1 = Player(1,input("Quel est votre nom joueur 1? "))
    j2 = Player(2,input("Quel est votre nom joueur 2? "))
    Banque = House([j1.name,j2.name])

if nb_joueur == 3:
    j1 = Player(1,input("Quel est votre nom joueur 1? "))
    j2 = Player(2,input("Quel est votre nom joueur 2? "))
    j3 = Player(3,input("Quel est votre nom joueur 3? "))
    Banque = House([j1.name,j2.name,j3.name])

if nb_joueur == 4:
    j1 = Player(1,input("Quel est votre nom joueur 1? "))
    j2 = Player(2,input("Quel est votre nom joueur 2? "))
    j3 = Player(3,input("Quel est votre nom joueur 3? "))
    j4 = Player(4,input("Quel est votre nom joueur 4? "))
    Banque = House([j1.name,j2.name,j3.name,j4.name])

if nb_joueur == 5:
    j1 = Player(1,input("Quel est votre nom joueur 1? "))
    j2 = Player(2,input("Quel est votre nom joueur 2? "))
    j3 = Player(3,input("Quel est votre nom joueur 3? "))
    j4 = Player(4,input("Quel est votre nom joueur 4? "))
    j5 = Player(5,input("Quel est votre nom joueur 5? "))
    Banque = House([j1.name,j2.name,j3.name,j4.name,j5.name])

Banque.Start_game()
while len(Banque.ingame) != len(players_stay):
    print("0 - Prendre une carte?")
    print("1 - Rester?")

    if len(Banque.ingame) == 1:
        for i in range(len(Banque.ingame) +1):
            if i == j1.player_num:
                choice = int(input("Que voulez vous faire ?"+  str(j1.name)))
                if choice == 0:
                    j1.card()
                else:
                    j1.stay()

    if len(Banque.ingame) == 2:
        for i in range(len(Banque.ingame) +1):
            if i == j1.player_num:
                choice = int(input("Que voulez vous faire ?"+  str(j1.name)))
                if choice == 0:
                    j1.card()
                else:
                    j1.stay()

            if i == j2.player_num:
                choice = int(input("Que voulez vous faire " +  str( j2.name)))
                if choice == 0:
                    j2.card()
                else:
                    j2.stay()

    if len(Banque.ingame) == 3:
        for i in range(len(Banque.ingame) +1):
            if i == j1.player_num:
                choice = int(input("Que voulez vous faire ?"+  str(j1.name)))
                if choice == 0:
                    j1.card()
                else:
                    j1.stay()

            if i == j2.player_num:
                choice = int(input("Que voulez vous faire " +  str( j2.name)))
                if choice == 0:
                    j2.card()
                else:
                    j2.stay()

            if i == j3.player_num:
                choice = int(input("Que voulez vous faire ?" + str( j3.name)))
                if choice == 0:
                    j3.card()
                else:
                    j3.stay()

    if len(Banque.ingame) == 4:
        for i in range(len(Banque.ingame) +1):
            if i == j1.player_num:
                choice = int(input("Que voulez vous faire ?"+  str(j1.name)))
                if choice == 0:
                    j1.card()
                else:
                    j1.stay()

            if i == j2.player_num:
                choice = int(input("Que voulez vous faire " +  str( j2.name)))
                if choice == 0:
                    j2.card()
                else:
                    j2.stay()

            if i == j3.player_num:
                choice = int(input("Que voulez vous faire ?" + str( j3.name)))
                if choice == 0:
                    j3.card()
                else:
                    j3.stay()

            if i == j4.player_num:
                choice = int(input("Que voulez vous faire ?"+ str( j4.name)))
                if choice == 0:
                    j4.card()
                else:
                    j4.stay()

    if len(Banque.ingame) == 5:
        for i in range(len(Banque.ingame) +1):
            if i == j1.player_num:
                choice = int(input("Que voulez vous faire ?"+  str(j1.name)))
                if choice == 0:
                    j1.card()
                else:
                    j1.stay()

            if i == j2.player_num:
                choice = int(input("Que voulez vous faire " +  str( j2.name)))
                if choice == 0:
                    j2.card()
                else:
                    j2.stay()

            if i == j3.player_num:
                choice = int(input("Que voulez vous faire ?" + str( j3.name)))
                if choice == 0:
                    j3.card()
                else:
                    j3.stay()

            if i == j4.player_num:
                choice = int(input("Que voulez vous faire ?"+ str( j4.name)))
                if choice == 0:
                    j4.card()
                else:
                    j4.stay()

            if i == j5.player_num:
                choice = int(input("Que voulez vous faire ?"+ str(j5.name)))
                if choice == 0:
                    j5.card()
                else:
                    j5.stay()
Banque.Check()
