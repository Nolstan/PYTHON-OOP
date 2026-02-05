# A file are named locations to store information on disk
# A file is a collection of data stored on disk


# types of files
# 1. text file - Are files that contain human readable text
# examples: txt, csv,json
# stores data in ASCII format and Unicode



# 2. binary file - Are files that contain binary data
# examples: image, audio, video


# four main file operations
# 1. open
# 2. read
# 3. write
# 4. close


# OPENING A FILE
# file_object = open(file_name, mode)
# where file_object is just a pointer to the file
# mode is a string that specifies how the file will be opened

# MODES
# r - read - default, open file for reading
# if the file doesnt exist it will raise an error

# w - write - open file for writing
# if the file doesnt exist it will create it

# x - create - create a new file and open it for writing

# a - append - open file for appending
# if the file doesnt exist it will create it
# new data will be added at the end of the file

# r+ - read and write - open file for reading and writing
# if file doesnt exist it will shoot an eror

# w+ - write and read - open file for writing and reading
# if file doesnt exist it will create it

# a+ - append and read - open file for appending and reading


# 1 read    
f = open("test.txt","r")
# print(f.read())
f.close()


# 2 write
f1 = open("test2.txt","w")
# if f1:
    # f1.write("Hello Nolstan")
    # print("File written successfully")
# else:
    # print("Failed  to write file")
# f1.close


# r+ mode
f2  = open('test2.txt','r+')
# if f2:
#     print('This is the current informaton in the file')
#     print(f2.read())
#     print('will overwrite this information\t')
#     f2.write('This is the new information i was talking about bouy')
# else:
#     print('Failed to open file')
# f2.close()

# w+ mode
# f3 = open('test3.txt','w+')
# f3.write('This is from w+ mode,in this mode you write first then read')
# f3.seek(0) # to move the cursor to the start
# print(f3.read())
# f3.close()


# The difference between r+ and w+ is that
# in r+ you have to read first then write 
# this is because the cursor is at the end of the file

#in w+ you have to write first then read
# this is because the cursor is at the start of the file


# NOTICE THE seek() and tell() functions
# seek() is used to move the cursor to a specific position in the file
# tell() is used to get the current position of the cursor



# a mode
f4 = open('test2.txt','a+')
f4.write('Orewa! monkey D. Luffy .Kaizo ku O ni orewa naru!')


# a+ mode
f5 = open('test2.txt','a+')
f5.write('Orewa! monkey D. Luffy .Kaizo ku O ni orewa naru!')
f5.seek(0)
print(f5.read())
f5.close()


# Binary file modes
# rb - read binary
# wb - write binary
# ab - append binary
# rb+ - read and write binary
# wb+ - write and read binary
# ab+ - append and read binary

# they work the same as the text file modes
