from Models import GiftCard
import re

expected_card_number_length = 23
expected_pin_code_length    = 4

def is_valid_homedepot_gift_card(card):
	actual_card_number_length = len(str(card.card_number))
	actual_pin_code_length    = len(str(card.pin_code))

	while len(str(card.pin_code)) < 4:
		card.pin_code = "0" + str(card.pin_code)

	print(f"expected {expected_card_number_length}, got {actual_card_number_length}")
	print(f"expected  {expected_pin_code_length}, got {actual_pin_code_length}")

	if expected_card_number_length == actual_card_number_length:
		if expected_pin_code_length == actual_pin_code_length:
			print("Card is valid")
			return True

	return False

def commit(db, card):
	try:
		db.session.add(card)
		db.session.commit()
		print("Sucessfully added card")
	except Exception as e:
		print(f"failed to add card. Error={e}")
		db.session.rollback()

def remove_all_except_digits(string):
	return re.findall(r"\d+", string)[0]


def convert_from_request_to_gift_card(card):
	return GiftCard(
		card_number = remove_all_except_digits(card['cardNumber']), 
		pin_code    = remove_all_except_digits(card['pinCode']), 
		owner_id    = card['ownerId']
	)
