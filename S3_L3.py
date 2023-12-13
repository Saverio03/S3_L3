print("Calcolatore per il perimetro di figure geometriche")
print("Di quale figura vuoi calcolare il perimetro?")
print("1 = Quadrato 2 = Triangolo  3 = Rettangolo")
InputUtente = int(input())
if InputUtente == 1:
    print("inserisci la misura del lato del quadrato:")
    LatoQuadrato = int(input())
    PerimetroQuadrato = LatoQuadrato * LatoQuadrato
    print("il perimetro del quadrato è: " + str(PerimetroQuadrato))

elif InputUtente == 2:
    print("inserisci la lungezza dei tre lati del triangolo")
    print("primo lato: ")
    PrimoLato = int(input())
    print("secondo lato: ")
    SecondoLato = int(input())
    print("terzo lato: ")
    TerzoLato = int(input())
    PerimetroTriangolo = PrimoLato + SecondoLato + TerzoLato
    print("il perimetro del triangolo è: " + str(PerimetroTriangolo))

elif InputUtente == 3:
    print("inserisci la lunghezza del rettangolo: ")
    Base = int(input())
    print("inserisci l'altezza del rettangolo: ")
    Altezza = int(input())
    PerimetroRettangolo = (Base + Altezza) * 2
    print("il perimetro del rettangolo è: " + str(PerimetroRettangolo))
else:
    print("inserisci un numero valido")
