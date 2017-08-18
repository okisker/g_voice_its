import xlrd
book = xlrd.open_workbook(raw_input("File name: ")) #test.xls
myname = raw_input('Your name: ')

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
    #print("Date: ", date)
    #for col_idx in range(0, num_cols):  # Iterate through columns
        #cell_obj = sh.cell(row_idx, col_idx)  # Get cell object by row, col

    fullname = ("{0}".format(sh.cell_value(row_idx, colx=1)))
    print("Full name: ", fullname)
    firstname= fullname.split()[0]
    #print("First name: ", firstname)
    cell=(("{0}".format(sh.cell_value(row_idx, colx=5))))
    cell=cell.replace("-","")
    cell=cell.replace("/","")
    cell=cell.replace(".0","")
    #print("Cell: ", cell)
    home=("{0}".format(sh.cell_value(row_idx, colx=6)))
    home=home.replace("-","")
    home=home.replace("/","")
    home=home.replace(".0","")

        #print ('Column: [%s] text: [%s]' % (col_idx, cell_obj))
    messagetext=("Hello %s, my name is %s from the ITS Service Center at Syracuse University, letting you know that your NetID password will expire at the end of the day today, %s. Please change your password at netid.syr.edu before your account is locked tonight. If you have any questions, please call us at 315-443-2677. Thanks!" % (firstname, myname, date))
    #print(messagetext)
    #import subprocess
    #subprocess.call('./g_voice.py', shell=True)
    try:
        from googlevoice import Voice
        from googlevoice.util import input
        voice = Voice()
        voice.login()
        phoneNumber = cell
        text = 'testingtesting123'

        voice.send_sms(phoneNumber, text)
    except:
        print("You have sent too many texts!")

