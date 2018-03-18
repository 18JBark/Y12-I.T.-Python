import string
table = str.maketrans({key: None for key in string.punctuation})

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

frag1 = open('fragment1.txt')
frag1 = frag1.read()
frag1rs = str(frag1)
frag1s = frag1rs.translate(table)
frag1ss = "".join(frag1s.split())

frag2 = open('fragment2.txt')
frag2 = frag2.read()
frag2rs = str(frag1)
frag2s = frag1rs.translate(table)
frag2ss = "".join(frag2s.split())

frag3 = open('fragment3.txt')
frag3 = frag3.read()
frag3rs = str(frag3)
frag3s = frag1rs.translate(table)
frag3ss = "".join(frag3s.split())

frag4 = open('fragment4.txt')
frag4 = frag4.read()
frag4rs = str(frag4)
frag4s = frag1rs.translate(table)
frag4ss = "".join(frag4s.split())

frag5 = open('fragment5.txt')
frag5 = frag5.read()
frag5rs = str(frag5)
frag5s = frag1rs.translate(table)
frag5ss = "".join(frag5s.split())

frag6 = open('fragment6.txt')
frag6 = frag6.read()
frag6rs = str(frag1)
frag6s = frag1rs.translate(table)
frag6ss = "".join(frag6s.split())

suspect1 = open('suspect1.txt')
suspect1 = suspect1.read()
suspect1rs = str(suspect1)
suspect1s = suspect1rs.translate(table)
suspect1ss = "".join(suspect1s.split())

suspect2 = open('suspect2.txt')
suspect2 = suspect2.read()
suspect2rs = str(suspect2)
suspect2s = suspect2rs.translate(table)
suspect2ss = "".join(suspect2s.split())

suspect3 = open('suspect3.txt')
suspect3 = suspect3.read()
suspect3rs = str(suspect3)
suspect3s = suspect3rs.translate(table)
suspect3ss = "".join(suspect3s.split())

suspect4 = open('suspect4.txt')
suspect4 = suspect4.read()
suspect4rs = str(suspect4)
suspect4s = suspect4rs.translate(table)
suspect4ss = "".join(suspect4s.split())

suspect5 = open('suspect5.txt')
suspect5 = suspect5.read()
suspect5rs = str(suspect5)
suspect5s = suspect5rs.translate(table)
suspect5ss = "".join(suspect5s.split())

#\\\\\\\\\\\\\\\\\\\\\\\\1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

if frag1ss in suspect1ss:
    print ('Suspect 1 and Fragment 1 are a match')
else:
    print('Suspect 1 and Fragment 1 are not a match')

if frag2ss in suspect1ss:
    print ('Suspect 1 and Fragment 2 are a match')
else:
    print('Suspect 1 and Fragment 2 are not a match')

if frag3ss in suspect1ss:
    print ('Suspect 1 and Fragment 3 are a match')
else:
    print('Suspect 1 and Fragment 3 are not a match')

if frag4ss in suspect1ss:
    print ('Suspect 1 and Fragment 4 are a match')
else:
    print('Suspect 1 and Fragment 4 are not a match')

if frag5ss in suspect1ss:
    print ('Suspect 1 and Fragment 5 are a match')
else:
    print('Suspect 1 and Fragment 5 are not a match')

if frag6ss in suspect1ss:
    print ('Suspect 1 and Fragment 6 are a match')
else:
    print('Suspect 1 and Fragment 6 are not a match')

#\\\\\\\\\\\\\\\\\\\\\\\\\2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

if frag1ss in suspect2ss:
    print ('Suspect 2 and Fragment 1 are a match')
else:
    print('Suspect 2 and Fragment 1 are not a match')

if frag2ss in suspect2ss:
    print ('Suspect 2 and Fragment 2 are a match')
else:
    print('Suspect 2 and Fragment 2 are not a match')

if frag3ss in suspect2ss:
    print ('Suspect 2 and Fragment 3 are a match')
else:
    print('Suspect 2 and Fragment 3 are not a match')

if frag4ss in suspect2ss:
    print ('Suspect 2 and Fragment 4 are a match')
else:
    print('Suspect 2 and Fragment 4 are not a match')

if frag5ss in suspect2ss:
    print ('Suspect 2 and Fragment 5 are a match')
else:
    print('Suspect 2 and Fragment 5 are not a match')

if frag6ss in suspect2ss:
    print ('Suspect 2 and Fragment 6 are a match')
else:
    print('Suspect 2 and Fragment 6 are not a match')

#\\\\\\\\\\\\\\\\\\\\\\\\\3\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

if frag1ss in suspect3ss:
    print ('Suspect 3 and Fragment 1 are a match')
else:
    print('Suspect 3 and Fragment 1 are not a match')

if frag2ss in suspect3ss:
    print ('Suspect 3 and Fragment 2 are a match')
else:
    print('Suspect 3 and Fragment 2 are not a match')

if frag3ss in suspect3ss:
    print ('Suspect 3 and Fragment 3 are a match')
else:
    print('Suspect 3 and Fragment 3 are not a match')

if frag4ss in suspect3ss:
    print ('Suspect 3 and Fragment 4 are a match')
else:
    print('Suspect 3 and Fragment 4 are not a match')

if frag5ss in suspect3ss:
    print ('Suspect 3 and Fragment 5 are a match')
else:
    print('Suspect 3 and Fragment 5 are not a match')

if frag6ss in suspect3ss:
    print ('Suspect 3 and Fragment 6 are a match')
else:
    print('Suspect 3 and Fragment 6 are not a match')

#\\\\\\\\\\\\\\\\\\\\\\\\\4\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

if frag1ss in suspect4ss:
   print ('Suspect 4 and Fragment 1 are a match')
else:
    print('Suspect 4 and Fragment 1 are not a match')

if frag2ss in suspect4ss:
   print ('Suspect 4 and Fragment 2 are a match')
else:
    print('Suspect 4 and Fragment 2 are not a match')

if frag3ss in suspect4ss:
   print ('Suspect 4 and Fragment 3 are a match')
else:
    print('Suspect 4 and Fragment 3 are not a match')

if frag4ss in suspect4ss:
   print ('Suspect 4 and Fragment 4 are a match')
else:
    print('Suspect 4 and Fragment 4 are not a match')

if frag5ss in suspect4ss:
   print ('Suspect 4 and Fragment 5 are a match')
else:
    print('Suspect 4 and Fragment 5 are not a match')

if frag6ss in suspect4ss:
   print ('Suspect 4 and Fragment 6 are a match')
else:
    print('Suspect 4 and Fragment 6 are not a match')

#\\\\\\\\\\\\\\\\\\\\\\\\\5\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

if frag1ss in suspect5ss:
    print ('Suspect 5 and Fragment 1 are a match')
else:
    print('Suspect 5 and Fragment 1 are not a match')

if frag2ss in suspect5ss:
    print ('Suspect 5 and Fragment 2 are a match')
else:
    print('Suspect 5 and Fragment 2 are not a match')

if frag3ss in suspect5ss:
    print ('Suspect 5 and Fragment 3 are a match')
else:
    print('Suspect 5 and Fragment 3 are not a match')

if frag4ss in suspect5ss:
    print ('Suspect 5 and Fragment 4 are a match')
else:
    print('Suspect 5 and Fragment 4 are not a match')

if frag5ss in suspect5ss:
    print ('Suspect 5 and Fragment 5 are a match')
else:
    print('Suspect 5 and Fragment 5 are not a match')

if frag6ss in suspect5ss:
    print ('Suspect 5 and Fragment 6 are a match')
else:
    print('Suspect 5 and Fragment 6 are not a match')
