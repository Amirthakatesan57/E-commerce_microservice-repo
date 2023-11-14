print("\n\n\n")
str="|| Automobile management ||"
print(str.center(80))
print("\n\n\n")
while True:
    print("\n\n1.SIGN UP\n\n2.SIGN IN\n\n3.BODY PARTS\n\n4.CLOSE")
    choice=int(input("\n\nEnter:"))
    if choice==1:
        f=open('automobile management.txt',"a+")
        print("\nEnter username or email address:")
        username=input('')
        print("Enter password")
        password=input('')
        print(" The sign up  is Successfull...\nYou can proceed with your sign in and your order  ...")
    elif choice==2:
        print("Enter Email/Username:")
        user=input('')
        print("Enter password:")
        passw=input('')
        if username==user and password==passw:
            print(" The Login is Successfull...\nYou can proceed with your order  ...")
            while True:
                print("\nAUTOMOBILE INVENTORY MANAGEMENT SYSTEM ")
                print("\n1.ORDER PARTS \n\n2.YOUR ORDER \n\n3.GST FOR YOUR ORDER \n\n4.SIGNOUT\n\n5.DISCOVER OUR STORY\n\n6.EXIT")
                choice1=int(input("\nEnter YOUR CHOICE:"))
                if choice1==1:
                    print("\n\n===========[             PARTS LIST            ]=================")     
                    print("\n1  -  Floor light                                       - Rs 400"  )
                    print("\n2  -  Bumper                                            - Rs 6000"   )
                    print("\n3  -  Neon headlamp                                     - Rs 5000"  )
                    print("\n4  -  Spoiler                                           - Rs 3800"  )
                    print("\n5  -  Gear knob                                         - Rs 12000" )
                    print("\n6  -  Racing stearing wheel                             - Rs 14000" )
                    print("\n7  -  Exhaust                                           - Rs 3000"  )
                    print("\n8  -  side lips                                         - Rs 3200"  )
                    print("\n9  -  Turbo                                             - Rs 7500"  )
                    print("\n10 -  Engine work                                       - Rs 18500" )
                    print("\n11 -  bike alloy                                        - Rs 5850"  )
                    print("\n12 -  car alloy                                         - Rs 5900"  )
                    print("\n13 -  bike seat cover                                   - Rs 1250"  )
                    print("\n14 -  bike safety guard stick                           - Rs 4450"  )
                    print("\n15 -  bike visor                                        - Rs 1000"  )
                    print("\n16 -  scissor door                                      - Rs 35000" )
                    print("\n17 -  carbon hood                                       - Rs 4600"  )
                    print("\n18 -  Body kit for car                                  - Rs 7600"  )
                    print("\n19 -  wrap                                              - Rs 9500"  )
                    print("\n20 -  air bag suspension                                - Rs 9850"  )
                    print("\n21 -  Chassis control computer                          - Rs 8845"  )
                    print("\n22 -  Brake disc                                        - Rs 6540"   )
                    print("\n23 -  Door water-shield                                 - Rs 7890"  )
                    print("\n24 -  Inner door handle                                 - Rs 7410"  )
                    print("\n25 -  Sunroof Glass                                     - Rs 5840"  )
                    print("\n26 -  Glow Plug                                         - Rs 25000" )
                    print("\n27 -  ABS Sensor                                        - Rs 3210"  )
                    print("\n28 -  Interior harness                                  - Rs 1590"  )
                    print("\n29 -  Remote lock                                       - Rs 7560"  )
                    print("\n30 -  Engine computer and management system             - Rs 25300" )
                    print("\n31 -  Oil pressure sensor                               - Rs 1020"  )
                    print("\n32 -  Engine bay lighting                               - Rs 1905"  )
                    print("\n33 -  Headlight motor                                   - Rs 9046"  )
                    print("\n34 -  Light sensor                                      - Rs 8901"  )
                    print("\n35 -  Vacuum brake booster                              - Rs 8000"  )
                    print("\n36 -  Distilled Water                                   - Rs 50"    )
                    print("\n37 -  Temperature gauge                                 - Rs 7942"  )
                    print("\n38 -  Electronic timing controller                      - Rs 9025"  )
                    print("\n39 -  Fuse                                              - Rs 9990"  )
                    print("\n40 -  Brake booster hose                                - Rs 7770"  )
                    choice2=input("\n\n ENTER THE ITEM CODE ")
                    if choice2=="1": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('1  -  Floor light     - Rs 400 no. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*4000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                                
                    if choice2=="2": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                        
                            n=input()
                            a=('2  - Bumper - Rs 6000 no. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")


                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*600 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="3": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('Neon headlamp                                     - Rs 5000 '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*5000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="4": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                        
                            n=input()
                            a=('Spoiler                                           - Rs 3800 '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*3800 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="5": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                        
                            n=input()
                            a=('Gear knob                                         - Rs 12000 no. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")          

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*12000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="6": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('Racing stearing wheel                             - Rs 14000 no. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")  

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*14000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="7": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('Exhaust                                           - Rs 3000. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*3000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="8": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('side lips                                         - Rs 3200. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*3200 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="9": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('side lips                                         - Rs 3200 no. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*7500 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="10": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)")
                            
                            n=input()
                            a=('Engine work                                       - Rs 18500. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*18500 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="11": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=(' bike alloy                                        - Rs 5850. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*5850 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="12": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=(' car alloy                                         - Rs 5900. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*5900 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="13": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('bike seat cover                                   - Rs 1250. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*1250 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="14": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('bike safety guard stick                           - Rs 4450. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*4450 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="15": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('bike visor                                        - Rs 1000. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*1000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="16": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('scissor door                                      - Rs 35000. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*35000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="17": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('carbon hood                                       - Rs 46. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*4600 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="18": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('Body kit for car                                  - Rs 7600. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*7600 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="19": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                        
                            n=input()
                            a=('wrap                                              - Rs 9500. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*9500 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="20": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('air bag suspension                                - Rs 9850. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*9850 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="21": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                        
                            n=input()
                            a=('Chassis control computer                          - Rs 8845. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*8845 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="22": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('Brake disc                                        - Rs 654. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*654 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="23": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                        
                            n=input()
                            a=('Door water-shield                                 - Rs 7890. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*7890 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="24": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            
                            n=input()
                            a=('Inner door handle                                 - Rs 7410. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n")

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*7410 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="25": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Sunroof Glass                                     - Rs 5840. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*5840 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="26": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Glow Plug                                         - Rs 25000. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*25000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="27": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('ABS Sensor                                        - Rs 3210. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*3210 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="28": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Interior harness                                  - Rs 1590. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*1590 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="29": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('remote lock                                       - Rs 7560. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*7560 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="30": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Engine computer and management system             - Rs 25300. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*25300 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="31": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Oil pressure sensor                               - Rs 1020. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*1020 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="32": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Engine bay lighting                               - Rs 1905. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*1905 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="33": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Headlight motor                                   - Rs 9046. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*9046 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="34": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Light sensor                                      - Rs 8901. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*8901 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="35": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Vacuum brake booster                              - Rs 8000. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*8000 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="36": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Distilled Water                                   - Rs 50. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*50 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="37": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Temperature gauge                                 - Rs 7942. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*7942 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="38": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Electronic timing controller                      - Rs 9025. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*9025 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="39": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Fuse                                              - Rs 9990. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*9990 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 
                    if choice2=="40": 

                        print("\nWould You Like to Confirm ORDER?") 

                        choice01=int(input("1 - Yes\n2 - No\n")) 

                        if choice01==1: 

                            print("QUANTITY YOU WANT TO ORDER (maximum ORDER=10)") 

                            n=input()
                            a=('Brake booster hose                                - Rs 7770. of parts '+n)
                            f.write(a)
                            f.flush()
                            n=int(n)
                            f.write("\n") 

                            if(0<n<=10): 

                                print("Transaction method:") 

                                print("1.Card \n2.Net banking\n") 

                                amount=int(input("Your payment method: \n")) 

                                if amount==1: 

                                    Name=input("Name on card: ") 

                                    C=int(input("Credit Card Number: ")) 

                                    m=int(input("Expiry Month: ")) 

                                    cvv=int(input("CVV(last three digits on back of your credit card): ")) 

                                else: 

                                    print("select your bank for transaction") 

                                    print("a.SBI Bank \nb.Indian overseas bank\n ") 

                                    bank=input() 

                                    if bank=="a"or"b": 

                                        print("Please wait your Transaction is in process") 

                                    else: 

                                        print("Invalid try again") 

                                print("\nORDER PLACED!\n") 

                                k=n*7770 

                                print("YOUR AMOUNT IS",k) 

                            else: 

                                print("YOUR QUANTITY IS EXEEDING THE LIMIT") 

                        else: 

                            print("Press any key to continue") 

                
                elif choice1==2:
                    print("\n\nYou have ordered the quantity of ",n,"and a total of ",k,"Rs  for the order NO ",choice2)
                    
                elif choice1==3:
                    print("1% will be detected for GST")
                    
                    c=k*(1/100) 
                    k=c 
                    print("GST for your ORDER IS Rs",k,"\nWhich has been taken from your mode of  Transfer of cash") 
                    
                elif choice1==4:
                    print("\nYou have been successfully sign out!!!")
                elif choice1==5:
                    print("\nThis was opened in 2019 Dec 10.We have planned to give all our customer happy and we have the coolest custom parts from all brand from the world.\nOur main supplier is from japan and we import and export all our parts all over the world we are going to open many outlet after this year.\nHope you will enjoy our service thank you have a good day")
                    print("OUTLETS\nChennai\nPune\nDubai\nItaly\nUS\nJapan\nMumbai\nMany more Outlets will be added next years by you.Thank you for making us big as your heart!!!")
                else:
                     break
            print("\n\nTHANK YOU ORDERING IN OUR AUTOMOBILE INVENTORY ....\n\nPLEASE VISIT US AGAIN FOR  MORE DISCOUNT...")
                
        else:
            print("\nThe Username or the Password you had entered is incorrect...\nPlease enter a correct Username and Password!!")
    elif choice==3:
                    print("\n============= AUTOMOBILE INVENTORY MANAGEMENT SYSTEM ==============")
                    print("\n1  -  Floor light                                       - Rs 4000"  )
                    print("\n2  -  Bumper                                            - Rs 600"   )
                    print("\n3  -  Neon headlamp                                     - Rs 5000"  )
                    print("\n4  -  Spoiler                                           - Rs 3800"  )
                    print("\n5  -  Gear knob                                         - Rs 12000" )
                    print("\n6  -  Racing stearing wheel                             - Rs 14000" )
                    print("\n7  -  Exhaust                                           - Rs 3000"  )
                    print("\n8  -  side lips                                         - Rs 3200"  )
                    print("\n9  -  Turbo                                             - Rs 7500"  )
                    print("\n10 -  Engine work                                       - Rs 18500" )
                    print("\n11 -  bike alloy                                        - Rs 5850"  )
                    print("\n12 -  car alloy                                         - Rs 5900"  )
                    print("\n13 -  bike seat cover                                   - Rs 1250"  )
                    print("\n14 -  bike safety guard stick                           - Rs 4450"  )
                    print("\n15 -  bike visor                                        - Rs 1000"  )
                    print("\n16 -  scissor door                                      - Rs 35000" )
                    print("\n17 -  carbon hood                                       - Rs 4600"  )
                    print("\n18 -  Body kit for car                                  - Rs 7600"  )
                    print("\n19 -  wrap                                              - Rs 9500"  )
                    print("\n20 -  air bag suspension                                - Rs 9850"  )
                    print("\n21 -  Chassis control computer                          - Rs 8845"  )
                    print("\n22 -  Brake disc                                        - Rs 654"   )
                    print("\n23 -  Door water-shield                                 - Rs 7890"  )
                    print("\n24 -  Inner door handle                                 - Rs 7410"  )
                    print("\n25 -  Sunroof Glass                                     - Rs 5840"  )
                    print("\n26 -  Glow Plug                                         - Rs 25000" )
                    print("\n27 -  ABS Sensor                                        - Rs 3210"  )
                    print("\n28 -  Interior harness                                  - Rs 1590"  )
                    print("\n29 -  Remote lock                                       - Rs 7560"  )
                    print("\n30 -  Engine computer and management system             - Rs 25300" )
                    print("\n31 -  Oil pressure sensor                               - Rs 1020"  )
                    print("\n32 -  Engine bay lighting                               - Rs 1905"  )
                    print("\n33 -  Headlight motor                                   - Rs 9046"  )
                    print("\n34 -  Light sensor                                      - Rs 8901"  )
                    print("\n35 -  Vacuum brake booster                              - Rs 8000"  )
                    print("\n36 -  Distilled Water                                   - Rs 50"    )
                    print("\n37 -  Temperature gauge                                 - Rs 7942"  )
                    print("\n38 -  Electronic timing controller                      - Rs 9025"  )
                    print("\n39 -  Fuse                                              - Rs 9990"  )

                    print("\n40 -  Brake booster hose                                - Rs 7770"  )
    else:
        break
   
        
            

