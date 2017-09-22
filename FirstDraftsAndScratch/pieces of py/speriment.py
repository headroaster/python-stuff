def gatherNotes (event = None):
    inputs = []
    with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
        for line in notes:
            inputs.append(line)

        gathered = {}
        for item in inputs:
            gathered[inputs.index(item)+1] = item
        return gathered




def gatherNotes (self):
    prompts = {'inputNotes[3]' : "Customer Name: ", 'inputNotes[4]' : "TID:  ",
    'inputNotes[5]' : "Call Driver: ", 'inputNotes[6]' : "Caller's Name: ",
    'inputNotes[7]' : "Phone Number: ", 'inputNotes[8]' : "Serial Number: ",
    'inputNotes[9]' : "Street Address: ", 'inputNotes[10]' : "ZIP or Postal Code: ",
    'inputNotes[11+]' : "Notes: "}
    gathered = ({})
    for item in prompts:
        gathered[prompts[item]] = item.GetValue()
        return gathered
