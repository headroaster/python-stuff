name = raw_input ("What's your name?")
print "Nice to meet you, ", name
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
print "Oh you're going to learn to code and make a huge stack of money, then retire early and never actually grow up?  Perfect!!"
gend = raw_input ("Are you a girl or a boy?")
grade = raw_input ("What grade are you in?")
subj = raw_input ("What's your favorite color?")
print "...Oh...You know what they say about- never mind..."
instr = raw_input ("What's your favorite instrument, for listening to OR playing?")
print "Music is super important to people and", instr, " helps develop your brain.  Good for you!"
season = raw_input ("What's your favorite season?")
print season,  "that's good.  I was really just hoping you wouldn't say 'Opera'"
file = open("%s.html" % (name), "w")
file.write("""
<!DOCTYPE html>
<main>
<header>
<h1>Name</h1>
</header>
<body>
<p>
""")
#file.write("Hi, Im {0}.  Im a {1} year old {2} in grade {3}.  My favorite subject is {4}, and Im going to be a {5}.  Im from {6}, and really like {7}.  Thats why {8} is my favorite.") .format ( name, age, gend, grade, subj, tbwgu, place, sport, season) 
file.write("Hi, Im %s.  Im a %s year old %s in grade %s.  My favorite subject is %s, and Im going to be a %s.  Im from %s and really like %s.  That's why %s is my favorite." %(name, age, gend, grade, subj, tbwgu, place, sport, season))  
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
