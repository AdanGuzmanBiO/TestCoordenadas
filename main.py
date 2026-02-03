LlistaMapa= [[1,2,3],[4,5,6],[7,8,9]]
posMapX= 1
posMapY= 1

while True:
    posicionMapa = [[posMapX],[posMapY]]

    moviment = (input("Cap a on et vols moure? " ))
    match moviment:
        case "nord":
            posMapY += 1
    
        case "sud":
            posMapY -= 1
        
        case "est":
            posMapX += 1

        case "oest":
            posMapX -= 1

    print (posicionMapa)
    
    match posicionMapa:
        case 1:
            print ("estas a l'escena 1")
        
        case 2:
            print ("estas a l'escena 2")
        
        case 3:
            print ("estas a l'escena 3")

        case 4:
            print ("estas a l'escena 4")
        
        case 5:
            print ("estas a l'escena 6")
        
        case 6:
            print ("estas a l'escena 6")
        
        case 7:
            print ("estas a l'escena 7")

        case 8:
            print ("estas a l'escena 4")
        
        case 9:
            print ("estas a l'escena 9")