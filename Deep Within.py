#Ecran titre
print("____________________________________________________________________________________________________________________________________________________________________________")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
print("")
print("｜―――――\      ｜―――――― ｜    ｜―――――― ｜  ｜―――― \         ―――           ―――   ―――――――  ｜―――――――――｜  ｜――｜   ｜――｜   ―――――――   ｜――｜ ｜――｜")
print("｜         ｜    ｜ ｜―――――｜    ｜ ｜―――――｜  ｜         \        ｜  \    ――   /  ｜      ｜  ｜      ｜―――――――――｜  ｜   ｜   ｜   ｜     ｜  ｜       ｜    \ ｜   ｜")
print("｜  ｜--\    ｜   ｜ ｜             ｜ ｜            ｜  ｜>     ｜       \   \  /  \  /   /       ｜  ｜            ｜ ｜         ｜   ｜――｜   ｜     ｜  ｜       ｜     \｜   ｜")
print("｜  ｜   ｜   ｜  ｜  ―――――｜    ｜  ―――――｜    ｜         /         \   \/    \/   /        ｜  ｜            ｜ ｜         ｜            ｜     ｜  ｜       ｜           ｜")
print("｜  ｜--/    ｜   ｜ ｜             ｜ ｜             ｜  ｜――/            \     /\     /         ｜  ｜            ｜ ｜         ｜   ｜――｜   ｜     ｜  ｜       ｜   ｜\     ｜")
print("｜         ｜    ｜ ｜―――――｜    ｜ ｜―――――｜    ｜  ｜                 \   /  \   /          ｜  ｜            ｜ ｜         ｜   ｜   ｜   ｜     ｜  ｜       ｜   ｜ \    ｜")
print("｜―――――/      ｜―――――― ｜    ｜―――――― ｜    ｜――｜                 ――    ――        ―――――――       ―――――       ｜――｜   ｜――｜  ―――――――   ｜――｜ ｜――｜")
print("")
print("")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("____________________________________________________________________________________________________________________________________________________________________________")
print("")
print("                                                                Appuyer sur 'Enter' pour commencer...")
input("")

import time
#permet de clarifier le visuel (console)
def effacer_console():
 print("\n" * 100)
#permet de vérifier une condition
def classecheck(Classe,Demande):
  if Demande in Classe :
   return 0
  else:
   return 1
def objcheck(ChoixObj, objdrpt):
      if ChoixObj in objdrpt:
          return 0
      else:
          return 1
def ChoixMenuCheck(Action):
 if Action == 1:
  return 0
 elif Action == 2:
  return 0
 elif Action == 3:
  return 0
 elif Action == 4:
  return 0
 else:
  return 1
#Permet de trouver et copier les bonnes informations dans la fiche de personnage
def statGuerrier(Demande, Classe):
 if Demande == Classe[0]:
  y = []
  try:
   with open("FClasse.txt", "r", encoding="utf-8") as f:
    x = f.readlines()
    y = x[10:18]
    y = [line.strip() for line in y]
   with open("FichePerso.txt", "a", encoding="utf-8") as f:
    for i in range(0,8):
     f.write(y[i]+"\n")
  except FileNotFoundError:
   return"Le fichier n'a pas été trouvé"
  except Exception as e:
   return f"ta race:{e}"
def statVagabond(Demande, Classe):
 if Demande == Classe[1]:
  y = []
  try:
   with open("FClasse.txt", "r", encoding="utf-8") as f:
    x = f.readlines()
    y = x[20:28]
    y = [line.strip() for line in y]
   with open("FichePerso.txt", "a", encoding="utf-8") as f:
    for i in range(0,8):
     f.write(y[i]+"\n")
  except FileNotFoundError:
   return"Le fichier n'a pas été trouvé"
  except Exception as e:
   return f"ta race:{e}"
def statMage(Demande, Classe):
 if Demande == Classe[2]:
  y = []
  try:
   with open("FClasse.txt", "r", encoding="utf-8") as f:
    x = f.readlines()
    y = x[30:38]
    y = [line.strip() for line in y]
   with open("FichePerso.txt", "a", encoding="utf-8") as f:
    for i in range(0,8):
     f.write(y[i]+"\n")
  except FileNotFoundError:
   return"Le fichier n'a pas été trouvé"
  except Exception as e:
   return f"pourquoijem'infligeca:{e}"
def statBandit(Demande, Classe):
 if Demande == Classe[3]:
  y = []
  try:
   with open("FClasse.txt", "r", encoding="utf-8") as f:
    x = f.readlines()
    y = x[40:48]
    y = [line.strip() for line in y]
   with open("FichePerso.txt", "a", encoding="utf-8") as f:
    for i in range(0,8):
     f.write(y[i]+"\n")
  except FileNotFoundError:
   return"Le fichier n'a pas été trouvé"
  except Exception as e:
   return f"huhu:{e}"
def statSamurai(Demande, Classe):
 if Demande == Classe[4]:
  y = []
  try:
   with open("FClasse.txt", "r", encoding="utf-8") as f:
    x = f.readlines()
    y = x[50:58]
    y = [line.strip() for line in y]
   with open("FichePerso.txt", "a", encoding="utf-8") as f:
    for i in range(0,8):
     f.write(y[i]+"\n")
  except FileNotFoundError:
   return"Le fichier n'a pas été trouvé"
  except Exception as e:
   return f":):{e}"
def statChasseur(Demande, Classe):

 if Demande == Classe[5]:
  y = []
  try:
   with open("FClasse.txt", "r", encoding="utf-8") as f:
    x = f.readlines()
    y = x[60:68]
    y = [line.strip() for line in y]
   with open("FichePerso.txt", "a", encoding="utf-8") as f:
    for i in range(0,8):
     f.write(y[i]+"\n")
  except FileNotFoundError:
   return"Le fichier n'a pas été trouvé"
  except Exception as e:
   return f":/:{e}"
def statClerc(Demande, Classe):
 if Demande == Classe[6]:
  y = []
  try:
   with open("FClasse.txt", "r", encoding="utf-8") as f:
    x = f.readlines()
    y = x[70:78]
    y = [line.strip() for line in y]
   with open("FichePerso.txt", "a", encoding="utf-8") as f:
    for i in range(0,8):
     f.write(y[i]+"\n")
  except FileNotFoundError:
   return"Le fichier n'a pas été trouvé"
  except Exception as e:
   return f"huhuhu:{e}"
def statPyromancien(Demande, Classe):
    if Demande == Classe[7]:
     y = []
     try:
      with open("FClasse.txt", "r", encoding="utf-8") as f:
       x = f.readlines()
       y = x[80:88]
       y = [line.strip() for line in y]
      with open("FichePerso.txt", "a", encoding="utf-8") as f:
       for i in range(0, 8):
        f.write(y[i]+"\n")
     except FileNotFoundError:
      return "Le fichier n'a pas été trouvé"
     except Exception as e:
      return f"ha:{e}"

effacer_console()
Action=0
while Action != 2:
 print("--------------------------------------------------------------------------------------------------------")
 print("                Pour continuer entrer dans la console le nombre associé à son action ")
 print()
 print("                                     1.Nouvelle partie...")
 print("                                     2.Continuer la partie...")
 print("                                     3.Règles et informations...")
 print("                                     4.Quitter le jeu...")
 print()
 print()
 print("--------------------------------------------------------------------------------------------------------")
 Action=int(input("Que voulez vous faire?: "))
 if ChoixMenuCheck(Action) == 1:
     while ChoixMenuCheck(Action) != 0:
         Action = int(input("Malheuresment, aucune action n'est lié au nombre choisit.Veuillez recommencer:"))
 if Action ==4:
  exit()
 elif Action ==3:
  effacer_console()
  with open("Rgl+info.txt","r",encoding="utf-8")as f:
   print(f.read())
  input("                                              Enter sur 'Enter' pour retourner au menu")
 elif Action ==1:
  print()
  print("                                                 Debut de la partie",end="",flush=True             )
  for _ in range(3):
   time.sleep(1)
   print(".", end="", flush=True)
  effacer_console()

  #Choix du nom
  print("------------------------------------------------------------------------------------------")
  print()
  print("                                Quel est votre nom ?")
  print()
  print("------------------------------------------------------------------------------------------")
  Nom =str(input("Que choisissez vous ?: "))
  with open("FichePerso.txt","w",encoding="utf-8") as f:
   f.write(Nom+"\n")
  effacer_console()

  #Choix classe
  Classe=["Guerrier","Vagabond","Mage","Bandit","Samurai","Chasseur","Clerc","Pyromancien"]
  print("------------------------------------------------------------------------------------------")
  print("           Veuillez rentrer dans la console le nom de la classe souhaité")
  print()
  print("                              1.Guerrier")
  print("                              2.Vagabond")
  print("                              3.Mage")
  print("                              4.Bandit")
  print("                              5.Samurai")
  print("                              6.Chasseur")
  print("                              7.Clerc")
  print("                              8.Pyromancien")
  print()
  print("------------------------------------------------------------------------------------------")
  Demande=str(input("Veuiller choisir votre classe: "))
  if classecheck(Classe,Demande) ==1:
   while classecheck(Classe,Demande)!=0:
    Demande = str(input("Veuillez rechoisir"))
  effacer_console()
  if Demande == Classe[0]:
   statGuerrier(Demande,Classe)
  elif Demande == Classe[1]:
   statVagabond(Demande,Classe)
  elif Demande == Classe[2]:
   statMage(Demande,Classe)
  elif Demande == Classe[3]:
   statBandit(Demande,Classe)
  elif Demande == Classe[4]:
   statSamurai(Demande,Classe)
  elif Demande == Classe[5]:
   statChasseur(Demande,Classe)
  elif Demande == Classe[6]:
   statClerc(Demande,Classe)
  elif Demande == Classe[7]:
   statPyromancien(Demande,Classe)

  #Choix objet:
  objdprt=["Kit de crochetage","Kit de soin","Potion du Berserker","Talisman de Rohen","Chaussure du renard"]
  print("------------------------------------------------------------------------------------------")
  print("           Veuillez rentrer dans la console le nom de l'objet souhaité")
  print()
  print("                           1.Kit de soin // recommandé")
  print("                           2.Kit de crochetage")
  print("                           3.Potion du Berserker")
  print("                           4.Talisman de Rohen")
  print("                           5.Chaussure du renard")
  print()
  print("------------------------------------------------------------------------------------------")
  ChoixObj=str(input("Choissisez un objet de départ: "))
  if objcheck(ChoixObj,objdprt) == 1:
   while objcheck(ChoixObj,objdprt) !=0 :
    ChoixObj=str(input("Veuillez rechoisir l'objet"))
  Action = 2
  effacer_console()
  with open("FichePerso.txt","a",encoding="utf-8") as f:
   f.write(ChoixObj)

#rencontres monstres spéciaux:
from random import randint
def rencontre_spe():
 Tas = randint(1, 7)
 if Tas==1:
  #dragon
  return 1
 elif Tas== 2:
  #Banshee
  return 2
 elif Tas== 3:
  #Gargouille
  return 3
 elif Tas==4:
  #Boule
  return 4
 elif Tas== 5:
  #Chien difforme
  return 5
 elif Tas==6:
  #chimère
  return 6
#rencontre personnage passifs:
def rencontre_persoP():
 Tas=randint(1,5)
 if Tas==1:
  #petite fille
  return 1
 elif Tas==2:
  #mercenaire
  return 2
 elif Tas==3:
  #arnaqueuse
  return 3
 elif Tas==4:
  #Vétéran
  return 4
#rencontre énigme
def rencontre_enigme():
 Tas=randint(1,4)
 if Tas==1:
  return 1
 elif Tas==2:
  return 2
 elif Tas ==3:
  return 3
#rencontre piège:
def rencontre_piege():

 Tas=randint(1,9)
 if Tas ==1:
  #Clous
  return 1
 elif Tas==2:
  #nourriture périmé
  return 2
 elif Tas ==3:
  #PlanteC
  return 3
 elif Tas ==4:
  #Sol instable
  return 4
 elif Tas ==5:
  #Pièges à loup:
  return 5
 elif Tas ==6:
  #gaz
  return 6
 elif Tas ==7:
  #coupure
  return 7
 elif Tas==8:
  #tableau
   return 8
#rencontre Classique:
def rencontreC():
    Tas=randint(1,13)
    if Tas == 1:
        # Zombie
        return 1
    elif Tas == 2:
        # momie
        return 2
    elif Tas == 3:
        # Araignée moyenne
        return 3
    elif Tas == 4:
        #Gobelins
        return 4
    elif Tas == 5:
        # Fou
        return 5
    elif Tas == 6:
        # Serviteur
        return 6
    elif Tas == 7:
        # Zombies armée
        return 7
    elif Tas == 8:
        # Orc
        return 8
    elif Tas == 9:
        #Boucher
        return 9
    elif Tas == 10:
        # Mère araignée
        return 10
    elif Tas == 11:
        #Chevalier noir
        return 11
#rencontre Multiple:
def rencontreMulti():
    TASDuo=randint(1,10)
    TASTrio=randint(1,30)
    if TASDuo==1:
        return 2
    elif TASTrio==1:
        return 3
    else:
        return 1
#rencontre Animaux
def rencontreAni():
    TAS=randint(1,6)
    if TAS==1:
        #chien
        return 1
    elif TAS==2:
        #corbeau
        return 2
    elif TAS==3:
        #souris
        return 3
    elif TAS==4:
        #Sinje
        return 4
    elif TAS==5:
        #Paon
        return 5

#système combat:
#1.récupère les stats des monstres
def zombie():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[5:8]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def fou():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[10:13]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def momie():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[15:18]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def araigneeM():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[20:23]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def gobelin():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[25:28]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def orc():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[30:33]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def serviteur():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[35:38]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def zombieA():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[40:43]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def boucher():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[45:48]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def Mairaignee():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[50:53]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def ChevalierN():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[55:58]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def banshee():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[60:63]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def amas():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[65:68]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def tresh():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[70:73]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def chimere():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[75:78]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def dragon():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[80:83]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y
def chienD():
    try:
        with open("StatMonstre.txt", "r", encoding="utf-8") as f:
            x = f.readlines()
            y = x[85:88]
            y = [line.strip() for line in y]
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé"
    except Exception as e:
        return f"ta race:{e}"
    return y

def Yaqlq(A):
    """Vérifie le nombre d'ennemie restant"""
    if A == 3:
        return 0
    else:
        return 1
#système de combat
def combat(Adversaire, Vie):
    AdvPresent = 0
    t = len(Adversaire)
    #les stats des monstres présent dans la variable Advsaire (liste) sont récupéré
    if t == 1:
        if Adversaire[0] == "Zombie":
            StatM1 = [i for i in zombie()]
        elif Adversaire[0] == "Fou":
            StatM1 = [i for i in fou()]
        elif Adversaire[0] == "Momie":
            StatM1 = [i for i in momie()]
        elif Adversaire[0] == "Araignée Moy":
            StatM1 = [i for i in araigneeM()]
        elif Adversaire[0] == "Gobelin":
            StatM1 = [i for i in gobelin()]
        elif Adversaire[0] == "Orc":
            StatM1 = [i for i in orc()]
        elif Adversaire[0] == "Serviteur":
            StatM1 = [i for i in serviteur()]
        elif Adversaire[0] == "Zombie armé":
            StatM1 = [i for i in zombieA()]
        elif Adversaire[0] == "Boucher":
            StatM1 = [i for i in boucher()]
        elif Adversaire[0] == "Mère araignée":
            StatM1 = [i for i in Mairaignee()]
        elif Adversaire[0] == "Chevalier noir":
            StatM1 = [i for i in ChevalierN()]
        elif Adversaire[0] == "Banshee":
            StatM1 = [i for i in banshee()]
        elif Adversaire[0] == "Amas":
            StatM1 = [i for i in amas()]
        elif Adversaire[0] == "Tresh":
            StatM1 = [i for i in tresh()]
        elif Adversaire[0] == "Chimère":
            StatM1 = [i for i in chimere()]
        elif Adversaire[0] == "Dragon":
            StatM1 = [i for i in dragon()]
        elif Adversaire[0] == "Chien Difforme":
            StatM1 = [i for i in chienD()]
    if t == 2:
        # Premier monstre
        if Adversaire[0] == "Zombie":
            StatM1 = [i for i in zombie()]
        elif Adversaire[0] == "Fou":
            StatM1 = [i for i in fou()]
        elif Adversaire[0] == "Momie":
            StatM1 = [i for i in momie()]
        elif Adversaire[0] == "Araignée Moy":
            StatM1 = [i for i in araigneeM()]
        elif Adversaire[0] == "Gobelin":
            StatM1 = [i for i in gobelin()]
        elif Adversaire[0] == "Orc":
            StatM1 = [i for i in orc()]
        elif Adversaire[0] == "Serviteur":
            StatM1 = [i for i in serviteur()]
        elif Adversaire[0] == "Zombie armé":
            StatM1 = [i for i in zombieA()]
        elif Adversaire[0] == "Boucher":
            StatM1 = [i for i in boucher()]
        elif Adversaire[0] == "Mère araignée":
            StatM1 = [i for i in Mairaignee()]
        elif Adversaire[0] == "Chevalier noir":
            StatM1 = [i for i in ChevalierN()]
        elif Adversaire[0] == "Banshee":
            StatM1 = [i for i in banshee()]
        elif Adversaire[0] == "Amas":
            StatM1 = [i for i in amas()]
        elif Adversaire[0] == "Tresh":
            StatM1 = [i for i in tresh()]
        elif Adversaire[0] == "Chimère":
            StatM1 = [i for i in chimere()]
        elif Adversaire[0] == "Dragon":
            StatM1 = [i for i in dragon()]
        elif Adversaire[0] == "Chien Difforme":
            StatM1 = [i for i in chienD()]
        # Second Monstre
        if Adversaire[1] == "Zombie":
            StatM2 = [i for i in zombie()]
        elif Adversaire[1] == "Fou":
            StatM2 = [i for i in fou()]
        elif Adversaire[1] == "Momie":
            StatM2 = [i for i in momie()]
        elif Adversaire[1] == "Araignée Moy":
            StatM2 = [i for i in araigneeM()]
        elif Adversaire[1] == "Gobelin":
            StatM2 = [i for i in gobelin()]
        elif Adversaire[1] == "Orc":
            StatM2 = [i for i in orc()]
        elif Adversaire[1] == "Serviteur":
            StatM2 = [i for i in serviteur()]
        elif Adversaire[1] == "Zombie armé":
            StatM2 = [i for i in zombieA()]
        elif Adversaire[1] == "Boucher":
            StatM2 = [i for i in boucher()]
        elif Adversaire[1] == "Mère araignée":
            StatM2 = [i for i in Mairaignee()]
        elif Adversaire[1] == "Chevalier noir":
            StatM2 = [i for i in ChevalierN()]
        elif Adversaire[1] == "Banshee":
            StatM2 = [i for i in banshee()]
        elif Adversaire[1] == "Amas":
            StatM2 = [i for i in amas()]
        elif Adversaire[1] == "Tresh":
            StatM2 = [i for i in tresh()]
        elif Adversaire[1] == "Chimère":
            StatM2 = [i for i in chimere()]
        elif Adversaire[1] == "Dragon":
            StatM2 = [i for i in dragon()]
        elif Adversaire[1] == "Chien Difforme":
            StatM2 = [i for i in chienD()]
    if t == 3:
        # Premier monstre
        if Adversaire[0] == "Zombie":
            StatM1 = [i for i in zombie()]
        elif Adversaire[0] == "Fou":
            StatM1 = [i for i in fou()]
        elif Adversaire[0] == "Momie":
            StatM1 = [i for i in momie()]
        elif Adversaire[0] == "Araignée Moy":
            StatM1 = [i for i in araigneeM()]
        elif Adversaire[0] == "Gobelin":
            StatM1 = [i for i in gobelin()]
        elif Adversaire[0] == "Orc":
            StatM1 = [i for i in orc()]
        elif Adversaire[0] == "Serviteur":
            StatM1 = [i for i in serviteur()]
        elif Adversaire[0] == "Zombie armé":
            StatM1 = [i for i in zombieA()]
        elif Adversaire[0] == "Boucher":
            StatM1 = [i for i in boucher()]
        elif Adversaire[0] == "Mère araignée":
            StatM1 = [i for i in Mairaignee()]
        elif Adversaire[0] == "Chevalier noir":
            StatM1 = [i for i in ChevalierN()]
        elif Adversaire[0] == "Banshee":
            StatM1 = [i for i in banshee()]
        elif Adversaire[0] == "Amas":
            StatM1 = [i for i in amas()]
        elif Adversaire[0] == "Tresh":
            StatM1 = [i for i in tresh()]
        elif Adversaire[0] == "Chimère":
            StatM1 = [i for i in chimere()]
        elif Adversaire[0] == "Dragon":
            StatM1 = [i for i in dragon()]
        elif Adversaire[0] == "Chien Difforme":
            StatM1 = [i for i in chienD()]
        # Second Monstre
        if Adversaire[1] == "Zombie":
            StatM2 = [i for i in zombie()]
        elif Adversaire[1] == "Fou":
            StatM2 = [i for i in fou()]
        elif Adversaire[1] == "Momie":
            StatM2 = [i for i in momie()]
        elif Adversaire[1] == "Araignée Moy":
            StatM2 = [i for i in araigneeM()]
        elif Adversaire[1] == "Gobelin":
            StatM2 = [i for i in gobelin()]
        elif Adversaire[1] == "Orc":
            StatM2 = [i for i in orc()]
        elif Adversaire[1] == "Serviteur":
            StatM2 = [i for i in serviteur()]
        elif Adversaire[1] == "Zombie armé":
            StatM2 = [i for i in zombieA()]
        elif Adversaire[1] == "Boucher":
            StatM2 = [i for i in boucher()]
        elif Adversaire[1] == "Mère araignée":
            StatM2 = [i for i in Mairaignee()]
        elif Adversaire[1] == "Chevalier noir":
            StatM2 = [i for i in ChevalierN()]
        elif Adversaire[1] == "Banshee":
            StatM2 = [i for i in banshee()]
        elif Adversaire[1] == "Amas":
            StatM2 = [i for i in amas()]
        elif Adversaire[1] == "Tresh":
            StatM2 = [i for i in tresh()]
        elif Adversaire[1] == "Chimère":
            StatM2 = [i for i in chimere()]
        elif Adversaire[1] == "Dragon":
            StatM2 = [i for i in dragon()]
        elif Adversaire[1] == "Chien Difforme":
            StatM2 = [i for i in chienD()]
        # troisième monstre
        if Adversaire[2] == "Zombie":
            StatM3 = [i for i in zombie()]
        elif Adversaire[2] == "Fou":
            StatM3 = [i for i in fou()]
        elif Adversaire[2] == "Momie":
            StatM3 = [i for i in momie()]
        elif Adversaire[2] == "Araignée Moy":
            StatM3 = [i for i in araigneeM()]
        elif Adversaire[2] == "Gobelin":
            StatM3 = [i for i in gobelin()]
        elif Adversaire[2] == "Orc":
            StatM3 = [i for i in orc()]
        elif Adversaire[2] == "Serviteur":
            StatM3 = [i for i in serviteur()]
        elif Adversaire[2] == "Zombie armé":
            StatM3 = [i for i in zombieA()]
        elif Adversaire[2] == "Boucher":
            StatM3 = [i for i in boucher()]
        elif Adversaire[2] == "Mère araignée":
            StatM3 = [i for i in Mairaignee()]
        elif Adversaire[2] == "Chevalier noir":
            StatM3 = [i for i in ChevalierN()]
        elif Adversaire[2] == "Banshee":
            StatM3 = [i for i in banshee()]
        elif Adversaire[2] == "Amas":
            StatM3 = [i for i in amas()]
        elif Adversaire[2] == "Tresh":
            StatM3 = [i for i in tresh()]
        elif Adversaire[2] == "Chimère":
            StatM3 = [i for i in chimere()]
        elif Adversaire[2] == "Dragon":
            StatM3 = [i for i in dragon()]
        elif Adversaire[2] == "Chien Difforme":
            StatM3 = [i for i in chienD()]
    #Attribution des Stats pour chaque monstre + perso
    with open("FichePerso.txt", "r", encoding="utf-8") as f:
        y = f.readlines()
        x = y[2]
        HForce = int(x)
        w = y[3]
        HChance = int(w)
        z = y[7]
        Hpreci = int(z)
        p = y[5]
        HAgi = int(p)
        Hvie = int(Vie)
        m = y[1]
        Hviemax = int(m)
    if t == 1:
        M1vie = int(StatM1[0])
        M1force = int(StatM1[1])
        M1resi = int(StatM1[2])
    elif t == 2:
        M1vie = int(StatM1[0])
        M1force = int(StatM1[1])
        M1resi = int(StatM1[2])
        M2vie = int(StatM2[0])
        M2force = int(StatM2[1])
        M2resi = int(StatM2[2])
    else:
        M1vie = int(StatM1[0])
        M1force = int(StatM1[1])
        M1resi = int(StatM1[2])
        M2vie = int(StatM2[0])
        M2force = int(StatM2[1])
        M2resi = int(StatM2[2])
        M3vie = int(StatM3[0])
        M3force = int(StatM3[1])
        M3resi = int(StatM3[2])

    while AdvPresent != 3:
        print("------------------------------------------------------------------------------------------")
        print("            // Veuillez rentrer dans la console le nombre associé à l'action souhaité //")
        print()
        print("                                       1.Attaquer")
        print("                                       2.Utiliser un objet")
        print()
        print()
        print("------------------------------------------------------------------------------------------")
        A = int(input("Que voulez-vous faire?:  "))
        if A == 1:
            effacer_console()
            print("------------------------------------------------------------------------------------------")
            print("        // Veuillez rentrer dans la console le chiffre associé à l'action souhaité //")
            print()
            print("                                 1.Attaque Physique")
            print("                                 2.Attaque Magique")
            print()
            print("------------------------------------------------------------------------------------------")
            B = int(input("Choisisser votre action:  "))
            effacer_console()
            Nb = len(Adversaire)
            print("------------------------------------------------------------------------------------------")
            print("          // Veuillez rentrer dans la console le chiffre associé à l'action souhaité //", end="",
                  flush=True)
            for i in range(0, Nb):
                Num = str(i + 1) + "."
                print("\n" + Num + Adversaire[i])
            print()
            print("------------------------------------------------------------------------------------------")
            C = int(input("Qui voulez vous attaquer:  "))
            while not 1 <= C <= Nb:
                C = int(input("Veuiller rechoisir votre Action"))
            effacer_console()
            # t correspond au nombre de monstre en combat. Les combats peuvent donc varier de 1V1 à 1V3
            if t == 1:
                ApercuVH = ["■"] * Hvie
                ApercuVM1 = ["■"] * M1vie
                print("------------------------------------------------------------------------------------------")
                print()
                print("Votre vie:")
                print(ApercuVH)
                print()
                print("Vie de l'adversaire")
                print(ApercuVM1)
                print()
                print("------------------------------------------------------------------------------------------")
                if C == 1:
                    Degat = HForce - (M1resi / 2)
                    if 1 <= randint(1, 101) <= HChance:
                        Degat = int(Degat) * 2
                    print()
                    print("                                                 Lancement de l'attaque", end="", flush=True)
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    if 1 <= randint(1, 101) <= Hpreci:
                        print()
                        print("                                                       // Attaque raté ! // ")
                        time.sleep(4)
                        print()
                        print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                              flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        effacer_console()
                        Degat = M1force
                        if 1 <= randint(1, 101) <= HAgi:
                            print()
                            print("                                 // Vous avez esquivé l'attaque //")
                        else:
                            Hvie = Hvie - (Degat)
                            if Hvie <= 0:
                                print("                   ███████████████████████████")
                                print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                print("                   ███████▄░░░░░░░░░░░▄███████")
                                print("                   ██████████▄▄▄▄▄▄▄██████████")
                                print()
                                print("                       // VOUS ETES MORT //")
                                time.sleep(7)
                                exit()
                            else:
                                ApercuVH = ["■"] * Hvie
                            print("\n" + "------------------------------------------------------------------------------------------")
                            print()
                            print("Votre vie:")
                            print(ApercuVH)
                            print()
                            print("Vie de l'adversaire")
                            print(ApercuVM1)
                            print()
                            print("------------------------------------------------------------------------------------------")
                            time.sleep(5)
                            effacer_console()
                    else:
                        effacer_console()
                        M1vie = int(M1vie) - int(Degat)
                        ApercuVH = ["■"] * Hvie
                        if M1vie <= 0:
                            ApercuVM1 = ["☠"]
                            AdvPresent = 3
                        else:
                            ApercuVM1 = ["■"] * M1vie
                        print("------------------------------------------------------------------------------------------")
                        print()
                        print("Votre vie:")
                        print(ApercuVH)
                        print()
                        print("Vie de l'adversaire")
                        print(ApercuVM1)
                        print()
                        print("------------------------------------------------------------------------------------------")
                        if Yaqlq(AdvPresent) == 1:
                            print()
                            print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                                  flush=True)
                            for _ in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True)
                            effacer_console()
                            Degat = M1force
                            if 1 <= randint(1, 101) <= HAgi:
                                print()
                                print("                                 // Vous avez esquivé l'attaque //")
                            else:
                                Hvie = Hvie - (Degat)
                                if Hvie <= 0:
                                    print("                   ███████████████████████████")
                                    print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                    print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                    print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                    print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                    print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                    print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                    print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                    print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                    print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                    print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                    print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                    print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                    print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                    print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                    print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                    print("                   ███████▄░░░░░░░░░░░▄███████")
                                    print("                   ██████████▄▄▄▄▄▄▄██████████")
                                    print()
                                    print("                       // VOUS ETES MORT //")
                                    time.sleep(7)
                                    exit()
                                else:
                                    ApercuVH = ["■"] * Hvie
                                print("\n" + "------------------------------------------------------------------------------------------")
                                print()
                                print("Votre vie:")
                                print(ApercuVH)
                                print()
                                print("Vie de l'adversaire")
                                print(ApercuVM1)
                                print()
                                print("------------------------------------------------------------------------------------------")
                                time.sleep(5)
                                effacer_console()
                        else:
                            return 0
            if t == 2:
                ApercuVH = ["■"] * Hvie
                if M1vie <= 0:
                    ApercuVM1 = ["☠"]
                else:
                    ApercuVM1 = ["■"] * M1vie
                if M2vie <= 0:
                    ApercuVM2 = ["☠"]
                else:
                    ApercuVM2 = ["■"] * M2vie
                print("------------------------------------------------------------------------------------------")
                print()
                print("Votre vie:")
                print(ApercuVH)
                print()
                print("Vie des adverdaires:")
                print(ApercuVM1)
                print(ApercuVM2)
                print()
                print()
                print("------------------------------------------------------------------------------------------")
                if C == 1:
                    Degat = HForce - (M1resi / 2)
                    if 1 <= randint(1, 101) <= HChance:
                        Degat = int(Degat) * 2
                    print()
                    print("                                                 Lancement de l'attaque", end="", flush=True)
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    if 1 <= randint(1, 101) <= Hpreci:
                        print()
                        print("                                                       // Attaque raté ! // ")
                        time.sleep(4)
                        print()
                        print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                              flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        effacer_console()
                        Degat = M1force
                        if 1 <= randint(1, 101) <= HAgi:
                            print()
                            print("                                 // Vous avez esquivé l'attaque //")
                        else:
                            Hvie = Hvie - (Degat)
                            if Hvie <= 0:
                                print("                   ███████████████████████████")
                                print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                print("                   ███████▄░░░░░░░░░░░▄███████")
                                print("                   ██████████▄▄▄▄▄▄▄██████████")
                                print()
                                print("                       // VOUS ETES MORT //")
                                time.sleep(7)
                                exit()
                            else:
                                ApercuVH = ["■"] * Hvie
                            print("------------------------------------------------------------------------------------------")
                            print()
                            print("Votre vie:")
                            print(ApercuVH)
                            print()
                            print("Vie de l'adversaire")
                            print(ApercuVM1)
                            print(ApercuVM2)
                            print()
                            print("------------------------------------------------------------------------------------------")
                            time.sleep(5)
                            effacer_console()
                    else:
                        effacer_console()
                        M1vie = int(M1vie) - int(Degat)
                        ApercuVH = ["■"] * Hvie
                        AdvPresent = 0
                        if M1vie <= 0:
                            ApercuVM1 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM1 = ["■"] * M1vie
                        if M2vie <= 0:
                            ApercuVM2 = ["☠"]
                            AdvPresent = AdvPresent + 2
                        else:
                            ApercuVM2 = ["■"] * M2vie
                        print("------------------------------------------------------------------------------------------")
                        print()
                        print("Votre vie:")
                        print(ApercuVH)
                        print()
                        print("Vie de l'adversaire")
                        print(ApercuVM1)
                        print(ApercuVM2)
                        print()
                        print("------------------------------------------------------------------------------------------")
                        if Yaqlq(AdvPresent) == 1:
                            print()
                            print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                                  flush=True)
                            for _ in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True)
                            effacer_console()
                            Degat = M1force
                            if 1 <= randint(1, 101) <= HAgi:
                                print()
                                print("                                 // Vous avez esquivé l'attaque //")
                            else:
                                Hvie = Hvie - (Degat)
                                if Hvie <= 0:
                                    print("                   ███████████████████████████")
                                    print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                    print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                    print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                    print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                    print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                    print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                    print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                    print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                    print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                    print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                    print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                    print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                    print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                    print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                    print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                    print("                   ███████▄░░░░░░░░░░░▄███████")
                                    print("                   ██████████▄▄▄▄▄▄▄██████████")
                                    print()
                                    print("                       // VOUS ETES MORT //")
                                    time.sleep(7)
                                    exit()
                                else:
                                    ApercuVH = ["■"] * Hvie
                                print("------------------------------------------------------------------------------------------")
                                print()
                                print("Votre vie:")
                                print(ApercuVH)
                                print()
                                print("Vie de l'adversaire")
                                print(ApercuVM1)
                                print(ApercuVM2)
                                print()
                                print("------------------------------------------------------------------------------------------")
                                time.sleep(5)
                                effacer_console()
                        else:
                          return 0
                if C == 2:
                    Degat = HForce - (M2resi / 2)
                    if 1 <= randint(1, 101) <= HChance:
                        Degat = int(Degat) * 2
                    print()
                    print("                                                 Lancement de l'attaque", end="", flush=True)
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    if 1 <= randint(1, 101) <= Hpreci:
                        print()
                        print("                                                       // Attaque raté ! // ")
                        time.sleep(4)
                        print()
                        print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                              flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        effacer_console()
                        Degat = M2force
                        if 1 <= randint(1, 101) <= HAgi:
                            print()
                            print("                                 // Vous avez esquivé l'attaque //")
                        else:
                            Hvie = Hvie - (Degat)
                            if Hvie <= 0:
                                print("                   ███████████████████████████")
                                print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                print("                   ███████▄░░░░░░░░░░░▄███████")
                                print("                   ██████████▄▄▄▄▄▄▄██████████")
                                print()
                                print("                       // VOUS ETES MORT //")
                                time.sleep(7)
                                exit()
                            else:
                                ApercuVH = ["■"] * Hvie
                            print("------------------------------------------------------------------------------------------")
                            print()
                            print("Votre vie:")
                            print(ApercuVH)
                            print()
                            print("Vie de l'adversaire")
                            print(ApercuVM1)
                            print(ApercuVM2)
                            print()
                            print("------------------------------------------------------------------------------------------")
                            time.sleep(5)
                            effacer_console()
                    else:
                        effacer_console()
                        M2vie = int(M2vie) - int(Degat)
                        ApercuVH = ["■"] * Hvie
                        AdvPresent = 0
                        if M1vie <= 0:
                            ApercuVM1 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM1 = ["■"] * M1vie
                        if M2vie <= 0:
                            ApercuVM2 = ["☠"]
                            AdvPresent = AdvPresent + 2
                        else:
                            ApercuVM2 = ["■"] * M2vie
                        print("------------------------------------------------------------------------------------------")
                        print()
                        print("Votre vie:")
                        print(ApercuVH)
                        print()
                        print("Vie de l'adversaire")
                        print(ApercuVM1)
                        print(ApercuVM2)
                        print()
                        print("------------------------------------------------------------------------------------------")
                        if Yaqlq(AdvPresent) == 1:
                            print()
                            print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                                  flush=True)
                            for _ in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True)
                            effacer_console()
                            Degat = M2force
                            if 1 <= randint(1, 101) <= HAgi:
                                print()
                                print("                                 // Vous avez esquivé l'attaque //")
                            else:
                                Hvie = Hvie - (Degat)
                                if Hvie <= 0:
                                    print("                   ███████████████████████████")
                                    print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                    print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                    print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                    print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                    print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                    print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                    print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                    print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                    print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                    print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                    print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                    print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                    print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                    print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                    print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                    print("                   ███████▄░░░░░░░░░░░▄███████")
                                    print("                   ██████████▄▄▄▄▄▄▄██████████")
                                    print()
                                    print("                       // VOUS ETES MORT //")
                                    time.sleep(7)
                                    exit()
                                else:
                                    ApercuVH = ["■"] * Hvie
                                print("\n" + "------------------------------------------------------------------------------------------")
                                print()
                                print("Votre vie:")
                                print(ApercuVH)
                                print()
                                print("Vie de l'adversaire")
                                print(ApercuVM1)
                                print(ApercuVM2)
                                print()
                                print("------------------------------------------------------------------------------------------")
                                time.sleep(5)
                                effacer_console()
                        else:
                            return 0
            if t == 3:
                ApercuVH = ["■"] * Hvie
                if M1vie <= 0:
                    ApercuVM1 = ["☠"]
                else:
                    ApercuVM1 = ["■"] * M1vie
                if M2vie <= 0:
                    ApercuVM2 = ["☠"]
                else:
                    ApercuVM2 = ["■"] * M2vie
                if M3vie <= 0:
                    ApercuVM3 = ["☠"]
                else:
                    ApercuVM3 = ["■"] * M3vie
                print("------------------------------------------------------------------------------------------")
                print()
                print("Votre vie:")
                print(ApercuVH)
                print()
                print("Vie des adverdaires:")
                print(ApercuVM1)
                print(ApercuVM2)
                print(ApercuVM3)
                print()
                print("------------------------------------------------------------------------------------------")
                if C == 1:
                    Degat = HForce - (M1resi / 2)
                    if 1 <= randint(1, 101) <= HChance:
                        Degat = int(Degat) * 2
                    print()
                    print("                                                 Lancement de l'attaque", end="", flush=True)
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    if 1 <= randint(1, 101) <= Hpreci:
                        print()
                        print("                                                       // Attaque raté ! // ")
                        time.sleep(4)
                        print()
                        print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                              flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        effacer_console()
                        Degat = M1force
                        if 1 <= randint(1, 101) <= HAgi:
                            print()
                            print("                                 // Vous avez esquivé l'attaque //")
                        else:
                            Hvie = Hvie - (Degat)
                            if Hvie <= 0:
                                print("                   ███████████████████████████")
                                print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                print("                   ███████▄░░░░░░░░░░░▄███████")
                                print("                   ██████████▄▄▄▄▄▄▄██████████")
                                print()
                                print("                       // VOUS ETES MORT //")
                                time.sleep(7)
                                exit()
                            else:
                                ApercuVH = ["■"] * Hvie
                            print("------------------------------------------------------------------------------------------")
                            print()
                            print("Votre vie:")
                            print(ApercuVH)
                            print()
                            print("Vie de l'adversaire")
                            print(ApercuVM1)
                            print(ApercuVM2)
                            print(ApercuVM3)
                            print()
                            print("------------------------------------------------------------------------------------------")
                            time.sleep(5)
                            effacer_console()
                    else:
                        effacer_console()
                        M1vie = int(M1vie) - int(Degat)
                        ApercuVH = ["■"] * Hvie
                        AdvPresent = 0
                        if M1vie <= 0:
                            ApercuVM1 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM1 = ["■"] * M1vie
                        if M2vie <= 0:
                            ApercuVM2 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM2 = ["■"] * M2vie
                        if M3vie <= 0:
                            ApercuVM3 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM3 = ["■"] * M3vie
                        print("------------------------------------------------------------------------------------------")
                        print()
                        print("Votre vie:")
                        print(ApercuVH)
                        print()
                        print("Vie de l'adversaire")
                        print(ApercuVM1)
                        print(ApercuVM2)
                        print(ApercuVM3)
                        print()
                        print("------------------------------------------------------------------------------------------")
                        if Yaqlq(AdvPresent) == 1:
                            print()
                            print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                                  flush=True)
                            for _ in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True)
                            effacer_console()
                            Degat = M1force
                            if 1 <= randint(1, 101) <= HAgi:
                                print()
                                print("                                 // Vous avez esquivé l'attaque //")
                            else:
                                Hvie = Hvie - (Degat)
                                if Hvie <= 0:
                                    print("                   ███████████████████████████")
                                    print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                    print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                    print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                    print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                    print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                    print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                    print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                    print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                    print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                    print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                    print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                    print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                    print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                    print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                    print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                    print("                   ███████▄░░░░░░░░░░░▄███████")
                                    print("                   ██████████▄▄▄▄▄▄▄██████████")
                                    print()
                                    print("                       // VOUS ETES MORT //")
                                    time.sleep(7)
                                    exit()
                                else:
                                    ApercuVH = ["■"] * Hvie
                                print("------------------------------------------------------------------------------------------")
                                print()
                                print("Votre vie:")
                                print(ApercuVH)
                                print()
                                print("Vie de l'adversaire")
                                print(ApercuVM1)
                                print(ApercuVM2)
                                print(ApercuVM3)
                                print()
                                print("------------------------------------------------------------------------------------------")
                                time.sleep(5)
                                effacer_console()
                        else:
                            return 0
                elif C == 2:
                    Degat = HForce - (M2resi / 2)
                    if 1 <= randint(1, 101) <= HChance:
                        Degat = int(Degat) * 2
                    print()
                    print("                                                 Lancement de l'attaque", end="", flush=True)
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    if 1 <= randint(1, 101) <= Hpreci:
                        print()
                        print("                                                       // Attaque raté ! // ")
                        time.sleep(4)
                        print()
                        print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                              flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        effacer_console()
                        Degat = M2force
                        if 1 <= randint(1, 101) <= HAgi:
                            print()
                            print("                                 // Vous avez esquivé l'attaque //")
                        else:
                            Hvie = Hvie - (Degat)
                            if Hvie <= 0:
                                print("                   ███████████████████████████")
                                print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                print("                   ███████▄░░░░░░░░░░░▄███████")
                                print("                   ██████████▄▄▄▄▄▄▄██████████")
                                print()
                                print("                       // VOUS ETES MORT //")
                                time.sleep(7)
                                exit()
                            else:
                                ApercuVH = ["■"] * Hvie
                            print("------------------------------------------------------------------------------------------")
                            print()
                            print("Votre vie:")
                            print(ApercuVH)
                            print()
                            print("Vie de l'adversaire")
                            print(ApercuVM1)
                            print(ApercuVM2)
                            print(ApercuVM3)
                            print()
                            print()
                            print("------------------------------------------------------------------------------------------")
                            time.sleep(5)
                            effacer_console()
                    else:
                        effacer_console()
                        M2vie = int(M2vie) - int(Degat)
                        ApercuVH = ["■"] * Hvie
                        AdvPresent = 0
                        if M1vie <= 0:
                            ApercuVM1 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM1 = ["■"] * M1vie
                        if M2vie <= 0:
                            ApercuVM2 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM2 = ["■"] * M2vie
                        if M3vie <= 0:
                            ApercuVM3 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM3 = ["■"] * M3vie

                        print("------------------------------------------------------------------------------------------")
                        print()
                        print("Votre vie:")
                        print(ApercuVH)
                        print()
                        print("Vie de l'adversaire")
                        print(ApercuVM1)
                        print(ApercuVM2)
                        print(ApercuVM3)
                        print()
                        print("------------------------------------------------------------------------------------------")
                        if Yaqlq(AdvPresent) == 1:
                            print()
                            print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                                  flush=True)
                            for _ in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True)
                            effacer_console()
                            Degat = M2force
                            if 1 <= randint(1, 101) <= HAgi:
                                print()
                                print("                                 // Vous avez esquivé l'attaque //")
                            else:
                                Hvie = Hvie - (Degat)
                                if Hvie <= 0:
                                    print("                   ███████████████████████████")
                                    print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                    print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                    print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                    print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                    print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                    print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                    print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                    print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                    print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                    print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                    print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                    print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                    print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                    print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                    print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                    print("                   ███████▄░░░░░░░░░░░▄███████")
                                    print("                   ██████████▄▄▄▄▄▄▄██████████")
                                    print()
                                    print("                       // VOUS ETES MORT //")
                                    time.sleep(7)
                                    exit()
                                else:
                                    ApercuVH = ["■"] * Hvie
                                print("------------------------------------------------------------------------------------------")
                                print()
                                print("Votre vie:")
                                print(ApercuVH)
                                print()
                                print("Vie de l'adversaire")
                                print(ApercuVM1)
                                print(ApercuVM2)
                                print(ApercuVM3)
                                print("------------------------------------------------------------------------------------------")
                                time.sleep(5)
                                effacer_console()
                        else:
                            return 0
                if C == 3:
                    Degat = HForce - (M3resi / 2)
                    if 1 <= randint(1, 101) <= HChance:
                        Degat = int(Degat) * 2
                    print()
                    print("                                                 Lancement de l'attaque", end="", flush=True)
                    for _ in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    if 1 <= randint(1, 101) <= Hpreci:
                        print()
                        print("                                                       // Attaque raté ! // ")
                        time.sleep(4)
                        print()
                        print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                              flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        effacer_console()
                        Degat = M3force
                        if 1 <= randint(1, 101) <= HAgi:
                            print()
                            print("                                 // Vous avez esquivé l'attaque //")
                        else:
                            Hvie = Hvie - (Degat)
                            if Hvie <= 0:
                                print("                   ███████████████████████████")
                                print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                print("                   ███████▄░░░░░░░░░░░▄███████")
                                print("                   ██████████▄▄▄▄▄▄▄██████████")
                                print()
                                print("                       // VOUS ETES MORT //")
                                time.sleep(7)
                                exit()
                            else:
                                ApercuVH = ["■"] * Hvie
                            print("------------------------------------------------------------------------------------------")
                            print()
                            print("Votre vie:")
                            print(ApercuVH)
                            print()
                            print("Vie de l'adversaire")
                            print(ApercuVM1)
                            print(ApercuVM2)
                            print(ApercuVM3)
                            print()
                            print("------------------------------------------------------------------------------------------")
                            time.sleep(5)
                            effacer_console()
                    else:
                        effacer_console()
                        M3vie = int(M3vie) - int(Degat)
                        ApercuVH = ["■"] * Hvie
                        AdvPresent = 0
                        if M1vie <= 0:
                            ApercuVM1 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM1 = ["■"] * M1vie
                        if M2vie <= 0:
                            ApercuVM2 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM2 = ["■"] * M2vie
                        if M3vie <= 0:
                            ApercuVM3 = ["☠"]
                            AdvPresent = AdvPresent + 1
                        else:
                            ApercuVM3 = ["■"] * M3vie
                        print("------------------------------------------------------------------------------------------")
                        print()
                        print("Votre vie:")
                        print(ApercuVH)
                        print()
                        print("Vie de l'adversaire")
                        print(ApercuVM1)
                        print(ApercuVM2)
                        print(ApercuVM3)
                        print()
                        print("------------------------------------------------------------------------------------------")
                        if Yaqlq(AdvPresent) == 1:
                            print()
                            print("                             // Tour de l'adversaire: Tour d'attaque //", end="",
                                  flush=True)
                            for _ in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True)
                            effacer_console()
                            Degat = M3force
                            if 1 <= randint(1, 101) <= HAgi:
                                print()
                                print("                                 // Vous avez esquivé l'attaque //")
                            else:
                                Hvie = Hvie - (Degat)
                                if Hvie <= 0:
                                    print("                   ███████████████████████████")
                                    print("                   ███████▀▀▀░░░░░░░▀▀▀███████")
                                    print("                   ████▀░░░░░░░░░░░░░░░░░▀████")
                                    print("                   ███│░░░░░░░░░░░░░░░░░░░│███")
                                    print("                   ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
                                    print("                   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
                                    print("                   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
                                    print("                   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
                                    print("                   ██▌░│██████▌░░░▐██████│░▐██")
                                    print("                   ███░│▐███▀▀░░▄░░▀▀███▌│░███")
                                    print("                   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
                                    print("                   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
                                    print("                   ████▄─┘██▌░░░░░░░▐██└─▄████")
                                    print("                   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
                                    print("                   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
                                    print("                   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
                                    print("                   ███████▄░░░░░░░░░░░▄███████")
                                    print("                   ██████████▄▄▄▄▄▄▄██████████")
                                    print()
                                    print("                       // VOUS ETES MORT //")
                                    time.sleep(7)
                                    exit()
                                else:
                                    ApercuVH = ["■"] * Hvie
                                print("------------------------------------------------------------------------------------------")
                                print()
                                print("Votre vie:")
                                print(ApercuVH)
                                print()
                                print("Vie de l'adversaire")
                                print(ApercuVM1)
                                print(ApercuVM2)
                                print(ApercuVM3)
                                print()
                                print("------------------------------------------------------------------------------------------")
                                time.sleep(5)
                                effacer_console()
                        else: return 0

        #Système d'objet
        elif A == 2:
            effacer_console()
            with open("FichePerso.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
                if len(lignes) >= 10:
                    y = lignes[9]
                    x = [j.strip() for j in y.split(",")]
                    Nb = len(x)
                    print("------------------------------------------------------------------------------------------")
                    print()
                    print("                                  Voici Votre Inventaire:")
                    print("       // Veuillez rentrer dans la console le nom de l'objet que vous souhaiter utiliser //",
                          end="",
                          flush=True)
                    for i in range(0, Nb):
                        Num = str(i + 1) + "."
                        print("\n" + Num + x[i])
                    print()
                    print("            Entrer:'retour' dans la console si vous voulez ne pas utiliser d'objet")
                    print("------------------------------------------------------------------------------------------")
                    Objet = str(input("Quel Objet Choississez-vous: "))
                    if Objet != "retour":
                        while not Objet in x:
                            Objet = input("Veuillez rechoisir: ")

                        if Objet == "Kit de soin" and Objet in x:
                            Hvie = Hvie + 5
                            if Hvie >= Hviemax:
                                Hvie = Hviemax
                            stp = x.index("Kit de soin")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Kit de crochetage" and Objet in x:
                            print()
                            print("                            // Malheuresement cet objet n'est pas utilisable en combat //")
                            time.sleep(3)
                            effacer_console()
                        if Objet == "Potion du Berserker" and Objet in x:
                            HForce = HForce + 6
                            stp = x.index("Potion du Berserker")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Talisman de Rohen" and Objet in x:
                            print()
                            print("                                         Le talisman dissipe le mal", end="",
                                  flush=True)
                            for _ in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True)
                            AdvPresent = 3
                            effacer_console()
                        if Objet == "Chaussure du renard" and Objet in x:
                            print()
                            print("                          // Malheuresement cet objet n'est pas utilisable en combat //")
                            time.sleep(3)
                            effacer_console()

                        if Objet == "Scie à os" and Objet in x:
                            print()
                            print("                            // Malheuresement cet objet n'est pas utilisable en combat //")
                            time.sleep(3)
                            effacer_console()

                        if Objet == "Pomme" and Objet in x:
                            Hvie = Hvie + 1
                            if Hvie >= Hviemax:
                                Hvie = Hviemax
                            stp = x.index("Pomme")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Fruit sec" and Objet in x:
                            Hvie = Hvie + 1
                            if Hvie >= Hviemax:
                                Hvie = Hviemax
                            stp = x.index("Fruit sec")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Bouteille d'eau" and Objet in x:
                            Hvie = Hvie + 2
                            if Hvie >= Hviemax:
                                Hvie = Hviemax
                            stp = x.index("Bouteille d'eau")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Nectar de pêche" and Objet in x:
                            Hvie = Hvie + 2
                            if Hvie >= Hviemax:
                                Hvie = Hviemax
                            stp = x.index("Nectar de pêche")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Viande séchée" and Objet in x:
                            Hvie = Hvie + 3
                            if Hvie >= Hviemax:
                                Hvie = Hviemax
                            stp = x.index("Viande séchée")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Pilon de Poulet" and Objet in x:
                            Hvie = Hvie + 3
                            if Hvie >= Hviemax:
                                Hvie = Hviemax
                            stp = x.index("Pilon de Poulet")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Part de gateau au miel" and Objet in x:
                            Hvie = Hvie + 4
                            if Hvie >= Hviemax:
                                Hvie = Hviemax
                            stp = x.index("Part de gateau au miel")
                            x.pop(stp)
                            del lignes[9]
                            with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                f.writelines(lignes)
                                f.writelines(",".join(x))
                            effacer_console()
                        if Objet == "Alcool" and Objet in x:
                            print()
                            print("                            // Malheuresement cet objet n'est pas utilisable en combat //")
                            time.sleep(3)
                            effacer_console()

                        if Objet == "Opium" and Objet in x:
                            print()
                            print("                            // Malheuresement cet objet n'est pas utilisable en combat //")
                            time.sleep(3)
                            effacer_console()

                        if Objet == "Traitement de fleur médicinal" and Objet in x:
                            print()
                            print(
                                "                            // Malheuresement cet objet n'est pas utilisable en combat //")
                            time.sleep(3)
                            effacer_console()
                    else:
                        effacer_console()
                else:
                    print("                     Vous n'avez pas d'Objet dans votre inventaire")
                    time.sleep(3)
                    effacer_console()




print()
print("                                                 Votre Aventure commence Maintenant",end="",flush=True             )
for _ in range(3):
   time.sleep(1)
   print("!", end="", flush=True)
effacer_console()

#système de tour
def FouilleMultiple():
    TAS = randint(1, 4)
    TAS2 = randint(1, 10)
    if TAS == 1:
        return 2
    elif TAS2 == 1:
        return 3
    else:
        return 1
def ChoixFouilleNormal():
    TAS = randint(1, 10)
    return TAS
def ChoixFouilleSpe():
    TAS = randint(1, 6)
    return TAS
FinDJ=0
FDT=0
NBT=0
with open("FichePerso.txt", "r", encoding="utf-8") as f:
    y = f.readlines()
    Hvie = int(y[1])
HSM = 10
HSaturation = 10
while FinDJ==0:
 FDT = 0
 NBT=NBT+1
 Adversaire=[]
 CombatStop=[]
 if NBT == 1:
     with open("Desciption.txt", "r", encoding="utf-8") as f:
         y = []
         Texte = f.readlines()
         n = len(Texte)
         for i in range(0, n):
             y.append(Texte[i])
     Desc = y[42]
     print("------------------------------------------------------------------------------------------")
     print()
     print(Desc.replace(".", ".\n"))
     print("------------------------------------------------------------------------------------------")
     input("                         Appuyer sur 'Enter' pour rentrer dans le chateau")
     effacer_console()
     DejaFOuiller = 0
     while FDT != 1:
         def FouilleMultiple():
             TAS = randint(1, 4)
             TAS2 = randint(1, 10)
             if TAS == 1:
                 return 2
             elif TAS2 == 1:
                 return 3
             else:
                 return 1


         def ChoixFouilleNormal():
             TAS = randint(1, 10)
             return TAS


         def ChoixFouilleSpe():
             TAS = randint(1, 6)
             return TAS


         effacer_console()
         print("------------------------------------------------------------------------------------------------------")
         print("            // Veuillez rentrer dans la console le chiffre associé à l'action souhaité // ")
         print()
         print("                                  1. Fouiller la pièce ")
         print("                                  2. S'assurer de son bien être")
         print("                                  3. Utiliser un objet")
         print("                                  4. Se déplacer vers une nouvelle salle")
         print()
         print("------------------------------------------------------------------------------------------------------")
         Choix = int(input("Que voulez vous faire: "))
         while Choix != 1 and Choix != 2 and Choix != 3 and Choix != 4:
             Choix = int(input("Veuiller rechoisir: "))
         if Choix == 1:
             if DejaFOuiller >= 1:
                 print()
                 print("                          Malheuresement, vous avez déjà fouillé cette salle")
                 time.sleep(4)
                 effacer_console()
             else:
                 print()
                 print("                                               Vous fouiller la salle", end="", flush=True)
                 for _ in range(3):
                     time.sleep(1)
                     print(".", end="", flush=True)
                 effacer_console()
                 # Chance d'avoir un item
                 if 1 <= randint(1, 101) <= 75:
                     ObjetT = []
                     for j in range(0, FouilleMultiple()):
                         # Item rare
                         tas = ChoixFouilleSpe()
                         tas2 = ChoixFouilleNormal()
                         if randint(1, 3) == 1:
                             if tas == 1:
                                 ObjetT.append("Kit de soin")
                             elif tas == 2:
                                 ObjetT.append("Kit de soin")
                             elif tas == 3:
                                 ObjetT.append("Potion du Berserker")
                             elif tas == 4:
                                 ObjetT.append("Talisman de Rohen")
                             elif tas == 5:
                                 ObjetT.append("Scie à os")
                             elif tas == 6:
                                 ObjetT.append("Kit de soin")
                         # Item normal
                         else:
                             if tas2 == 1:
                                 ObjetT.append("Pomme")
                             if tas2 == 2:
                                 ObjetT.append("Nectar de pêche")
                             if tas2 == 3:
                                 ObjetT.append("Alcool")
                             if tas2 == 4:
                                 ObjetT.append("Viande séchée")
                             if tas2 == 5:
                                 ObjetT.append("Pilon de Poulet")
                             if tas2 == 6:
                                 ObjetT.append("Fruit sec")
                             if tas2 == 7:
                                 ObjetT.append("Traitement de fleur médicinal")
                             if tas2 == 8:
                                 ObjetT.append("Opium")
                             if tas2 == 9:
                                 ObjetT.append("Part de gateau au miel")
                             if tas2 == 10:
                                 ObjetT.append("Bouteille d'eau")
                     Nb = len(ObjetT)
                     DejaFOuiller += 1
                     print(
                         "------------------------------------------------------------------------------------------------------")
                     print("                                      Vous avez trouvé:")
                     for i in range(0, Nb):
                         Num = str(i + 1) + "."
                         print("\n" + Num + ObjetT[i])
                     print()
                     print(
                         "------------------------------------------------------------------------------------------------------")
                     print("                             Appuyer sur 'Enter' pour continuer...")
                     input("")
                     with open("FichePerso.txt", "r", encoding="utf-8") as f:
                         l = f.readlines()
                     if l:
                         dl = l[-1].strip()
                         nl = dl + "," + ",".join(ObjetT)
                         l[-1] = nl + "\n"
                     else:
                         l.append(" ".join(ObjetT) + "\n")
                     with open("FichePerso.txt", "w", encoding="utf-8") as f:
                         f.writelines(l)
                     effacer_console()
                 else:
                     print()
                     print("           Malheuresement, rien dans cette pièce ne peux vous aider dans votre quête",
                           end="",
                           flush=True)
                     for _ in range(3):
                         time.sleep(1)
                         print(".", end="", flush=True)
                     DejaFOuiller += 1
                     effacer_console()
         elif Choix == 2:
             effacer_console()
             ApercuHvie = ["■"] * Hvie
             ApercuHsatu = ["▲"] * HSaturation
             ApercuHFolie = ["●"] * HSM
             print(
                 "------------------------------------------------------------------------------------------------------")
             print()
             print("Barre de vie:")
             print(ApercuHvie)
             print()
             print("Barre de saturation:")
             print(ApercuHsatu)
             print()
             print("Barre de votre santé mentale:")
             print(ApercuHFolie)
             print()
             print(
                 "------------------------------------------------------------------------------------------------------")
             print("                                 Appuer sur 'Enter' pour retourner au menu")
             input()
             effacer_console()
         elif Choix == 3:
             with open("FichePerso.txt", "r", encoding="utf-8") as f:
                 lignes = f.readlines()
                 if len(lignes) >= 10:
                     y = lignes[9]
                     x = [j.strip() for j in y.split(",")]
                     Nb = len(x)
                     effacer_console()
                     print("------------------------------------------------------------------------------------------")
                     print()
                     print("                                  Voici Votre Inventaire:")
                     print(
                         "       // Veuillez rentrer dans la console le nom de l'objet que vous souhaiter utiliser //",
                         end="",
                         flush=True)
                     for i in range(0, Nb):
                         Num = str(i + 1) + "."
                         print("\n" + Num + x[i])
                     print()
                     print("            Entrer:'retour' dans la console si vous voulez ne pas utiliser d'objet")
                     print("------------------------------------------------------------------------------------------")
                     Objet = str(input("Quel Objet voulez-vous utiliser: "))
                     if Objet != "retour":
                         while not Objet in x and Objet != "retour":
                             Objet = input("Veuillez rechoisir: ")
                             effacer_console()

                         if Objet == "Kit de soin" and Objet in x:
                             with open("FichePerso.txt", "r", encoding="utf-8") as f:
                                 y = f.readlines()
                                 m = y[1]
                                 Hviemax = int(m)
                             Hvie = Hvie + 5
                             if Hvie >= Hviemax:
                                 Hvie = Hviemax
                             stp = x.index("Kit de soin")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Kit de crochetage" and Objet in x:
                             print()
                             print(
                                 "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                             time.sleep(3)
                             effacer_console()
                         if Objet == "Potion du Berserker" and Objet in x:
                             print()
                             print(
                                 "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                             time.sleep(3)
                             effacer_console()
                         if Objet == "Talisman de Rohen" and Objet in x:
                             print()
                             print(
                                 "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                             time.sleep(3)
                             effacer_console()
                         if Objet == "Chaussure du renard" and Objet in x:
                             print()
                             print(
                                 "                          // Malheuresement cet objet n'est pas utilisable en combat //")
                             time.sleep(3)
                             effacer_console()
                         if Objet == "Scie à os" and Objet in x:
                             Hvie = Hvie - 3
                             print()
                             print("                            Vous vous sciez la jambe", end="", flush=True)
                             for _ in range(3):
                                 time.sleep(1)
                                 print("!", end="", flush=True)
                             effacer_console()
                         if Objet == "Pomme" and Objet in x or Objet == "Fruit sec" and Objet in x:
                             HSaturation = HSaturation + 1
                             if HSaturation >= 10:
                                 HSaturation = 10
                             effacer_console()
                         if Objet == "Bouteille d'eau" and Objet in x or Objet == "Nectar de pêche" and Objet in x:
                             HSaturation = HSaturation + 2
                             if HSaturation >= 10:
                                 HSaturation = 10
                             effacer_console()
                         if Objet == "Viande séchée" and Objet in x:
                             HSaturation = HSaturation + 3
                             if HSaturation >= 10:
                                 HSaturation = 10
                             effacer_console()
                         if Objet == "Pilon de Poulet" and Objet in x or Objet == "Part de gateau au miel" and Objet in x:
                             HSaturation = HSaturation + 4
                             if HSaturation >= 10:
                                 HSaturation = 10
                             effacer_console()
                         if Objet == "Alcool" and Objet in x:
                             HSM = HSM + 2
                             if HSM >= 10:
                                 HSM = 10
                             effacer_console()
                         if Objet == "Opium" and Objet in x:
                             HSM = HSM + 5
                             if HSM >= 10:
                                 HSM = 10
                             effacer_console()
                         if Objet == "Traitement de fleur médicinal" and Objet in x:
                             HSM = HSM + 3
                             if HSM >= 10:
                                 HSM = 10
                             effacer_console()
                     else:
                         effacer_console()
                 else:
                     print("                     Vous n'avez pas d'Objet dans votre inventaire")
                     time.sleep(3)
                     effacer_console()
         elif Choix == 4:
             print()
             print("                       Vous décidez de changer de salle", end="", flush=True)
             for _ in range(3):
                 time.sleep(1)
                 print(".", end="", flush=True)
             FDT = 1
             effacer_console()
 #rencontre bagar
 else:
  if 1<=randint(1,101)<=81:
    n = rencontreMulti()
    for j in range(0, n):
     if 1<=randint(1,101)<=6:
         y=rencontre_spe()
         if y==1:
          #Dragon
          Adversaire.append("Dragon")
         elif y==2:
          #Banshee
          Adversaire.append("Banshee")
         elif y==3:
          #Gargouille
          CombatStop.append("Gargouille")
         elif y==4:
          #Boule
          Adversaire.append("Amas")
         elif y==5:
          #Chien difforme
          Adversaire.append("Chien Difforme")
         elif y==6:
          #Chimère
          Adversaire.append("Chimère")
     else:
         z=rencontreC()
         if z == 1:
             # Zombie
             Adversaire.append("Zombie")
         elif z == 2:
             # momie
             Adversaire.append("Momie")
         elif z == 3:
             # Araignée moyenne
             Adversaire.append("Araignée Moy")
         elif z == 4:
             # Gobelins
             Adversaire.append("Gobelin")
         elif z == 5:
             # Fou
             Adversaire.append("Fou")
         elif z == 6:
             # Serviteur
             Adversaire.append("Serviteur")
         elif z == 7:
             # Zombies armée
             Adversaire.append("Zombie armé")
         elif z == 8:
             # Orc
             Adversaire.append("Orc")
         elif z == 9:
             # Boucher
             Adversaire.append("Boucher")
         elif z == 10:
             # Mère araignée
             Adversaire.append("Mère araignée")
         elif z == 11:
             # Chevalier noir
             Adversaire.append("Chevalier noir")

  #Description salle
  with open("Desciption.txt", "r", encoding="utf-8") as f:
         y = []
         Texte = f.readlines()
         n = len(Texte)
         for i in range(0, n):
             y.append(Texte[i])
  n = randint(4, 8)
  Desc = y[n]
  print("------------------------------------------------------------------------------------------")
  print()
  print(Desc.replace(".", ".\n"))
  print("------------------------------------------------------------------------------------------")
  input("                                      Appuyer sur 'Enter' pour continuer")
  effacer_console()
  #Combat si Adversaire présent
  t=len(Adversaire)
  if t != 0:
         if t == 1:
             if Adversaire[0] == "Zombie":
                with open("Desciption.txt", 'r', encoding="utf-8") as f:
                  y =f.readlines()
                  DescM1 = y[32]
             if Adversaire[0] == "Fou":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[33]
             if Adversaire[0] == "Momie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[31]
             if Adversaire[0] == "Araignée Moy":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[34]
             if Adversaire[0] == "Gobelin":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[30]
             if Adversaire[0] == "Serviteur":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[38]
             if Adversaire[0] == "Zombie armé":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[35]
             if Adversaire[0] == "Orc":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[37]
             if Adversaire[0] == "Boucher":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[36]
             if Adversaire[0] == "Mère araignée":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[39]
             if Adversaire[0] == "Chevalier noir":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[40]
             if Adversaire[0] == "Dragon":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[20]
             if Adversaire[0] == "Banshee":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[25]
             if Adversaire[0] == "Gargouille":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[21]
             if Adversaire[0] == "Chien Difforme":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[22]
             if Adversaire[0] == "Chimère":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[24]
             if Adversaire[0] == "Tresh":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[23]
             if Adversaire[0] == "Amas":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[26]
             print("------------------------------------------------------------------------------------------")
             print()
             print("Alors que vous rentrer dans la salle," + DescM1.replace(".", ".\n"))
             print()
             print("------------------------------------------------------------------------------------------")
             print("                          Appuyer sur 'Enter' pour commencer la combat")
             input()
             effacer_console()
             combat(Adversaire, Hvie)
             time.sleep(3)
             effacer_console()
             HSaturation =HSaturation - 2
             HSM =HSM - 1
             DejaFOuiller = 0
             while FDT == 0:
                 print("------------------------------------------------------------------------------------------------------")
                 print("            // Veuillez rentrer dans la console le chiffre associé à l'action souhaité // ")
                 print()
                 print("                                  1. Fouiller la pièce ")
                 print("                                  2. S'assurer de son bien être")
                 print("                                  3. Utiliser un objet")
                 print("                                  4. Se déplacer vers une nouvelle salle")
                 print()
                 print("------------------------------------------------------------------------------------------------------")
                 Choix = int(input("Que voulez vous faire: "))
                 while Choix != 1 and Choix != 2 and Choix != 3 and Choix != 4:
                     Choix = int(input("Veuiller rechoisir: "))
                 if Choix == 1:
                     if DejaFOuiller >= 1:
                         print()
                         print("                          Malheuresement, vous avez déjà fouillé cette salle")
                         time.sleep(4)
                         effacer_console()
                     else:
                         print()
                         print("                                               Vous fouiller la salle", end="",
                               flush=True)
                         for _ in range(3):
                             time.sleep(1)
                             print(".", end="", flush=True)
                         effacer_console()
                         # Chance d'avoir un item
                         if 1 <= randint(1, 101) <= 75:
                             ObjetT = []
                             for j in range(0, FouilleMultiple()):
                                 # Item rare
                                 tas = ChoixFouilleSpe()
                                 tas2 = ChoixFouilleNormal()
                                 if randint(1, 3) == 1:
                                     if tas == 1:
                                         ObjetT.append("Kit de soin")
                                     elif tas == 2:
                                         ObjetT.append("Kit de soin")
                                     elif tas == 3:
                                         ObjetT.append("Potion du Berserker")
                                     elif tas == 4:
                                         ObjetT.append("Talisman de Rohen")
                                     elif tas == 5:
                                         ObjetT.append("Scie à os")
                                     elif tas == 6:
                                         ObjetT.append("Kit de soin")
                                 # Item normal
                                 else:
                                     if tas2 == 1:
                                         ObjetT.append("Pomme")
                                     if tas2 == 2:
                                         ObjetT.append("Nectar de pêche")
                                     if tas2 == 3:
                                         ObjetT.append("Alcool")
                                     if tas2 == 4:
                                         ObjetT.append("Viande séchée")
                                     if tas2 == 5:
                                         ObjetT.append("Pilon de Poulet")
                                     if tas2 == 6:
                                         ObjetT.append("Fruit sec")
                                     if tas2 == 7:
                                         ObjetT.append("Traitement de fleur médicinal")
                                     if tas2 == 8:
                                         ObjetT.append("Opium")
                                     if tas2 == 9:
                                         ObjetT.append("Part de gateau au miel")
                                     if tas2 == 10:
                                         ObjetT.append("Bouteille d'eau")
                             Nb = len(ObjetT)
                             DejaFOuiller += 1
                             print("------------------------------------------------------------------------------------------------------")
                             print("                                      Vous avez trouvé:")
                             for i in range(0, Nb):
                                 Num = str(i + 1) + "."
                                 print("\n" + Num + ObjetT[i])
                             print()
                             print("------------------------------------------------------------------------------------------------------")
                             print("                             Appuyer sur 'Enter' pour continuer...")
                             input("")
                             with open("FichePerso.txt", "r", encoding="utf-8") as f:
                                 l = f.readlines()
                             if l:
                                 dl = l[-1].strip()
                                 nl = dl + "," + ",".join(ObjetT)
                                 l[-1] = nl + "\n"
                             else:
                                 l.append(" ".join(ObjetT) + "\n")
                             with open("FichePerso.txt", "w", encoding="utf-8") as f:
                                 f.writelines(l)
                         else:
                             print()
                             print("           Malheuresement, rien dans cette pièce ne peux vous aider dans votre quête",
                                 end="",
                                 flush=True)
                             for _ in range(3):
                                 time.sleep(1)
                                 print(".", end="", flush=True)
                             DejaFOuiller += 1
                             effacer_console()
                 elif Choix == 2:
                     effacer_console()
                     ApercuHvie = ["■"] * Hvie
                     ApercuHsatu = ["▲"] * HSaturation
                     ApercuHFolie = ["●"] * HSM
                     print("------------------------------------------------------------------------------------------------------")
                     print()
                     print("Barre de vie:")
                     print(ApercuHvie)
                     print()
                     print("Barre de saturation:")
                     print(ApercuHsatu)
                     print()
                     print("Barre de votre santé mentale:")
                     print(ApercuHFolie)
                     print()
                     print("------------------------------------------------------------------------------------------------------")
                     print("                                 Appuer sur 'Enter' pour retourner au menu")
                     input()
                     effacer_console()
                 elif Choix == 3:
                     with open("FichePerso.txt", "r", encoding="utf-8") as f:
                         lignes = f.readlines()
                         if len(lignes) >= 10:
                             y = lignes[9]
                             x = [j.strip() for j in y.split(",")]
                             Nb = len(x)
                             effacer_console()
                             print(
                                 "------------------------------------------------------------------------------------------")
                             print()
                             print("                                  Voici Votre Inventaire:")
                             print(
                                 "       // Veuillez rentrer dans la console le nom de l'objet que vous souhaiter utiliser //",
                                 end="",
                                 flush=True)
                             for i in range(0, Nb):
                                 Num = str(i + 1) + "."
                                 print("\n" + Num + x[i])
                             print()
                             print("            Entrer:'retour' dans la console si vous voulez ne pas utiliser d'objet")
                             print(
                                 "------------------------------------------------------------------------------------------")
                             Objet = str(input("Quel Objet voulez-vous utiliser: "))
                             if Objet != "retour":
                                 while not Objet in x and Objet != "retour":
                                     Objet = input("Veuillez rechoisir: ")

                                 if Objet == "Kit de soin" and Objet in x:
                                     with open("FichePerso.txt", "r", encoding="utf-8") as f:
                                         y = f.readlines()
                                         m = y[1]
                                         Hviemax = int(m)
                                     Hvie = Hvie + 5
                                     if Hvie >= Hviemax:
                                         Hvie = Hviemax
                                     stp = x.index("Kit de soin")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Kit de crochetage" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Potion du Berserker" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Talisman de Rohen" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Chaussure du renard" and Objet in x:
                                     print()
                                     print(
                                         "                          // Malheuresement cet objet n'est pas utilisable en combat //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Scie à os" and Objet in x:
                                     Hvie = Hvie - 3
                                     print()
                                     print("                            Vous vous sciez la jambe", end="", flush=True)
                                     for _ in range(3):
                                         time.sleep(1)
                                         print("!", end="", flush=True)
                                     stp = x.index("Scie à os")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Pomme" and Objet in x:
                                     HSaturation = HSaturation + 1
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Pomme")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Fruit sec" and Objet in x:
                                     HSaturation = HSaturation + 1
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Fruit sec")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Bouteille d'eau" and Objet in x:
                                     HSaturation = HSaturation + 2
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Bouteille d'eau")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Nectar de pêche" and Objet in x:
                                     HSaturation = HSaturation + 2
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Nectar de pêche")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Viande séchée" and Objet in x:
                                     HSaturation = HSaturation + 3
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Viande séchée")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Pilon de Poulet" and Objet in x:
                                     HSaturation = HSaturation + 4
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Pilon de Poulet")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Part de gateau au miel" and Objet in x:
                                     HSaturation = HSaturation + 4
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Part de gateau au miel")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Alcool" and Objet in x:
                                     HSM = HSM + 2
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Alcool")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Opium" and Objet in x:
                                     HSM = HSM + 5
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Opium")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Traitement de fleur médicinal" and Objet in x:
                                     HSM = HSM + 3
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Traitement de fleur médicinal")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                             else:
                                 effacer_console()
                         else:
                             print("                     Vous n'avez pas d'Objet dans votre inventaire")
                             time.sleep(3)
                             effacer_console()
                 elif Choix == 4:
                     print()
                     print("                       Vous décidez de changer de salle", end="", flush=True)
                     for _ in range(3):
                         time.sleep(1)
                         print(".", end="", flush=True)
                     FDT = 1
                     effacer_console()
         if t == 2:
             if Adversaire[0] == "Zombie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[32]
             if Adversaire[0] == "Fou":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[33]
             if Adversaire[0] == "Momie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[31]
             if Adversaire[0] == "Araignée Moy":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[34]
             if Adversaire[0] == "Gobelin":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[30]
             if Adversaire[0] == "Serviteur":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[38]
             if Adversaire[0] == "Zombie armé":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[35]
             if Adversaire[0] == "Orc":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[37]
             if Adversaire[0] == "Boucher":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[36]
             if Adversaire[0] == "Mère araignée":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[39]
             if Adversaire[0] == "Chevalier noir":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[40]
             if Adversaire[0] == "Dragon":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[20]
             if Adversaire[0] == "Banshee":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[25]
             if Adversaire[0] == "Gargouille":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[21]
             if Adversaire[0] == "Chien Difforme":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[22]
             if Adversaire[0] == "Chimère":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[24]
             if Adversaire[0] == "Tresh":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[23]
             if Adversaire[0] == "Amas":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[26]
             # Choix de la deuxième description
             if Adversaire[1] == "Zombie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[32]
             if Adversaire[1] == "Fou":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[33]
             if Adversaire[1] == "Momie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[31]
             if Adversaire[1] == "Araignée Moy":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[34]
             if Adversaire[1] == "Gobelin":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[30]
             if Adversaire[1] == "Serviteur":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[38]
             if Adversaire[1] == "Zombie armé":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[35]
             if Adversaire[1] == "Orc":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[37]
             if Adversaire[1] == "Boucher":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[36]
             if Adversaire[1] == "Mère araignée":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[39]
             if Adversaire[1] == "Chevalier noir":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[40]
             if Adversaire[1] == "Dragon":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[20]
             if Adversaire[1] == "Banshee":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[25]
             if Adversaire[1] == "Gargouille":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[21]
             if Adversaire[1] == "Chien Difforme":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[22]
             if Adversaire[1] == "Chimère":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[24]
             if Adversaire[1] == "Tresh":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[23]
             if Adversaire[1] == "Amas":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[26]
             print("------------------------------------------------------------------------------------------")
             print()
             print("Alors que vous rentrer dans la salle," + DescM1.replace(".", ".\n"))
             print("Mais ce n'est pas tout," + DescM2.replace(".", ".\n"))
             print()
             print("------------------------------------------------------------------------------------------")
             print("                          Appuyer sur 'Enter' pour commencer la combat")
             input()
             effacer_console()
             combat(Adversaire, Hvie)
             time.sleep(3)
             effacer_console()
             HSaturation = HSaturation - 3
             HSM = HSM - 2
             DejaFOuiller = 0
             while FDT == 0:
                 print("------------------------------------------------------------------------------------------------------")
                 print("            // Veuillez rentrer dans la console le chiffre associé à l'action souhaité // ")
                 print()
                 print("                                  1. Fouiller la pièce ")
                 print("                                  2. S'assurer de son bien être")
                 print("                                  3. Utiliser un objet")
                 print("                                  4. Se déplacer vers une nouvelle salle")
                 print()
                 print("------------------------------------------------------------------------------------------------------")
                 Choix = int(input("Que voulez vous faire: "))
                 while Choix != 1 and Choix != 2 and Choix != 3 and Choix != 4:
                     Choix = int(input("Veuiller rechoisir: "))
                 if Choix == 1:
                     if DejaFOuiller >= 1:
                         print()
                         print("                          Malheuresement, vous avez déjà fouillé cette salle")
                         time.sleep(4)
                         effacer_console()
                     else:
                         print()
                         print("                                               Vous fouiller la salle", end="",
                               flush=True)
                         for _ in range(3):
                             time.sleep(1)
                             print(".", end="", flush=True)
                         effacer_console()
                         # Chance d'avoir un item
                         if 1 <= randint(1, 101) <= 75:
                             ObjetT = []
                             for j in range(0, FouilleMultiple()):
                                 # Item rare
                                 tas = ChoixFouilleSpe()
                                 tas2 = ChoixFouilleNormal()
                                 if randint(1, 3) == 1:
                                     if tas == 1:
                                         ObjetT.append("Kit de soin")
                                     elif tas == 2:
                                         ObjetT.append("Kit de soin")
                                     elif tas == 3:
                                         ObjetT.append("Potion du Berserker")
                                     elif tas == 4:
                                         ObjetT.append("Talisman de Rohen")
                                     elif tas == 5:
                                         ObjetT.append("Scie à os")
                                     elif tas == 6:
                                         ObjetT.append("Kit de soin")
                                 # Item normal
                                 else:
                                     if tas2 == 1:
                                         ObjetT.append("Pomme")
                                     if tas2 == 2:
                                         ObjetT.append("Nectar de pêche")
                                     if tas2 == 3:
                                         ObjetT.append("Alcool")
                                     if tas2 == 4:
                                         ObjetT.append("Viande séchée")
                                     if tas2 == 5:
                                         ObjetT.append("Pilon de Poulet")
                                     if tas2 == 6:
                                         ObjetT.append("Fruit sec")
                                     if tas2 == 7:
                                         ObjetT.append("Traitement de fleur médicinal")
                                     if tas2 == 8:
                                         ObjetT.append("Opium")
                                     if tas2 == 9:
                                         ObjetT.append("Part de gateau au miel")
                                     if tas2 == 10:
                                         ObjetT.append("Bouteille d'eau")
                             Nb = len(ObjetT)
                             DejaFOuiller += 1
                             print("------------------------------------------------------------------------------------------------------")
                             print("                                      Vous avez trouvé:")
                             for i in range(0, Nb):
                                 Num = str(i + 1) + "."
                                 print("\n" + Num + ObjetT[i])
                             print()
                             print("------------------------------------------------------------------------------------------------------")
                             print("                             Appuyer sur 'Enter' pour continuer...")
                             input("")
                             with open("FichePerso.txt", "r", encoding="utf-8") as f:
                                 l = f.readlines()
                             if l:
                                 dl = l[-1].strip()
                                 nl = dl + "," + ",".join(ObjetT)
                                 l[-1] = nl + "\n"
                             else:
                                 l.append(" ".join(ObjetT) + "\n")
                             with open("FichePerso.txt", "w", encoding="utf-8") as f:
                                 f.writelines(l)
                         else:
                             print()
                             print("           Malheuresement, rien dans cette pièce ne peux vous aider dans votre quête",
                                 end="",
                                 flush=True)
                             for _ in range(3):
                                 time.sleep(1)
                                 print(".", end="", flush=True)
                             DejaFOuiller += 1
                             effacer_console()
                 elif Choix == 2:
                     effacer_console()
                     ApercuHvie = ["■"] * Hvie
                     ApercuHsatu = ["▲"] * HSaturation
                     ApercuHFolie = ["●"] * HSM
                     print("------------------------------------------------------------------------------------------------------")
                     print()
                     print("Barre de vie:")
                     print(ApercuHvie)
                     print()
                     print("Barre de saturation:")
                     print(ApercuHsatu)
                     print()
                     print("Barre de votre santé mentale:")
                     print(ApercuHFolie)
                     print()
                     print("------------------------------------------------------------------------------------------------------")
                     print("                                 Appuer sur 'Enter' pour retourner au menu")
                     input()
                     effacer_console()
                 elif Choix == 3:
                     with open("FichePerso.txt", "r", encoding="utf-8") as f:
                         lignes = f.readlines()
                         if len(lignes) >= 10:
                             y = lignes[9]
                             x = [j.strip() for j in y.split(",")]
                             Nb = len(x)
                             effacer_console()
                             print(
                                 "------------------------------------------------------------------------------------------")
                             print()
                             print("                                  Voici Votre Inventaire:")
                             print(
                                 "       // Veuillez rentrer dans la console le nom de l'objet que vous souhaiter utiliser //",
                                 end="",
                                 flush=True)
                             for i in range(0, Nb):
                                 Num = str(i + 1) + "."
                                 print("\n" + Num + x[i])
                             print()
                             print("            Entrer:'retour' dans la console si vous voulez ne pas utiliser d'objet")
                             print(
                                 "------------------------------------------------------------------------------------------")
                             Objet = str(input("Quel Objet voulez-vous utiliser: "))
                             if Objet != "retour":
                                 while not Objet in x and Objet != "retour":
                                     Objet = input("Veuillez rechoisir: ")

                                 if Objet == "Kit de soin" and Objet in x:
                                     with open("FichePerso.txt", "r", encoding="utf-8") as f:
                                         y = f.readlines()
                                         m = y[1]
                                         Hviemax = int(m)
                                     Hvie = Hvie + 5
                                     if Hvie >= Hviemax:
                                         Hvie = Hviemax
                                     stp = x.index("Kit de soin")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Kit de crochetage" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Potion du Berserker" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Talisman de Rohen" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Chaussure du renard" and Objet in x:
                                     print()
                                     print(
                                         "                          // Malheuresement cet objet n'est pas utilisable en combat //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Scie à os" and Objet in x:
                                     Hvie = Hvie - 3
                                     print()
                                     print("                            Vous vous sciez la jambe", end="", flush=True)
                                     for _ in range(3):
                                         time.sleep(1)
                                         print("!", end="", flush=True)
                                     stp = x.index("Scie à os")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Pomme" and Objet in x:
                                     HSaturation = HSaturation + 1
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Pomme")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Fruit sec" and Objet in x:
                                     HSaturation = HSaturation + 1
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Fruit sec")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Bouteille d'eau" and Objet in x:
                                     HSaturation = HSaturation + 2
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Bouteille d'eau")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Nectar de pêche" and Objet in x:
                                     HSaturation = HSaturation + 2
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Nectar de pêche")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Viande séchée" and Objet in x:
                                     HSaturation = HSaturation + 3
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Viande séchée")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Pilon de Poulet" and Objet in x:
                                     HSaturation = HSaturation + 4
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Pilon de Poulet")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Part de gateau au miel" and Objet in x:
                                     HSaturation = HSaturation + 4
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Part de gateau au miel")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Alcool" and Objet in x:
                                     HSM = HSM + 2
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Alcool")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Opium" and Objet in x:
                                     HSM = HSM + 5
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Opium")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Traitement de fleur médicinal" and Objet in x:
                                     HSM = HSM + 3
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Traitement de fleur médicinal")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                             else:
                                 effacer_console()
                         else:
                             print("                     Vous n'avez pas d'Objet dans votre inventaire")
                             time.sleep(3)
                             effacer_console()
                 elif Choix == 4:
                     print()
                     print("                       Vous décidez de changer de salle", end="", flush=True)
                     for _ in range(3):
                         time.sleep(1)
                         print(".", end="", flush=True)
                     FDT = 1
                     effacer_console()
         if t == 3:
             if Adversaire[0] == "Zombie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[32]
             if Adversaire[0] == "Fou":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[33]
             if Adversaire[0] == "Momie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[31]
             if Adversaire[0] == "Araignée Moy":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[34]
             if Adversaire[0] == "Gobelin":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[30]
             if Adversaire[0] == "Serviteur":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[38]
             if Adversaire[0] == "Zombie armé":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[35]
             if Adversaire[0] == "Orc":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[37]
             if Adversaire[0] == "Boucher":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[36]
             if Adversaire[0] == "Mère araignée":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[39]
             if Adversaire[0] == "Chevalier noir":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[40]
             if Adversaire[0] == "Dragon":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[20]
             if Adversaire[0] == "Banshee":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[25]
             if Adversaire[0] == "Chien Difforme":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[22]
             if Adversaire[0] == "Chimère":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[24]
             if Adversaire[0] == "Tresh":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[23]
             if Adversaire[0] == "Amas":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM1 = y[26]
             # Choix de la deuxième description
             if Adversaire[1] == "Zombie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[32]
             if Adversaire[1] == "Fou":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[33]
             if Adversaire[1] == "Momie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[31]
             if Adversaire[1] == "Araignée Moy":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[34]
             if Adversaire[1] == "Gobelin":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[30]
             if Adversaire[1] == "Serviteur":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[38]
             if Adversaire[1] == "Zombie armé":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[35]
             if Adversaire[1] == "Orc":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[37]
             if Adversaire[1] == "Boucher":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[36]
             if Adversaire[1] == "Mère araignée":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[39]
             if Adversaire[1] == "Chevalier noir":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[40]
             if Adversaire[1] == "Dragon":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[20]
             if Adversaire[1] == "Banshee":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[25]
             if Adversaire[1] == "Chien Difforme":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[22]
             if Adversaire[1] == "Chimère":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[24]
             if Adversaire[1] == "Tresh":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[23]
             if Adversaire[1] == "Amas":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM2 = y[26]
             # Choix description troisième monstre
             if Adversaire[2] == "Zombie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[32]
             if Adversaire[2] == "Fou":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[33]
             if Adversaire[2] == "Momie":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[31]
             if Adversaire[2] == "Araignée Moy":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[34]
             if Adversaire[2] == "Gobelin":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[30]
             if Adversaire[2] == "Serviteur":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[38]
             if Adversaire[2] == "Zombie armé":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[35]
             if Adversaire[2] == "Orc":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[37]
             if Adversaire[2] == "Boucher":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[36]
             if Adversaire[2] == "Mère araignée":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[39]
             if Adversaire[2] == "Chevalier noir":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[40]
             if Adversaire[2] == "Dragon":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[20]
             if Adversaire[2] == "Banshee":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[25]
             if Adversaire[2] == "Chien Difforme":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[22]
             if Adversaire[2] == "Chimère":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[24]
             if Adversaire[2] == "Tresh":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[23]
             if Adversaire[2] == "Amas":
                 with open("Desciption.txt", 'r', encoding="utf-8") as f:
                     y = f.readlines()
                     DescM3 = y[26]
             print("------------------------------------------------------------------------------------------")
             print()
             print("Alors que vous rentrer dans la salle," + DescM1.replace(".", ".\n"))
             print("Mais ce n'est pas tout," + DescM2.replace(".", ".\n"))
             print("Et alors que vous vous disiez que cela faisait beaucoup,"+DescM3.replace(".", ".\n"))
             print()
             print("------------------------------------------------------------------------------------------")
             print("                          Appuyer sur 'Enter' pour commencer la combat")
             input()
             effacer_console()
             combat(Adversaire, Hvie)
             time.sleep(3)
             effacer_console()
             HSaturation = HSaturation - 4
             HSM = HSM - 3
             DejaFOuiller = 0
             while FDT == 0:
                 print("------------------------------------------------------------------------------------------------------")
                 print("            // Veuillez rentrer dans la console le chiffre associé à l'action souhaité // ")
                 print()
                 print("                                  1. Fouiller la pièce ")
                 print("                                  2. S'assurer de son bien être")
                 print("                                  3. Utiliser un objet")
                 print("                                  4. Se déplacer vers une nouvelle salle")
                 print()
                 print("------------------------------------------------------------------------------------------------------")
                 Choix = int(input("Que voulez vous faire: "))
                 while Choix != 1 and Choix != 2 and Choix != 3 and Choix != 4:
                     Choix = int(input("Veuiller rechoisir: "))
                 if Choix == 1:
                     if DejaFOuiller >= 1:
                         print()
                         print("                          Malheuresement, vous avez déjà fouillé cette salle")
                         time.sleep(4)
                         effacer_console()
                     else:
                         print()
                         print("                                               Vous fouiller la salle", end="",
                               flush=True)
                         for _ in range(3):
                             time.sleep(1)
                             print(".", end="", flush=True)
                         effacer_console()
                         # Chance d'avoir un item
                         if 1 <= randint(1, 101) <= 75:
                             ObjetT = []
                             for j in range(0, FouilleMultiple()):
                                 # Item rare
                                 tas = ChoixFouilleSpe()
                                 tas2 = ChoixFouilleNormal()
                                 if randint(1, 3) == 1:
                                     if tas == 1:
                                         ObjetT.append("Kit de soin")
                                     elif tas == 2:
                                         ObjetT.append("Kit de soin")
                                     elif tas == 3:
                                         ObjetT.append("Potion du Berserker")
                                     elif tas == 4:
                                         ObjetT.append("Talisman de Rohen")
                                     elif tas == 5:
                                         ObjetT.append("Scie à os")
                                     elif tas == 6:
                                         ObjetT.append("Kit de soin")
                                 # Item normal
                                 else:
                                     if tas2 == 1:
                                         ObjetT.append("Pomme")
                                     if tas2 == 2:
                                         ObjetT.append("Nectar de pêche")
                                     if tas2 == 3:
                                         ObjetT.append("Alcool")
                                     if tas2 == 4:
                                         ObjetT.append("Viande séchée")
                                     if tas2 == 5:
                                         ObjetT.append("Pilon de Poulet")
                                     if tas2 == 6:
                                         ObjetT.append("Fruit sec")
                                     if tas2 == 7:
                                         ObjetT.append("Traitement de fleur médicinal")
                                     if tas2 == 8:
                                         ObjetT.append("Opium")
                                     if tas2 == 9:
                                         ObjetT.append("Part de gateau au miel")
                                     if tas2 == 10:
                                         ObjetT.append("Bouteille d'eau")
                             Nb = len(ObjetT)
                             DejaFOuiller += 1
                             print("------------------------------------------------------------------------------------------------------")
                             print("                                      Vous avez trouvé:")
                             for i in range(0, Nb):
                                 Num = str(i + 1) + "."
                                 print("\n" + Num + ObjetT[i])
                             print()
                             print("------------------------------------------------------------------------------------------------------")
                             print("                             Appuyer sur 'Enter' pour continuer...")
                             input("")
                             with open("FichePerso.txt", "r", encoding="utf-8") as f:
                                 l = f.readlines()
                             if l:
                                 dl = l[-1].strip()
                                 nl = dl + "," + ",".join(ObjetT)
                                 l[-1] = nl + "\n"
                             else:
                                 l.append(" ".join(ObjetT) + "\n")
                             with open("FichePerso.txt", "w", encoding="utf-8") as f:
                                 f.writelines(l)
                         else:
                             print()
                             print("           Malheuresement, rien dans cette pièce ne peux vous aider dans votre quête",
                                 end="",
                                 flush=True)
                             for _ in range(3):
                                 time.sleep(1)
                                 print(".", end="", flush=True)
                             DejaFOuiller += 1
                             effacer_console()
                 elif Choix == 2:
                     effacer_console()
                     ApercuHvie = ["■"] * Hvie
                     ApercuHsatu = ["▲"] * HSaturation
                     ApercuHFolie = ["●"] * HSM
                     print("------------------------------------------------------------------------------------------------------")
                     print()
                     print("Barre de vie:")
                     print(ApercuHvie)
                     print()
                     print("Barre de saturation:")
                     print(ApercuHsatu)
                     print()
                     print("Barre de votre santé mentale:")
                     print(ApercuHFolie)
                     print()
                     print("------------------------------------------------------------------------------------------------------")
                     print("                                 Appuer sur 'Enter' pour retourner au menu")
                     input()
                     effacer_console()
                 elif Choix == 3:
                     with open("FichePerso.txt", "r", encoding="utf-8") as f:
                         lignes = f.readlines()
                         if len(lignes) >= 10:
                             y = lignes[9]
                             x = [j.strip() for j in y.split(",")]
                             Nb = len(x)
                             effacer_console()
                             print(
                                 "------------------------------------------------------------------------------------------")
                             print()
                             print("                                  Voici Votre Inventaire:")
                             print(
                                 "       // Veuillez rentrer dans la console le nom de l'objet que vous souhaiter utiliser //",
                                 end="",
                                 flush=True)
                             for i in range(0, Nb):
                                 Num = str(i + 1) + "."
                                 print("\n" + Num + x[i])
                             print()
                             print("            Entrer:'retour' dans la console si vous voulez ne pas utiliser d'objet")
                             print(
                                 "------------------------------------------------------------------------------------------")
                             Objet = str(input("Quel Objet voulez-vous utiliser: "))
                             if Objet != "retour":
                                 while not Objet in x and Objet != "retour":
                                     Objet = input("Veuillez rechoisir: ")

                                 if Objet == "Kit de soin" and Objet in x:
                                     with open("FichePerso.txt", "r", encoding="utf-8") as f:
                                         y = f.readlines()
                                         m = y[1]
                                         Hviemax = int(m)
                                     Hvie = Hvie + 5
                                     if Hvie >= Hviemax:
                                         Hvie = Hviemax
                                     stp = x.index("Kit de soin")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Kit de crochetage" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Potion du Berserker" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Talisman de Rohen" and Objet in x:
                                     print()
                                     print(
                                         "                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Chaussure du renard" and Objet in x:
                                     print()
                                     print(
                                         "                          // Malheuresement cet objet n'est pas utilisable en combat //")
                                     time.sleep(3)
                                     effacer_console()
                                 if Objet == "Scie à os" and Objet in x:
                                     Hvie = Hvie - 3
                                     print()
                                     print("                            Vous vous sciez la jambe", end="", flush=True)
                                     for _ in range(3):
                                         time.sleep(1)
                                         print("!", end="", flush=True)
                                     stp = x.index("Scie à os")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Pomme" and Objet in x:
                                     HSaturation = HSaturation + 1
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Pomme")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Fruit sec" and Objet in x:
                                     HSaturation = HSaturation + 1
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Fruit sec")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Bouteille d'eau" and Objet in x:
                                     HSaturation = HSaturation + 2
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Bouteille d'eau")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Nectar de pêche" and Objet in x:
                                     HSaturation = HSaturation + 2
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Nectar de pêche")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Viande séchée" and Objet in x:
                                     HSaturation = HSaturation + 3
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Viande séchée")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Pilon de Poulet" and Objet in x:
                                     HSaturation = HSaturation + 4
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Pilon de Poulet")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Part de gateau au miel" and Objet in x:
                                     HSaturation = HSaturation + 4
                                     if HSaturation >= 10:
                                         HSaturation = 10
                                     stp = x.index("Part de gateau au miel")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Alcool" and Objet in x:
                                     HSM = HSM + 2
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Alcool")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Opium" and Objet in x:
                                     HSM = HSM + 5
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Opium")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                                 if Objet == "Traitement de fleur médicinal" and Objet in x:
                                     HSM = HSM + 3
                                     if HSM >= 10:
                                         HSM = 10
                                     stp = x.index("Traitement de fleur médicinal")
                                     x.pop(stp)
                                     del lignes[9]
                                     with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                         f.writelines(lignes)
                                         f.writelines(",".join(x))
                                     effacer_console()
                             else:
                                 effacer_console()
                         else:
                             print("                     Vous n'avez pas d'Objet dans votre inventaire")
                             time.sleep(3)
                             effacer_console()
                 elif Choix == 4:
                     print()
                     print("                       Vous décidez de changer de salle", end="", flush=True)
                     for _ in range(3):
                         time.sleep(1)
                         print(".", end="", flush=True)
                     FDT = 1
                     effacer_console()
  else:
      # Exploration de la salle si aucun monstre n'est présent
      DejaFOuiller = 0
      while FDT == 0:
         def FouilleMultiple():
             TAS = randint(1, 4)
             TAS2 = randint(1, 10)
             if TAS == 1:
                 return 2
             elif TAS2 == 1:
                 return 3
             else:
                 return 1
         def ChoixFouilleNormal():
             TAS = randint(1, 10)
             return TAS
         def ChoixFouilleSpe():
             TAS = randint(1, 6)
             return TAS
         effacer_console()
         print("------------------------------------------------------------------------------------------------------")
         print("            // Veuillez rentrer dans la console le chiffre associé à l'action souhaité // ")
         print()
         print("                                  1. Fouiller la pièce ")
         print("                                  2. S'assurer de son bien être")
         print("                                  3. Utiliser un objet")
         print("                                  4. Se déplacer vers une nouvelle salle")
         print()
         print("------------------------------------------------------------------------------------------------------")
         Choix = int(input("Que voulez vous faire: "))
         while Choix != 1 and Choix != 2 and Choix != 3 and Choix !=4:
             Choix = int(input("Veuiller rechoisir: "))
         if Choix == 1:
             if DejaFOuiller >= 1:
                 print()
                 print("                          Malheuresement, vous avez déjà fouillé cette salle")
                 time.sleep(4)
                 effacer_console()
             else:
                 print()
                 print("                                               Vous fouiller la salle", end="", flush=True)
                 for _ in range(3):
                     time.sleep(1)
                     print(".", end="", flush=True)
                 effacer_console()
                 # Chance d'avoir un item
                 if 1 <= randint(1, 101) <= 75:
                     ObjetT = []
                     for j in range(0, FouilleMultiple()):
                         # Item rare
                         tas = ChoixFouilleSpe()
                         tas2 = ChoixFouilleNormal()
                         if randint(1, 3) == 1:
                             if tas == 1:
                                 ObjetT.append("Kit de soin")
                             elif tas == 2:
                                 ObjetT.append("Kit de soin")
                             elif tas == 3:
                                 ObjetT.append("Potion du Berserker")
                             elif tas == 4:
                                 ObjetT.append("Talisman de Rohen")
                             elif tas == 5:
                                 ObjetT.append("Scie à os")
                             elif tas == 6:
                                 ObjetT.append("Kit de soin")
                         # Item normal
                         else:
                             if tas2 == 1:
                                 ObjetT.append("Pomme")
                             if tas2 == 2:
                                 ObjetT.append("Nectar de pêche")
                             if tas2 == 3:
                                 ObjetT.append("Alcool")
                             if tas2 == 4:
                                 ObjetT.append("Viande séchée")
                             if tas2 == 5:
                                 ObjetT.append("Pilon de Poulet")
                             if tas2 == 6:
                                 ObjetT.append("Fruit sec")
                             if tas2 == 7:
                                 ObjetT.append("Traitement de fleur médicinal")
                             if tas2 == 8:
                                 ObjetT.append("Opium")
                             if tas2 == 9:
                                 ObjetT.append("Part de gateau au miel")
                             if tas2 == 10:
                                 ObjetT.append("Bouteille d'eau")
                     Nb = len(ObjetT)
                     DejaFOuiller += 1
                     print(
                         "------------------------------------------------------------------------------------------------------")
                     print("                                      Vous avez trouvé:")
                     for i in range(0, Nb):
                         Num = str(i + 1) + "."
                         print("\n" + Num + ObjetT[i])
                     print()
                     print(
                         "------------------------------------------------------------------------------------------------------")
                     print("                             Appuyer sur 'Enter' pour continuer...")
                     input("")
                     with open("FichePerso.txt", "r", encoding="utf-8") as f:
                         l = f.readlines()
                     if l:
                         dl = l[-1].strip()
                         nl = dl + "," + ",".join(ObjetT)
                         l[-1] = nl + "\n"
                     else:
                         l.append(" ".join(ObjetT) + "\n")
                     with open("FichePerso.txt", "w", encoding="utf-8") as f:
                         f.writelines(l)
                 else:
                     print()
                     print("           Malheuresement, rien dans cette pièce ne peux vous aider dans votre quête",
                           end="",
                           flush=True)
                     for _ in range(3):
                         time.sleep(1)
                         print(".", end="", flush=True)
                     DejaFOuiller += 1
                     effacer_console()
         elif Choix == 2:
             effacer_console()
             ApercuHvie = ["■"] * Hvie
             ApercuHsatu = ["▲"] * HSaturation
             ApercuHFolie = ["●"] * HSM
             print("------------------------------------------------------------------------------------------------------")
             print()
             print("Barre de vie:")
             print(ApercuHvie)
             print()
             print("Barre de saturation:")
             print(ApercuHsatu)
             print()
             print("Barre de votre santé mentale:")
             print(ApercuHFolie)
             print()
             print("------------------------------------------------------------------------------------------------------")
             print("                                 Appuer sur 'Enter' pour retourner au menu")
             input()
             effacer_console()
         elif Choix == 3:
             with open("FichePerso.txt", "r", encoding="utf-8") as f:
                 lignes = f.readlines()
                 if len(lignes) >= 10:
                     y = lignes[9]
                     x = [j.strip() for j in y.split(",")]
                     Nb = len(x)
                     effacer_console()
                     print("------------------------------------------------------------------------------------------")
                     print()
                     print("                                  Voici Votre Inventaire:")
                     print(
                         "       // Veuillez rentrer dans la console le nom de l'objet que vous souhaiter utiliser //",
                         end="",
                         flush=True)
                     for i in range(0, Nb):
                         Num = str(i + 1) + "."
                         print("\n" + Num + x[i])
                     print()
                     print("            Entrer:'retour' dans la console si vous voulez ne pas utiliser d'objet")
                     print("------------------------------------------------------------------------------------------")
                     Objet = str(input("Quel Objet voulez-vous utiliser: "))
                     if Objet != "retour":
                         while not Objet in x and Objet != "retour":
                             Objet = input("Veuillez rechoisir: ")
                             effacer_console()

                         if Objet == "Kit de soin" and Objet in x:
                             with open("FichePerso.txt", "r", encoding="utf-8") as f:
                                 y = f.readlines()
                                 m = y[1]
                                 Hviemax = int(m)
                             Hvie = Hvie + 5
                             if Hvie >= Hviemax:
                                 Hvie = Hviemax
                             stp = x.index("Kit de soin")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Kit de crochetage" and Objet in x:
                             print()
                             print("                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                             time.sleep(3)
                             effacer_console()
                         if Objet == "Potion du Berserker" and Objet in x:
                             print()
                             print("                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                             time.sleep(3)
                             effacer_console()
                         if Objet == "Talisman de Rohen" and Objet in x:
                             print()
                             print("                            // Malheuresement cet objet n'est pas utilisable maintenant //")
                             time.sleep(3)
                             effacer_console()
                         if Objet == "Chaussure du renard" and Objet in x:
                             print()
                             print("                          // Malheuresement cet objet n'est pas utilisable en combat //")
                             time.sleep(3)
                             effacer_console()
                         if Objet == "Scie à os" and Objet in x:
                             Hvie = Hvie - 3
                             print()
                             print("                            Vous vous sciez la jambe", end="", flush=True)
                             for _ in range(3):
                                 time.sleep(1)
                                 print("!", end="", flush=True)
                             stp = x.index("Scie à os")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Pomme" and Objet in x:
                             HSaturation = HSaturation + 1
                             if HSaturation >= 10:
                                 HSaturation = 10
                             stp = x.index("Pomme")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Fruit sec" and Objet in x:
                             HSaturation = HSaturation + 1
                             if HSaturation >= 10:
                                 HSaturation = 10
                             stp = x.index("Fruit sec")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Bouteille d'eau" and Objet in x:
                             HSaturation = HSaturation + 2
                             if HSaturation >= 10:
                                 HSaturation = 10
                             stp = x.index("Bouteille d'eau")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Nectar de pêche" and Objet in x:
                             HSaturation = HSaturation + 2
                             if HSaturation >= 10:
                                 HSaturation = 10
                             stp = x.index("Nectar de pêche")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Viande séchée" and Objet in x:
                             HSaturation = HSaturation + 3
                             if HSaturation >= 10:
                                 HSaturation = 10
                             stp = x.index("Viande séchée")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Pilon de Poulet" and Objet in x:
                             HSaturation = HSaturation + 4
                             if HSaturation >= 10:
                                 HSaturation = 10
                             stp = x.index("Pilon de Poulet")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Part de gateau au miel" and Objet in x:
                             HSaturation = HSaturation + 4
                             if HSaturation >= 10:
                                 HSaturation = 10
                             stp = x.index("Part de gateau au miel")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                     f.writelines(lignes)
                                     f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Alcool" and Objet in x:
                             HSM = HSM + 2
                             if HSM >= 10:
                                 HSM = 10
                             stp = x.index("Alcool")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Opium" and Objet in x:
                             HSM = HSM + 5
                             if HSM >= 10:
                                 HSM = 10
                             stp = x.index("Opium")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                         if Objet == "Traitement de fleur médicinal" and Objet in x:
                             HSM = HSM + 3
                             if HSM >= 10:
                                 HSM = 10
                             stp = x.index("Traitement de fleur médicinal")
                             x.pop(stp)
                             del lignes[9]
                             with open("FichePerso.txt", 'w', encoding="utf-8") as f:
                                 f.writelines(lignes)
                                 f.writelines(",".join(x))
                             effacer_console()
                     else:
                         effacer_console()
                 else:
                     print("                     Vous n'avez pas d'Objet dans votre inventaire")
                     time.sleep(3)
                     effacer_console()
         elif Choix == 4:
             print()
             print("                       Vous décidez de changer de salle", end="", flush=True)
             for _ in range(3):
                 time.sleep(1)
                 print(".", end="", flush=True)
             FDT = 1
             effacer_console()






















