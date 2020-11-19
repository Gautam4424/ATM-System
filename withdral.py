import mysql.connector
import datetime
connection = mysql.connector.connect(host="localhost", user="root", passwd="Gautam@4424", database="atm")
cur = connection.cursor()

date_time=datetime.datetime.now()
def withdrawl():
    code = int(input("Enter your secret code"))
    cur.execute("SELECT * FROM Balance WHERE unique_code='{}'".format(code))
    validation = cur.fetchall()
    if validation!=[]:
        amount = float(input("Enter the amount you waant to withdrawl"))
        pin = int(input("Enter your 4 digit atm pin"))
        cur.execute("select atm_pin from balance where  unique_code='{}'".format(code))
        pin_validation = cur.fetchone()
        if pin_validation[0]==pin:
            try:
                cur.execute("select balance from balance where unique_code='{}'".format(code))
                bal=cur.fetchone()
                if bal[0]>amount:
                    print("successfully withdrawl")
                    cur.execute("update balance set balance=balance-'{}' where unique_code='{}'".format(amount, code))
                    connection.commit()
                    cur.execute("Insert into mini (ammount_withdrawl,date_time,unique_code) values('{}','{}','{}')".format(amount,date_time,code))
                    connection.commit()
                elif bal[0]==amount:
                    confirmation=int(input("Press 1 to withdrawl full amount"))
                    if confirmation==1:
                        cur.execute("update balance set balance=balance-'{}' where unique_code='{}'".format(amount, code))
                        print("successfully withdrawl")
                        cur.execute("Insert into mini (ammount_withdrawl,date_time,unique_code) values('{}','{}','{}')".format(amount,date_time,code))
                        connection.commit()
                    else:
                        print("Thank you for using this Atm")
                else:
                    print("Insufficient balance!!")

            except Exception as e:
                print(e)
                print("There is some problem please try again later!!!")
        else:
            print("Please Enter valid Pin")
    else:
        print("please enter valid code")

