f1= open('/Users/sadki/Desktop/DSA_Program/Python_Basic/File_handling/MyData','r')

for data in f1:
    print(data,end="")

#Read one line at a time
print("Read one line at a time-----------")
f3= open('/Users/sadki/Desktop/DSA_Program/Python_Basic/File_handling/MyData','r')
print(f3.readline(),end="")

#Read complete file at a time
print("Read complete file at a time----------")
f3= open('/Users/sadki/Desktop/DSA_Program/Python_Basic/File_handling/MyData','r')
print(f3.read(),end="")

# copy data from one fiel to another
    
f2 = open('/Users/sadki/Desktop/DSA_Program/Python_Basic/File_handling/Copied_data','w')
f1= open('/Users/sadki/Desktop/DSA_Program/Python_Basic/File_handling/MyData','r')
for data in f1:
    f2.write(data)


#appenf in existing file
    
f2 = open('/Users/sadki/Desktop/DSA_Program/Python_Basic/File_handling/Copied_data','a')
f2.write("\nAppended data")