import hashlib,json,sys,genanki
M=genanki.Model(1607392319,"Basic",fields=[{"name":"Front"},{"name":"Back"}],
 templates=[{"name":"Card 1","qfmt":"{{Front}}","afmt":"{{FrontSide}}<hr id=answer>{{Back}}"}],
 css=".card{font-family:arial;font-size:20px;text-align:center;color:black;background-color:white}")
c,n,o=sys.argv[1:4]
d=genanki.Deck(int(hashlib.sha1(n.encode()).hexdigest()[:8],16),n)
for x in {x["front"]:x for x in json.load(open(c))}.values():
    d.add_note(genanki.Note(model=M,fields=[x["front"],x["back"]],guid=genanki.guid_for(n,x["front"])))
genanki.Package(d).write_to_file(o)
print(len(d.notes))
