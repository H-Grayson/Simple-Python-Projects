
import sqlite3



#creates database called db_sub.db
con = sqlite3.connect('db_sub.db')

with con:
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tbl_txt(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
              col_fList TEXT)")
    con.commit

con = sqlite3.connect('db_sub.db')

# files used that are to be looped through
fileList = ('information,docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    
# loop through each object in the tuple to find names that end in y.
for x in fileList:
    if x.endswith('.txt'):
        with con:
            c = con.cursor()
        # The value for each row will be one name out of the tuple therefore (x,)
        # will denote a one element tuple for each file ending in .txt
            c.execute("INSERT INTO tbl_txt (col_fList) VALUES (?)", (x,))
            print(x)
