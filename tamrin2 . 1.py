name = (input("nam khod ra vard kon:"))

family = (input("name khanevadegi khod ra vard kon:"))

r = int(input("nomre dars ryazi khod ra vard kon:"))

f = int(input("nomre dars farsy khod ra vard kon:"))

o = int(input("nomre dars olom khod ra vard kon:"))

average = (r + f + o) / 3

if average >= 17:
    result = "great"

if 17 > average >= 12:
    result = "normal"

if average < 12:
    result = "fail"

print("asm shoma:",name,"famil shoma:",family,"vaz tahsili shoma",result)