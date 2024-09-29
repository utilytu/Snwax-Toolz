# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.
def DoxCreate():
    Title("Dox Create")
    try:
        by = input(f"{INPUT} Doxed By      : {reset}")
        reason = input(f"{INPUT} Reason        : {reset}")
        pseudo1 = input(f"{INPUT} First Pseudo  : {reset}")
        pseudo2 = input(f"{INPUT} Second Pseudo : {reset}")
        print(f"\n{INFO}{yellow} Discord Information:")
        token_input = input(f"{INPUT} Token ? (y/n) -> {reset}")
        if token_input.lower() in ["y", "yes"]:
            token = input(f"{INPUT} Token: {reset}")
            username_discord, display_name_discord, user_id_discord, avatar_url_discord, created_at_discord, email_discord, phone_discord, nitro_discord, friends_discord, gift_codes_discord, mfa_discord = TokenInfo(token)
        else:
            token = "None"
            username_discord = input(f"{INPUT} Username      : {reset}")
            display_name_discord = input(f"{INPUT} Display Name  : {reset}")
            user_id_discord = input(f"{INPUT} Id            : {reset}")
            avatar_url_discord = input(f"{INPUT} Avatar        : {reset}")
            created_at_discord = input(f"{INPUT} Created At    : {reset}")
            email_discord = input(f"{INPUT} Email         : {reset}")
            phone_discord = input(f"{INPUT} Phone         : {reset}")
            nitro_discord = input(f"{INPUT} Nitro         : {reset}")
            friends_discord = input(f"{INPUT} Friends       : {reset}")
            gift_codes_discord = input(f"{INPUT} Gift Code     : {reset}")
            mfa_discord = input(f"{INPUT} Mfa           : {reset}")
        print(f"\n{INFO}{yellow} IP Information:")
        ip_public = input(f"{INPUT} IP Public     : {reset}")
        ip_local = input(f"{INPUT} IP Local      : {reset}")
        ipv6 = input(f"{INPUT} IPv6          : {reset}")
        vpn_pc = input(f"{INPUT} VPN           : {reset}")
        isp_ip, org_ip, as_ip = IpInfo(ip_public)
        print(f"\n{INFO}{yellow} PC Information:")
        name_pc = input(f"{INPUT} Name          : {reset}")
        username_pcc = input(f"{INPUT} Username      : {reset}")
        displayname_pc = input(f"{INPUT} Display Name  : {reset}")
        platform_pc = input(f"{INPUT} Platform      : {reset}")
        exploitation_pc = input(f"{INPUT} OS            : {reset}")
        windowskey_pc = input(f"{INPUT} Windows Key   : {reset}")
        mac_pc = input(f"{INPUT} MAC Address   : {reset}")
        hwid_pc = input(f"{INPUT} HWID Address  : {reset}")
        cpu_pc = input(f"{INPUT} CPU           : {reset}")
        gpu_pc = input(f"{INPUT} GPU           : {reset}")
        ram_pc = input(f"{INPUT} RAM           : {reset}")
        disk_pc = input(f"{INPUT} Disk          : {reset}")
        mainscreen_pc = input(f"{INPUT} Screen Main   : {reset}")
        secscreen_pc = input(f"{INPUT} Screen Sec    : {reset}")
        print(f"\n{INFO}{yellow} Phone Information:")
        phone_number = input(f"{INPUT} Phone Number  : {reset}")
        brand_phone = input(f"{INPUT} Brand         : {reset}")
        operator_phone, type_number_phone, country_phone, region_phone, timezone_phone = NumberInfo(phone_number)
        print(f"\n{INFO}{yellow} Personal Information:")
        gender = input(f"{INPUT} Gender        : {reset}")
        last_name = input(f"{INPUT} Last Name     : {reset}")
        first_name = input(f"{INPUT} First Name    : {reset}")
        age = input(f"{INPUT} Age           : {reset}")
        mother = input(f"{INPUT} Mother        : {reset}")
        father = input(f"{INPUT} Father        : {reset}")
        brother = input(f"{INPUT} Brother       : {reset}")
        sister = input(f"{INPUT} Sister        : {reset}")
        print(f"\n{INFO}{yellow} Location Information:")
        continent = input(f"{INPUT} Continent     : {reset}")
        country = input(f"{INPUT} Country       : {reset}")
        region = input(f"{INPUT} Region        : {reset}")
        postal_code = input(f"{INPUT} Postal Code   : {reset}")
        city = input(f"{INPUT} City          : {reset}")
        address = input(f"{INPUT} Address       : {reset}")
        timezone = input(f"{INPUT} Timezone      : {reset}")
        longitude = input(f"{INPUT} Longitude     : {reset}")
        latitude = input(f"{INPUT} Latitude      : {reset}")
        email = input(f"{INPUT} Email         : {reset}")
        password = input(f"{INPUT} Password      : {reset}")
        other = input(f"{INPUT} Other Info    : {reset}")
        database = input(f"{INPUT} Database Info : {reset}")
        logs = input(f"{INPUT} Logs Info     : {reset}")
        report = f"""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██████╗   ██████╗  ██╗  ██╗
██╔══██╗ ██╔═══██╗ ╚██╗██╔╝
██║  ██║ ██║   ██║  ╚███╔╝ 
██║  ██║ ██║   ██║  ██╔██╗ 
██████╔╝ ╚██████╔╝ ██╔╝ ██╗ 
╚═════╝   ╚═════╝  ╚═╝  ╚═╝   
Doxed By : {by}
Reason   : {reason}
Pseudo   : "{pseudo1}", "{pseudo2}"
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
 DISCORD:
 =====================================================================================
[+] Username     : {username_discord}
[+] Display Name : {display_name_discord}
[+] ID           : {user_id_discord}
[+] Avatar       : {avatar_url_discord}
[+] Created At   : {created_at_discord}
[+] Token        : {token}
[+] E-Mail       : {email_discord}
[+] Phone        : {phone_discord}
[+] Nitro        : {nitro_discord}
[+] Friends      : {friends_discord}
[+] Gift Code    : {gift_codes_discord}
[+] Multi-Factor Authentication : {mfa_discord}
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
...
(add rest of the template here as you defined)
...
"""
        print(report)
    except Exception as e:
        ErrorModule(e)
# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.