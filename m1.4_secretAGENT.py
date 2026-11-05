name = input("Enter your name: ")
favoriteGADGET = input("What is your favorite gadget: ")
agentNUMBER = 7
speedRATING = 9.5
missionCOUNT = 9
Height = 153.9
Status = True
agentNUMBERnew = str(agentNUMBER)
mission_countNEW = str(missionCOUNT) 
speedRATINGnew = str(speedRATING)
status_2 = str(Status)
print(type(agentNUMBERnew))
print(type(status_2))
print(type(speedRATINGnew))
first3letter_name = name[0:3]
lastLEtter_name = name[-1]
codename = first3letter_name + lastLEtter_name
reverse_gadgetNAME = favoriteGADGET[::-1]
badgeline1 = "agent " + codename.upper()
badgeline2 = "id: " + agentNUMBERnew + ", missions: " + mission_countNEW
badgeline3 = "speed " + speedRATINGnew + " active value " + status_2
badgeline4 = "secret gadget code " + reverse_gadgetNAME
print(badgeline1)
print(badgeline2)
print(badgeline3)
print(badgeline4)


