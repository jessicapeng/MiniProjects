
"""
Append input (which is 6) to the beginning
of every choice and output it into a txt file
"""

append = '6'
file = open('input_photos.txt', 'r')
output = open('photo_choices.txt', 'w')

lines=file.readlines()

for line in lines:
   print(line)
   output.write(append+line+'')
   
output.close()