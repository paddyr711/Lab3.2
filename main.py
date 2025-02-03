import sqlite3

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database

class DBOperations:
 
 sql_create_table_firsttime = """
 CREATE TABLE IF NOT EXISTS flights (
 flightID INTEGER PRIMARY KEY, 
 originID INTEGER, 
 destinationID INTEGER, 
 status VARCHAR(15), 
 departureTime DATETIME, 
 pilotID INTEGER 
 )
 """
 sql_create_pilot_table_firsttime = """
 CREATE TABLE IF NOT EXISTS pilots (
 pilotID INTEGER PRIMARY KEY, 
 Name VARCHAR(30), 
 Carrier VARCHAR(30)
 )
 """
 sql_create_destination_table_firsttime = """
 CREATE TABLE IF NOT EXISTS destinations (
 destinationID INTEGER PRIMARY KEY, 
 flightDestination VARCHAR(30)
 )
 """

# sql_create_table = "CREATE TABLE flights (flightID INTEGER PRIMARY KEY, flightOrigin VARCHAR(15), flightDestination VARCHAR(15), status VARCHAR(15), departureTime DATETIME)"

 sql_insert_first_time = "INSERT INTO flights (flightID, originID, destinationID, status, departureTime, pilotID)  VALUES (?, ?, ?, ?, ?, ?)"
 sql_insert_pilot_first_time = "INSERT INTO pilots (pilotID, Name, Carrier)  VALUES (?, ?, ?)"
 sql_insert_destination_first_time = "INSERT INTO destinations (destinationID, flightDestination)  VALUES (?, ?)"

 sql_insert = "INSERT INTO flights (flightID, flightOrigin, flightDestination, status, departureTime)  VALUES (?, ?, ?, ?, ?)"
 
 sql_select_all = """
 select * 
 from flights AS f 
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID 
 INNER JOIN destinations AS d ON f.destinationID = d.destinationID
 """
 sql_search_flightID = """
 select * 
 from flights as f 
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID 
 INNER JOIN destinations AS d ON f.destinationID = d.destinationID
 where flightID = ?
 """
 sql_search_flightDestination = """
 Select * 
 FROM flights as f
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID 
 where destinationID = (select d.destinationID from destinations as d 
 INNER JOIN flights AS f ON f.destinationID = d.destinationID
 where d.flightDestination = ?)
 """
 sql_search_status = """ 
 select * from flights as f 
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID 
 INNER JOIN destinations AS d ON f.destinationID = d.destinationID
 where status = ?
 """
 sql_search_departureTime = "select * from flights where DATE(departureTime) = ?"
 
 sql_alter_data = ""
 
 sql_update_departureTime = "UPDATE flights SET departureTime = ? where flightID = ?"
 sql_update_status = "UPDATE flights SET status = ? where flightID = ?"
 sql_update_pilot = "UPDATE flights SET pilotID = ? where flightID = ?"
 sql_update_destination = "UPDATE destinations SET flightDestination = ? where destinationID = ?"

 sql_delete_data = "DELETE from flights where flightID = ?"
 sql_drop_table = "DROP TABLE flights"
 
 sql_view_pilots = """
 select f.pilotID, p.Name, f.flightID, d.flightDestination,f.departureTime, f.status 
 from flights AS f 
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID 
 INNER JOIN destinations AS d ON f.destinationID = d.destinationID
 GROUP BY 1,2,3,4,5,6 
 Order BY 1 ASC
 """
 sql_view_destinations = """
 select d.flightDestination, f.flightID, f.departureTime, f.status 
 from flights AS f 
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID 
 INNER JOIN destinations AS d ON f.destinationID = d.destinationID 
 GROUP BY 1,2,3,4
 Order BY 3 ASC
 """
 sql_summary_pilot = """
 select p.Name, count(flightID) 
 from flights AS f 
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID 
 INNER JOIN destinations AS d ON f.destinationID = d.destinationID 
 GROUP BY 1
 Order BY 2 ASC
 """
 sql_summary_destination = """
 select p.flightDestination, count(flightID) 
 from flights AS f 
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID 
 INNER JOIN destinations AS p ON f.destinationID = p.destinationID 
 GROUP BY 1
 Order BY 2 ASC
 """

 flights_data = [
      (1,	1,	11,	'On Time',	'2023-10-01 08:00:00',	9),
      (2,	2,	12,	'Delayed',	'2023-10-02 09:00:00',	6),
      (3,	3,	13,	'Cancelled',	'2023-10-03 10:00:00',	9),
      (4,	4,	14,	'On Time',	'2023-10-04 11:00:00',	3),
      (5,	5,	15,	'On Time',	'2023-10-05 12:00:00',	9),
      (6,	6,	16,	'Delayed',	'2023-10-06 13:00:00',	7),
      (7,	7,	17,	'On Time',	'2023-10-07 14:00:00',	2),
      (8,	8,	18,	'On Time',	'2023-10-08 15:00:00',	5),
      (9,	9,	19,	'On Time',	'2023-10-09 16:00:00',	2),
      (10,	10,	20,	'Delayed',	'2023-10-10 17:00:00',	1)
 ]

 pilots_data = [
      (1,	'John Smith',	'Skybound Airlines'),
      (2,	'Jane Doe',	'Horizon Airways'),
      (3,	'David Lee',	'Starlink Aviation'),
      (4,	'Sarah Jones',	'Emerald Skies'),
      (5,	'Michael Brown',	'Apex Flight Group'),
      (6,	'Emily Davis',	'Global Wings'),
      (6,	'Robert Wilson',	'Voyager Airlines'),
      (7,	'Jessica Garcia',	'Summit Air'),
      (9,	'Christopher Rodriguez',	'Coastal Carriers'),
      (10,	'Ashley Martinez',	'Northern Lights Airlines')
 ]

 destination_data = [
      (1,	'London'),
      (2,	'Paris'),
      (3,	'Berlin'),
      (4,	'Rome'),
      (5,	'Madrid'),
      (6,	'Amsterdam'),
      (7,	'Dublin'),
      (8,	'Vienna'),
      (9,	'Zurich'),
      (10,	'Stockholm'),
      (11,	'New York'),
      (12,	'Tokyo'),
      (13,	'Sydney'),
      (14,	'Toronto'),
      (15,	'Buenos Aires'),
      (16,	'Cape Town'),
      (17,	'Mumbai'),
      (18,	'Shanghai'),
      (19,	'Los Angeles'),
      (20,	'Mexico City')
 ]

 def __init__(self):
   try:
     self.conn = sqlite3.connect("DBFlights.db")
     self.cur = self.conn.cursor()
     
     self.cur.execute(self.sql_create_table_firsttime)
     self.cur.execute(self.sql_create_pilot_table_firsttime)
     self.cur.execute(self.sql_create_destination_table_firsttime)
     
     self.conn.commit()
     
     self.cur.execute("select count(*) from flights")
     existing_rows = self.cur.fetchone()[0]

     if existing_rows == 0:
       for flight in self.flights_data:
         try:
           self.cur.execute(self.sql_insert_first_time,flight)
         except sqlite3.IntegrityError as e:
           print(f"Skipping insert due to error: {e}")
     
       self.conn.commit()

     self.cur.execute("select count(*) from pilots")
     existing_rows = self.cur.fetchone()[0]

     if existing_rows == 0:
       for pilot in self.pilots_data:
         try:
           self.cur.execute(self.sql_insert_pilot_first_time,pilot)
         except sqlite3.IntegrityError as e:
           print(f"Skipping insert due to error: {e}")
     
       self.conn.commit()
     
     self.cur.execute("select count(*) from destinations")
     existing_rows = self.cur.fetchone()[0]

     if existing_rows == 0:
       for destination in self.destination_data:
         try:
           self.cur.execute(self.sql_insert_destination_first_time,destination)
         except sqlite3.IntegrityError as e:
           print(f"Skipping insert due to error: {e}")
     
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
        self.cur.execute(self.sql_select_all)  # Execute your SQL query
        result = self.cur.fetchall()
       
        # Get column names from cursor.description
       # headers = [description[0] for description in self.cur.description]
       # print(headers)

        for row in result:
            print(row)

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
     # print(self.cur.execute("select DATE(departureTime) from flights"))
     result = self.cur.fetchall()

     for row in result:
      print(row)  # Print each row
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


 def update_pilot(self):
  try:
     self.get_connection()
     # Update statement
     while True:
      flightID = int(input("Enter FlightNo: "))
      pilotID = input("To Assign Pilot Enter PilotID: ")
      self.cur.execute(self.sql_update_pilot, (pilotID,flightID))
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

 def view_pilots(self):
   try:
     self.get_connection()
     self.cur.execute(self.sql_view_pilots)
     result = self.cur.fetchall()

     for row in result:
      print(row)  # Print each row
   except Exception as e:
     print(e)
   finally:
     self.conn.close()


 def view_destinations(self):
   try:
     self.get_connection()
     self.cur.execute(self.sql_view_destinations)
     result = self.cur.fetchall()

     for row in result:
      print(row)  # Print each row
   except Exception as e:
     print(e)
   finally:
     self.conn.close()

 def update_destination(self):
  try:
     self.get_connection()
     # Update statement
     while True:
      destinationID = int(input("Enter Destination ID: "))
      self.cur.execute("Select flightDestination from destinations where destinationID = ?",tuple(str(destinationID)))
      self.conn.commit()  # Commit changes

      result = self.cur.fetchone()[0]
      print("Current Flight Destination: "+ str(result))

      flightDestination = input("Enter New Flight Destination: ")
      self.cur.execute(self.sql_update_destination, (flightDestination,destinationID))
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

 def summary(self):
   try:
     self.get_connection()
     # Update statement

     while True:
      print("\n 1. View No. Flights per Destination")
      print(" 2. View No. Flights per Pilot")

      search_choice = int(input("Enter your choice: "))
      if search_choice == 1:
        self.cur.execute(self.sql_summary_destination)

      elif search_choice == 2:
        self.cur.execute(self.sql_summary_pilot)
      
      result = self.cur.fetchall()
      for row in result:
       print(row)  # Print each row
      break
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
 print(" 1. Add a New Flight")
 print(" 2. View All Flights")
 print(" 3. Search for Flight by Criteria")
 print(" 4. Update Flight Information")
 print(" 5. Delete Flight Information")
 print(" 6. Assign Pilot")
 print(" 7. View Pilot Schedule")
 print(" 8. Udpate Destination")
 print(" 9. View Destinations")
 print(" 10. View Summary Data")
 print(" 11. Drop table")
 print(" 12. Exit\n")


 __choose_menu = int(input("Enter your choice: "))
 db_ops = DBOperations()
 if __choose_menu == 1:
   db_ops.insert_data()
 elif __choose_menu == 2:
   db_ops.select_all()
 elif __choose_menu == 3:
   db_ops.search_data()
 elif __choose_menu == 4:
   db_ops.update_data()
 elif __choose_menu == 5:
   db_ops.delete_data()
 elif __choose_menu == 6:
   db_ops.update_pilot()
 elif __choose_menu == 7:
   db_ops.view_pilots()
 elif __choose_menu == 8:
   db_ops.update_destination()
 elif __choose_menu == 9:
   db_ops.view_destinations()
 elif __choose_menu == 10:
   db_ops.summary()
 elif __choose_menu ==11:
   db_ops.drop_table() 
 elif __choose_menu == 12:
   exit(0)
 else:
   print("Invalid Choice")


