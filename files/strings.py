"""Module which contains all strings used in the project"""


def get_configuration_file_form():
    """Contains the form of the configuration file of the server."""

    return "MONGODB_NAME=metrics" \
        "\nMONGODB_URI=mongodb://user:password13@ds261521.mlab.com:61521/metrics" \
        "\nRABBITMQ_ADDRESS=localhost" \
        "\nRABBITMQ_PORT=5672" \
        "\nFLASK_ADDRESS=localhost" \
        "\nFLASK_PORT=500"


def get_configuration_file_re():
    """Contain the regex expression to check the validity of the configuration file"""

    return r"MONGODB_NAME=(.)" \
        r"\nMONGODB_URI=(.)" \
        r"\nRABBITMQ_ADDRESS=(localhost)" \
        r"\nRABBITMQ_PORT=(\d{1,5})" \
        r"\nFLASK_ADDRESS=(localhost)" \
        r"\nFLASK_PORT=(\d{1,5})"


def get_mongodb_name_re():
    """Contains the regex expression for the mongodb_name"""

    return r"MONGODB_NAME=([^\n]+)"


def get_mongodb_uri_re():
    """Contains the regex expression for the mongodb_uri"""

    return r"MONGODB_URI=([^\n]+)"


def get_rabbitmq_address_re():
    """Contains the regex expression for the rabbitmq_address"""

    return r"RABBITMQ_ADDRESS=(localhost)"


def get_rabbitmq_port_re():
    """Contains the regex expression for the rabbitmq_port"""

    return r"RABBITMQ_PORT=(\d{1,5})"


def get_flask_address_re():
    """Contains the regex expression for the flask_address"""

    return r"FLASK_ADDRESS=(localhost)"


def get_flask_port():
    """Contains the regex expression for the flask_port"""

    return r"FLASK_PORT=(\d{1,5})"

def get_rabbit_queue():

    return "metrics_queue"




