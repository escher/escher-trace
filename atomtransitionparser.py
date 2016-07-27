
json = ""
#file = open(filename)
#output = open('output.txt', 'w')
#print "Here's your file %r:" % filename

with open("Hello.txt","r") as infile, open("Output.txt","w") as outfile:
    for line in infile:
        outfile.write("{")
        outfile.write('"')
        for ch in line:
            if ch == ":":
                line.replace(":",'": {')
            if ch == "(":
            	outfile.write("{")
            	outfile.write('"')
            if ch == "->"
            	outfile.write("")
            if ch == "<->"
            	outfile.write("1")
            if ch == "->"
            	outfile.write("-1")
        outfile.write(ch)


        #outfile.write("{")
        #outfile.write('"')
        #outfile.write(line)
        #if '"' in line:
            #print("Hello")
