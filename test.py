

with open("quotes.txt", encoding="utf8") as q:
	lines = q.readlines()

qs = []

for line in lines:
	# line.replace('\n', '')
	q = line.split("|")
	qs.append({'author':q[0], 'quote':q[1]})

# print(qs)
# print(len(lines))