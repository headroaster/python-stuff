with open(os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:

         lines = notes.readlines()
         with open (os.path.expanduser("~/Documents/notes/ticketNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "a") as finalNotes:
             def border():
                 finalNotes.write("\n*********************************************************\n")
                 return
             border()
             finalNotes.writelines(lines)
             border()
            return
