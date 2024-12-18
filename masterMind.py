import random
length_of_sequence_number = 6
length_of_secret_combination = 4
try_number = 10


print(f'\t\t{"-"*10}BIENVENUE DANS LE JEU MASTERMIND{"-"*10}')
# definitions de la liste des nombres aleatoires
list_of_number = []
list_of_number = random.sample(range(0, 10), length_of_sequence_number)

print(f'{"-"*10}Devinez la combinaison secrete à {length_of_secret_combination} chiffres a partir de la liste suivants {"-"*10}')
print(
    f'-----------------------------------{list_of_number} -----------------------------------')
print(f'Vous avez {try_number} tentatives. Bonne chance!!')


# [9, 3, 5, 8, 0, 4]
# fonction qui renvoit la combinaison secrete


def secret_combination():
    # #creation de 4  index aleatoire das la liste de nombre pour former la combinaison secrete
    index_aleatoire = random.sample(
        range(0, len(list_of_number)), length_of_secret_combination)
    # combinaison secrete
    return [(list_of_number[index]) for index in index_aleatoire]


combinaison_secrete = secret_combination()
print(f"combinaison secret est : {combinaison_secrete}")

# fonction pour recuperer la proposition de l'utilisateur
# def get_user_input():
#     """
#         :recuperer la saisais du user
#         :verifier la saisis du user
#         :taiter la saisis du user
        
#     """
check = False
while check == False:
    user_input = input(f"Saisir la combinaison a {length_of_secret_combination} chiffres: ")
    if len(user_input) == length_of_secret_combination:
        for char in user_input:
            if type(char) == int:
                if char in list_of_number:
                    if user_input.index(char) ==  combinaison_secrete.index(char):
                        print("c'est bon")
                        check = True 
                else:
                    print("vous avez saisis un chiffres qui n'est pas dans la liste")
            else:  
                print("Entrez un combinaison de chiffres")
                
    else: 
        print(f"votre saisie n'est pas de {length_of_secret_combination} chiffres verifier...") 
        
                     