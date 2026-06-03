import random
import time

money = 100
debt = 0
reputation = 50
occupation = []
investing = 0
originalInvestment = 1
stress = 0
totalStress = 0
skill = 0

jobs = {
    "Paperboy": {"wage": 12, "stress": 5, "rarity": 1, "skill": 0},
    "Dog Walker": {"wage": 14, "stress": 5, "rarity": 1, "skill": 0},
    "Fast Food Worker": {"wage": 18, "stress": 30, "rarity": 1, "skill": 5},
    "Retail Assistant": {"wage": 19, "stress": 25, "rarity": 1, "skill": 5},
    "Cashier": {"wage": 20, "stress": 20, "rarity": 1, "skill": 5},
    "Cleaner": {"wage": 22, "stress": 15, "rarity": 1, "skill": 0},
    "Call Centre Agent": {"wage": 24, "stress": 45, "rarity": 1, "skill": 10},
    "Warehouse Worker": {"wage": 26, "stress": 40, "rarity": 1, "skill": 10},

    "Delivery Driver": {"wage": 30, "stress": 35, "rarity": 2, "skill": 15},
    "Security Guard": {"wage": 32, "stress": 25, "rarity": 2, "skill": 15},
    "Receptionist": {"wage": 34, "stress": 20, "rarity": 2, "skill": 20},
    "Mechanic": {"wage": 38, "stress": 45, "rarity": 2, "skill": 25},
    "Chef": {"wage": 42, "stress": 70, "rarity": 2, "skill": 25},
    "Teacher": {"wage": 45, "stress": 55, "rarity": 2, "skill": 30},
    "Carpenter": {"wage": 47, "stress": 40, "rarity": 2, "skill": 25},

    "Electrician": {"wage": 48, "stress": 35, "rarity": 3, "skill": 35},
    "Plumber": {"wage": 50, "stress": 40, "rarity": 3, "skill": 35},
    "Police Officer": {"wage": 52, "stress": 80, "rarity": 3, "skill": 35},
    "Firefighter": {"wage": 54, "stress": 85, "rarity": 3, "skill": 40},
    "Nurse": {"wage": 60, "stress": 75, "rarity": 3, "skill": 45},
    "Construction Manager": {"wage": 65, "stress": 60, "rarity": 3, "skill": 45},
    "Estate Agent": {"wage": 70, "stress": 50, "rarity": 3, "skill": 40},

    "Accountant": {"wage": 75, "stress": 40, "rarity": 4, "skill": 50},
    "Game Developer": {"wage": 78, "stress": 70, "rarity": 4, "skill": 55},
    "Software Developer": {"wage": 85, "stress": 50, "rarity": 4, "skill": 55},
    "Data Analyst": {"wage": 90, "stress": 45, "rarity": 4, "skill": 60},

    "Data Scientist": {"wage": 95, "stress": 55, "rarity": 5, "skill": 65},
    "Project Manager": {"wage": 100, "stress": 65, "rarity": 5, "skill": 65},
    "Cybersecurity Analyst": {"wage": 105, "stress": 70, "rarity": 5, "skill": 70},
    "Lawyer": {"wage": 110, "stress": 85, "rarity": 5, "skill": 75},

    "Airline Pilot": {"wage": 130, "stress": 75, "rarity": 6, "skill": 80},
    "Doctor": {"wage": 140, "stress": 90, "rarity": 6, "skill": 85},
    "Business Owner": {"wage": 160, "stress": 95, "rarity": 6, "skill": 75},

    "Investment Banker": {"wage": 180, "stress": 95, "rarity": 7, "skill": 85},
    "Stock Trader": {"wage": 200, "stress": 95, "rarity": 7, "skill": 85},
    "Senior Software Engineer": {"wage": 220, "stress": 60, "rarity": 7, "skill": 85},
    "Management Consultant": {"wage": 250, "stress": 90, "rarity": 7, "skill": 90},

    "Surgeon": {"wage": 300, "stress": 100, "rarity": 8, "skill": 95},
    "Hedge Fund Manager": {"wage": 400, "stress": 95, "rarity": 8, "skill": 95},
    "Company Director": {"wage": 500, "stress": 90, "rarity": 8, "skill": 95},

    "Chief Technology Officer": {"wage": 700, "stress": 85, "rarity": 9, "skill": 98},
    "Chief Executive Officer": {"wage": 1000, "stress": 95, "rarity": 10, "skill": 100}
}

availableJobs = {}

lastJobRefresh = 0
lastWagesRefresh = 0
lastReputationRefresh = True
lastDebtRefresh = 0
lastRandomEventRefresh = 0
lastInvestmentRefresh = 0
lastTaxRefresh = 0
lastStressRefresh = 0

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
        "money": -200,
        "stress": 30
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
        "money": -800,
        "skill": 10
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
        "reputation": -15,
        "stress": 15
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
        "reputation": 30,
        "stress": 15
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
    
    global lastRandomEventRefresh, money, reputation, occupation, debt, totalStress, skill
    if time.time() - lastRandomEventRefresh >= 30:
        lastRandomEventRefresh = time.time()
        if random.random() < 0.2:
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
                
            if "stress" in event:
                print(f"Stress: {event["stress"]}")
                totalStress += event["stress"]
                
            if "skill" in event:
                print(f"Skill: {event["skill"]}")
                skill += event["skill"]
                
            print()
                

def randomiseJobs():
    global availableJobs
    global lastJobRefresh
    
    availableJobs = {}

    jobList = list(jobs.items())
    random.shuffle(jobList)

    jobList = []

    for job, info in jobs.items():
        weight = max(1, 11 - info["rarity"])
        jobList.extend([job] * weight)

    selectedJobs = random.sample(jobList, 10)

    availableJobs = {}
    for job in selectedJobs:
        availableJobs[job] = jobs[job]
        
    lastJobRefresh = time.time()

def checkJobRefresh():
    if time.time() - lastJobRefresh >= 60:
        randomiseJobs()
        print("\nNew jobs are now available!\n")
        
def checkWagesRefresh():
    
    global money, lastWagesRefresh, skill
    
    if time.time() - lastWagesRefresh >= 60:
        lastWagesRefresh = time.time()
        if occupation != []:
            print(f"You were payed the following: \n")
            for job in range(len(occupation)):
                print(f"{occupation[job][0]} +{occupation[job][1]}")
                money += occupation[job][1]
                print(f"You also gained {occupation[job][1] // 30} skill!")
                skill += occupation[job][1] // 30

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
        if money < 0:
            tax = 0
        print(f"\nYou were taxed {tax}!\n")
        money -= tax
        
def checkStressIncrease():
    global totalStress, stress, lastStressRefresh, occupation
    totalStress += int(((time.time() - lastStressRefresh)/300) * stress)
    lastStressRefresh = time.time()
    if totalStress > 150:
        jobToLeave = None
        max = 100000
        for job in range(len(occupation)):
            if occupation[job][1] < max:
                max = occupation[job][1]
                jobToLeave = occupation[job]
            
        print(f"Too high stress! You were forced to leave {jobToLeave[0]}")
        occupation.remove(jobToLeave)
        totalStress -= stress
        stress -= jobToLeave[2]

def tick():
    checkJobRefresh()
    checkWagesRefresh()
    checkReputationRefresh()
    checkDebtRefresh()
    randomEvent()
    checkInvestmentRefresh()
    checkTaxesRefresh()
    checkStressIncrease()

def main():
    
    global occupation
    global reputation  
    global money
    global debt
    global investing
    global originalInvestment
    global stress
    global totalStress
    global skill
    
    while True:
        tick()
        playerInput = input("Main Menu | Type ? for help. ").lower()
        if playerInput == "?":
            print("You can use the following commands: \nStatus\nActions \n")
        elif playerInput == "status":
            print("Here is your status:")
            print()
            print(f"Current occupations: \n")
            for job in range(len(occupation)):
                print(f"{occupation[job][0]} - {occupation[job][1]}", end = ", ")
                
            print(f"\nCurrent money: {money} \nCurrent debt: {debt} \nReputation: {reputation}\nInvesting: {investing} \nSkill: {skill} \nStress: {totalStress}")
            
        elif playerInput == "actions":
            while True:
                tick()
                playerInput = input("Main Menu > Actions | Type ? for help. ").lower()
                if playerInput == "?":
                    print("You can use the following commands: \nBack \nJobs \nGamble \nLoan \nInvest \nDonate \nVolunteer \nCrime \nLearn \n")
                elif playerInput == "back":
                    break
                elif playerInput == "jobs":
                    if occupation is None:
                        print("You have no occupation.")
                    else:
                        print(f"Current occupations: \n")
                        for job in range(len(occupation)):
                            print(f"{occupation[job][0]} Wages: {occupation[job][1]}")
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
                            for job, info in availableJobs.items():
                                print(f"Occupation: {job}\n    Wage: {info["wage"]}, Stress: {info["stress"]}, Skill required: {info["skill"]}")
                            playerInput = input("Enter job you want to apply for: ").title()
                            if playerInput in availableJobs:
                                
                                jobData = availableJobs[playerInput]
                                
                                if totalStress + jobData["stress"] > 150:
                                    print("You cannot apply for this job, you are too stressed.")
                                    
                                elif skill < jobData["skill"]:
                                        print(f"You need {jobData['skill']} skill for this job. Current skill: {skill}")
                                    
                                else:
                                    if random.random() < max(0.1, reputation / 100):
                                        occupation.append((playerInput, jobData["wage"], jobData["stress"]))
                                        stress += jobData["stress"]
                                        print("You got the job!")
                                    else:
                                        print("You were turned down.")
                                        del availableJobs[playerInput]
                                
                            else:
                                print(f"No job available called {playerInput}")
                        elif playerInput == "quit":
                            stress = 0
                            totalStress = 0
                            occupation.clear()
                            
                        elif playerInput == "promote":
                            reputation = max(0, reputation - 15)
                            if random.random() < (reputation / 100):
                                for i in range(len(occupation)):
                                    name, wage, stress = occupation[i]
                                    occupation[i] = (name, int(wage * 1.1), stress)
                                print(f"Success, you were promoted in your current jobs")
                                for name, wage in occupation:
                                    print(f"{name} now pays {wage}")
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
                    skill = min(100, skill + playerInput // 5)
                    print(f"You gained {playerInput // 2} reputation and skill!")
                    
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
                            print("You can use the following commands: \nBack \nHome \nPoker \nLottery \nBlackJack\n")
                        elif playerInput == "back":
                            break
                        elif playerInput == "home":
                            main()
                
                elif playerInput == "learn":
                    while True:
                        tick()
                        playerInput = input("Main Menu > Actions > Learn | Type ? for help. ").lower()
                        if playerInput == "?":
                            print("You can use the following commands: \nBack \nHome \nPublic \nPrivate \n")
                        elif playerInput == "back":
                            break
                        elif playerInput == "home":
                            main()
                        elif playerInput == "public":
                            playerInput = int(input("How long do you want to learn for? "))
                            for second in range(playerInput):
                                time.sleep(1)
                                print(f"{playerInput - second - 1} seconds left!")
                            skill = min(100, skill + playerInput // 3)
                            print(f"You gained {playerInput // 3} skill!")
                        elif playerInput == "private":
                            spend = int(input("How much do you want to spend on your education?"))
                            playerInput = int(input("How long do you want to learn for? "))
                            for second in range(playerInput):
                                time.sleep(1)
                                print(f"{playerInput - second - 1} seconds left!")
                            skill = min(100, skill + playerInput // 3 * ((spend // 100) + 1))
                            print(f"You gained {playerInput // 3 * ((spend // 100) + 1)} skill!")
                            
                else:
                    print("Invalid command")
        else:
            print("Invalid command")
        
main()