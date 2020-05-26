from celery_app import add_cards_to_database
from flask import request
from init import app

@app.route("/add-gift-card", methods=["POST"])
def add():
	cards = request.get_json()
	chunks_of_cards = [cards[x:x+500] for x in range(0, len(cards), 100)]
	for smaller_chunk_of_cards in chunks_of_cards:
		print("Adding card")
		add_cards_to_database.delay(smaller_chunk_of_cards)

	return {"success": True}

if __name__ == "__main__":
	app.run()
