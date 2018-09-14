import sqlite3

dbFile = raw_input("Enter file name:  ") + '.db'

conn = sqlite3.connect(dbFile)
dbQuer = conn.cursor()

class Student(object):
    def __init__(self, IdNo, FirstName, LastName, Course, YearLevel,Gender):
        self.idNum = IdNo
        self.firstName = FirstName
        self.lastName = LastName
        self.course = Course
        self.year = YearLevel
        self.gender = Gender


def createDB():
     dbQuer.execute('''CREATE TABLE IF NOT EXISTS records(IDno TEXT, fname TEXT, lname TEXT, course TEXT,year TEXT,gender TEXT)''')
     
def main():
    createDB()

    while(True):

        print "\n"
        print "     [1]  Add Student"
        print "     [2]  Delete Student"
        print "     [3]  Update Student"
        print "     [4]  Show database"
        print "     [5]  EXIT"

        feature_select = raw_input("\t\t\tSelect a number:   ")
        if feature_select == "1":
            idNo = raw_input("\t\tEnter your ID no: ")
            fName = raw_input("\t\tEnter your First Name: ")
            lName = raw_input("\t\tEnter your Last Name: ")
            gender = raw_input("\t\tEnter your Gender: ")
            course = raw_input("\t\tEnter your Course: ")
            year = raw_input("\t\tEnter your Year Level: ")
            student = Student(idNo, fName, lName,gender,course,year)
            addStud(student)
        elif feature_select == "2":
            deleteStud()
        elif feature_select == "3":
            updateStud()
        elif feature_select == "4":
            printStud()
        elif feature_select == "5":
            quit(1)
        else:
            print '\n\t\tERROR : INVALID. TRY AGAIN! '

def addStud(student):
    print "\n"
    dbQuer.execute('''INSERT into records(IDno, fname, lname, course,year,gender)VALUES(?,?,?,?,?,?)''',(student.idNum, student.firstName, student.lastName, student.course,student.year,student.gender))
    print '\n\t\tSUCCESSFULLY ADDED! '
    conn.commit()

def deleteStud():
    print "\n"
    delID = raw_input('Enter ID:  ')
    dbQuer.execute("DELETE from records WHERE IDno = ?",(delID,))
    print '\n\t\tSUCCESSFULLY DELETED!'
    conn.commit()

def updateStud():
    print "\n"
    updateID = raw_input('\tEnter ID:   ')
    print '\tWhat do you want to update? [Choose a number]'
    print "\n"
    print '\t\t[1]   First Name'
    print '\t\t[2]   Last Name'
    print '\t\t[3]   Gender'
    print '\t\t[4]   Course'
    print '\t\t[5]   Year Level'
    print "\n"
    updateSelect = raw_input('Number:   ')

    if updateSelect == "1":
        new_fName = raw_input("New First Name:   ")
        conn.execute("UPDATE records set fname = ? where IDno =?",(new_fName,updateID,))
        print '\n\t\t\tSUCCESSFULLY UPDATED!'
        conn.commit()
    elif updateSelect == "2":
        new_lName = raw_input("New Last Name:   ")
        conn.execute("UPDATE records set lname = ? where IDno = ?",(new_lName, updateID,))
        print '\n\t\t\tSUCCESSFULLY UPDATED!'
        conn.commit()
    elif updateSelect =="3":
        new_gender = raw_input("New Gender: ")
        conn.execute("UPDATE records set gender = ? where IDNo = ?", (new_gender,updateID))
        print '\n\t\t\tSUCCESSFULLY UPDATED!'
    elif updateSelect == "4":
        new_course = raw_input("New Course:   ")
        conn.execute("UPDATE records set course = ? where IDno = ?", (new_course,updateID,))
        print '\n\t\t\tSUCCESSFULLY UPDATED!'
        conn.commit()
    elif updateSelect == "5":
        new_year = raw_input("New Year Level: ")
        conn.execute("UPDATE records set year = ? where IDNo = ?", (new_year,updateID))
        print '\n\t\t\tSUCCESSFULLY UPDATED!'
    else:
         print '\n\t\tERROR : INVALID. TRY AGAIN! '

def printStud():
    dbQuer.execute('SELECT * FROM records')
    for row in dbQuer.fetchall():
        print "  ",row[0],"\t\t",row[1]," \t\t",row[2]," \t\t",row[3], " \t\t", row[4], " \t\t", row[5]





    dbQuer.close()
    conn.close()


if __name__ == '__main__':
    main()