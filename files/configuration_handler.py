"""Module which creates the CONFIG.txt file if it
 does not exist or it's invalid."""
import os
import re
from files.strings import get_configuration_file_form,\
    get_configuration_file_re, get_metrics_file_form


class CreateConfiguration:
    """Class which handles the creation and validity
     of the configuration file."""

    def __init__(self):
        """Keeps the path to the CONFIG.txt file in config_path.
        If the CONFIG.txt file already exists and it valid,
        then it does nothing.
        Else, it creates a new default configuration file."""

        self.root_path = os.path.dirname(os.path.abspath(__file__))[:-5]
        self.config_path = os.path.join(self.root_path, "files\\CONFIG.txt")
        self.metrics_path = os.path.join(self.root_path, "files\\metrics.txt")

        self.setup_metrics_file()

        if self.check_configuration() is False:
            self.setup_configuration_file()

    def setup_metrics_file(self):
        """Writes the current supported metrics in
        the metrics.txt file."""

        with open(self.metrics_path, "w+") as f_metrics:

            f_metrics.write(get_metrics_file_form())

    def setup_configuration_file(self):
        """Creates the CONFIG.txt file, which contains the metrics
         which are possible to monitor.
        In order to deactivate one metric, write FALSE instead of TRUE"""

        with open(self.config_path, "w+") as f_config:

            f_config.write(get_configuration_file_form())

    def validate_configuration_file(self):
        """Checks whether the structure of the configuration file is correct"""

        with open(self.config_path, "r+") as f_config:
            return bool(re.search(get_configuration_file_re(),
                                  f_config.read()))

    def check_configuration(self):
        """Checks to see if the configuration file already
        exists and it's valid
        and creates another if it doesn't"""

        return bool(os.path.isfile(self.config_path) and
                    self.validate_configuration_file())
