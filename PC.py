from turtle import end_fill
Ve= input("Entrez la vitesse de l'eau")
Vie= input("Entrez la viscosité cinématique")
D1= input("Entrez la diamètre  de la conduite")
try:
    Ve=float(Ve)
    Vie=float(Vie)
    D1=float(D1)
    Re=((Ve*D1)/Vie)
    print(Re)
    if Re>100000:
        print("Régime Turbulent")
    else:
        print("Régime laminaire")
except:
     print("Erreur")
print("Question2")
Vf= input("Entrez la vetesse de fuel")
Vif= input("Entrez la viscosité cinématique")
try:
    Vf=float(Vf)
    Vif=float(Vif)
    Re2=((Vf*D1)/Vif)
    print(Re2)
    if Re<100000:
        print("Régime Turbulent")
    else:
        print("Régime laminaire")
except:
    print("Erreur")
