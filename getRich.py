import random
import time

money = 100
debt = 0
reputation = 50
occupation = None
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

def randomEvent():
    global lastRandomEventRefresh, money, reputation, occupation
    if time.time() - lastRandomEventRefresh == 60:
        lastRandomEventRefresh = time.time()
        if random.random() > 0.95:
            choice = random.randint(1,5)
            if choice == 1:
                pass
                

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
    debt += int(((time.time() - lastDebtRefresh)/100) * debt)
    lastDebtRefresh = time.time()
    if debt > 100000:
        print("\nYOU WERE ARRESTED FOR TO MUCH DEBT!\n")

def tick():
    checkJobRefresh()
    checkWagesRefresh()
    checkReputationRefresh()
    checkDebtRefresh()
    randomEvent()

def main():
    
    global occupation
    global reputation  
    global money
    global debt
    
    while True:
        tick()
        playerInput = input("Main Menu | Type ? for help. ").lower()
        if playerInput == "?":
            print("You can use the following commands: \nStatus\nActions \n")
        elif playerInput == "status":
            print("Here is your status:")
            print()
            print(f"Current money: {money} \nCurrent debt: {debt} \nReputation: {reputation} \nOccupation: {occupation} \n")
        elif playerInput == "actions":
            while True:
                tick()
                playerInput = input("Main Menu > Actions | Type ? for help. ").lower()
                if playerInput == "?":
                    print("You can use the following commands: \nBack \nJobs \nGambling \nLoan \nInvest \nDonate \nVolunteer \nCrime \n")
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
                            
                            
                            
                else:
                    print("Invalid command")
        else:
            print("Invalid command")
        
main()