from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from zappa.asynchronous import task

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://homepoor_userV2:I3f@NPtdCo1*%Y3kck5$@96.127.186.10/homepoor_v2'
db = SQLAlchemy(app)

class GiftCard(db.Model):
	__tablename__ = "gift_cards"
	card_number = db.Column(db.String(50), primary_key=True,  nullable=False)
	pin_code    = db.Column(db.String(50), nullable=False)
	owner_id    = db.Column(db.Integer   , nullable=False)

def gift_card_from_request(card):
	return GiftCard(
		card_number=card['cardNumber'], 
		pin_code=card['pinCode'], 
		owner_id=card['ownerId']
	)

@app.route("/")
def index():
	return "hello"

@task
def add_cards_to_database(chunks_of_cards):
	for card in chunks_of_cards:
		db.session.add(gift_card_from_request(card))
		db.session.commit()

@app.route("/add-gift-card", methods=["POST"])
def add():
	cards = request.get_json()
	chunks_of_cards = [cards[x:x+500] for x in range(0, len(cards), 100)]
	
	for smaller_chunk_of_cards in chunks_of_cards:
		add_cards_to_database(smaller_chunk_of_cards)	
	
	return {"success": True}


if __name__ == "__main__":
	app.run(debug=True)