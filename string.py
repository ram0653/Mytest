s='''hari maths 75
raju maths 70
hari science 71
raju science 72
hari social 91
raju social 76'''


subjects = 3
app = []
total = 0
l = s.splitlines()
for x in l:
	i=x.split()
	if "raju" in i:
		total = total+int(i[2])
print total
