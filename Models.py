from init import db
from datetime import datetime

class GiftCard(db.Model):
	__tablename__ = "gift_cards"
	card_number = db.Column(db.String(50), primary_key=True,  nullable=False)
	pin_code    = db.Column(db.String(50), nullable=False)
	owner_id    = db.Column(db.Integer   , nullable=False)

	def __repr__(self):
		return str({
			'card_number' : self.card_number, 
			'pin_code'    : self.pin_code,
			'owner_id'    : str(self.owner_id)
		})