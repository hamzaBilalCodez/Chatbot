# ==========================================
# KISAN POINT SMART CHATBOT SYSTEM
# Developed in Python
# ==========================================

def show_profile(name, location, phone):
    print("\n========== KISAN PROFILE ==========")
    print(f"Naam      : {name}")
    print(f"Ilaqa     : {location}")
    print(f"Contact   : {phone}")
    print("===================================\n")


def crop_disease():
    print("\n===== FASAL KI BIMARI =====")
    print("1. Keera Lag Gaya")
    print("2. Pattay Peelay Ho Gaye")
    print("3. Fungal Disease")
    print("4. Wapas Main Menu")

    choice = input("Option Select Karain: ")

    if choice == "1":
        print("\nHal:")
        print("- Suitable pesticide spray istemal karain.")
        print("- Subah ya sham spray karain.\n")

    elif choice == "2":
        print("\nHal:")
        print("- Nitrogen ki kami ho sakti hai.")
        print("- Urea khaad ka istemal karain.\n")

    elif choice == "3":
        print("\nHal:")
        print("- Fungicide spray karain.")
        print("- Zyada nami se bachain.\n")

    elif choice == "4":
        return

    else:
        print("Invalid Option\n")


def water_management():
    print("\n===== PAANI MANAGEMENT =====")
    print("1. Gehun")
    print("2. Cotton")
    print("3. Rice")
    print("4. Wapas")

    choice = input("Option Select Karain: ")

    if choice == "1":
        print("\nGehun ko 4-5 dafa paani dena munasib hai.\n")

    elif choice == "2":
        print("\nCotton ko 7-10 din baad paani den.\n")

    elif choice == "3":
        print("\nRice ke liye lagatar nami zaroori hai.\n")

    elif choice == "4":
        return

    else:
        print("Invalid Option\n")


def fertilizer_guide():
    print("\n===== KHAAD AUR BEEJ =====")
    print("1. Gehun")
    print("2. Cotton")
    print("3. Rice")
    print("4. Wapas")

    choice = input("Select Crop: ")

    if choice == "1":
        print("\nGehun:")
        print("- DAP: 1 Bag per Acre")
        print("- Urea: 2 Bags per Acre\n")

    elif choice == "2":
        print("\nCotton:")
        print("- DAP: 1.5 Bags")
        print("- Urea: 2-3 Bags\n")

    elif choice == "3":
        print("\nRice:")
        print("- Nitrogen Rich Fertilizer")
        print("- Potash Recommended\n")

    elif choice == "4":
        return

    else:
        print("Invalid Option\n")


def weather_info():
    print("\n===== MOSAM KI MALOOMAT =====")
    print("Aaj Mosam:")
    print("Temperature : 35°C")
    print("Humidity    : 60%")
    print("Rain Chance : 20%")
    print("Advice      : Fasal ko sham ke waqt paani den.\n")


def market_prices():
    print("\n===== MARKET RATE =====")
    print("Gehun   : Rs. 3100 per 40kg")
    print("Cotton  : Rs. 8500 per 40kg")
    print("Rice    : Rs. 4200 per 40kg")
    print("Sugarcane: Rs. 450 per 40kg\n")


def expert_advice():
    print("\n===== AGRICULTURE EXPERT =====")
    print("1. Pest Control")
    print("2. Soil Testing")
    print("3. Modern Farming")
    print("4. Wapas")

    choice = input("Select Option: ")

    if choice == "1":
        print("\nIntegrated Pest Management use karain.\n")

    elif choice == "2":
        print("\nHar season se pehle soil test karwain.\n")

    elif choice == "3":
        print("\nDrip Irrigation aur Smart Farming apnain.\n")

    elif choice == "4":
        return

    else:
        print("Invalid Option\n")


def kisan_chatbot():

    farmer_name = "BILAL AHMAD"
    location = "Jalal Pur Pir Wala"
    phone_number = "0349-0857003"

    print("=" * 55)
    print("      WELCOME TO KISAN POINT SMART CHATBOT")
    print("=" * 55)

    print(f"\nAssalam-o-Alaikum Uncle {farmer_name}")
    print("Aap ke tamam ziraati masail ka hal yahan mojood hai.\n")

    while True:

        print("============== MAIN MENU ==============")
        print("1. Fasal Ki Bimari")
        print("2. Paani Ka Nizam")
        print("3. Khaad Aur Beej")
        print("4. Mosam Ki Maloomat")
        print("5. Market Rates")
        print("6. Agriculture Expert Advice")
        print("7. Kisan Profile")
        print("8. Help Line")
        print("9. Exit")
        print("=======================================\n")

        choice = input("Apna Option Select Karain (1-9): ")

        if choice == "1":
            crop_disease()

        elif choice == "2":
            water_management()

        elif choice == "3":
            fertilizer_guide()

        elif choice == "4":
            weather_info()

        elif choice == "5":
            market_prices()

        elif choice == "6":
            expert_advice()

        elif choice == "7":
            show_profile(
                farmer_name,
                location,
                phone_number
            )

        elif choice == "8":
            print("\n===== HELP LINE =====")
            print("Agriculture Helpline : 0800-17000")
            print("Local Officer        : 0300-1234567")
            print("Emergency Support    : 1122\n")

        elif choice == "9":
            print("\nAllah Aap Ki Fasal Mein Barkat Ata Farmaye.")
            print("Shukriya Kisan Point Istemal Karnay Ka.")
            print("Khuda Hafiz!\n")
            break

        else:
            print("\nInvalid Input! Sirf 1-9 Tak Number Enter Karain.\n")


# Program Start
kisan_chatbot()