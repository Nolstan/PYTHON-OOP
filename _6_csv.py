# In this file will learn to read ,write and parse a csv file
import csv

# parsing a csv file
with open("names.csv",'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # print(csv_reader)  # this will print an object carrying csv info, so we neeed to loop

    with  open('new_name.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='\t')

        
        # next(csv_reader) # this will looop over the first line
        # for line in csv_reader:
            # print(line)

        # writing work
        for line in csv_reader:
            csv_writer.writerow(line)


# USING DICTIONARY READER AND WRITER
