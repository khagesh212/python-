def parrot_trouble(talking,hour):
    if talking==True and (talking<7 or talking>20):
        return True
    else:
        return False

print(parrot_trouble(True,6))
print(parrot_trouble(True,7))
print(parrot_trouble(False,9))