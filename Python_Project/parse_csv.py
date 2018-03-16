import csv
# use context manager, to read the file say
with open('Data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
# passing the csv file through the reader method


    # next(csv_reader)
# this lets you skip the header column, step over it in an iterable, will loop over the first line,

    with open('new_data.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name' ] #email is commented out to select first and last name
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter = '\t')

        csv_writer.writeheader()
        # writes out headers as first line

        for line in csv_reader:
            del line['email']
            # so when it writes that row will only write first and last name


            # for each line in the origional file
            csv_writer.writerow(line)
            # we are writing out to the new file each line of the origional file

            # print(line[2])
    # the index tells you which peice of data you're grabbing- in this case all the emails
