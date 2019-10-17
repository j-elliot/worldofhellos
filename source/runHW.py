#So this program should demonstrate user input, searching for and interpreting
#files, executing command line, and that's about itself.

import os
import webbrowser

listAddr = "../list"

#get user input
#simply gets the name of a language from the user
def queryUser():
    print("What language should I look for?")
    lang = raw_input()
    return lang

#Check list
#takes a file name and the name of the programming language in question
#returns the contents of the filename and start and end ints of relevant data
def readList(fileName, selfName):

    file = open(fileName, "r")

    instList = []
    start = 0
    end = 0
    flag = False

    if (file.mode == 'r'):

        instList = file.readlines()

        for i, line in enumerate(instList):

            if (line == (selfName + "{\n")):

                start = i
                flag = True

            if (flag and (line == "}\n")):

                end = i
                flag = False

    return instList[start:end]

#get instructions
#validates user input
def getIns():

    ins = readList(listAddr, queryUser())

    while (len(ins) == 0):

        print("I'm sorry, I couldn't find that language. Please try again or press CTRL + c to exit.")

        ins = readList(listAddr, queryUser())

    return ins

#parse instructions
def parseIns(ins):

    ls = ["","","","",""]

    for line in ins:

        if line.find("sourcefile:") > -1:
            ls[0] = line[12:len(line)-1]

        if line.find("command:") > -1:
            ls[1] = line[9:len(line)-1]

        if line.find("compile:") > -1:
            ls[2] = line[9:len(line)-1]

        if line.find("run:") > -1:
            ls[3] = line[5:len(line)-1]

        if line.find("markupfile:") > -1:
            ls[4] = line[12:len(line)-1]

    return ls



#find source file
#accepts a file name, validates its existence
def findFile(fil):

    dirCont = os.popen('ls').read()

    return (dirCont.find(fil) > -1)

#run file
#accepts file and format and executes command
#will need additional handling for compiled langauges
def runFile(fil, com=None, run=None, mark=None):

    if run:

        loadedCommand = com.replace("<sourcefile>", fil)

        os.system(loadedCommand)

        os.system(run)

        return os.popen(run).read()

    elif mark:

        site = mark

        webbrowser.open_new(site)

    else:

        loadedCommand = com.replace("<sourcefile>", fil)

        os.system(loadedCommand)

        return os.popen(loadedCommand).read()

#check output
def check(out):

    print("-->")

    if "Hello World" in out:

        print("Program was successfully executed")

    else:

        print("Program seems to have failed")

#driver
def driver():

    controlList = parseIns(getIns())

    if(findFile(controlList[0])) and not controlList[2] and not controlList[4]:

        check(runFile(controlList[0], com=controlList[1]))

    elif(findFile(controlList[0])) and not controlList[1] and not controlList[4]:

        check(runFile(controlList[0], com=controlList[2], run=controlList[3]))

    elif(findFile(controlList[0])) and controlList[4]:

        check(runFile(controlList[0], mark=controlList[4]))



driver()
