def gatherNotes (event = None):
    inputs = []
    with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
        for line in notes:
            inputs.append(line.rstrip("\n"))
            print(inputs)
            gathered = {}
            for item in inputs:
                head = str.split(inputs[item][0], ': ')
                print(head[0], head[1])
                gathered[head[0]] = head[1]
            return gathered


def gatherNotes (event = None):
    inputs = []
    gathered = {}
    with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
        for line in notes:
            inputs.append(line.rstrip("\n"))
            print(inputs)

            for item in inputs:
                head = str.split(inputs[item][0], ': ')
                gathered[inputs.index(item)+1] = [item]

        return gathered


def gatherNotes (event = None):
    inputs = []
    with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
        for line in notes:
            inputs.append(line.rstrip("\n"))
            gathered = {}
            for item in inputs:
                gathered[inputs.index(item)+1] = [item]
        return gathered
