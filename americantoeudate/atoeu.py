#Python script to search a directory for filenames with american style dates and convert
#them to europian style dates

import re , os , shutil

datef = re.compile(r"^(.*?)(\d?\d)-(\d?\d)-(\d\d\d\d)(.*)$")
for filename in os.listdir("./dates"):
    name = datef.findall(filename)
    if name != []:
        print(filename)
        print(name)
        date = name[0][2] + "-" + name[0][1] + "-" + name[0][3]
        print(date)
        newname = name[0][0] + date + name[0][4]
        print(newname)
        shutil.move("./dates/{}".format(filename) , "./dates/{}".format(newname))
    
    

    
    
