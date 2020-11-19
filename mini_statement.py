import mysql.connector
connection = mysql.connector.connect(host="localhost", user="root", passwd="Gautam@4424", database="atm")
cur = connection.cursor()
def mini_statement():
    code = int(input("Enter your secret code"))
    cur.execute("SELECT * FROM Balance WHERE unique_code='{}'".format(code))
    validation = cur.fetchall()
    if validation!=[]:
        pin = int(input("Enter your 4 digit atm pin"))
        cur.execute("select atm_pin from balance where  unique_code='{}'".format(code))
        pin_validation = cur.fetchone()
        if pin_validation[0]==pin:
            cur.execute("Select * from mini where unique_code='{}'".format(code))
            mini_entries=cur.fetchall()
            print(mini_entries)
        else:
            print("Please enter valid pin")
    else:
        print("please enter valid code")
