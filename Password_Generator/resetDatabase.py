import sqlite3
def Restart_Table():
    #try:
        Connection = sqlite3.connect(r'C:\Users\HP\VSCODE\ANNUAL-CSC-PROJECT\Django_Annual\db.sqlite3')
        cursor = Connection.cursor()
        print("Successfully Connected to SQLite database")
        _query1 = 'DROP TABLE Password_Generator_Registration'
        cursor.execute(_query1)
        print('Table Dropped')
        _query2 = '''
        CREATE TABLE "new__DPA_registration" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "CSV_file" varchar(100) NOT NULL, "Name" varchar(300) NOT NULL, "Email" varchar(300) NOT NULL, "Contact_Number" integer NOT NULL, "Level" varchar(300) NOT NULL, "Subject" varchar(300) NOT NULL);
        INSERT INTO "new__DPA_registration" ("id", "Name", "Email", "Contact_Number", "Level", "Subject", "CSV_file") SELECT "id", "Name", "Email", "Contact_Number", "Level", "Subject", NULL FROM "DPA_registration";
        DROP TABLE "DPA_registration";
        ALTER TABLE "new__DPA_registration" RENAME TO "DPA_registration";
        COMMIT;'''
        cursor.execute(_query2)
        print('Table has been created again.')
        Query = 'SELECT * FROM Password_Generator_Registration'
        cursor.execute(Query)
        record = cursor.fetchall()
        cursor.close()
        print(record)
    #except sqlite3.Error as error:
        print("Error while connecting to sqlite: ", error, sep = "\n")
    #finally:
        if Connection.is_connected():
            Connection.close()
            print("The SQLite connection is closed")
if __name__ == "__main__":
    Restart_Table()