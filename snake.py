import random
from threading import Timer
def placeApple(lst):

    line = random.randint(0, len(lst)-1)
    placement = random.randint(0, len(lst)-1)
    isIn = False
    finished = False
    placementLst = []
    for items in lst:
        if "⬜" in items:
            isIn = True
    if isIn == False:
        print("You win!")
        print("You got", apples, "apples!")
        main()
    while finished == False:
        
        line = random.randint(0, len(lst)-1)
        placement = random.randint(0, len(lst)-1)
        placementLst.append([line, placement])
        while len(placementLst) > apples:
            placementLst.pop(-1)
        if len(tailLst) >= 1:
            if placementLst[0] not in tailLst:
                placementLst = []
                finished = True
        else:
            placementLst = []
            finished = True
        placementLst = []

    text = lst[line]
    new = list(text)
    new[placement] = '🍎'
    new = ''.join(new)
    lst[line] = new
    return lst

def main():
    emojis = "⬜ 🟥 😩 🍎"
    lst = ["⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"]
    global apples
    apples = 0
    tails = 0
    global tailLst
    tailLst = []


    lst = placeApple(lst)

    text = lst[random.randint(3, len(lst)-4)]
    new = list(text)
    new[random.randint(3, len(new)-4)] = '😩'
    new = ''.join(new) 
    lst[random.randint(3, len(lst)-4)] = new



    class tail:
        def __init__(self, locationX, locationY):
            self.locationX = locationX
            self.locationY = locationY
        def delete(self):
            thing = tailLst[0]
            thingX = thing[0]
            thingY = thing[1]
            funny = lst[thingX]
            new = list(funny)
            new[thingY] = "⬜"
            new = ''.join(new) 
            lst[thingX] = new
            tailLst.pop(0)

    direction = "w"
    while True:
        funniLst = ["w", "a", "s", "d"]
        yes = False
        for i in range(len(lst)):
            print(lst[i])

        seconds = 0.5 - 0.01*apples
        timer = Timer(seconds, print,)
        timer.start()
        print("What direction")
        answer = input()
        if timer.is_alive():
            timer.cancel()
            move = answer.lower()
            direction = move
        else:
            timer.cancel()
            move = direction
        for i in range(len(lst)):
            if "😩" in lst[i]:
                item = lst[i]
                for j in range(len(item)):
                    if item[j] == "😩":
                        headLine = i
                        headPlace = j
        if move.lower() == "w":
            direction = "w"
            text = lst[headLine-1]
            new = list(text)
            if headLine-1 == -1:
                print("You lose! You had", apples, "apples")
                main()
            if new[headPlace] == "🍎":
                apples += 1
                yes = True
            elif new[headPlace] == "🟥":
                print("You lose! You had", apples, "apples")
                main()
            new[headPlace] = '😩'
            new = ''.join(new) 
            lst[headLine-1] = new
            text = lst[headLine]
            new = list(text)
            new[headPlace] = '🟥'
            pro = tail(headLine, headPlace)
            
            tailLstLst = [pro.locationX, pro.locationY]
            tailLst.append(tailLstLst)
            tails += 1
            new = ''.join(new) 
            lst[headLine] = new
        elif move.lower() == "s":
            direction = "s"
            try:
                text = lst[headLine+1]
            except:
                print("You lose! You had", apples, "apples")
                main()
            new = list(text)
            if new[headPlace] == "🍎":
                apples += 1
                yes = True
            elif new[headPlace] == "🟥":
                print("You lose! You had", apples, "apples")
                main()
            new[headPlace] = '😩'
            new = ''.join(new) 
            lst[headLine+1] = new
            text = lst[headLine]
            new = list(text)
            new[headPlace] = '🟥'
            pro = tail(headLine, headPlace)
            tailLstLst = [pro.locationX, pro.locationY]
            tailLst.append(tailLstLst)
            tails += 1
            new = ''.join(new) 
            lst[headLine] = new
        elif move.lower() == "a":
            direction = "a"
            text = lst[headLine]
            new = list(text)
            if headPlace-1 == -1:
                print("You lose! You had", apples, "apples")
                main()
            if new[headPlace-1] == "🍎":
                apples += 1
                yes = True
            elif new[headPlace-1] == "🟥":
                print("You lose! You had", apples, "apples")
                main()
            new[headPlace-1] = '😩'
            new[headPlace] = '🟥'
            pro = tail(headLine, headPlace)
            tailLstLst = [pro.locationX, pro.locationY]
            tailLst.append(tailLstLst)
            tails += 1
            new = ''.join(new)
            lst[headLine] = new
        elif move.lower() == "d":
            direction = "d"
            text = lst[headLine]
            new = list(text)
            if headPlace+1 == len(lst):
                print("You lose! You had", apples, "apples")
                main()
            if new[headPlace+1] == "🍎":
                apples += 1
                yes = True
            elif new[headPlace+1] == "🟥":
                print("You lose! You had", apples, "apples")
                main()
            new[headPlace+1] = '😩'
            new[headPlace] = '🟥'
            pro = tail(headLine, headPlace)
            tailLstLst = [pro.locationX, pro.locationY]
            tailLst.append(tailLstLst)
            tails +=1
            new = ''.join(new)
            lst[headLine] = new

        if yes == True:
            placeApple(lst)
        if tails > apples:
            tails -= 1
            pro.delete()

main()