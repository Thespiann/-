#Ασκηση 6
import random
blackpoints=0
whitepoints=0
#Θα φτιάξω την σκακιέρα 8*8
rows=8
cols=8
board=[[[j, i, "pawn"] for i in range(rows)]for j in range(cols)]
#εχω κατι τέτοιο:
#[[[0, 0, 'pawn'], [0, 1, 'pawn'], [0, 2, 'pawn'], [0, 3, 'pawn'], [0, 4, 'pawn'], [0, 5, 'pawn'], [0, 6, 'pawn'], [0, 7, 'pawn']],
#[[1, 0, 'pawn'], [1, 1, 'pawn'], [1, 2, 'pawn'], [1, 3, 'pawn'], [1, 4, 'pawn'], [1, 5, 'pawn'], [1, 6, 'pawn'], [1, 7, 'pawn']],
#[[2, 0, 'pawn'], [2, 1, 'pawn'], [2, 2, 'pawn'], [2, 3, 'pawn'], [2, 4, 'pawn'], [2, 5, 'pawn'], [2, 6, 'pawn'], [2, 7, 'pawn']],
#[[3, 0, 'pawn'], [3, 1, 'pawn'], [3, 2, 'pawn'], [3, 3, 'pawn'], [3, 4, 'pawn'], [3, 5, 'pawn'], [3, 6, 'pawn'], [3, 7, 'pawn']],
#[[4, 0, 'pawn'], [4, 1, 'pawn'], [4, 2, 'pawn'], [4, 3, 'pawn'], [4, 4, 'pawn'], [4, 5, 'pawn'], [4, 6, 'pawn'], [4, 7, 'pawn']],
#[[5, 0, 'pawn'], [5, 1, 'pawn'], [5, 2, 'pawn'], [5, 3, 'pawn'], [5, 4, 'pawn'], [5, 5, 'pawn'], [5, 6, 'pawn'], [5, 7, 'pawn']],
#[[6, 0, 'pawn'], [6, 1, 'pawn'], [6, 2, 'pawn'], [6, 3, 'pawn'], [6, 4, 'pawn'], [6, 5, 'pawn'], [6, 6, 'pawn'], [6, 7, 'pawn']],
#[[7, 0, 'pawn'], [7, 1, 'pawn'], [7, 2, 'pawn'], [7, 3, 'pawn'], [7, 4, 'pawn'], [7, 5, 'pawn'], [7, 6, 'pawn'], [7, 7, 'pawn']]]

#θα δημιουργησω συναρτησεις ωστε να "τρωνε" τα πιονια
def rookeats(a,b):#ενας ασπρος πυργος που βρίσκεται στην σειρα a και στην στηλη b θα τρωει την μαυρη βασίλισσα όταν "eats=True"
    eats=False
    for i in range(8):
        if board[i][a][2]=="bqueen":#ελεγχω αν ο πυργος τρωει κατακόρυφα
            eats= True
        if board[b][i][2]=="bqueen":#ελεγχω αν ο πυργος τρωει οριζόντια
            eats= True
        else:
            eats= False
    return eats

#φτιάχνω μία συνάρτηση για να μου δίνει μία λίστα με τις διαγώνιους της θέσης χ,υ που δίνω ωστε να δω πως "τρωει" ο αξιωματικός και η βασίλισσα
def samediag(x,y):
    samediags=[]
    for i in range(8):
        for j in range(8):
            if i+j==x+y:
                samediags.append([i,j])
            if i-j==x-y:
                samediags.append([i,j])
    return samediags

def bishopeats(a,b):#ενας ασπρος αξιωματικός που βρίσκεται στην σειρα a και στην στηλη b θα τρωει την μαυρη βασίλισσα όταν "eats=True"
    eats=False
    bishopdiag=samediag(a,b)
    for i in range(len(bishopdiag)):
        x=bishopdiag[i][0]
        y=bishopdiag[i][1]
        if board[x][y][2]=="bqueen":
            eats=True
        else:
            eats=False
    return eats

def queeneatsrook(a,b):# μια μαυρη βασίλισσα στα a,b τρωει τον ασπρο πύργο ή τον αξιωματικό όταν "eats=True"
    eats=False
    queendiag=samediag(a,b)
    for i in range(len(queendiag)):
        x=queendiag[i][0]
        y=queendiag[i][1]
        if board[x][y][2]=="wrook":
            eats=True
            break
        else:
            for i in range(8):
                if board[i][b][2]=="wrook":
                    eats=True
                    break
                if board[a][i][2]=="wrook":
                    eats=True
                    break
                else:
                    eats=False
    return eats

def queeneatsbishop(a,b):# μια μαυρη βασίλισσα στα a,b τρωει τον ασπρο πύργο ή τον αξιωματικό όταν "eats=True"
    eats=False
    queendiag=samediag(a,b)
    for i in range(len(queendiag)):
        x=queendiag[i][0]
        y=queendiag[i][1]
        if board[x][y][2]=="wbishop":
            eats=True
            break
        else:
            for i in range(8):
                if board[i][b][2]=="wbishop":
                    eats=True
                    break
                if board[a][i][2]=="wbishop":
                    eats=True
                    break
                else:
                    eats=False
    return eats
def randomplaces():
    myboard=[]
    #θα τοποθετησω τα πιονια σε τυχαιεσ θεσεις
    puton= range(8)
    x1=random.choice(puton)
    y1=random.choice(puton)
    x2=random.choice(puton)
    y2=random.choice(puton)
    x3=random.choice(puton)
    y3=random.choice(puton)#x=σειρα y=στηλη 1=rook 2=bishop 3=queen


    if [x1,y1]!=[x2,y2]!=[x3,x3]:
        myboard=[x1,y1,x2,y2,x3,y3]
    else:
        x1=random.choice(puton)
        y1=random.choice(puton)
        x2=random.choice(puton)
        y2=random.choice(puton)
        x3=random.choice(puton)
        y3=random.choice(puton)
        myboard=[x1,y1,x2,x2,x3,y3]
    return myboard

for i in range(100):
    pawnsplaces=randomplaces()
    xr=pawnsplaces[0]
    yr=pawnsplaces[1]
    xb=pawnsplaces[2]
    yb=pawnsplaces[3]
    xq=pawnsplaces[4]
    yq=pawnsplaces[5]
    board[xr][yr][2]="wrook"
    board[xb][yb][2]="wbishop"
    board[xq][yq][2]="bqueen"

    if rookeats(xr,yr)==True:
        whitepoints+=1
    if bishopeats(xb,yb)==True:
        whitepoints+=1
    if queeneatsrook(xq,yq)==True:
        blackpoints+=1
    if queeneatsbishop(xq,yq)==True:
        blackpoints+=1

blackpointss=str(blackpoints)
whitepointss=str(whitepoints)
print("Black has "+blackpointss+" points")
print("White has "+whitepointss+" points")
