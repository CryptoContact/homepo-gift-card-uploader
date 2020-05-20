from init import db
from homepoTools import (
        is_valid_homedepot_gift_card,
        commit, 
        remove_all_except_digits, 
        convert_from_request_to_gift_card
)
from celery import Celery


celery_app = Celery('gift_card_uploader', broker='pyamqp://kristian:kristian@localhost/giftCardUploaderQueue')


@celery_app.task
def add_single_card_to_database(card_from_request):
    card = convert_from_request_to_gift_card(card_from_request)
    if is_valid_homedepot_gift_card(card):
        commit(db, card)


@celery_app.task
def add_cards_to_database(chunks_of_cards):
    result = []
    for card in chunks_of_cards:
        id = add_single_card_to_database.delay(card)
        result.append(id)
    return id
