
from celery import Celery

celery_app = Celery('gift_card_uploader', broker='pyamqp://guest@localhost//')


from flask import request
from init import app, db
from homepoTools import (
	is_valid_homedepot_gift_card,
	commit, 
	remove_all_except_digits, 
	convert_from_request_to_gift_card
)

@celery_app.task
def add_cards_to_database(chunks_of_cards):
	for card in chunks_of_cards:
		card = convert_from_request_to_gift_card(card)
		if is_valid_homedepot_gift_card(card):
			commit(db, card)

@app.route("/add-gift-card", methods=["POST"])
def add():
	cards = request.get_json()
	chunks_of_cards = [cards[x:x+500] for x in range(0, len(cards), 100)]
	for smaller_chunk_of_cards in chunks_of_cards:
		add_cards_to_database(smaller_chunk_of_cards)

	return {"success": True}

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
