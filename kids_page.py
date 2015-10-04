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

file = open ("name.html", "w")

file.write("""
<!DOCTYPE html>
<main>
<header>
<h1>Name</h1>
</header>
<body>
<p>Hi, I'm name.  I'm a age year old gend in grade.  My favorite subject is subj, and I'm going to be a tbwgu.
	I'm from place, and really like sport.  season is my favorite season.</p>
</body>
<footer>
<h3>headroaster made this</h3>
</footer>
</main>
""")
file.close

