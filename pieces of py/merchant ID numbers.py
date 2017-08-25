linesOfBiz = {"Cardtronics" : "2000300", "ASAI" : "2000800", "ATM USA" : "2001200", "National" : "2001300", "OptConnect" : "2001600", "EGlobal ATM" : "2001700", "Cord Financial" : "2002000", "CT Can" : "2002300", "CAI" : "2002400", "First" : "2002600", "ISA" : "2003200", "Kahuna" : "2003600",  "Jarrett" : "2003800",  "Paramount" : "2004400",  "Access One" : "2004700",  "Intelli-Call" : "2005900", "Tidel" : "2000600"}

print ('customers name')
while True:
    selection = input('What line is this coming in on?')
    if selection in linesOfBiz:
        print("The customer's account number is {station}".format(
              station=linesOfBiz[selection]))
        break
    else:
        print ('ya dun fucked up.')
