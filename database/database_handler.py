"""Module which manages the information sent by the Flask server."""
from flask_pymongo import PyMongo
from files.read_configuration_handler import ConfigurationFileReader


class DatabaseHandler(object):
    """Enables adding an object of the type metrics, time and id to the database,
    configuring the database with user and ur, get information about the data."""

    def __init__(self, app):

        self.app = app

        reader = ConfigurationFileReader()

        print(reader.get_mongodb_uri())

        self.app.config['MONGODB_NAME'] = reader.get_mongodb_name()
        self.app.config['MONGO_URI'] = reader.get_mongodb_uri()

    def add_packet_to_database(self, packet):
        """Adds a packet to the database."""

        database = PyMongo(self.app)
        inserter = database.db.node
        inserter.insert(packet)

    def get_packet_info(self, id):
        """Searches for the data of a specific node, given by the IP address."""

        database = PyMongo(self.app)
        inserter = database.db.node

        packets = inserter.find({'id': id})

        return packets