# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.
import requests
import hashlib
from colorama import Fore, Style
def check_password_leak(password) :
    sha1_hash = hashlib.sha1 ( password.encode ( 'utf-8' ) ).hexdigest ().upper ()
    prefix, suffix = sha1_hash[:5], sha1_hash[5 :]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get ( url )
    response.raise_for_status ()
    hashes = (line.split ( ':' ) for line in response.text.splitlines ())
    for hash_suffix, count in hashes :
        if hash_suffix == suffix :
            return int ( count )
    return 0
def main() :
    print ( Fore.YELLOW + "\n--- Password Lookup ---\n" + Style.RESET_ALL )
    password = input ( Fore.YELLOW + Style.BRIGHT + "Enter the password to check: " + Style.RESET_ALL )
    count = check_password_leak ( password )
    if count :
        print ( Fore.RED + f"Password has been found in {count} data breaches!" + Style.RESET_ALL )
    else :
        print ( Fore.GREEN + "Password has not been found in data breaches." + Style.RESET_ALL )
if __name__ == "__main__" :
    main ()
# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.