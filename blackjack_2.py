from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
import random

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("blackjack.ui", self)
		self.setWindowTitle("BlackJack!") 
		

		# Define our widgets
		self.dealerCard1 = self.findChild(QLabel, "dealerCard1")
		self.dealerCard2 = self.findChild(QLabel, "dealerCard2")
		self.dealerCard3 = self.findChild(QLabel, "dealerCard3")
		self.dealerCard4 = self.findChild(QLabel, "dealerCard4")
		self.dealerCard5 = self.findChild(QLabel, "dealerCard5")
		
		self.playerCard1 = self.findChild(QLabel, "playerCard1")
		self.playerCard2 = self.findChild(QLabel, "playerCard2")
		self.playerCard3 = self.findChild(QLabel, "playerCard3")
		self.playerCard4 = self.findChild(QLabel, "playerCard4")
		self.playerCard5 = self.findChild(QLabel, "playerCard5")

		self.dealerHeaderLabel = self.findChild(QLabel, "dlabel")
		self.playerHeaderLabel = self.findChild(QLabel, "plabel")

		self.shuffleButton = self.findChild(QPushButton, "spushButton")
		self.hitMeButton = self.findChild(QPushButton, "hitMeButton")
		self.standButton = self.findChild(QPushButton, "standButton")


		# Shuffle Cards
		self.shuffle()

		# Click Buttons
		self.shuffleButton.clicked.connect(self.shuffle)
		self.hitMeButton.clicked.connect(self.playerHit)

		# Show The App
		self.show()
		

	# Check For Blackjack
	def blackjack_check(self, player):
		if player == "dealer":
			if len(self.dealer_score) == 2:
				if self.dealer_score[0] + self.dealer_score[1] == 21:
					# Winner message
					QMessageBox.about(self, "Dealer Wins!", "Blackjack!  Dealer Wins!")
					# Disable buttons
					self.hitMeButton.setEnabled(False)
					self.standButton.setEnabled(False)


		if player == "player":
			if len(self.player_score) == 2:
				if self.player_score[0] + self.player_score[1] == 21:
					# Winner message
					QMessageBox.about(self, "Player Wins!", "Blackjack!  Player Wins!")
					# Disable buttons
					self.hitMeButton.setEnabled(False)
					self.standButton.setEnabled(False)

	def shuffle(self):
		# Enable Buttons
		self.hitMeButton.setEnabled(True)
		self.standButton.setEnabled(True)
		
		# Reset Card Images
		pixmap = QPixmap('images/cards/green.png')
		self.dealerCard1.setPixmap(pixmap)
		self.dealerCard2.setPixmap(pixmap)
		self.dealerCard3.setPixmap(pixmap)
		self.dealerCard4.setPixmap(pixmap)
		self.dealerCard5.setPixmap(pixmap)
		
		self.playerCard1.setPixmap(pixmap)
		self.playerCard2.setPixmap(pixmap)
		self.playerCard3.setPixmap(pixmap)
		self.playerCard4.setPixmap(pixmap)
		self.playerCard5.setPixmap(pixmap)

		# Define Our Deck
		suits = ["diamonds", "clubs", "hearts", "spades"]
		values = range(2, 15)
		# 11 = Jack, 12=Queen, 13=King, 14=Ace

		# Create Deck
		#global deck
		self.deck = []

		for suit in suits:
			for value in values:
				self.deck.append(f"{value}_of_{suit}")
		
		# Create Our Players
		#global dealer, player
		self.dealer = []
		self.player = []
		self.dealer_score = []
		self.player_score = []
		self.playerSpot = 0
		self.dealerSpot = 0

		self.dealerHit()
		self.dealerHit()

		self.playerHit()
		self.playerHit()
		
	def dealCards(self):
		try:
			# Grab a random Card for Dealer
			card = random.choice(self.deck)
			# Remove That Card From The Deck
			self.deck.remove(card)
			# Add That Card To Dealers List
			self.dealer.append(card)
			#Output Card To Screen
			pixmap = QPixmap(f'images/cards/{card}.png')
			self.dealerCard1.setPixmap(pixmap)

			# Grab a random Card for Player
			card = random.choice(self.deck)
			# Remove That Card From The Deck
			self.deck.remove(card)
			# Add That Card To Dealers List
			self.player.append(card)
			#Output Card To Screen
			pixmap = QPixmap(f'images/cards/{card}.png')
			self.playerCard1.setPixmap(pixmap)

			# Update Titlebar
			self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

		except:
			self.setWindowTitle("Game Over")
			
	def dealerHit(self):
		if self.dealerSpot < 5:
			try:
				# Grab a random Card for Player
				card = random.choice(self.deck)
				# Remove That Card From The Deck
				self.deck.remove(card)
				# Add That Card To Dealers List
				self.dealer.append(card)

				# Add Card To Dealer Score
				self.dcard = int(card.split("_", 1)[0])
				if self.dcard == 14:
					self.dealer_score.append(11)
				elif self.dcard == 11 or self.dcard == 12 or self.dcard == 13:
					self.dealer_score.append(10)
				else:
					self.dealer_score.append(self.dcard)


				#Output Card To Screen
				pixmap = QPixmap(f'images/cards/{card}.png')
				
				if self.dealerSpot == 0:
					self.dealerCard1.setPixmap(pixmap)
					self.dealerSpot += 1
				
				elif self.dealerSpot == 1:
					self.dealerCard2.setPixmap(pixmap)
					self.dealerSpot += 1
				
				elif self.dealerSpot == 2:
					self.dealerCard3.setPixmap(pixmap)
					self.dealerSpot += 1

				elif self.dealerSpot == 3:
					self.dealerCard4.setPixmap(pixmap)
					self.dealerSpot += 1

				elif self.dealerSpot == 4:
					self.dealerCard5.setPixmap(pixmap)
					self.dealerSpot += 1

				# Update Titlebar
				self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

			except:
				self.setWindowTitle("Game Over")

			# Check for blackjack
			self.blackjack_check("dealer")

	def playerHit(self):
		if self.playerSpot < 5:
			try:
				# Grab a random Card for Player
				card = random.choice(self.deck)
				# Remove That Card From The Deck
				self.deck.remove(card)
				# Add That Card To Dealers List
				self.player.append(card)

				# Add Card To Player Score
				self.pcard = int(card.split("_", 1)[0])
				if self.pcard == 14:
					self.player_score.append(11)
				elif self.pcard == 11 or self.pcard == 12 or self.pcard == 13:
					self.player_score.append(10)
				else:
					self.player_score.append(self.pcard)


				#Output Card To Screen
				pixmap = QPixmap(f'images/cards/{card}.png')
				
				if self.playerSpot == 0:
					self.playerCard1.setPixmap(pixmap)
					self.playerSpot += 1
				
				elif self.playerSpot == 1:
					self.playerCard2.setPixmap(pixmap)
					self.playerSpot += 1
				
				elif self.playerSpot == 2:
					self.playerCard3.setPixmap(pixmap)
					self.playerSpot += 1

				elif self.playerSpot == 3:
					self.playerCard4.setPixmap(pixmap)
					self.playerSpot += 1

				elif self.playerSpot == 4:
					self.playerCard5.setPixmap(pixmap)
					self.playerSpot += 1

				# Update Titlebar
				self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

			except:
				self.setWindowTitle("Game Over")

			# Check For Blackjack
			self.blackjack_check("player")
	
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

