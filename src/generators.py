from mypyc.primitives.misc_ops import yield_from_except_op


def filter_by_currency(all_transactions, name_currency: str):
    for transaction in all_transactions:
        if transaction["operationAmount"]["currency"]["name"] == name_currency:
            yield transaction

def transaction_descriptions(transactions):
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start,end):
    for num in range(start, end+1):
        str_num = f"{num:016}"
        yield f'{str_num[:4]} {str_num[4:8]} {str_num[8:12]} {str_num[12:]}'


for card_number in card_number_generator(4000123456789010, 4000123456789015):
    print(card_number)

