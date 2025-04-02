# database_manager.py
from neo4j import GraphDatabase

class DatabaseManager:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_record(self, recording_data):
        with self.driver.session() as session:
            session.run("CREATE (a:Recording {data: $data})", data=recording_data)
