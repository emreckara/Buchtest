class Geld(object):
    wechselkurs = {'USD':0.84998,
                 'GBP':1.39480,
                 'EUR':1.0,
                 'JPY':0.007168
                 'TL': 0.15  
                 }
    def __init__(self, waehrung, betrag):
        self.waehrung = waehrung
        self.betrag = float(betrag)

    def getEuro(self):
        return self.betrag*self.wechselkurs[self.waehrung]

    def add(self, geld):
        summe_in_euro = self.getEuro() + geld.getEuro()
        summe = Geld(self.waehrung, summe_in_euro/self.wechselkurs[self.waehrung])
        return summe

hotelrechnung = Geld('USD', 123.45)
mietwagen = Geld('EUR', 527.30)

summe1 = hotelrechnung.add(mietwagen)
print(summe1.waehrung, round(summe1.betrag, 2))

summe2 = mietwagen.add(hotelrechnung)
print(summe2.waehrung, round(summe2.betrag, 2))

