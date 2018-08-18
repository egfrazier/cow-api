# Correlates of War API

## A RESTful Application Programming interface for data sets from the Correlates of War project.

The Correlates of War data set is a collection of global conflict data dating back 1816. The project was founded in 1963 at the University of Michigan. Currently the data is available as downloadable CSV files from correlatesofwar.org. The purpose of the COW API project is to make this data accessible via RESTful API so that it can be accessed progromatically.

Endpoints (in progress):
* /api/v1/resources/state/{state id number}
  * JSON response containing details of a specific state (e.g. ID number, full name, etc).
* /api/v1/resources/states
  * JSON response containing details for all states that have ever existed in the international state system.
* /api/v1/resources/system_tenure/{state id number}
  * JSON response containing the start and end dates of a specific states tenure (membership) in the international state system.
* /api/v1/resources/major_tenure/{state id number}
  * JSON response containing the start and end dates of a specific states tenure (membership) as a major power in the international state system.