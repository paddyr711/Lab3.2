import sqlite3

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database

class DBOperations:
 sql_create_table_firsttime = "create table if not exists "


 sql_create_table = "CREATE TABLE flights (flightID INTEGER PRIMARY KEY, flightOrigin VARCHAR(15), flightDestination VARCHAR(15), status VARCHAR(15), departureTime DATETIME)"


 sql_insert = "INSERT INTO flights (flightID, flightOrigin, flightDestination, status, departureTime)  VALUES (?, ?, ?, ?, ?)"
 sql_select_all = "select * from flights"
 sql_search_flightID = "select * from flights where flightID = ?"
 sql_search_flightDestination = "select * from flights where flightDestination = ?"
 sql_search_status = "select * from flights where status = ?"
 sql_search_departureTime = "select * from flights where DATE(departureTime) = ?"
 sql_alter_data = ""
 sql_update_departureTime = "UPDATE flights SET departureTime = ? where flightID = ?"
 sql_update_status = "UPDATE flights SET status = ? where flightID = ?"
 sql_delete_data = "DELETE from flights where flightID = ?"
 sql_drop_table = "DROP TABLE flights"


 def __init__(self):
   try:
     self.conn = sqlite3.connect("DBFlights.db")
     self.cur = self.conn.cursor()
     self.cur.execute(self.sql_create_table_firsttime)
     self.conn.commit()
   except Exception as e:
     print(e)
   finally:
     self.conn.close()


 def get_connection(self):
   self.conn = sqlite3.connect("DBFlights.db")
   self.cur = self.conn.cursor()


 def create_table(self):
   try:
     self.get_connection()
     self.cur.execute(self.sql_create_table)
     self.conn.commit()
     print("Table created successfully")
   except Exception as e:
     print(e)
   finally:
     self.conn.close()


 def insert_data(self):
   try:
     self.get_connection()


     flight = FlightInfo()
     flight.set_flight_id(int(input("Enter FlightID: ")))
     flight.set_flight_origin(str(input("Enter FlightOrigin: ")))
     flight.set_flight_destination(str(input("Enter FlightDestination: ")))
     flight.set_status(str(input("Enter FlightStatus: ")))
     flight.set_departure_time(str(input("Enter FlightDepartureTime: ")))


     self.cur.execute(self.sql_insert, tuple(str(flight).split("\n")))


     self.conn.commit()
     print("Inserted data successfully")
   except sqlite3.IntegrityError as e:  # Catch the UNIQUE constraint error
    print("Error: FlightID already exists. Please use a different ID.")
   except Exception as e:
     print(e)
   finally:
     self.conn.close()


 def select_all(self):
   try:
     self.get_connection()
     self.cur.execute(self.sql_select_all)
     result = self.cur.fetchall()

     for row in result:
      print(row)  # Print each row


     # think how you could develop this method to show the records


   except Exception as e:
     print(e)
   finally:
     self.conn.close()


 def search_data(self):
  try:
    self.get_connection()
    while True:
     print("\n 1. Search by FlightId")
     print(" 2. Search by Flight Destination")
     print(" 3. Search by Flight Status")
     print(" 4. Search by Flight Departure Time")

     search_choice = int(input("Enter your choice: "))
     if search_choice == 1:
      flightID = int(input("Enter FlightNo: "))
      self.cur.execute(self.sql_search_flightID, tuple(str(flightID)))
     elif search_choice == 2:
      flightDestination = str(input("Enter Flight Destination: "))
      self.cur.execute(self.sql_search_flightDestination, (flightDestination,))
     elif search_choice == 3:
      flightStatus = str(input("Enter Flight Status: "))
      self.cur.execute(self.sql_search_status, (flightStatus,))
     elif search_choice == 4:
      flightDepartureDate = str(input("Enter Flight Departure Date (YYYY-MM-DD): "))
      self.cur.execute(self.sql_search_departureTime, (flightDepartureDate,))
     
     result = self.cur.fetchone()

     if type(result) == type(tuple()):
       for index, detail in enumerate(result):
         if index == 0:
           print("\nFlight ID: " + str(detail))
         elif index == 1:
           print("Flight Origin: " + detail)
         elif index == 2:
           print("Flight Destination: " + detail)
         elif index == 3:
           print("Status: " + detail)
         else:
           print("Flight Departure Time: " + str(detail))
     else:
       print("No Record")
     break

  except Exception as e:
    print(e)
  finally:
    self.conn.close()


 def update_data(self):
  try:
     self.get_connection()
     # Update statement

     while True:
      print("\n 1. Update Flight Departure Time")
      print(" 2. Update Flight Status")

      search_choice = int(input("Enter your choice: "))
      if search_choice == 1:
        flightID = int(input("Enter FlightNo: "))
        departureTime = input("Enter New Flight Departure Time: ")
        self.cur.execute(self.sql_update_departureTime, (departureTime,flightID))
        self.conn.commit()  # Commit changes
      elif search_choice == 2:
        flightID = int(input("Enter FlightNo: "))
        flightStatus = input("Enter New Flight Status: ")
        self.cur.execute(self.sql_update_status, (flightStatus,flightID))
        self.conn.commit()  # Commit changes
      result = self.cur
      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")
      break
  except Exception as e:
    print(e)
  finally:
      self.conn.close()




# Define Delete_data method to delete data from the table. The user will need to input the flight id to delete the corrosponding record.


 def delete_data(self):
   try:
     self.get_connection()
     flightID = int(input("Enter FlightNo: "))
     self.cur.execute(self.sql_delete_data, tuple(str(flightID)))
     self.conn.commit()
     
     result = self.cur
     if result.rowcount != 0:
       print(str(result.rowcount) + "Row(s) affected.")
     else:
       print("Cannot find this record in the database")


   except Exception as e:
     print(e)
   finally:
     self.conn.close()

 def drop_table(self):
   try:
     self.get_connection()
     self.cur.execute(self.sql_drop_table)
     print('Table dropped!')
   except Exception as e:
     print(e)
   finally:
     self.conn.close()


class FlightInfo:


 def __init__(self):
   self.flightID = 0
   self.flightOrigin = ''
   self.flightDestination = ''
   self.status = ''
   self.flightDepartureTime = ''


 def set_flight_id(self, flightID):
   self.flightID = flightID


 def set_flight_origin(self, flightOrigin):
   self.flightOrigin = flightOrigin


 def set_flight_destination(self, flightDestination):
   self.flightDestination = flightDestination


 def set_status(self, status):
   self.status = status

 def set_departure_time(self, flightDepartureTime):
   self.flightDepartureTime = flightDepartureTime

 def get_flight_id(self):
   return self.flightID


 def get_flight_origin(self):
   return self.flightOrigin


 def get_flight_destination(self):
   return self.flightDestination


 def get_status(self):
   return self.status

 def get_departure_time(self):
   return self.flightDepartureTime

 def __str__(self):
   return str(
     self.flightID
   ) + "\n" + self.flightOrigin + "\n" + self.flightDestination + "\n" + str(
     self.status + "\n" + self.flightDepartureTime)




# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.


while True:
 print("\n Menu:")
 print("**********")
 print(" 1. Create table FlightInfo")
 print(" 2. Insert data into FlightInfo")
 print(" 3. Select all data from FlightInfo")
 print(" 4. Search a flight")
 print(" 5. Update data some records")
 print(" 6. Delete data some records")
 print(" 7. Drop table")
 print(" 8. Exit\n")


 __choose_menu = int(input("Enter your choice: "))
 db_ops = DBOperations()
 if __choose_menu == 1:
   db_ops.create_table()
 elif __choose_menu == 2:
   db_ops.insert_data()
 elif __choose_menu == 3:
   db_ops.select_all()
 elif __choose_menu == 4:
   db_ops.search_data()
 elif __choose_menu == 5:
   db_ops.update_data()
 elif __choose_menu == 6:
   db_ops.delete_data()
 elif __choose_menu == 7:
   db_ops.drop_table() 
 elif __choose_menu == 8:
   exit(0)
 else:
   print("Invalid Choice")

