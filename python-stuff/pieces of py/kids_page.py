def clear:
   print ("/n" * 200)

clear()
name = raw_input ("What's your name?")
print "Nice to meet you, ", name
color = raw_input ("What's your favorite color?")
print "Ok, I'll remember that in the future."
age = raw_input ("How old are you?")
print age, " I remember being that old..."
place = raw_input ("Where are you from?")
print "Oh, I've been to ", place, "I really liked it!"
sport = raw_input ("What's your favorite sport?")
print "Right on,", sport, " is really fun, I can see why you'd like it."
animal = raw_input ("What's your favorite animal?")
print "Excellent, and..."
pet = raw_input ("What's your favorite animal to keep as a pet?")
tbwgu = raw_input ("What are you going to be when you grow up?")
print "Follow that dream, you may or may not get to where you thought you were going, but you might, and you will have an interesting journey."
gend = raw_input ("Are you a girl or a boy?")
print "...And -"
grade = raw_input ("What grade are you in?")
subj = raw_input ("What's your favorite subject?")
print "Right on, I've always enjoyed learning about ", subj, " myself."
instr = raw_input ("What's your favorite instrument, for listening to OR playing?")
print "Music is super important to people and", instr, " helps develop your brain.  Good for you!"
season = raw_input ("What's your favorite season?")
print season,  "that's good.  I was really just hoping you wouldn't say 'Opera'"
file = open("%s.html" % (name), "w")
file.write("""
<!DOCTYPE html>
<head>""")
file.write('<link rel="stylesheet" type="text/css"')
file.write('href="%s.css"' %(name))
file.write("""
>
</head>
<main>
<header>
<h1>
""")

file.write("%s" %(name))
file.write("""
</h1>
</header>
<body>
<p>
""")
file.write("Hi, my name is  %s." %(name))
file.write("  I am a %s year old %s in grade %s." %(age, gend, grade))
file.write(" My favorite subject is %s, and I want to be a %s." %(subj, tbwgu))
file.write("  I am from %s and really like %s, and that's why %s is my favorite." %(place, sport, season))  
file.write("""
</p>
</body>
<footer>
<h3>headroaster made this</h3>
</footer>
</main>
""")
file.close

my_age=42
my_weight=215
my_height=70

print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

file = open("%s.css" % (name), "w")
file.write("""
body{
        background-image: url("http://upload.wikimedia.org/wikipedia/commons/f/f3/Hubble_Ultra_Deep_Field_part_d.jpg");
        background-color: #008f00;
        color: Yellow;
        font-family: Trebuchet MS;
        }
h1      {
        background-image: url("https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSUpMb2e7VSqfJuvvFcEk3wt-VX_jXOj1Xivxi5LQZsU1Se5MZWPQ");

        margin:  5px;
        padding: 20px;
        outline-width: 5px;
        outline-style: double;
        outline-color: Black;
        text-align: center;
        text-shadow: 9px 9px 10px Red, -9px -9px 10px Red,11px 11px 10px Orange, -11px -11px 10px Orange, 13px 13px 10px Yellow, -13px -13px 10px Yellow, 15px 15px 10px Green, -15px -15px 10px Green, 17px 17px 10px Blue, -17px -17px 10px Blue, 19px 19px 10px Indigo, -19px -19px 10px Indigo, 21px 21px 10px Violet, -21px -21px 10px Violet;
        }
div {
        color: Green;
        float: left;
        clear: left;

        text-align: center;
        border-radius: 100%;

        font-size: 14;
        color: Yellow;
        background-color: Blue;
        }
img {
        margin: 5px;
        float: right;
        width: 30%;
        height: 30%;
        box-shadow: 7px 7px 10px Black;
        }
#two{
        width: 43%;
        height: 43%;
        }
.primary
        {
        border-radius: 0;
        margin: 5px;
        background-color: Grey;
        float:left;
        width: 22%;
        height: 15%;
        }
.secondary 
        {
        margin: 3px;
        height: 13%;
        width: 23%;
        }
.tertiary
        {
        color: Orange;
        border-radius: 0;
        width: 100%;
        height: 17%;
        background-color: Transparent;
        }
#clicks
        {
        float: right;
        clear: right;
        width: 55%;
        height: 17%;
        background-color: Transparent;
        }

unused
        {

        -7px -7px 10px Black
        box-shadow: 7px 7px 10px Black;
        text-shadow: 7px 7px 10px Black, -7px -7px 10px Black;
        }
""")
file.close
