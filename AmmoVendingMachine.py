print("Welcome, soldier..\n\nThis is an ammuntion vending machine..🔫🔫 \n\nPress 1 for Assault Rifle ammo\nPress 2 for SMG ammo\nPress 3 for LMG ammo\nPress 4 for Shotgun ammo\nPress 5 for Sniper Rifle ammo\nPress 6 for Pistol ammo\n\nPress 0 to leave\n")
error_count = 0

while True:
        i = int(input("Enter choice of ammo: "))
        if i<0 or i>6:
            error_count += 1
            if error_count == 3:
                exit()
            print(f"Oops.. That's an invalid input.. Automation will stop after 3 tries.. {error_count}/3")
        else:
            break


while i>=0:

        def ammo_type(i):
                switcher={
                        1:'Assault Rifle Ammo',
                        2:'SMG Ammo',
                        3:'LMG Ammo',
                        4:'Shotgun Ammo',
                        5:'Sniper Rifle Ammo',
                        6:'Pistol Ammo'
                        }
                return switcher.get(i)


        if i>=1 and i<=6:
                print("You chose",ammo_type(i))
                print("Now enter the number of ammo needed")
                x = int(input())
                print("\n")
                print("✅✅Order validated✅✅\n",x,"rounds of",ammo_type(i),"have been obtained..")
                print("\nThank you..Have a nice day👋👋")
                break
        elif i==0:
                print("\nHope we can be of assistance in the future..🙁🙁\n\nThank you..Have a nice day👋👋")
                break
        else: 
                print("❌❌Invalid❌❌\n\nTry again...😵😵")
                break
        break