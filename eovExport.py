###############################################################################################
#                                       Diplomamunka                                          #
# A pilota nelkuli rendszerek (UAS) felhasznalasi lehetosegei a kozeli legi fotogrammetriaban #
#                                       Repas Zoltan                                          #
#                SZTE-TTIK TERMESZETI FOLDRAJZI ES GEOINFORMATIKAI TANSZEK                    #
#                                       2014 Komarom                                          #
#                                repas.zoltan.geo@gmail.com                                   #
###############################################################################################
#               Ortofoto exprotalasa AgiSoft-bol EOV 1:10 000 szelvenyekre                    #
###############################################################################################



#### Inicializalas PhotoSann-hez ##############################################################
import PhotoScan
doc = PhotoScan.app.document
chunk = doc.activeChunk
#### Inicializalas vege #######################################################################

#### Beallitasok ##############################################################################
# Ezeket SZEKESZTENI kell:
#   Kep tipusa:
type = "tif"

#   Eleresi ut:
mappa = "E:/python/HelloAgiSoft/"

#   Felbontas:
d_x = d_y = 0.5


#   Vetulet:
proj = PhotoScan.CoordinateSystem()
proj.init("EPSG::23700")
#EOV:"EPSG::23700"
#WGS84:"EPSG::4326"

#### Beallitasok vege ########################################################################


#### Exportalas deffinialas modositast nem igenyel ###########################################
def export_eov(szelveny):
    #Ki kell deriteni, hany tagu az elotag 2 vagy 3, ezert megszamoljuk:
    szelveny = str(szelveny)
    hossz = len(szelveny)
    #a haromjegyu elotag miatt ket eset lehetseges, itt jon az utvalasztó:
    #Normal ut pl.:23-213
    if hossz == 6:
            # sor: szelveny[0] oszlop: szelveny[1]
            #Az EOV szelvenyezes kezdokoordinatai:
            y_kezdo = 384000
            x_kezdo = 32000

            #EOV szelveny eleinek hossza (m):
            dy_100 = 48000
            dx_100 = 32000

            dy_50 = 24000
            dx_50 = 16000

            dy_25 = 12000
            dx_25 = 8000

            dy_10 = 6000
            dx_10 = 4000

            #Szelveny bontasa:
            sor = int(szelveny[0])
            oszlop = int(szelveny[1])
            sz50 =  int(szelveny[3])
            sz25 =  int(szelveny[4])
            sz10 =  int(szelveny[5])

            #EOV szelvenyszam ellenorzes
            if sz50 > 4 or sz25 > 4 or sz10 > 4:
                print ("Nem EOV 10 000-res szevenyszamot adtal meg!")

            else:
                #100-res Szelveny bal alsó koordinatai:
                y_also_100 = y_kezdo + oszlop * dy_100
                x_also_100 = x_kezdo + sor * dx_100
                #100-res Szeveny jobb felso koordinatai:
                y_felso_100 = y_also_100 + dy_100
                x_felso_100 = x_also_100 + dx_100


                #50-res koordinatak szamitasa:
                #Negyed keresese:
                if sz50 == 1:
                        y_t= 0
                        x_t= 1
                if sz50 == 2:
                        y_t= 1
                        x_t= 1
                if sz50 == 3:
                        y_t= 0
                        x_t= 0
                if sz50 == 4:
                        y_t= 1
                        x_t= 0

                y_also_50 = y_also_100 + dy_50 * y_t
                x_also_50 = x_also_100 + dx_50 * x_t

                y_felso_50 = y_also_50 + dy_50
                x_felso_50 = x_also_50 + dx_50

                #25-res koordinatak szamitasa:
                #Negyed keresese:
                if sz25 == 1:
                	y_t= 0
                	x_t= 1
                if sz25 == 2:
                	y_t= 1
                	x_t= 1
                if sz25 == 3:
                	y_t= 0
                	x_t= 0
                if sz25 == 4:
                	y_t= 1
                	x_t= 0

                y_also_25 = y_also_50 + dy_25 * y_t
                x_also_25 = x_also_50 + dx_25 * x_t

                y_felso_25 = y_also_25 + dy_25
                x_felso_25 = x_also_25 + dx_25

                #10-res koordinatak szamitasa:
                #Negyed keresese:
                if sz10 == 1:
                	y_t= 0
                	x_t= 1
                if sz10 == 2:
                	y_t= 1
                	x_t= 1
                if sz10 == 3:
                	y_t= 0
                	x_t= 0
                if sz10 == 4:
                	y_t= 1
                	x_t= 0

                y_also_10 = y_also_25 + dy_10 * y_t
                x_also_10 = x_also_25 + dx_10 * x_t

                y_felso_10 = y_also_10 + dy_10
                x_felso_10 = x_also_10 + dx_10

                eovszam = [szelveny[0],szelveny[1],"-",szelveny[3],szelveny[4],szelveny[5],"."]
                print ("EOV 10 000 szelveny:")
                nev = "".join(eovszam)
                print (nev)
                print (y_also_10)
                print (x_also_10)
                print (y_felso_10)
                print (x_felso_10)



    #Keleti ut:
    if hossz == 7:
            # sor: szelveny[0] oszlop: szelveny[1]
            #Az EOV szelvenyezes kezdokoordinatai:
            y_kezdo = 384000
            x_kezdo = 32000

            #EOV szelveny eleinek hossza (m):
            dy_100 = 48000
            dx_100 = 32000

            dy_50 = 24000
            dx_50 = 16000

            dy_25 = 12000
            dx_25 = 8000

            dy_10 = 6000
            dx_10 = 4000

            #Szelveny bontasa:
            sor = int(szelveny[0])
            oszlop = int(szelveny[1] + szelveny[2])
            sz50 =  int(szelveny[4])
            sz25 =  int(szelveny[5])
            sz10 =  int(szelveny[6])

            #EOV szelvenyszam ellenorzes
            if sz50 > 4 or sz25 > 4 or sz10 > 4:
                print ("Nem EOV 10 000-res szevenyszamot adtal meg!")

            else:
                #100-res Szelveny bal alsó koordinatai:
                y_also_100 = y_kezdo + oszlop * dy_100
                x_also_100 = x_kezdo + sor * dx_100
                #100-res Szeveny jobb felso koordinatai:
                y_felso_100 = y_also_100 + dy_100
                x_felso_100 = x_also_100 + dx_100


                #50-res koordinatak szamitasa:
                #Negyed keresese:
                if sz50 == 1:
                        y_t= 0
                        x_t= 1
                if sz50 == 2:
                        y_t= 1
                        x_t= 1
                if sz50 == 3:
                        y_t= 0
                        x_t= 0
                if sz50 == 4:
                        y_t= 1
                        x_t= 0

                y_also_50 = y_also_100 + dy_50 * y_t
                x_also_50 = x_also_100 + dx_50 * x_t

                y_felso_50 = y_also_50 + dy_50
                x_felso_50 = x_also_50 + dx_50

                #25-res koordinatak szamitasa:
                #Negyed keresese:
                if sz25 == 1:
                	y_t= 0
                	x_t= 1
                if sz25 == 2:
                	y_t= 1
                	x_t= 1
                if sz25 == 3:
                	y_t= 0
                	x_t= 0
                if sz25 == 4:
                	y_t= 1
                	x_t= 0

                y_also_25 = y_also_50 + dy_25 * y_t
                x_also_25 = x_also_50 + dx_25 * x_t

                y_felso_25 = y_also_25 + dy_25
                x_felso_25 = x_also_25 + dx_25

                #10-res koordinatak szamitasa:
                #Negyed keresese:
                if sz10 == 1:
                	y_t= 0
                	x_t= 1
                if sz10 == 2:
                	y_t= 1
                	x_t= 1
                if sz10 == 3:
                	y_t= 0
                	x_t= 0
                if sz10 == 4:
                	y_t= 1
                	x_t= 0

                y_also_10 = y_also_25 + dy_10 * y_t
                x_also_10 = x_also_25 + dx_10 * x_t

                y_felso_10 = y_also_10 + dy_10
                x_felso_10 = x_also_10 + dx_10

                eovszam = [szelveny[0],szelveny[1],szelveny[2],"-",szelveny[4],szelveny[5],szelveny[6],"."]
                print ("EOV 10 000 szelveny:")
                nev = "".join(eovszam)
                print (nev)
                print (y_also_10)
                print (x_also_10)
                print (y_felso_10)
                print (x_felso_10)


    #Egyik sem:
    if hossz < 6 or hossz > 7:
            print ("Nem EOV 10 000-res szevenyszamot adtal meg!")

    print ("Exportalas kezdodik:")
    path = mappa + nev + type
    print (path)
    sarkok =(y_also_10, x_also_10, y_felso_10, x_felso_10)
    chunk.exportOrthophoto(path, type, "mosaic", projection = proj, region = sarkok, dx = d_x, dy = d_y, write_kml=False, write_world=False)
    print (" ")
#### Exportalas deffinialas vege modositast nem igenyel ######################################


# EOV szelvenyek felsorolasa, megadas: - legyen 0 pl.: 23-123 -->230123   ####################
export_eov(230121)
export_eov(8100122)
# EOV szelvenyek felsorolasa vege ############################################################
