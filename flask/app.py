from flask import Flask
from flask import render_template
from threads.get_objects_from_rabbit import RabbitObjectHandler
from files.configuration_handler import CreateConfiguration
from files.read_metrics import read_metrics
from files.read_configuration_handler import ConfigurationFileReader
from database.database_handler import DatabaseHandler
from files.strings import get_main_page_html, get_metric_list_html

app = Flask(__name__, template_folder="templates")
config = CreateConfiguration()
database_handler = DatabaseHandler(app)

@app.route('/')
def main_page_route():
    """Displays the main page and the types of information you can get the server to display."""

    return render_template("main_page.html")


@app.route('/current_supported_metrics')
def current_supported_metrics_route():
    """Displays the currently supported metrics."""

    return render_template("current_supported_metrics.html", metrics=read_metrics())


@app.route('/packets')
def packets_route():
    """Displays information about all the packages in the database."""

    all_packets = database_handler.get_all_packets()
    packets_list = []

    for packets in all_packets:
        for packet in packets:
            del packet['_id']
            packets_list.append(packet)

    return render_template("all_packets.html", nodes=packets_list)


@app.route('/packets/<id>')
def packets_id(id):
    """Displays information about a package based on the package ID"""
    packet_info = database_handler.get_packet_info(str(id))

    for packet in packet_info:
        packets_new = database_handler.delete_database_id(packet)

    return render_template("packet_information.html", packets=packets_new)

if __name__ == '__main__':

    consume_packet_thread = RabbitObjectHandler(app)
    consume_packet_thread.start()

    reader = ConfigurationFileReader()

    app.run(reader.get_flask_address(),reader.get_flask_port())

