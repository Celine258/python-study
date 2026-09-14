reponses = {}
polling_active = True
while polling_active == True:
    name = input("\nWhat`s your name?")
    reponse = input("\nWhich mountain do you want to climb?")
    
    reponses[name] = reponse

    answer = input("\nWhoud you like to let another person respond?(Yes/No)")
    if answer == 'No':
        polling_active = False
for name,response in reponses.items():
    print(f"\n{name} want to climb {reponse}.")