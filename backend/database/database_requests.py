"""This file holds main requests types that can be sent to the database
when the user wants to access some information"""
class DBrequests:

    def __init__(self, table):
        """
        Establish a connection to a specific table in the recommendations.db file
        table (str): table to connect to. Either Games or Movies
        """
        import sqlite3
        self.table = table
        try:
            self.conn = sqlite3.connect("backend/database/recommendations.db")
        except Exception as e:
            print(e)
        self.c = self.conn.cursor()

    def __str__(self):
        return f'A class that allows for the connection to the recommendations.db and the {self.table} table'

    def __repr__(self):
        return f'Connection bridge to the {self.table} table in the recommendations.db'

    def closeConnection(self):
        """
        Consider closing the connection after the request has been sent and information returned
        """
        self.conn.close
        
    def accidentalRecommendation(self):
        """
        Recommend an accidental entry in the database selected on the __init__.
        """
        import sqlite3
        from random import randint
        
        # Establish how many records there are to chose from
        self.c.execute(f"SELECT COUNT(*) FROM ({self.table})")
        self.conn.commit()
        rows = self.c.fetchone()[0]

        # Generate a random value, that will represent the row information will be chosen from
        row = randint(1, rows)
        
        # Make a selection of the row that was chosen
        self.c.execute(f"SELECT * FROM {self.table} WHERE rowid = (:row)", {'row': row})
        self.conn.commit()
        recommendation = self.c.fetchone()
        column_names = [description[0] for description in self.c.description]
        self.closeConnection()

        # Combine names with the output to make life easier in reading files
        selection = {}
        for idx in range(len(column_names)):
            selection[column_names[idx]] = recommendation[idx]
        return selection  

    def retrieveFullDatabase(self):
        """
        Check all the records that are present in a particular table. This will populate
        the api/management page. 
        """
        import sqlite3

        # Make a request to a table and retrieve all of the records by their name that it holds
        self.c.execute(f"""SELECT name
                           FROM {self.table}
                           ORDER BY name asc
                        """)
        self.conn.commit()
        contents = self.c.fetchall()
        self.closeConnection()

        # Update the output in the json format, so that it would be easier to handle later
        # On the frontend, while updating the full list of items in the database
        selection = {}
        for idx in contents:
            selection[idx[0]] = idx[0]

        # Give the full output
        return selection

    def deleteOneInstance(self, idx):
        """
        Delete one instance in the selected database
        param: idx (str): name of the item we want to delete
        """
        import sqlite3

        # Make a request to the table in regards to what we want to delete
        self.c.execute(f"DELETE FROM {self.table} WHERE name = (:idx)", {'idx': idx})
        self.conn.commit()
        self.conn.close()

    def updateOneInstance(self, idx, year, img, description):
        """
        Update one instance in the selected database
        param: idx (str): name of the item we want to update and change something to
        param: year (str): year to which we want to change some information
        param: img (str): source of the image that we want to change
        param: description (str): description to which we want to change the information to
        """
        import sqlite3

        # Make a request to the table in regards to what we want to update
        self.c.execute(f"""UPDATE {self.table} 
                           SET name = (:idx),
                               year = (:year),
                               img = (:img),
                               description = (:description)
                            WHERE name = (:idx)""",
                            {'idx': idx,
                             'year': year,
                             'img': img,
                             'description': description})
        self.conn.commit()
        self.conn.close()

    def addOneInstance(self, idx='', year='', img='', description=''):
        """
        Adds an instance to the database being worked with
        param:
            idx (str): name of the item. Default: ''
            year (str): year when the item was released. Default: ''
            img (str): https link to an image. Default: ''
            description (str): description of an item. Default: ''
        """
        import sqlite3

        self.c.execute(f"""INSERT INTO {self.table}
                        VALUES ((:idx), (:description), (:year), (:img), (:consumed))
                       """,
                       {
                            'idx': idx,
                            'year': year,
                            'img': img,
                            'description': description,
                            'consumed': 0
                        })
        self.conn.commit()
        self.conn.close()

    def retrieveOneInstance(self, idx):
        """
        Retrieve information for only one instance that we want to examine
        param: idx (str): name of the item we want to delete
        """
        import sqlite3

        # Make a request to the table we want
        self.c.execute(f"SELECT * FROM {self.table} WHERE name = (:idx)", {'idx': idx})
        self.conn.commit()
        contents = self.c.fetchone()
        self.conn.close()

        # Update the information so it could be returned in a json format
        selection = {}
        column_names = [description[0] for description in self.c.description]
        for i in range(len(column_names)):
            selection[column_names[i]] = contents[i]
        return selection