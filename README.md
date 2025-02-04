# Lab3.2: Flight Management Database


## Introduction
A database application that includes a user-friendly menu system, allowing staff to add, retrieve, update and delete information about flights, pilots and destinations

### Repository Contents:  
- main.py - Python file  
- DBFlights.db - Database file
  
## 1. Database setup in SQLite
### Database Schema:  
**Flights Table**
| Column                | Description               |
|-----------------------|---------------------------|
| flightID              | INTEGER PRIMARY KEY       |
| originID              | INTEGER                   |
| destinationID         | INTEGER                   |
| status                | VARCHAR(15)               |
| departureTime         | DATETIME (ISO 8601 format)|
| pilotID               | INTEGER                   |

**Pilots Table**
| Column                | Description               |
|-----------------------|---------------------------|
| pilotID               | INTEGER PRIMARY KEY       |
| Name                  | VARCHAR(30)               |
| Carrier               | VARCHAR(30)               |

**Destinations Table**
| Column                | Description               |
|-----------------------|---------------------------|
| destinationID         | INTEGER PRIMARY KEY       |
| flightDestination     | INTEGER                   |

## 2. SQL queries and database interaction
**Flight Retrieval**  
Example:  
sql_search_flightID = """  
 select *  
 from flights as f  
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID  
 INNER JOIN destinations AS d ON f.destinationID = d.destinationID  
 where flightID = ?  
 """   
**Schedule Modification**  
Example:  
sql_update_departureTime = "UPDATE flights SET departureTime = ? where flightID = ?"  

**Pilot Assignment**  
Example:  
sql_update_pilot = "UPDATE flights SET pilotID = ? where flightID = ?"  

**Destination Management** 
Example:  
 sql_update_destination = "UPDATE destinations SET flightDestination = ? where destinationID = ?"  
 
**Summarise Data**  
Example:  
sql_summary_pilot = """  
 select p.Name, count(flightID)   
 from flights AS f   
 INNER JOIN pilots AS p ON f.pilotID = p.pilotID   
 INNER JOIN destinations AS d ON f.destinationID = d.destinationID   
 GROUP BY 1  
 Order BY 2 ASC  
 """  
## 3. Application development in python (using SQLite3)
Functionality:
- Add a New Flight
- View Flights by Criteria
- Update Flight Information: Modify details of an existing flight.
- Assign Pilot to Flight
- View Pilot Schedule
- View/Update Destination Information
- Summarise Data: No. of flights per destination/pilot
## 4. How to run the program
1. Open the main.py file in Github
2. Run the file using Github Codespaces
3. Interact with the menu system
