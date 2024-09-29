# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.
import requests
import time
from colorama import Fore, Style
def send_webhook_message() :
    print ( Fore.YELLOW + "\n--- Discord Webhook Message Sender ---\n" + Style.RESET_ALL )
    webhook_url = input ( Fore.YELLOW + Style.BRIGHT + "Enter the Discord Webhook URL: " + Style.RESET_ALL )
    message_content = input ( Fore.YELLOW + Style.BRIGHT + "Enter the message to send: " + Style.RESET_ALL )
    number_of_messages = int (
        input ( Fore.YELLOW + Style.BRIGHT + "Enter the number of messages to send: " + Style.RESET_ALL ) )
    delay = float (
        input ( Fore.YELLOW + Style.BRIGHT + "Enter the delay (in seconds) between each message: " + Style.RESET_ALL ) )
    data = {
        "content" : message_content,
        "username" : "Webhook Bot"
    }
    try :
        for i in range ( number_of_messages ) :
            response = requests.post ( webhook_url, json=data )
            if response.status_code == 204 :
                print ( Fore.GREEN + f"Message {i + 1} sent successfully!" + Style.RESET_ALL )
            else :
                print (
                    Fore.RED + f"\nFailed to send message {i + 1}. Status code: {response.status_code}\n" + Style.RESET_ALL )
            time.sleep ( delay )
    except Exception as e :
        print ( Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL )
send_webhook_message ()
# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.