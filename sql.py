import sqlite3
## connect to sqlite3
connection=sqlite3.connect("student.db")

## create a curors object to inset record,create table,retrieve
coursor=connection.cursor()
##create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

"""
coursor.execute(table_info)

## Insert some more info
coursor.execute('''Insert Into Student values('Lupin','Data Science','A',90)''')
coursor.execute('''Insert Into Student values('SAMMY','DEPLOMA','b',100)''')
coursor.execute('''Insert Into Student values('RAKTIM','AI','A',50)''')
coursor.execute('''Insert Into Student values('KOBRA','Data Science','A',34)''')
##dISPLAY ALL THE RECORD
print("The inserted records are")

data=coursor.execute('''Select * From STUDENT ''')

for row in data:
    print(row)
##close the connection
connection.commit()
connection.close   