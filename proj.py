want_play = input("Do you want play? ")

if want_play.lower() != "yes":
    quit()

print("lets go playing")
# what is the name for the channel?
# who is the owner for tesla?
# who is the owner for space x?

answer = input("what is the name for my channel? ")
if answer.lower() == "learncodeeasily":
    print("Correct!")
else:
    print("Incorrect!") 
    quit()   

answer = input("who is the owner of tesla? ")
if answer.lower() == "elon":
    print("Correct!")
else:
    print("Incorrect!")  
    quit()
answer = input("who is the owner of space x? ")
if answer.lower() == "elon":
    print("Correct!")
else:
    print("Incorrect!")            
    quit()

print("cangurolation, you win")