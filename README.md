# Time Tracker Project
Project intended to familiarize again qith SQL databases and extend python knowledge (type hints, class overriding, better coding pratices)

Perform the majority of the development steps in notebooks, then convert them to scripts using:
`jupyter nbconvert --to script YourNotebook.ipynb`


## Requirements

Create time tracker desktop application capable of:
- Adding / Change / remove time entries
- Perform real time tracking
- Store time entries in local database
- Link local database to webserver / TimeCamp database over their API
- Automatic export of time entries summary at end of month -> in csv / pdf
## Documentation
### Time Camp API
Link to timecamp api:

[ https://developer.timecamp.com/docs/timecamp-api/bc8b702b5473b-time-camp-api ]

## Datastructure
A Time camp entry regroups the following parameters:
- id: id of the entry.
- duration: total duration of the time entry, in seconds.
- user_id: id of the user to which the entry bellongs
- user_name: email address of the user to which the entry bellongs
- taks_id: task id
- last_modify: date and time of last modification of the entry
- date: date of the entry
- start_time: start time of the entry
- end_time: end time of the entry
- locked: if entry is locked (0 or 1)
- addons_external_id: id assigned to entry from external addons to timecamp
- billable: if entry is billable (0 or 1)
- invoiceId: ID when invoice 


An example of multiple time entries:
| id | duration | user_id |user_name | task_id |
| :-----: | :-----: | :-----: |:-----: | :-----: |
| 188198079 | 10453 | 283   |


# Local Database
Implement a local SQL database, to store the entries fetched from the API and those inserted manually(locally) in the GUI.

In the long term, the SQL Database should be able to be fully synchronized when the local machine has internet access.

## SQL Database learnings.
- Queries: Allows to get, insert, update and delete data.
- Schema: defines the structure of the database (tables, fields in each table, tables/fields relationships)
- Indexes: Used to speed up data retrieval on a database table -> access elements by index.
- Foreign key: links 

## Database strucuture
For now only use 2 tables, one responsible of all the users (one for now), and another responsible for all the time entries.

### Users table
| UserId | Name | Email | Token |  
| :-----: | :-----: | :-----: | :-----: |
| 1288 | David | -------------@gmail.com  | 45651325832556412 |

### TimeEntries table
| TimeEntryID | UserID | Date| StartTime | EndTime | Duration | TaskID |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | 
| 1 | 1288 |  2022-01-01 | 09:00:00 | 11:45:00 | 9900 | Meeting

## SQLite 3 to generate the database:

