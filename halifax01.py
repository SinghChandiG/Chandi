t=0  
with open('Bus_Stops.csv', 'r') as myfile
for line in myfile:
        words = line.split()
        for i in words:
            if(i==Terminal):
                t=t+1
print("total of bus terminal:")
print(t)

