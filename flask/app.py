from flask import Flask
from threads.get_objects_from_rabbit import RabbitObjectHandler
from files.configuration_handler import CreateConfiguration
from files.read_configuration_handler import ConfigurationFileReader

app = Flask(__name__)


@app.route('/')
def index_route():
    return 'Hey, babes!'


if __name__ == '__main__':

    CreateConfiguration()

    consume_packet_thread = RabbitObjectHandler(app)
    consume_packet_thread.start()

    reader = ConfigurationFileReader()

    app.run(reader.get_flask_address(),reader.get_flask_port())

