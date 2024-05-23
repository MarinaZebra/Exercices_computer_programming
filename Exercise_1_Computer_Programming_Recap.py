from pyqgis_scripting_ext.core import*

#folder = r""C:\Users\00mar\Desktop\Master_Bolz\Semester_2\Advance_geomatics\Marina_Perez_Entrega_1

# path = f"{folder}01_exe_rain_data_1year.txt"

# wit open (path, 'r') as file:
#     lines = file.readlines()
    
# for line in lines:
#     print(line)


#Exercice 1
age=25
name="Mario Rossi"
activity="skating"
job="engineer"
print(f"Hei, I am {name}\n I am {age} years old and I love to go {activity}\nI work as an {job}")

#Exercice 2
csvPath= "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\01_exe2_data.csv"
print(csvPath)
with open(csvPath,"r") as file:
    lines=file.readlines()
for line in lines:
    line = line.strip()
    lineSplit = line.split(";")
    print(lineSplit)
    
    analogString = lineSplit[0]
    analogSplit=analogString.split(":")
    print(analogSplit)
    x1=float(analogSplit[1])
    print(x1)
    
    maxvoltageString = lineSplit[1]
    y2=float(maxvoltageString[11:])
    
    maxanalogString = lineSplit[2]
    x2= float(maxanalogString.split(":")[1])
    
    #x2/x1=y2/y1
    y1=y2*x1/x2
    
    print(x1, x2, y1, y2)
   

#Exercice 3
string1=" a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s"
string2 = string1.replace(",",";")
print(string2)
[' a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s']

#Exercice 4
list = [ 1, 2, 3, 4, 5]
for items in list:
    print (f" {items}")

#Exercice 5
for items in list:
    print (f" Number {items}")
    
#Exercice 6
list2 = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
list3 = list2[:5]
print(list3)
for items in list3:
    print (f" Number {items}")
    
#Exercice 7
list4 = [1, 2, 3, 4, 5]
list5 = ["first","second","third","fourth","fifth"]
for number, names in zip(list4,list5):
    print(f"{number} is {names}")
    
#Exercice 8
#Characters count
string_exercice8 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum."""
lenght_string_exercice8= len(string_exercice8)
print(lenght_string_exercice8)
string_exercice8_without_space=string_exercice8
#Character count wihout a space 
def remove(string_exercice8_without_space):
    return string_exercice8_without_space.replace(" ", "")
print(remove(string_exercice8_without_space))
lenght_string_exercice8_without_space=remove(string_exercice8_without_space)
len(lenght_string_exercice8_without_space)
#Words count 
words = len(string_exercice8.split())
print("Number of words:", words)

#Exercice 9 
csvPath2= "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\01_exe9_data.csv"

with open(csvPath2, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:  
        continue
    lineSplit = line.split(",")  
    stationId = lineSplit[0]
    print(lineSplit)

#Eercice 10
csvPath2 = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\01_exe9_data.csv"

with open(csvPath2, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    # Skip lines that start with "#" or are empty
    if line.startswith("#") or len(line) == 0:
        continue
    lineSplit = line.split(",")
    # Ensure there are at least two elements to process
    if len(lineSplit) >= 2:
        # Attempt to convert the second element to a float
        try:
            value = float(lineSplit[1].strip())
            # Skip this line if the value is greater than 1000
            if value > 1000:
                continue
        except ValueError:
            # If conversion fails, skip the rest of the loop and move to the next line
            # This is useful if the data is not a number, to avoid crashing the program
            continue
        # Print the station ID and the value, correctly formatted
        print(f"{lineSplit[0]}, {lineSplit[1].strip()}")

#Exercice 11
csvPath3="C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\01_exe11_data.csv"
with open(csvPath3, "r") as file:
    lines = file.readlines()
for line in lines:
    line.strip()
    x=line.replace("=",";")
    
    b=x.split(";")[0]
    b_len=x.split(";")[1]
    b_len=float(b_len[:-2])
    
    h=x.split(";")[2]
    h_len=float(x.split(";")[3])
    
    print(f"{b}*{h}/2={b_len}*{h_len}={b_len*h_len/2}cm2")

# Exercice 12 

who = {
     "Daisy": 11,
     "Joe":201,
     "Will": 23,
     "Hanna": 44,
}
what = {
     44: "runs",
     11: "dreams",
     201: "plays",
     23: "walks",
}
where = {
     44: "to town",
     11: "in her bed",
     201: "in the living room",
     23: " up in the mountains",
}

sentences = []
for person, verb in who.items():
    action = what[verb]
    location = where[verb]
    sentence = f"{person} {action} {location}."
    sentences.append(sentence)
    print(sentence)
    
# Exercice 13

list1 = ["a","b","c","d","e","f"]
list2 = ["c","d","e","f","g","h","a"]
list3 = ["c","d","e","f","g"]
list4 = ["c","d","e","h","a"]

All_list = list1 + list2 + list3 + list4
print(All_list)

A, B, C, D, E, F, G, H = [], [], [], [], [], [], [], []

for item in All_list:
    if item == "a":
        A.append(item)
    elif item == "b":
        B.append(item)
    elif item == "c":
        C.append(item)
    elif item == "d":
        D.append(item)
    elif item == "e":
        E.append(item)
    elif item == "f":
        F.append(item)
    elif item == "g":
        G.append(item)
    elif item == "h":
        H.append(item)

print(len(A))
print(len(B))
print(len(C))
print(len(D))
print(len(E))
print(len(F))
print(len(G))
print(len(H))

#Exercice 14 
txtPath = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"
with open(txtPath, 'r') as file:
    for i, line in enumerate(file, 1):
        print(line, end='')
        if i == 20:
            break

#Exercice 15 

txtPath="C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"
line_count = 0
with open(txtPath, 'r') as file:
    for line in file:
        line_count += 1
# Print the total number of lines
print(f"The file has {line_count} stations.")

#Exercice 16
txtPath16 = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"
with open(txtPath16, 'r') as file:
    for line in file:
        if line.strip():  
            columns_count = len(line.split(','))
            print(f'The file has {columns_count} columns.')
            break  

# Exercice 17
txtPath = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"

with open(txtPath, 'r') as file:
    for i, line in enumerate(file, 1):
        columns = line.strip().split(',')
        if len(columns) >= 3:
            print(f"{columns[0]}, {columns[1]}")
        else:
            print("Not enough columns in line", i)
        if i == 20: 
            break

# Exercice 18 
file_path = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"
with open(file_path,"r")as file:
    lines = file.readlines()[1:]
sum=0
count=0
for line in lines:
    hght=float(line.strip().split(",")[5])
    sum=sum+hght
    count+=1
print(sum/count)
# Exercice 19 
txtpath= 'C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt'
with open(txtpath,"r")as file:
    lines = file.readlines()[1:]
sum=0
count=0
for line in lines:
    hght=float(line.strip().split(",")[5])
    sum+=hght
    count+=1
avg=round(sum/count,1)

print(f"Stations count:{count}\naverage value: {avg}\nAvailable fields:")
with open(txtpath,"r")as file:
    line=file.readline()
    line=line.replace(" ","").replace("#","").strip().split(",")
    for item in line:
        print(f"    ->{item}")

# Exercice 20
txtpath= 'C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\station_data.txt'

with open(txtpath,"r")as file:
    lines = file.readlines()[1:]
sum=0
count=0

for line in lines:
    if "-9999" in line:
        continue
    else:
        hght=float(line.strip().split(",")[3])
        sum+=hght
        count+=1
avg=round(sum/count,1)

print(f"Stations count:{count}\naverage value: {avg}\nAvailable fields:")
with open(txtpath,"r")as file:
    line=file.readline()
    line=line.replace(" ","").replace("#","").strip().split(",")
    for item in line:
        print(f"    ->{item}")

print("First data lines:")

with open(txtpath,"r")as file:
    lines = file.readlines()[:5]
for line in lines:
    print(f"{line}")


# Exercice 21 
n= 10
m= 5
print(('*'*5 + '\n') * n) 

# Exercice 22
List = []
while len(List) < 10:
    List.append('*')
    print(List)
    
# Exercice 23
List2 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*','*']
while len(List2) > 1:
    List2.remove('*')
    print(List2)

# Exercice 24
a = 10
Empty_list = []
Final_list= []
Other_list=[]
counter = 0
while len(Empty_list) < a:
    Empty_list.append(counter)
    
    if counter % 2 == 0:
        Final_list.append(counter)
    else:
        Other_list.append(counter)
    
    counter += 1

print("Even numbers:", Final_list)
print("Odd numbers:", Other_list)

# Exercice 25 
numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]
New_list = []
counter2 = 0
for number in numbers:
    if counter2 % 2 == 0:
        New_list.append(counter2)
    counter2 += 1 

print(New_list)



