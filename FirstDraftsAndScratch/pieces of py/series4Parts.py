Cabinets = {\
     '1' : "Series 4 cabinet with Standard Capacity Bill Acceptors",
     '2' : "Series 4 cabinet with Extended Capacity Bill Acceptors",
     '3' : "Series 4 cabinet with hardened steel doors",
     '4' : "Series 4 cabinet with hardened steel doors and Extended Capacity Cassettes",
     '5' : "No Description Please check your part number",
     '6' : "TACC-VI"}

Electronics ={\
      '1' : "Series 4 standard electronics",
      '2' : "Series 4 with add-on module capability",
      '3' : "Series 4 with additional Bill Acceptor Vault attached (2 acceptors)"}

AcceptorQTY = {\
     '0' : "None",
     '1' : "One Acceptor Head",
     '2' : "Two Acceptor Heads"}

Acceptors = {\
     "S" : "644-0106-303S BILL ACCEPTOR HEAD, (MEI SINGLE NOTE FEEDER)",
     "B" : "644-0117-434S BILL ACCEPTOR HEAD, (MEI BULK NOTE FEEDER)",
    "NA" : "644-0106-300R BILL ACCEPTOR HEAD, (MEI SINGLE NOTE FEEDER), USA, RECONDITIONED For 66mm notes"}

Currency = {}

Printers = {\
     '1' : "644-0132-101S PCB, PRINTER (KFI)",
     '2' : "644-0132-402S PRINTER, KFI INTEGRATED (BUILT-IN)"}

Addons = {\
     '0' : ("None"),
     '1' : ("Tube Vend With Drop Vault Base"),
     '2' : ("Storage Vault with Drop Vault Base"),
     '3' : ("Tube Vend with Storage Vault and Drop Vault Base"),
     '4' : ("Tube Vend with Mailbox Vault Base"),
     '5' : ("Storage Vault with Mailbox Vault Base"),
     '6' : ("Storage Vault with Tube Vend and Mailbox Vault Base"),
     '7' : ("Small Drop Vault base and additional Narrow Storage vault"),
     "A" : ("Small Drop Vault base and additional (old style) wider Storage vault "),
     "B" : ("Mailbox Vault base and additional (old style) wider Storage vault"),
     "C" : ("Small Drop Vault base and additional (old style) wider Storage vault and Tube Vend Module"),
     "D" : ("Mailbox Vault base and additional (old style) wider Storage vault and Tube Vend Module")}

ControlPCB = {\
     '1' : ("210-0240-104S", "For customers with Brinks association only For Serial#'s below UG-07470 and UH-01900"),
     '2' : ("210-0320-104S", "For Series 4 units only. For customers with Brinks association only For Serial#'s above UG-07470 and UH-01900"),
     '3' : ("210-0240-109S", "For Series 4 units with add-on Storage Vault module For customers with Brinks association only For Serial#'s below UG-07470 and UH-01900"),
     '4' : ("210-0320-109S", "For Series 4 units with add-on Storage Vault module For customers with Brinks association only For Serial#'s above UG-07470 and UH-01900"),
     '5' : ("210-0240-105S", "For Series 4 units only. For customers with Loomis association only For Serial#'s below UG-07470 and UH-01900"),
     '6' : ("210-0320-105S", "For Series 4 units only. For customers with Loomis association only For Serial#'s above UG-07470 and UH-01900")}

DistributionPCB = {\
     '1' : ("210-0360-001S", "For Series 4 and Series 4e units. For Serial #'s above UG-07470 and UH-01900 Control Panel PCB"),
     '2' : ("210-0260-001S", "For Series 4 and Series 4e units. For Serial #'s below UG-07470 and UH-01900 Control Panel PCB")}

Power = {\
     '1' : ("642-0015-101S", "For Series 4 units only. Left Side +24 VDC"),
     '2' : ("642-0002-101S", "For Series 4 units only. Right Side +5 VDC and +12 VDC")}

Display = {\
     '1' : ("633-0020-007S", "DISPLAY/TOUCHSCREEN ASSEMBLY WITH BACKLIGHT BULB")}

safePartNum = "CC112S000000B004"
def getParts ():
	print(Cabinets[safePartNum[2]])
	print(Electronics[safePartNum[3]])
	print(AcceptorQTY[safePartNum[4]])
	print(Acceptors[safePartNum[5]])
	print(Printers[safePartNum[7]])
	
	return
