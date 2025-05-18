myfile = open('sample.txt')
while (myfile.closed == False):
    print(myfile.read())
    if (myfile.seekable()):
        myfile.close()
