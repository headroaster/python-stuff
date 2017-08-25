#!/usr/bin/python3

from tkinter import *
fields = 'Customer Name:', 'TID:', 'Serial:', 'Reason for Call:', 'Action taken or needed:'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()


'''
customerName = input("What line is this coming in on? ")
tid = input("What is the TID for this machine? ")
callDriver = input("Why is this person calling you? ")
caller = input("What's their name? ")
callBack = input("What's their phone number? ")
serial = input("What's the serial number? ")
address = "" #input("What's the address? ")
zip = "" #input("What's the ZIP or Postal Code? ")
notes = input("What did you do, or what needs to be done? ")
'''
