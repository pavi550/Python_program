with open('file1.txt','r') as file1:
        print('file opened')
        print('The cursor is at',file1.tell())
        data = file1.read(20)
        print("The data is: ",data)
        print('The cursor is at', file1.tell())
        file1.seek(5)
        print('The cursor is at', file1.tell())
        data = file1.read(20)
        print("The data is: ", data)
        print('The cursor is at', file1.tell())
        file1.seek(75)
        print('The cursor is at', file1.tell())
        data = file1.read(50)
        print("The data is: ", data)
        print('The cursor is at', file1.tell())
        print('write operation completes')
print('Code completed...')
