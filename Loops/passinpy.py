for i in range(5,10,2):
    if(i==7):
        continue
    else:
        print(i)
else:
    print("Condition failed so it reached here")
    #reached here means that the loop is finished and it will execute the else block after the loop is finished.
    #u can use break statement to exit the loop and it will not execute the else block.
    # u can use pass without loops like continue.