# Objectif : Écrire une fonction chiffre_cesar qui prend en entrée une chaîne de caractères 
# et un décalage (nombre entier) et retourne la chaîne chiffrée. 

#Conseils : 

#Utiliser string.ascii_lowercase pour les lettres minuscules. 

#Appliquer l'opérateur modulo pour gérer le décalage circulaire.

#Exemple :

#>>> chiffre_cesar("abc", 1)
#'bcd'
#>>> chiffre_cesar("abc", 26)
#'abc'

# importation de la librairie string
import string

# rédaction de la fonction chiffre_cesar
def chiffre_cesar(texte_clair, decalage):
    # texte_clair : texte à chiffrer
    # decalage : nombre de décalage pour le chiffrement


# string.ascii_lowercase sert à obtenir l'alphabet en minuscule

    alphabet_minuscule = string.ascii_lowercase  # On met tout en minuscule / 'abcdefghijklmnopqrstuvwxyz'
    chaine_chiffrée = ""

    for caractere in texte_clair:
        
        if caractere in alphabet_minuscule:
            
            # Calculer la nouvelle position en utilisant le modulo


            # lettre "décryptée" = (lettre "cryptée" - décalage) modulo 26
            # index me permet de trouver la position de la lettre dans l'alphabet

            nouvelle_position = (alphabet_minuscule.index(caractere) + decalage) %26 # %26 pour gérer le décalage circulaire

            # à partir de ma chaine de caractère vide, ajouter le caractère chiffré

            chaine_chiffrée += alphabet_minuscule[nouvelle_position]

        else:
            # Si ce n'est pas une lettre, on le garde inchangé
            chaine_chiffrée += caractere

    return chaine_chiffrée

# application exemple

texte_clair = "hello world "

decalage = 5

# utilisation de la fonction
texte_chiffre = chiffre_cesar(texte_clair, decalage)
print("Texte chiffré :", texte_chiffre)


#Objectif : Écrire une fonction dechiffre_cesar qui prend en entrée une chaîne chiffrée et un décalage et retourne la chaîne originale. 

#Conseils : 

#Utiliser un décalage négatif pour déchiffrer. 

def dechiffre_cesar(texte_chiffre, decalage):
    return chiffre_cesar(texte_chiffre, -decalage)

texte_chiffre = chiffre_cesar(texte_clair, decalage)

# application exemple

texte_dechiffre = dechiffre_cesar(texte_chiffre, decalage)
print("Texte déchiffré :", texte_dechiffre)

#Objectif : Écrire un script qui applique le déchiffrement de César avec tous les décalages possibles sur une chaîne chiffrée et affiche les résultats. 

#Conseils :

#Itérer sur tous les décalages possibles (0 à 25)

#Utiliser dechiffre_cesar pour chaque décalage.

def dechiffre_cesar_tous(texte_chiffre):

    # 26 car il y a 26 lettres dans l'alphabet
    for iteration in range(26):
        # afficher le texte déchiffrék

        # i est le nombre de fois que l'on décale
        print(dechiffre_cesar(texte_chiffre, iteration))

# application exemple

dechiffre_cesar_tous(texte_chiffre)



