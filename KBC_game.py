questions = [["What is the full form of CPU?","Central Processing Unit", "Computer Processing Unit,", "Central Program Unit", "None of the above",1],
            ["What is the full form of RAM?" ,"Random Access Memory","Read Only Memory" ,"Readable And Mutable Memory","None of the above", 1],
            ["What is the full form of ROM" , "Random access Memory", "Read Only Memory", "REadable and Mutable Memory" , "None of the Above", 2],
            ["What is the full form of ALU?", "Algorithm and logic Unit", "Algorithmic Logic Unit", "Arthmetic Logic Unit", "None of the above", 3],
            ["What is the full form of GPU?", "Graphics Procssing Unix", "Graphic Processing Unit","Graphics Program Unit", "None of the above", 2],
            ["What is the ful form of BIOS?", "Basic IN Out system", "Basic Input Output System","Basic Input output Service", "none of the above",2],
            ["What is the full form of OS?", "Operating System", "Operation System", "Operating Service", "None of the above", 1],
            ["What is the full form of GUI?", "Graphical User Interface", "Graphic User Interface", "Graph User Interface"," All of the above", 1],
            ["What is the full form of CLI?", "Command Line Interface", "Commando Linux Ice-Cream", "Common Unified Interface", "None of the above", 1],
            ["What is the full form of API?", "Application program Interface", "Application Programming Interface", "Appoclyps predefine Interface", "None of the above", 1],
]
levels= [1000,3000,5000,10000,20000,50000,1000000,5000000,10000000,25000000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for ₹{levels[i]}") 
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4):\n"))
    if not 0 < reply<=4 :
        raise ValueError("Not a valid option")
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won ₹ {levels[i]}")
        if(i == 4):
            money = 1000
        # elif (i == 9):
        #     money = 25000000
        # elif (i == 14):
        #     money = 10000000
        # else:
        #     print(("Wrong Answer!"))
        #     break
print((f"Your take home money is {levels[i]}"))
