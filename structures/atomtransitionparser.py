

#file = open(filename)
#output = open('output.txt', 'w')
#print "Here's your file %r:" % filename

with open("Hello.txt","r") as infile, open("Output.txt","w") as outfile:
    d={}
    for line in infile:
        x = line.split(":")
        y = line.split(" ")
        a = x[0] #splits the string in half
        b = x[1] #the other half
        c = y[3]
        #c = y[0]
        #c = b.split("(")
        d[a] = b
        




        print (d)








#nested python dict
    #d[][] = 'value'


        #outfile.write("{")
        #outfile.write('"')
        #outfile.write(line)
        #if '"' in line:
            #print("Hello")
