import mysql.connector
try:
                conn = mysql.connector.connect(host="localhost",username="root",password="password",database="mydb",port="3307")
                my_cursor = conn.cursor()
             
                conn.commit()
                my_cursor.close()
                conn.close()
                print("Connection Sucessful")
      
                


except mysql.connector.Error as error:
                    print("Error:", error)

def Reception():      
       Que = input("Enter que number ")
       Previous_counter =input("Enter previous counter ")
       Current_counter = input("Enter current_counter ")
       Transaction_Type = input("Enter transaction type: ")
       conn = mysql.connector.connect(host="localhost",username="root",password="password",database="mydb",port="3307")

       my_cursor = conn.cursor()
       query = ("INSERT INTO DummyClient (que,previous_counter,current_counter,transaction_type)  VALUES ( %s, %s, %s,%s)")
       data = (Que,Previous_counter,Current_counter,Transaction_Type)
       my_cursor.execute(query,data)             
       conn.commit()
       my_cursor.close()
       print("Data submitted successfully")
       conn.close()


def CounterFunction():
       Previous_counter =input("Enter previous counter: ")
       Current_counter = input("Enter current_counter: ")
       que_number = input("Enter que Number: ")

       conn = mysql.connector.connect(host="localhost",username="root",password="password",database="mydb",port="3307")

       my_cursor = conn.cursor()
       select_query = "SELECT que, Transaction_Type FROM DummyCLient where que = %s"
       my_cursor.execute(select_query,(que_number,))
       existing_data = my_cursor.fetchone()

       if existing_data:
            que, transaction_type = existing_data
            query = "INSERT INTO DummyClient (que, previous_counter, current_counter, transaction_type) VALUES (%s, %s, %s, %s)"
            data = (que, Previous_counter, Current_counter, transaction_type)
            my_cursor.fetchall()
            my_cursor.execute(query, data)
            conn.commit()
            my_cursor.close()
            print("Data submitted successfully")


            conn.close()
       else:
            print("Data Not Submitted")




def Call():
    que = input("Enter que Number: ")
    conn = mysql.connector.connect(host="localhost", username="root", password="password", database="mydb", port="3307")
    my_cursor = conn.cursor()

    select_query = "SELECT que, Transaction_Type, Previous_counter, Current_counter FROM DummyCLient where que = %s"
    my_cursor.execute(select_query,(que,))
    existing_data = my_cursor.fetchone()

    
    if existing_data:
            que, transaction_type, Previous_counter, Current_counter = existing_data
            query = "INSERT INTO DummyClient (que, previous_counter, current_counter, transaction_type) VALUES (%s, %s, %s, %s)"
            data = (que, Previous_counter, Current_counter, transaction_type)
            update_query = "UPDATE DummyClient SET status = %s WHERE que = %s"
            data = ("in process", que)
            my_cursor.fetchall()
            my_cursor.execute(query, data)
            my_cursor.execute(update_query, data)
            conn.commit()
            my_cursor.close()
            print("Data submitted successfully")


            conn.close()
       
    else:
            print("Data Not Submitted")
 



  
Call()