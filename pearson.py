#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt
import numpy

#zadeklarowanie wartości słownika użytkownicy: klucz - imię użytkownia, wartość - kolejne słowniki 
users = {
        "Ania": 
            {"Blues Traveler": 1.0,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": 0.5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

 #definicja funkcji manhattan, gdzie zmiennymi są dwie oceny      
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
  
#deklaracja, że kluczem nr 1 są oceny u pierwszego użytkownika, czyli Ani, a kluczem 2  oceny Boni; 
#uzyskanie nazw zespołów i ich ocen, które są kluczami w danych słownikach 
    # TODO: wpisz kod
    klucze1 = rating1.keys() 
    klucze2 = rating2.keys()
    
#jeżeli odległość =0, czyli wartości są takie same, nie udało się ich porównać
#początkowy warunek, że użytkownicy ocenili te same zespoły
    odleglosc = 0
    udaloSiePorownac = False

    
    for klucz in klucze1: #wykonuje dla wszystkich kluczy w klucze1
        if klucz in rating2.keys():     #jeśli klucz z 1szego słownika znajduje się w drugim zbiorze kluczy
            udaloSiePorownac = True     #użytkownicy ocenili jakieś te same zespoły
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])    #obliczenie odległości    
    
    if (udaloSiePorownac==True):  #jeśli mieli jakieś wspólne zespoły zwraca odległość
        print "Odleglosc Manhattan:"
        print odleglosc
        return odleglosc
    else: #użytkownicy nie mają wspólnych zespołów
        return -1

def pearson(rating1, rating2): # definicja funkcji pearsona, gdzie wartościami są oceny 1 i oceny 2 użytkownia
    klucze1 = rating1.keys() #wskazujemy, który klucz ze słownika bierzemy do obliczeń
    klucze2 = rating2.keys()
    #początkowe warunki 
    korelacja=0 
    sumaXY=0
    sumaX=0
    sumaY=0
    n=0
    sumaXX=0
    sumaYY=0

    """pętla for: jeżeli klucz znajdue się u obu użytkowników, to dla każdej z tych wartości obliczamy sumy poszczególnych liczb
    niezbędne do policzenia współczynnika korelacji pearsona"""
    for klucz in klucze1:
        if klucz in rating2.keys():
            sumaX= sumaX+ rating1[klucz]
            sumaY= sumaY+ rating2[klucz] 
            sumaXY= sumaXY + rating1[klucz]*rating2[klucz]
            sumaXX= sumaXX + rating1[klucz]*rating1[klucz]
            sumaYY= sumaYY + rating2[klucz]*rating2[klucz]
            n= n+1 

#określenie wartości licznika i mianownika oraz podstawienie do wzoru    
    wart_licznik= sumaXY- sumaX*sumaY/n
    wart_mianownik= sqrt(sumaXX- sumaX*sumaX/n) * sqrt(sumaYY-sumaY*sumaY/n)
    korelacja= wart_licznik/wart_mianownik
    print "Wartosc korelacji: "
    print korelacja
    if korelacja == 0:
        print "Brak korelacji"
    elif korelacja < 0:
        print "korelacja ujemna - gdy wartości jednej cechy rosną, wartości drugiej maleją"
    else:
        print "korelacja dodatnia - gdy wartości jednej cechy rosną, wartości drugiej również i odwrotnie"
    return korelacja

#obliczenie współczynika Pearsona korzystając z biblioteki numpy oraz funkcji corrcoef
def pearsonNumpy(rating1, rating2):
    korelacja=0
    keys = list(rating1.viewkeys() | rating2.viewkeys()) # wyświetlenie listy kluczy
    korelacja=numpy.corrcoef([rating1[x] for x in keys], [rating2[x] for x in keys])[0][1] 
    return korelacja

manhattan(users["Ania"], users["Bonia"])
pearson(users["Ania"], users["Bonia"])
print "Korelacja numpy " + str(pearsonNumpy(users["Bonia"],users["Ania"]))
