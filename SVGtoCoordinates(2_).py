file = open(r"Text_File_Location","r")
i = 0
k = 0
count = 0
index = 0
scale = 1.5
strx = ''
stry = ''
x = '0.0'
y = '0.0'
firstx = ''
firsty = ''
Coordinates = """[
"""
for line in file:
    line = line.replace("path(\"",'')
    line = line.replace("\");",'')
    while (k != len(line)):
        if ((line[k] == "m") or (line[k] == "M")):
            k = k + 2
            while (line[k] != ' '):
                firstx = firstx + line[k]
                k = k + 1
            k = k + 1
            while (line[k] != ' '):
                firsty = firsty + line[k]
                k = k + 1
            k = k + 1
            x = str(float(x) + float(firstx))
            y = str(float(y) + float(firsty))
            x = str(float(x)*scale)
            y = str(float(y)*scale)
            Coordinates = Coordinates + "{x: " + x + ",y: " + y + "},\n"
            x = str(float(x)/scale)
            y = str(float(y)/scale)
        elif (line[k] == 'l'):
            k = k + 2
            while (line[k] != ' '):
                strx = strx + line[k]
                k = k + 1
            k = k + 1
            while (line[k] != ' '):
                stry = stry + line[k]
                k = k + 1
            k = k + 1
            x = str(float(x) + float(strx))
            y = str(float(y) + float(stry))
            x = str(float(x)*scale)
            y = str(float(y)*scale)
            Coordinates = Coordinates + "{x: " + x + ",y: " + y + "},\n"
            x = str(float(x)/scale)
            y = str(float(y)/scale)
        elif (line[k] == 'L'):
            k = k + 2
            while (line[k] != ' '):
                strx = strx + line[k]
                k = k + 1
            k = k + 1
            while (line[k] != ' '):
                stry = stry + line[k]
                k = k + 1
            k = k + 1
            x = str(float(strx))
            y = str(float(stry))
            x = str(float(x)*scale)
            y = str(float(y)*scale)
            Coordinates = Coordinates + "{x: " + x + ",y: " + y + "},\n"
            x = str(float(x)/scale)
            y = str(float(y)/scale)
        elif (line[k] == 'h'):
            k = k + 2
            while (line[k] != ' '):
                strx = strx + line[k]
                k = k + 1
            k = k + 1
            x = str(float(x) + float(strx))
            y = str(float(y))
            x = str(float(x)*scale)
            y = str(float(y)*scale)
            Coordinates = Coordinates + "{x: " + x + ",y: " + y + "},\n"
            x = str(float(x)/scale)
            y = str(float(y)/scale)
        elif (line[k] == 'H'):
            k = k + 2
            while (line[k] != ' '):
                strx = strx + line[k]
                k = k + 1
            k = k + 1
            x = str(float(strx))
            y = str(float(y))
            x = str(float(x)*scale)
            y = str(float(y)*scale)
            Coordinates = Coordinates + "{x: " + x + ",y: " + y + "},\n"
            x = str(float(x)/scale)
            y = str(float(y)/scale)
        elif (line[k] == 'v'):
            k = k + 2
            while (line[k] != ' '):
                stry = stry + line[k]
                k = k + 1
            k = k + 1
            x = str(float(x))
            y = str(float(y) + float(stry))
            x = str(float(x)*scale)
            y = str(float(y)*scale)
            Coordinates = Coordinates + "{x: " + x + ",y: " + y + "},\n"
            x = str(float(x)/scale)
            y = str(float(y)/scale)
        elif (line[k] == 'V'):
            k = k + 2
            while (line[k] != ' '):
                strx = strx + line[k]
                k = k + 1
            k = k + 1
            y = str(float(strx))
            x = str(float(x))
            x = str(float(x)*scale)
            y = str(float(y)*scale)
            Coordinates = Coordinates + "{x: " + x + ",y: " + y + "},\n"
            x = str(float(x)/scale)
            y = str(float(y)/scale)
        elif ((line[k] == 'Z') or (line[k] == 'z')):
            k = k + 1
            y = str(float(firsty))
            x = str(float(firstx))
            x = str(float(x)*scale)
            y = str(float(y)*scale)
            Coordinates = Coordinates + "{x: " + x + ",y: " + y + "},\n"
            x = str(float(x)/scale)
            y = str(float(y)/scale)
            
        strx = ''
        stry = ''
    
file.close()
Coordinates = Coordinates + """]
"""
f = open(r"Text_File_Location","w")
f.write(Coordinates)
f.close() 
