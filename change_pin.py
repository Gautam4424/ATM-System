import mysql.connector
connection = mysql.connector.connect(host="localhost", user="root", passwd="Gautam@4424", database="atm")
cur = connection.cursor()
def change_pin():
    code = int(input("Enter your secret code"))
    cur.execute("SELECT * FROM Balance WHERE unique_code='{}'".format(code))
    validation = cur.fetchall()
    if validation!=[]:
        pin = int(input("Enter your 4 digit atm pin"))
        cur.execute("select atm_pin from balance where  unique_code='{}'".format(code))
        pin_validation = cur.fetchone()
        if pin_validation[0] == pin:
            try:
                new_pin=int(input("Enter the 4 digit new pin"))
                if len(str(new_pin))>4:
                    print("Please enter new pin of 4 digits")
                    change_pin()
                else:
                    confirmation=int(input("Press 1 for confirm your pin"))
                    if confirmation==1:
                        cur.execute("update balance set atm_pin='{}'where unique_code='{}'".format(new_pin,code))
                        print("Pin change successfully")
                        connection.commit()
                    else:
                        change_pin()
            except Exception as e:
                print("Some problem id arrise please try again later")
        else:
            print("Please enter valid pin")
    else:
        print("please enter the valid code")

