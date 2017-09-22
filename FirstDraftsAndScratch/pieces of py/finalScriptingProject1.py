import os, time, shutil 

source='C:/Python27/Lib/idlelib/source/'
dest='/Python27/Lib/idlelib/destination' 

os.chdir(source)
for filename in os.listdir(os.getcwd()):
    head, tail = os.path.split(filename)
    chdate = os.path.getmtime(filename)
    source = head
    if (int(time.time()-chdate)/3600 < 24):
        shutil.copy2(head+tail, dest)

