import random
import re
import time

print("Preparing Quizes....")
time.sleep(1)
ans = {"Rajasthan" : "Jaipur" , "Uttrakhand" : "Dehradun" , "Assam" : "Guwahati" , "UP" : "Lucknow" , "MP" : "Bhopal"}
questions = ["\nQ. What is the capital of {} ?\n ".format(s) for s in ans.keys()]
city = re.compile("|".join(ans.keys()))
for i in range(3):
    print("Shuffling questions.....")
    random.shuffle(questions)
    f = open("q{}.txt".format(i) , "w")
    f.write("Namae Wa :\nDate :\n\n\t\tQUIZ PAPER {}\n".format(i+1))
    for q in questions:
        f.write(q)
        options = random.sample(list(ans.values()) ,3)
        f.write("\n ".join(options))
    f.close()
    print("Quiz {} generated!!".format(i))
    time.sleep(1)
    fans = open("a{}.txt".format(i) , "w")
    for x in questions:
        c = city.search(x)
        fans.write("{}\n".format(ans[c.group()]))
    fans.close()