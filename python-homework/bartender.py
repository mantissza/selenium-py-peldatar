# 028.md hw's solution aka bartender if...else statement

prius = 0
print("Would you like to order a drink? We have fine beer and coke. (beer/coke)")
guest_drink = input()
print("What is your age? (positive number)")
guest_age = int(input())

if guest_drink == 'beer' and guest_age < 18:
    print("Excuse me you are too young for this order. I can't give you alcoholic type of drinks yet. " +
          "Come back later...")
    prius = 1

if guest_drink == 'coke' and guest_age > 60:
    print("Caffeine causes high blood pressure. I'm afraid that this choice is bad for your health, my Lord. " +
          "Wouldn't you rather have a beer? (beer/coke)")
    guest_drink = input()
    # Esetében nincs kizárva, hogy megkaphassa a kóláját, ha nagyon ragaszkodik hozzá. => nem kap priust

if guest_drink != 'beer' and guest_drink != 'coke':
    print("Unfortunately I can exclusively serve beer and coffee for you. Sorry.")
    prius = 1

if prius == 0:
    print("Enjoy your drink.")
else:
    print("Goodbye!")
