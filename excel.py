import xlrd
book = xlrd.open_workbook(input("File name in quotes: "))
sh = book.sheet_by_index(0)
#print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
#for rx in range(sh.nrows):
    #print(sh.row(rx))

# Print all values, iterating through rows and columns
#
num_cols = sh.ncols   # Number of columns
for row_idx in range(1, sh.nrows):    # Iterate through rows
    print ('-'*40)
    #print ('Row: %s' % row_idx)   # Print row number
    date=sh.cell_value(row_idx, colx=0)
    y, m, d, h, i, s = xlrd.xldate_as_tuple(date, book.datemode)
    date = ("{0}/{1}/{2}".format(m, d, y))
    #for col_idx in range(0, num_cols):  # Iterate through columns
        #cell_obj = sh.cell(row_idx, col_idx)  # Get cell object by row, col

    fullname = ("{0}".format(sh.cell_value(row_idx, colx=1)))
    firstname= fullname.split()[0]
    print("Cell: {0}".format(sh.cell_value(row_idx, colx=5)))
    print("Home: {0}".format(sh.cell_value(row_idx, colx=6)))

        #print ('Column: [%s] text: [%s]' % (col_idx, cell_obj))
    print("Hello %s, my name is Olivia from the ITS Service Center at Syracuse University, letting you know that your NetID password will expire at the end of the day today, %s. Please change your password at netid.syr.edu before your account is locked tonight. If you have any questions, please call us at 315-443-2677. Thanks!" % (firstname, date))
