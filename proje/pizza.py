import csv
import datetime


# pizza üst sinifimiz:

class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost

#pizza ust sinifindan sonra  onun metodlarini tasiyan alt siniflar
class KlasikPizza(Pizza):
    cost = 50

    def __init__(self):
        self.description = "\nKlasik pizzamiz: Salam,Sosis,Sucuk,Kasar ve Zeytinden olusmaktadir..."
        print(self.description)


class MargaritaPizza(Pizza):
    cost = 45

    def __init__(self):
        self.description = "\nMargarita pizzamiz: Mozarella,Domates,Feslegen ve Zeytinyagindan olusmaktadir..."
        print(self.description)


class TurkPizza(Pizza):
    cost = 60

    def __init__(self):
        self.description = "\nTurk pizzamiz: Kıyma,Sogan,Sarimsak ve Naneden olusmaktadir..."
        print(self.description)


class SadePizza(Pizza):
    cost = 40

    def __init__(self):
        self.description = "\nSade pizzamiz: Kasar,Salam ve Zeytinden olusmaktadir..."
        print(self.description)


# pizza sinifinin ozelliklerini tasiyan decorator sinifimizin olusturulmasi

class Decorator(Pizza):
    def __init__(self, ing):
        super().__init__()
        self.component = ing

    def get_cost(self):
        return self.component.get_cost() + \
               Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
               ' ;' + Pizza.get_description(self)


# decoratorun subclasslari olan malzeme classlari

class Zeytin(Decorator):
    cost = 3.5

    def __init__(self, ing):
        super().__init__(ing)


class Mantar(Decorator):
    cost = 4.5

    def __init__(self, ing):
        super().__init__(ing)


class KeciPeynir(Decorator):
    cost = 6.0

    def __init__(self, ing):
        super().__init__(ing)


class Et(Decorator):
    cost = 8.0

    def __init__(self, ing):
        super().__init__(ing)


class Sogan(Decorator):
    cost = 3.0

    def __init__(self, ing):
        super().__init__(ing)


class Misir(Decorator):
    cost = 2.5

    def __init__(self, ing):
        super().__init__(ing)


# Menuyu ekrana yazdirma fonksiyonu bir ayni zamanda main fonksiyonu diyebiliriz:

def main():
    with open("Menu.txt", "r") as cust_menu:
        for i in cust_menu:
            print(i, end="")

    class_dict = {1: KlasikPizza,
                  2: MargaritaPizza,
                  3: TurkPizza,
                  4: SadePizza,
                  11: Zeytin,
                  12: Mantar,
                  13: KeciPeynir,
                  14: Et,
                  15: Sogan,
                  16: Misir}

    button = input("Lütfen Pizzanızı Seçiniz: ")
    while button not in ["1", "2", "3", "4"]:
        button = input("Lutfen gecerli bir sayi giriniz: ")

    order = class_dict[int(button)]()

    while button != "q":
        button = input(
            "Fazladan malzeme almak istiyorsaniz numara giriniz (Direkt Siparişinizi Onaylamak İçin 'q' ya  basiniz): ")
        if button in ["11", "12", "13", "14", "15", "16"]:
            order = class_dict[int(button)](order)

    print("\n" + order.get_description().strip() + "; $" + str(order.get_cost()))
    print("\n")

    # Siparis Bilgilendirme sistemi aciyoruz ve kullaniciyi veritabanina kaydediyoruz

    print("----------Siparisi Verenin Bilgileri----------\n")
    name = input("İsminiz: ")
    TC = input("TC Kimlik Numaranız: ")
    cc_no = input("Kredi Kartı Numaranızı Giriniz: ")
    cc_pass = input("Kredi Kartı Şifrenizi Giriniz: ")
    time = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, TC, cc_no, cc_pass, order.get_description(), time])
    print("Siparişiniz Onaylandı.")


main()