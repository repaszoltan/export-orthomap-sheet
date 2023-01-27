#RÉPÁS Zoltán
#2023.01



#### Init for PhotoSann software ##############################################################################
import PhotoScan
doc = PhotoScan.app.document
chunk = doc.activeChunk
#### End of inti####### ########################################################################################

#### SETTINGS ##################################################################################################
# Edit before use:
#   file type of the result picture:
type = "tif"

#   path of working directory:
folder = "C:/python/HelloAgiSoft/"

#   Resolution of the ortho mosaic in [m]:
d_x = d_y = 0.5


#   Coordinate System Datum:
proj = PhotoScan.CoordinateSystem()
proj.init("EPSG::23700")
#EOV:"EPSG::23700"
#WGS84:"EPSG::4326"

#### End of SETTINGS ############################################################################################

def readEOV(mapSectionNumber):
    """Define an export instruction for AgiSoft Photoscan"""

    def getEOVRowColumn(mapSectionNumber):
        #There ara 4 case
        #An 1:10 000 EOV section number mask: XX-XXX or XXX-XXX eg.: 40-214
        #Where the numbers are:[row] [column] - [section 1:50 000] [section 1:25 000] [section 1:10 000]
        #The row and column numbers can be 2 or 3 caracter long, and it is important which is the double long

        #Case 1. row and column are one-one caracters
        #Case 2. row is two caratcer long
        #Case 3. cloumn is two caracter long
        #Case 4. bad input

        #Init the long of the frist section
        correctValue = True                         #For checking the end of the process
        counter = 0
        for x in mapSectionNumber:
            if x == '-':
                break
            else:
                counter = counter + 1
        #Branching in four directions
        if counter == 2:                        #Case 1.
            rowEOV = int(mapSectionNumber[0])
            columnEOV = int(mapSectionNumber[1])

        elif counter == 3:                      #Case 2. and Case 3.
            if int(mapSectionNumber[0]) == 1:   #Case 2.
                rowEOV = int(mapSectionNumber[0] + mapSectionNumber[1])
                columnEOV = int(mapSectionNumber[2])
            else:                               #Case 3.
                rowEOV = int(mapSectionNumber[0])
                columnEOV = int(mapSectionNumber[1] + mapSectionNumber[2])

        else:                                   #Case 4.
            correctValue = False
        #Value checking
            #May some section do not fall within the territory of Hungary, 
            #but we will leave that aside for now

        #Get the result list back:
        if correctValue == True:
            rowAndColumnList = [rowEOV,columnEOV]
            return(rowAndColumnList)
        else:
            return(False)


    def getEOVSections(mapSectionNumber):
        #The 1st nuber represent the 1:50 000 scale section
        #The 2nd number represent the 1:25 000 scale section
        #The 3rd - 1:10 000, 4th - 1:4 000, 5th - 1:2 000, 6th - 1:1 000, 7th - 1:500, thats all.
        #A higher secton divide for 4 lower sections (Higher in hierarchy, but smaller in scale, bc 1:50 000 is smaller than 1:500)
        #So the secton numbers can be only 1, 2, 3 or 4

        #Init the long of the frist section
        counter = 0
        for x in mapSectionNumber:
            if x == '-':
                counter = counter + 1
                break
            else:
                counter = counter + 1
        
        charactersOfSections = mapSectionNumber[(counter):]             #get a str value of useful characters
        sectionNumbersList = []                                         #makeing a list for the section nubers
        for x in charactersOfSections:
            sectionNumbersList.append(int(x))                           #copy the str values to a list, and make them integer
        #Value checking
        correctValue = ""                                               #a marker for the value checking
        for x in sectionNumbersList:
            if 0 < x and x < 5:                                         #only 1, 2, 3 and 4 allowed
                correctValue = True
            else:
                correctValue = False
                print('The', mapSectionNumber, 'contains incorrect data input.')
                break
        if len(sectionNumbersList) > 7:                                 #Only 7 digits alowed
            correctValue = False

        if correctValue == True:
            return(sectionNumbersList)                                  #If everithing is OK, return the result list of section values
        else:
            return(False)
    
    def getEOVCornerCoords(sectionEOV):
        #Def strating values
        start_y_coord = 384000
        start_x_coord = 32000
        #EOV sections side lenght in meter:
        #1:100 000
        delta_y = 48000
        delta_x = 32000
        #Hint:
        #1:50 000
        # delta_y / 2**1
        #1:20 000
        # delta_y / 2**2 etc...

        #Init the section level and coords of the down left + upper right coords
        level = len(sectionEOV) - 2                                 #The first two element is the row and column value, we need the rest of
        powerExponent = 1                                           #for calculate the delta_y and delta_x values for each scale levels (delta_y / 2**powerExponent)
        #Calc 1:100 000 coords
        down_left_x = start_x_coord + delta_x * sectionEOV[0]       #The row number define the start x coords
        down_left_y = start_y_coord + delta_y * sectionEOV[1]       #The row number define the start y coords
        #Calc the coords of each scale level
        while level > 0:                                            #Analyze the section values to define coords ofset values
            if sectionEOV[powerExponent + 1] == 1:
                    y_t= 0
                    x_t= 1
            if sectionEOV[powerExponent + 1] == 2:
                    y_t= 1
                    x_t= 1
            if sectionEOV[powerExponent + 1] == 3:
                    y_t= 0
                    x_t= 0
            if sectionEOV[powerExponent + 1] == 4:
                    y_t= 1
                    x_t= 0
            #Calculate the down left corner coords in each iterations
            down_left_y = down_left_y  + (delta_y / 2**powerExponent) * y_t
            down_left_x = down_left_x  + (delta_x / 2**powerExponent) * x_t
            powerExponent = powerExponent + 1                                       #Increment the "powerExponent" variable
            level = level - 1                                                       #Reduction the "level" variable
        print('Y1:',down_left_y)
        print('X1:',down_left_x)
        up_riht_y = down_left_y + (delta_y / 2**(powerExponent-1))                  #Calc the upper right y coord
        up_right_x = down_left_x  + (delta_x / 2**(powerExponent-1))                #Calc the upper right x coord
        print('Y2:',up_riht_y)
        print('X2:',up_right_x)
        cornerCoords = [up_riht_y, up_right_x, down_left_y, down_left_x]
        return(cornerCoords)
    
    def getEOVSectionScale(mapSectionNumber, sectionEOV):
        scaleLevel = len(sectionEOV)
        if scaleLevel == 3:
            sectionScale = '1:50 000'
        elif scaleLevel == 4:
            sectionScale = '1:25 000'
        elif scaleLevel == 5:
            sectionScale = '1:10 000'
        elif scaleLevel == 6:
            sectionScale = '1:4 000'            
        elif scaleLevel == 7:
            sectionScale = '1:2 000'
        elif scaleLevel == 8:
            sectionScale = '1:1 000'
        elif scaleLevel == 9:
            sectionScale = '1:500'
        print('The ',mapSectionNumber,'section scale is:',sectionScale)
        return (sectionScale)


    #Make the list of section numbers
    sectionEOV = []                                                     #The correct list of section numbers
    rowColumnList =getEOVRowColumn(mapSectionNumber)
    sectionList = getEOVSections(mapSectionNumber)
    if rowColumnList == False or sectionList == False:                  #Check if incorrect datainput was given
        print('The', mapSectionNumber, 'contains incorrect data input.')
    else:                                                               #If input was corret
        for x in rowColumnList:
            sectionEOV.append(x)
        for x in sectionList:
            sectionEOV.append(x)

        getEOVSectionScale(mapSectionNumber,sectionEOV)                          #Give scale info about the section
        coords = getEOVCornerCoords(sectionEOV)                                  #Calc the coordinates
        print ('Starting export:')
        path = folder + mapSectionNumber + type
        print (path)
        # Define an export instruction for AgiSoft Photoscan
        chunk.exportOrthophoto(path, type, "mosaic", projection = proj, region = coords, dx = d_x, dy = d_y, write_kml=False, write_world=False)
        print (" ")


# Listing the EOV section numbers ################################################################################
readEOV('40-1123')
readEOV('109-3211223')
readEOV('1111111')
readEOV('910-21341111')
readEOV('9100-21341')