import time

def create_country_dictionary(country):
    if country == "India":
        states = {
            "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Tirupati"],
            "Arunachal Pradesh": ["Itanagar", "Naharlagun", "Pasighat"],
            "Assam": ["Guwahati", "Silchar", "Dibrugarh"],
            "Bihar": ["Patna", "Gaya", "Bhagalpur"],
            "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur"],
            "Goa": ["Panaji", "Margao", "Vasco da Gama"],
            "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
            "Haryana": ["Chandigarh", "Faridabad", "Gurugram"],
            "Himachal Pradesh": ["Shimla", "Mandi", "Dharamshala"],
            "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad"],
            "Karnataka": ["Bengaluru", "Mysuru", "Hubballi"],
            "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode"],
            "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur"],
            "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
            "Manipur": ["Imphal", "Thoubal", "Bishnupur"],
            "Meghalaya": ["Shillong", "Tura", "Nongpoh"],
            "Mizoram": ["Aizawl", "Lunglei", "Saiha"],
            "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
            "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela"],
            "Punjab": ["Chandigarh", "Ludhiana", "Amritsar"],
            "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur"],
            "Sikkim": ["Gangtok", "Namchi", "Mangan"],
            "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
            "Telangana": ["Hyderabad", "Warangal", "Karimnagar"],
            "Tripura": ["Agartala", "Udaipur", "Dharmanagar"],
            "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra"],
            "Uttarakhand": ["Dehradun", "Haridwar", "Roorkee"],
            "West Bengal": ["Kolkata", "Howrah", "Durgapur"]
        }
    elif country == "USA":
        states = {
            "California": ["Los Angeles", "San Francisco", "San Diego"],
            "New York": ["New York City", "Buffalo", "Rochester"],
            "Texas": ["Houston", "Dallas", "Austin"],
            "Florida": ["Miami", "Orlando", "Tampa"],
            "Illinois": ["Chicago", "Springfield", "Peoria"],
            "Pennsylvania": ["Philadelphia", "Pittsburgh", "Harrisburg"],
            "Ohio": ["Columbus", "Cleveland", "Cincinnati"],
            "Georgia": ["Atlanta", "Savannah", "Augusta"],
            "Michigan": ["Detroit", "Grand Rapids", "Lansing"],
            "North Carolina": ["Charlotte", "Raleigh", "Greensboro"],
            "Washington": ["Seattle", "Spokane", "Tacoma"],
            "Arizona": ["Phoenix", "Tucson", "Mesa"],
            "Massachusetts": ["Boston", "Worcester", "Springfield"],
            "Colorado": ["Denver", "Colorado Springs", "Aurora"],
            "Indiana": ["Indianapolis", "Fort Wayne", "Evansville"],
            "Virginia": ["Virginia Beach", "Norfolk", "Richmond"],
            "Tennessee": ["Nashville", "Memphis", "Knoxville"],
            "Missouri": ["Kansas City", "St. Louis", "Springfield"],
            "Maryland": ["Baltimore", "Annapolis", "Frederick"],
            "Wisconsin": ["Milwaukee", "Madison", "Green Bay"]
        }
    else:
        states = {}
    return states

def print_states(states):
    print("\nList of all states:")
    for state in states:
        print(state)

def get_user_states():
    user_states = []
    for _ in range(6):
        state = input("Enter a state: ")
        user_states.append(state)
    return user_states

def print_research_message(user_states, country):
    print(f"The explorer is doing his research on the following cities of {country}:")
    for state in user_states:
        if state in states:
            cities = states[state]
            if cities:
                print(*cities, sep=", ")
            else:
                print(f"No cities found for {state}")
        else:
            print(f"{state} is not a valid state in {country}.")
        time.sleep(1)

def find_treasure(user_states, country):
    if country == "India":
        for state in user_states:
            if state == "Goa":
                print("Congratulations! The treasure is hidden in Panaji city of Goa.")
                return True
    elif country == "USA":
        for state in user_states:
            if state == "California":
                print("Congratulations! The treasure is hidden in Los Angeles city of California.")
                return True
    print("Sorry, the treasure is not hidden in any of the selected states.")
    return False

def play_game():
    print("Welcome to the Treasure Hunt game!")
    print("In this adventure, you are a explorer on a quest to uncover hidden treasures.")
    print("Your mission is to explore different cities within a chosen country,")
    print("gather clues, and ultimately discover the secret location of the treasure.")
    print()
    print("Currently, you can choose from the following countries:")
    print("1. India")
    print("2. USA")
    print()
       
    country = input("Enter a country: ")
    global states
    states = create_country_dictionary(country)
    print_states(states)
    while True:
        user_states = get_user_states()
        print_research_message(user_states, country)
        if find_treasure(user_states, country):
            break
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


if __name__ == "__main__":
    play_game()
