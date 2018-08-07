"""Module which handles the RabbitMQ connection."""
from threading import Thread
import json
import pika
from database.database_handler import DatabaseHandler
from files.strings import get_rabbit_queue
from files.read_configuration_handler import ReadHandler


class RabbitObjectHandler(Thread):
    """Class which handles the RabbitMQ connection."""

    def __init__(self, app):
        """Initialises the connection between RabbitMQ queue and Flask server,
        in order to get the objects waiting in Rabbit queue and put them in
        the database."""

        Thread.__init__(self)

        self.connection_channel = False
        self.app = app

        self.handle_connection()
        self.database_handler = DatabaseHandler(self.app)

    def handle_connection(self):
        """Handles the connection."""

        reader = ReadHandler()

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                reader.get_rabbitmq_address(), reader.get_rabbitmq_port()))
        self.connection_channel = connection.channel()
        self.connection_channel.queue_declare(queue=get_rabbit_queue())

    def collect_packet(self, channel, method, properties, body):
        """Adds the packet collected from the Rabbit queue to the database."""

        self.database_handler.add_packet_to_database(json.loads(body))
        print(body)

    def run(self):
        """Starts the thread which consumes the objects
         from the RabbitMQ queue."""

        self.connection_channel.basic_consume(self.collect_packet,
                                              queue=get_rabbit_queue(),
                                              no_ack=True)

        self.connection_channel.start_consuming()
