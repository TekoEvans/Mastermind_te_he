import random
import time

length_of_sequence_number = 6
length_of_secret_combination = 4
try_number = 4
code = []


print(f'\t\t{"-"*10}BIENVENUE DANS LE JEU MASTERMIND{"-"*10}')
# definitions de la liste des nombres aleatoires
print(f'{"-"*10}Devinez la combinaison secrete à {length_of_secret_combination} chiffres {"-"*10}')
time.sleep(1)
print(
    f'----------------------------------------------------------------------')
print()
for _ in range(0, length_of_secret_combination):
    code.append(random.randint(0, length_of_sequence_number))

print(code)  
for i in range(0, try_number):
    print(f" Vous avez {try_number-i} tentative")
    
    try:
        # Demande à l'utilisateur de saisir un nombre
        user_input = int(input("Veuillez saisir un entier : "))
        print(f"Vous avez saisi l'entier : {user_input}")
        user_input = list(str(user_input))
        user_input =  [int(i) for i in user_input]
        help_code = user_input
        if len(user_input) != len(code):
            print(f"Saisir  {length_of_secret_combination} chiffres ")
        elif user_input == code: 
                print("vous avez gagner")
                break
        else: 
            for i, char in enumerate(user_input):
                if char == code[i]: 
                    _code[i]= char  
                else:     
                    help_code[i]= "*"
            print(f"Guide: {help_code}")   
                
      
    



    except ValueError:
        # Message d'erreur en cas de saisie incorrecte
        print("Erreur : Veuillez entrer un nombre entier valide.")
        continue
        
    
       
    
        
        
    