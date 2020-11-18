print("How many kilometers did you cycle today?")

Leave = False
while Leave == False:
    kms = input() #get user input
    miles = float(kms)/1.60934 #convert from string to float and divide (1.60943 is miles)
    miles = round(miles, 2) #round the result
    print(f"Your {kms}km ride was {miles}mi ")  
    teste = input("Do you want to leave? (Yes/No?): ")
    if teste == "s":
        sair = True



