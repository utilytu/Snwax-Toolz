# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.
import random
from colorama import Fore, Style
def luhn_checksum(card_number) :
    def digits_of(n) :
        return [int ( d ) for d in str ( n )]
    digits = digits_of ( card_number )
    odd_digits = digits[-1 : :-2]
    even_digits = digits[-2 : :-2]
    checksum = sum ( odd_digits )
    for d in even_digits :
        checksum += sum ( digits_of ( d * 2 ) )
    return checksum % 10
def complete_card_number(prefix, length) :
    card_number = [int ( x ) for x in str ( prefix )]
    while len ( card_number ) < (length - 1) :
        digit = random.randint ( 0, 9 )
        card_number.append ( digit )
    checksum = luhn_checksum ( int ( ''.join ( map ( str, card_number ) ) ) * 10 )
    card_number.append ( 0 if checksum == 0 else 10 - checksum )
    return ''.join ( map ( str, card_number ) )
def generate_credit_card_number() :
    # Different card types can have different prefixes, e.g., Visa starts with 4, MasterCard starts with 5
    prefix = random.choice ( [4, 5] )  # 4 for Visa, 5 for MasterCard
    return complete_card_number ( prefix, 16 )
def generate_expiration_date_and_cvv() :
    month = random.randint ( 1, 12 )
    year = random.randint ( 24, 29 )  # Random year between 2024 and 2029
    cvv = random.randint ( 100, 999 )  # 3-digit CVV
    return f"{month:02d}/{year}", cvv
def generate_fake_credit_card() :
    card_number = generate_credit_card_number ()
    expiration_date, cvv = generate_expiration_date_and_cvv ()
    print ( Fore.YELLOW + Style.BRIGHT + "\nGenerated Fake Credit Card Info:" + Style.RESET_ALL )
    print ( Fore.YELLOW + f"Card Number      : {card_number}" + Style.RESET_ALL )
    print ( Fore.YELLOW + f"Expiration Date  : {expiration_date}" + Style.RESET_ALL )
    print ( Fore.YELLOW + f"CVV              : {cvv}" + Style.RESET_ALL )
    print ( Fore.YELLOW + "\nNote: These are randomly generated for educational purposes only.\n" + Style.RESET_ALL )
generate_fake_credit_card ()
# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.