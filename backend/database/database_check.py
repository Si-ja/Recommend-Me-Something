"""
A short checker that helps establish the state of the database - 
something that the user never interacts with and is only meant for the
back-end processes
"""
class DBchcek:

    @staticmethod
    def findTableNames():
        """
        Find the names of the tables that are currently in use.
        """
        import sqlite3
        conn = sqlite3.connect("backend/database/recommendations.db")
        results = conn.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
        tables_collection = []
        for name in results:
            tables_collection.append(name[0])
        conn.close
        return tables_collection