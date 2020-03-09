mask = input("Are you wearing a mask?")
scrubs = input("Are you wearing scrubs?")

if mask == "yes":
    if scrubs == "yes":
        print("You may enter the OT")
    else:
        print("You may not enter the OT")
else:
    print("You may not enter the OT")
