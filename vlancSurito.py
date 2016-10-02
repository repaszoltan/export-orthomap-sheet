# -*- coding: utf-8 -*-

import math
import re

class Pont:
    """
    Pont osztály, amely eltárolja egy pont adatait.
        psz - pontszám
        y - Y koordináta
        x - X koordináta

    Két pont közötti távolság az alábbi módon számítható: P1 & P2 ahol
    P1 és P2 objektumok a Pont osztályból lettek létrehozva.
    """
    def __init__(self, psz, y, x):
        self.psz = str(psz)
        self.y = float(y)
        self.x = float(x)

    def __and__(self, p):
        """ Két pont távolságát megadó metódus. Paraméterül Pont
            objektumot vár """
        return math.sqrt((p.y - self.y)**2 + (p.x - self.x)**2)

class Vonallanc:
    """
    Vonallánc osztály amely eltárolja egy vonallánc töréspontjait valamint
    képes besűríteni azokat megadott távolságokra.
    """
    def __init__(self, *tsp):
        self.tsp = list(tsp)

    def hozzafuz(self, p):
        """ Adott vonallánc objektumhoz utólag fűzhetünk hozzá töréspontokat
            a vonallánc végére """
        self.tsp.append(p)

    def surit(self, maxtav):
        """ Vizsgálja, hogy két vonallánc töréspont között mekkora a távolság
            és a megadott maxtav távolság függvényében annyi részre sűríti be
            az adott szakaszt amennyiszer a maxtav belefér.
            Az eljárás egy új vonallánccal tér vissza """
        vlanc = Vonallanc()
        
        for i in range(len(self.tsp) - 1):
            # Vonallánc egy szakaszának hossza
            shossz = self.tsp[i] & self.tsp[i+1];
            # Eredeti vonallánc töréspont hozzáfűzése az új vonallánchoz
            vlanc.hozzafuz(self.tsp[i])
            # Ha a két töréspont közötti szakasz hosszabb mint a megadott
            # maximális távolság
            if(shossz > maxtav):
                # Adott szakaszra hány töréspont kerül sűrítésre
                osztas = math.ceil(float(shossz) / float(maxtav))
                # Részhossz az adott vonalszakaszon
                dy = float(self.tsp[i+1].y - self.tsp[i].y)
                dx = float(self.tsp[i+1].x - self.tsp[i].x)
                for j in range(1, osztas):
                    # Eltolási értékek számítása
                    oy = (dy / osztas) * j
                    ox = (dx / osztas) * j

                    # Kimeneti vonalláchoz új pont hozzáfűzése
                    vlanc.hozzafuz(Pont(
                        "{0}+{1}".format(self.tsp[i].psz, j),
                        self.tsp[i].y + oy,
                        self.tsp[i].x + ox))

        # Az eredeti vonallánc utolsó pontjának hozzáfűzése
        # a kimeneti vonallánchoz
        vlanc.hozzafuz(self.tsp[len(self.tsp)-1])
        
        return vlanc

#******** MAIN **********#                
if(__name__ == "__main__"):
    vlancBe = Vonallanc()
    # Lista beolvasása
    try:
        f = open("./lista.txt", "r");
        for line in f:
            tmp = re.split("[\s;,]+", line)
            vlancBe.hozzafuz(Pont(
                tmp[0],
                round(tmp[1], 2),
                round(tmp[2], 2)))            
    except IOError:
        print("A megadott fájl nem olvasható!")
    finally:
        f.close()

    # Vonallánc szakaszainak sűrítése ha a szakasz 5 egységnél hosszabb
    vlancKi = vlancBe.surit(5)

    # Új lista kiírása
    try:
        f = open("./lista_ki.txt", "w")
        for pont in vlancKi.tsp:
            f.write("{0}\t{1}\t{2}\n".format(
                pont.psz,
                pont.y,
                pont.x))
    except IOError:
        print("A megadott fájl nem írható")
    finally:
        f.flush()
        f.close()
