import random
import time

money = 100
debt = 0
reputation = 50
occupation = None
investing = 0
originalInvestment = 1

jobs = {
    "Paperboy": 12,
    "Fast Food Worker": 18,
    "Cashier": 20,
    "Cleaner": 22,
    "Warehouse Worker": 26,
    "Delivery Driver": 30,
    "Security Guard": 32,
    "Mechanic": 38,
    "Chef": 42,
    "Electrician": 48,
    "Plumber": 50,
    "Carpenter": 47,
    "Police Officer": 52,
    "Firefighter": 54,
    "Nurse": 60,
    "Teacher": 45,
    "Software Developer": 85,
    "Game Developer": 78,
    "Data Scientist": 95,
    "Lawyer": 110,
    "Doctor": 140,
    "Pilot": 130,
    "Business Owner": 160,
    "Stock Trader": 200,
    "Movie Star": 500,
    "Professional Athlete": 750,
    "Crypto Influencer": 300,
}

availableJobs = {}

lastJobRefresh = 0
lastWagesRefresh = 0
lastReputationRefresh = True
lastDebtRefresh = 0
lastRandomEventRefresh = 0
lastInvestmentRefresh = 0
lastTaxRefresh = 0

def randomEvent():
    
    randomEvents = [
    {
        "name": "Found Money",
        "description": "You found cash blowing down the street.",
        "money": 50
    },

    {
        "name": "Crypto Crash",
        "description": "Your meme coin portfolio exploded... in the bad way.",
        "money": -200
    },
    
    {
        "name": "Bank Error",
        "description": "The bank accidentally deposited money into your account.",
        "money": 500
    },

    {
        "name": "Tax Audit",
        "description": "The government audited your finances.",
        "money": -350,
        "reputation": -10
    },

    {
        "name": "Celebrity Tweet",
        "description": "A celebrity randomly promoted your online business.",
        "money": 2000,
        "reputation": 15
    },

    {
        "name": "Coffee Disaster",
        "description": "You spilled coffee on your work computer.",
        "money": -150,
        "reputation": -5
    },

    {
        "name": "Fake Guru Course",
        "description": "You bought a 'Get Rich Quick' course from a guy in a Lamborghini.",
        "money": -800
    },

    {
        "name": "Dog Walking Empire",
        "description": "Your dog-walking side hustle suddenly went viral.",
        "money": 1200,
        "reputation": 10
    },

    {
        "name": "Casino Security",
        "description": "Casino security accused you of cheating and banned you.",
        "reputation": -20
    },

    {
        "name": "Mysterious Briefcase",
        "description": "You found a suspicious briefcase full of money.",
        "money": 2500,
        "reputation": -15
    },

    {
        "name": "Office Microwave Explosion",
        "description": "Your leftover fish curry exploded in the office microwave.",
        "reputation": -25
    },

    {
        "name": "Time Traveler Tip",
        "description": "A time traveler gave you stock advice that somehow worked.",
        "money": 7500
    },

    {
        "name": "Viral Meme",
        "description": "You accidentally became famous from a terrible meme.",
        "money": 900,
        "reputation": 30
    },

    {
        "name": "Identity Theft",
        "description": "A scammer stole your identity and maxed your cards.",
        "money": -4000,
        "debt": 2500
    },

    {
        "name": "Dumpster Treasure",
        "description": "You found a rare collectible in a dumpster.",
        "money": 1800
    }
]
    
    global lastRandomEventRefresh, money, reputation, occupation
    if time.time() - lastRandomEventRefresh >= 30:
        lastRandomEventRefresh = time.time()
        if random.random() < 0.1:
            event = random.choice(randomEvents)
            print(f"\n|| EVENT: {event["name"]} ||\n")
            print(event["description"])
            
            print("\nEffects:")
            
            if "money" in event:
                print(f"Money: {event["money"]}")
                money += event["money"]
                
            if "reputation" in event:
                print(f"Reputation: {event["reputation"]}")
                reputation += event["reputation"]

            if "debt" in event:
                print(f"Debt: {event["debt"]}")
                debt += event["debt"]
            print()
                

def randomiseJobs():
    global availableJobs
    global lastJobRefresh
    
    availableJobs = {}

    jobList = list(jobs.items())
    random.shuffle(jobList)

    for job, wage in jobList[:random.randint(5, 15)]:
        availableJobs[job] = wage
        
    lastJobRefresh = time.time()

def checkJobRefresh():
    if time.time() - lastJobRefresh >= 60:
        randomiseJobs()
        print("\nNew jobs are now available!\n")
        
def checkWagesRefresh():
    
    global money, lastWagesRefresh
    
    if time.time() - lastWagesRefresh >= 60:
        lastWagesRefresh = time.time()
        if occupation != None:
            money += occupation[1]
            print(f"\nYou were payed {occupation[1]}!\n")

def checkReputationRefresh():
    global occupation, lastReputationRefresh
    if reputation < 10:
        occupation = None
        if lastReputationRefresh:
            lastReputationRefresh = False
            print("\nYou were fired!\n")
            
def checkDebtRefresh():
    global debt, lastDebtRefresh
    debt += int(((time.time() - lastDebtRefresh)/300) * debt)
    lastDebtRefresh = time.time()
    if debt > 100000:
        print("\nYOU WERE ARRESTED FOR TO MUCH DEBT!\n")
        
def checkInvestmentRefresh():
    global investing, lastInvestmentRefresh
    multiplier = random.choice([1, -1])
    investing += int((((time.time() - lastInvestmentRefresh)/100) * investing) * multiplier)
    lastInvestmentRefresh = time.time()
    
def checkTaxesRefresh():
    global money, lastTaxRefresh
    if time.time() - lastTaxRefresh >= 30:
        lastTaxRefresh = time.time()
        tax = int(money * 0.05)
        print(f"\nYou were taxed {tax}!\n")
        money -= tax


def tick():
    checkJobRefresh()
    checkWagesRefresh()
    checkReputationRefresh()
    checkDebtRefresh()
    randomEvent()
    checkInvestmentRefresh()
    checkTaxesRefresh()

def main():
    
    global occupation
    global reputation  
    global money
    global debt
    global investing
    global originalInvestment
    
    while True:
        tick()
        playerInput = input("Main Menu | Type ? for help. ").lower()
        if playerInput == "?":
            print("You can use the following commands: \nStatus\nActions \n")
        elif playerInput == "status":
            print("Here is your status:")
            print()
            print(f"Current money: {money} \nCurrent debt: {debt} \nReputation: {reputation} \nOccupation: {occupation} \nInvesting: {investing}")
        elif playerInput == "actions":
            while True:
                tick()
                playerInput = input("Main Menu > Actions | Type ? for help. ").lower()
                if playerInput == "?":
                    print("You can use the following commands: \nBack \nJobs \nGamble \nLoan \nInvest \nDonate \nVolunteer \nCrime \n")
                elif playerInput == "back":
                    break
                elif playerInput == "jobs":
                    if occupation is None:
                        print("You have no occupation.")
                    else:
                        print(f"Current occupation: {occupation[0]} \nWages: {occupation[1]}")
                    while True:
                        tick()
                        playerInput = input("Main Menu > Actions > Jobs | Type ? for help. ").lower()
                        if playerInput == "?":
                            print("You can use the following commands: \nBack \nHome \nFind \nQuit \nPromote \n")
                        elif playerInput == "back":
                            break
                        elif playerInput == "home":
                            main()
                        elif playerInput == "find":
                            tick()
                            for job, wage in availableJobs.items():
                                print(f"Occupation: {job} Wage: {wage}")
                            playerInput = input("Enter job you want to apply for: ").title()
                            if playerInput in availableJobs:
                                if random.random() < (reputation / 100) > 0.1:
                                    occupation = (playerInput, availableJobs[playerInput])
                                    print("You got the job!")
                                else:
                                    print("You were turned down.")
                                    del availableJobs[playerInput]
                                
                            else:
                                print(f"No job available called {playerInput}")
                        elif playerInput == "quit":
                            occupation = None
                            
                        elif playerInput == "promote":
                            reputation = max(0, reputation - 15)
                            if random.random() < (reputation / 100):
                                occupation = (occupation[0], int(occupation[1] * 1.1))
                                print(f"Success, you were promoted in your current job: {occupation[0]} Your new wages are {occupation[1]}")
                            else:
                                print("You were not given the promotion.")
                                
                        else:
                            print("Invalid command")
                            
                elif playerInput == "volunteer":
                    playerInput = int(input("How long do you want to volunteer for? "))
                    for second in range(playerInput):
                        time.sleep(1)
                        print(f"{playerInput - second} seconds left!")
                    reputation = min(100, reputation + playerInput // 2)
                    print(f"You gained {playerInput // 2} reputation!")
                    
                elif playerInput == "donate":
                    playerInput = int(input("How much do you want to donate? "))
                    if playerInput > money:
                        print("Not enough money!")
                    else:
                        money -= playerInput
                        reputation = min(100, reputation + playerInput // 10)
                        print(f"Donated {playerInput}, reputation increased to {reputation}")
                    
                elif playerInput == "loan":
                    print(f"You currently own {debt} to the bank.\n")
                    
                    while True:
                        tick()
                        playerInput = input("Main Menu > Actions > Loan | Type ? for help. ").lower()
                        if playerInput == "?":
                            print("You can use the following commands: \nBack \nHome \nBorrow \nReturn \n")
                        elif playerInput == "back":
                            break
                        elif playerInput == "home":
                            main()
                        elif playerInput == "borrow":
                            if debt > 0:
                                print("You are in debt, you cannot borrow!")
                            else:
                                playerInput = int(input("How much would you like to borrow?"))
                                if playerInput > 10000:
                                    print("Too much!")
                                else:
                                    money += playerInput
                                    debt += playerInput
                        elif playerInput == "return":
                            playerInput = int(input(f"How much would you like to return? max: {debt} "))
                            if playerInput > debt:
                                print("Invalid amount!")
                            else:
                                debt -= playerInput
                                money -= playerInput
                        else:
                            print("Invalid command")
                            
                elif playerInput == "invest":
                    print(f"You have originally invested {originalInvestment - 1}, it is now {investing/originalInvestment * 100}% of the original amount. Currently you have {investing} waiting.")
                    
                    while True:
                        tick()
                        playerInput = input("Main Menu > Actions > Invest | Type ? for help. ").lower()
                        if playerInput == "?":
                            print("You can use the following commands: \nBack \nHome \nInvest \nRetrieve\n")
                        elif playerInput == "back":
                            break
                        elif playerInput == "home":
                            main()
                        elif playerInput == "invest":
                            playerInput = int(input(f"How much would you like to add to your current investment of {investing}? You have {money} "))
                            if playerInput > money:
                                print("You do not have enough money!")
                            else:
                                originalInvestment = playerInput + originalInvestment
                                investing += playerInput
                                money -= playerInput
                                print(f"You have invested {playerInput}. ")
                        elif playerInput == "retrieve":
                            playerInput = int(input(f"How much would you like to retrieve? (max: {investing}) "))
                            if playerInput > investing:
                                print("You do not have that much money in investment!")
                            else:
                                originalInvestment -= playerInput
                                investing -= playerInput
                                money += playerInput
                                print(f"You have retrieved {playerInput}. ")
                        else:
                            print("Invalid command")
                            
                elif playerInput == "gamble":
                    while True:
                        tick()
                        playerInput = input("Main Menu > Actions > Gamble | Type ? for help. ").lower()
                        if playerInput == "?":
                            print("You can use the following commands: \nBack \nHome \nPoker \nLottery\nBlackJack\n")
                        elif playerInput == "back":
                            break
                        elif playerInput == "home":
                            main()
                
                else:
                    print("Invalid command")
        else:
            print("Invalid command")
        
main()