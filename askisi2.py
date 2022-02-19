#Άσκηση 2
import random
counter=0
for i in range(100):
    #Φτιάχνω το τετράγωνο 3*3
    rows, cols= (3,3)
    wherewhat=["row","col","cap"] #ανα σειρα row και στηλη col εχω ένα cap, το cap είναι μια άδεια θεση για καπακι
    board=[[wherewhat for i in range(cols)]for j in range(rows)]

    #ελέγχω αν έχω νικήσει στις σειρές
    def winrows():
            win= None
            for r in range(rows):
                if board[r][0][2]<board[r][1][2]<board[r][2][2]!="cap":#ελεγχει αν τα καπάκια πάνε απο το μικρότερο στο μεγαλύτερο
                    win=True
                    break
                if board[r][0][2]==board[r][1][2]==board[r][2][2]!="cap":#ελεγχει αν τα καπάκια είναι όλα  ίδια και οτι δεν είναι cap
                    win=True
                    break
                else:
                    win=False
            return win

    #ελέγχω αν εχω νικήσει στις στήλες
    def wincols():
            win= None
            for c in range(cols):
                if board[0][c][2]<board[1][c][2]<board[2][c][2]!="cap":#ελεγχει αν τα καπάκια πάνε απο το μικρότερο στο μεγαλύτερο
                    win=True
                    break
                if board[0][c][2]==board[1][c][2]==board[2][c][2]!="cap":#ελεγχει αν τα καπάκια είναι όλα  ίδια και οτι δεν είναι cap
                    win=True
                    break
                else:
                    win=False
            return win

    #ελέγχω αν εχω νικήσει διαγώνια
    def windiagonals():
        win= None
        if board[0][0][2]<board[1][1][2]<board[2][2][2]!="cap":#ελεγχει αν τα καπάκια πάνε απο το μικρότερο στο μεγαλύτερο
            win=True
        if board[2][0][2]<board[1][1][2]<board[0][2][2]!="cap":#ελεγχει αν τα καπάκια πάνε απο το μικρότερο στο μεγαλύτερο(στην αλλη διαγώνιο)
            win=True
        if board[2][0][2]==board[1][1][2]==board[0][2][2]!="cap":#ελεγχει αν τα καπάκια είναι όλα  ίδια και οτι δεν είναι cap
            win=True
        if board[0][0][2]==board[1][1][2]==board[2][2][2]!="cap":#ελεγχει αν τα καπάκια είναι όλα  ίδια και οτι δεν είναι cap
            win=True
        else:
                win=False
        return win


    #Φτιαχνω μια λίστα που περιέχει όλα μου τα καπάκια
    smallcaps, mediumcaps, bigcaps = (9, 9, 9)
    mycaps=["1"]*smallcaps
    mycaps+=["2"]*mediumcaps
    mycaps+=["3"]*bigcaps

    #Φτιάχνω μία λίστα με τους αριθμους των σειρών και μια με των στηλών ώστε να τα χρησιμοποιησω σαν συντεταγμενες kαι να βάλω καπακια στο board
    putonrow= [0,1,2]
    putoncol= [0,1,2]

    #δημιουργώ όλους τους πιθανούς συνδυασμόυς θέσεων και ειδων απο καπάκια, εχω 3*3*27=243 επιλογές
    placeswithcaps=[(int(x),int(y),str(z)) for x in putonrow for y in putoncol for z in mycaps]
    #διαλέγω μία τυχαία θέση και ένα τυχαίο καπάκι
    combination=random.choice(placeswithcaps)

    while winrows()==False and wincols()==False and windiagonals()==False:
        x=combination[0]
        y=combination[1]

        if board[x][y][2]=="cap" :#εαν δεν υπαρχει καπακι στην τυχαία θεση βάζω το καπάκι μου
            board[x][y]=combination
            counter+=1
        if board[x][y][2]<combination[2]:
            board[x][y]=combination
            counter+=1
        else:
            combination=random.choice(placeswithcaps)
averagesteps=counter//100
print(averagesteps)
