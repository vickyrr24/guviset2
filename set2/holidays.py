string=input()
lst=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
if(string.lower() in lst):
    if(string.lower()=="sunday" or string.lower()=="saturday"):
        print("yes")
    else:
        print("no")
else:
    print("Invalid")
