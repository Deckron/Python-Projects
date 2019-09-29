#ok ill work out this portion later
'''def openfile():
    file= open("390notes.txt","w")
    file.write("here we go")
    file.write(" ")
    file.write("i have no idea what im doing")
    file.close()'''
#work from here until it works, work out the above some other time
def notes(notes):
    file =  open ("390notes.txt", "a")
    notes=input("input notes:")
    while "end" not in notes:
        if "end"in notes:
            file.close()
        file.write(notes)
        file.write(" ")
        file.write("\n")
        notes= input("input notes:")
    file.close()
notes(notes)

def readnotes():
    file=open("390notes.txt", "r")
    print (file.read())
readnotes()


#while notes is not "end":
       # file.write(notes)
        #file.write(" ")
        #file.write("\n")
        #break
    #while notes is "end":
     #   file.close()
#used stack overflow for \n resource


  #for word in notes:
   #     if word is not "end":
    #        file.write(word)
     #       file.write("\n")
      #      notes = input("input notes:")
       # if word is "end":
        #    return
