# cassandra/main.py
from cassandra.cluster import Cluster
from cassandra.cqlengine.connection import register_connection, set_default_connection
from .config import keyspace

def get_session():
    cluster = Cluster(["127.0.0.1"])  # Replace with your Cassandra cluster contact points
    session = cluster.connect()
    register_connection(keyspace, session=session)
    set_default_connection(keyspace)
    return session
