#IN4331-Web Data Management

Core Idea: Develop a movie informaiton web service
Create multiple backends for the web service
- Relational backend using PostgresSQL
- Document-based using MongoDB
- Graph-based using Neo4J

# Process
The steps are discussed which have to be taken during the project

## Getting started
Data is provided as a Posgres backup file, this is first set-up by doing the following steps:
- Install version 9.6 of PostgresSQL, and set-up bin-path 
- Import supplied backup file into new database within pgAdmin
- Do some maintenance operations such as vacuuming and reindexing
- Explore data using query tool

## Getting serious
It have been decided to use Python as the core programming language. The RESTFul Web Services are implemented. The web service calls via JSON. The web service endpoints are defined for the required functionality. And finally the service is connected to the backend data storage.

## Making it hard
Two additional back ends are used. The data is converted to the right format, this will be tricky. The web service is connected to the new backend. This is done to see how different technologies behave in the same usage scenario. To do this properly it must be running on at least three machine at the same time. This can be done using virtual machines or on different laptops.
