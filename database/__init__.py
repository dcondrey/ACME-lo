import sqlite3
import pymongo

class DatabaseConnection:
    def __init__(self, db_config):
        self.db_type = db_config['type']
        if self.db_type == 'sql':
            self.connection = sqlite3.connect(db_config['sqlite_path'])
            self.cursor = self.connection.cursor()
        elif self.db_type == 'nosql':
            self.client = pymongo.MongoClient(db_config['mongo_uri'])
            self.connection = self.client[db_config['mongo_db']]

    def close(self):
        if self.db_type == 'sql':
            self.connection.close()
        elif self.db_type == 'nosql':
            self.client.close()

class CRUDOperations:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create(self, data, table_or_collection):
        if self.db_connection.db_type == 'sql':
            columns = ', '.join(data.keys())
            placeholders = ', '.join('?' * len(data))
            query = f"INSERT INTO {table_or_collection} ({columns}) VALUES ({placeholders})"
            self.db_connection.cursor.execute(query, tuple(data.values()))
            self.db_connection.connection.commit()
        elif self.db_connection.db_type == 'nosql':
            self.db_connection.connection[table_or_collection].insert_one(data)

    def read(self, query, table_or_collection):
        if self.db_connection.db_type == 'sql':
            query = f"SELECT * FROM {table_or_collection} WHERE " + ' AND '.join([f"{k} = ?" for k in query])
            self.db_connection.cursor.execute(query, tuple(query.values()))
            return self.db_connection.cursor.fetchall()
        elif self.db_connection.db_type == 'nosql':
            return self.db_connection.connection[table_or_collection].find_one(query)

    def update(self, query, data, table_or_collection):
        if self.db_connection.db_type == 'sql':
            data_update = ', '.join([f"{k} = ?" for k in data])
            query_cond = ' AND '.join([f"{k} = ?" for k in query])
            sql_query = f"UPDATE {table_or_collection} SET {data_update} WHERE {query_cond}"
            self.db_connection.cursor.execute(sql_query, tuple(data.values()) + tuple(query.values()))
            self.db_connection.connection.commit()
        elif self.db_connection.db_type == 'nosql':
            self.db_connection.connection[table_or_collection].update_one(query, {'$set': data})

    def delete(self, query, table_or_collection):
        if self.db_connection.db_type == 'sql':
            query_cond = ' AND '.join([f"{k} = ?" for k in query])
            sql_query = f"DELETE FROM {table_or_collection} WHERE {query_cond}"
            self.db_connection.cursor.execute(sql_query, tuple(query.values()))
            self.db_connection.connection.commit()
        elif self.db_connection.db_type == 'nosql':
            self.db_connection.connection[table_or_collection].delete_one(query)

class DataPreprocessing:
    @staticmethod
    def clean(data):
        # Basic cleaning logic (e.g., removing leading/trailing spaces)
        return {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}

    @staticmethod
    def normalize(data):
        # Basic normalization (e.g., scaling numeric values)
        return {k: (v - min(v)) / (max(v) - min(v)) if isinstance(v, (int, float)) else v for k, v in data.items()}

    @staticmethod
    def transform(data):
        # Basic transformation (e.g., converting strings to lowercase)
        return {k: v.lower() if isinstance(v, str) else v for k, v in data.items()}

