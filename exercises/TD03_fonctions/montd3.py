#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    print(temps[0], temps[1], temps[2], temps [3])
    tempsenseconde = temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3]
    return tempsenseconde
mon_temps = (3,23,1,34)
mon_lendemain = (4,23,1,34)
print(type(mon_temps))
ma_valeur = tempsEnSeconde(mon_temps)
print(ma_valeur)  
ma_valeur = tempsEnSeconde(mon_lendemain)
print(ma_valeur) 