import  random

lower_case="azertyuiopqsdfghjklmwxcvbn"
Upper_case="AQWZSXEDCRFVTGBYHNUJIKOLPM"
number="0123456789"
symbols=";,:!ù^%§/.?~@(-)"
recuperation= lower_case + Upper_case +number + symbols
longueur_Du_Password=12

password="".join(random.sample(recuperation,longueur_Du_Password))
print("Votre mot de passe est : "+password)