import time , traceback

print("----STOPWATCH-----")
try:
    if input("Press ENTER to start stopwatch: ") == "":
        print("Stopwatch started!")
        lastlap , i= time.time() , 1
        while True:
            input()
            newlap = time.time()
            print("The time of {} lap was: ".format(i) + str(newlap - lastlap))
            lastlap = newlap
            i += 1
    else:
        raise Exception("Wrong Input!")
except:
    print(traceback.format_exc())
    print("Stopwatch stopped!")
    
        
    

