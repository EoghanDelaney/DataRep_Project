
import mysql.connector

# SQL commands to create Database, Table and describe table.

# CREATE DATABASE crimedb;

# *id, *User, *date, *type, *long, *lat, 
 CREATE TABLE crime (
     id int NOT NULL auto_increment,
     User varchar(255),
     date DATE,
     type varchar(255),
     lng FLOAT(10,7),
     lat FLOAT(10,7),
     PRIMARY KEY(id)
 );

# DESC crime;
# Date format YYYY - MM - DD
# insert into crime (User, date, type, lng, lat) values ("Eoghan" , "11-12-20" , "Murder", "9.63", "63.9");
# insert into crime (User, date, type, lng, lat) values ("Keith" , "08-03-21" , "Theft", "7.8", "6.9");
# insert into crime (User, date, type, lng, lat) values ("Stephen" , "03-08-16" , "J Walking", "12.9", "5.7");

class crimeDOA:
    db=""
    
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Maynooth",
            database="crimedb"
        )

    # Create
    def create(self, crime):
        cursor = self.db.cursor()
        sql="insert into crime (User, date, type, lng, lat) values (%s,%s,%s,%s,%s)"
        values = [
            crime['User'],
            crime['date'],
            crime['type'],
            crime['lng'],
            crime['lat'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # Get All
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from crime"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []

        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray


    # find By id
    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from crime where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        test = self.convertToDict(result)
        return test

    # Update
    def update(self, crime):
        cursor = self.db.cursor()
        sql="update crime set User= %s, date=%s, type= %s, lng=%s, lat=%s  where id =%s " 
        values = [
            crime['User'],
            crime['date'],
            crime['type'],
            crime['lng'],
            crime['lat'],
            crime['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()

    # Delete
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from crime where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

    def convertToDict(self, result):
        colnames = ['id','User', 'date', 'type', 'lng', 'lat']
        crime = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                crime[colName] = value
        return crime


crimeDOA = crimeDOA()