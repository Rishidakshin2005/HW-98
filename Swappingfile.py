def swapFileData():
    file2 = "C:\Users\Dell\Desktop\Module3\Swapping\\Myfile2.txt"
    file1 = "C::\Users\Dell\Desktop\Module3\Swapping\\Myfile.txt"

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as a:
        a.write(data_a)

    print("Successfully Swaped!")

swapFileData()