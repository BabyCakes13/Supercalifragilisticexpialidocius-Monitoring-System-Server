"""Module which reads the information from the config.txt file:
metric options, send time, ip and address."""
import os
import re
from files.strings import get_flask_address_re, get_flask_port, get_mongodb_name_re, get_mongodb_uri_re, get_rabbitmq_address_re, get_rabbitmq_port_re


class ConfigurationFileReader:
    """Class which handles reading metrics from the configuration file"""

    def __init__(self):
        """Contains the path to the config.txt file."""

        self.config_path = os.path.dirname(os.path.abspath(__file__))[:-5] + "files\\config.txt"
        print(self.config_path)

    def get_mongodb_name(self):
        """Returns the address on which the rabbitmq server connects. It is localhost by default."""
        f_config = open(self.config_path, "r")

        mongodb_name = re.search(get_mongodb_name_re(), f_config.read()).group()[13:]

        f_config.close()
        return mongodb_name

    def get_mongodb_uri(self):
        """Returns the address on which the rabbitmq server connects. It is localhost by default."""
        f_config = open(self.config_path, "r")

        mongodb_uri = re.search(get_mongodb_uri_re(), f_config.read()).group()[12:]

        f_config.close()
        return mongodb_uri

    def get_rabbitmq_address(self):
        """Returns the address on which the rabbitmq server connects. It is localhost by default."""
        f_config = open(self.config_path, "r")

        rabbitmq_address = re.search(get_rabbitmq_address_re(), f_config.read()).group()[-9:]

        f_config.close()
        return rabbitmq_address

    def get_rabbitmq_port(self):
        """Returns the address on which the rabbitmq server connects. It is localhost by default."""
        f_config = open(self.config_path, "r")

        rabbitmq_port = re.search(get_rabbitmq_port_re(), f_config.read()).group()[-4:]

        f_config.close()
        return rabbitmq_port

    def get_flask_address(self):
        """Returns the address on which the rabbitmq server connects. It is localhost by default."""
        f_config = open(self.config_path, "r")

        flask_address = re.search(get_flask_address_re(), f_config.read()).group()[-9:]

        f_config.close()
        return flask_address

    def get_flask_port(self):
        """Returns the address on which the rabbitmq server connects. It is localhost by default."""
        f_config = open(self.config_path, "r")

        flask_port = re.search(get_flask_port(), f_config.read()).group()[-3:]

        f_config.close()
        return flask_port



