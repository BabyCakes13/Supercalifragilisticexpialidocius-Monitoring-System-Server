"""Module which contains tests for
read_configuration_handler module."""
import os
import unittest
from files.read_configuration_handler import ReadHandler
from files.strings import get_configuration_file_form, get_metrics_file_form


class TestReadConfiguration(unittest.TestCase):
    """Class which contains functions for testing
    read_configuration_handler"""

    @classmethod
    def setUpClass(cls):
        """Initialises the READER and path to CONFIG.txt file"""

        cls.read_handler = ReadHandler()
        cls.root_path = os.path.dirname(os.path.abspath(__file__))[:-5]
        cls.config_path = cls.root_path + "files\\CONFIG.txt"

    def test_get_mongodb_name(self):
        """Tests whether the get_mongodb_name function works."""

        with open(self.config_path, "w") as f_config:
            f_config.write(get_configuration_file_form())

        expected_value = "database_name"

        self.assertEqual(self.read_handler.get_mongodb_name(), expected_value)
        self.assertNotEqual(self.read_handler.get_mongodb_name(), "donut")

    def test_get_mongodb_link(self):
        """Tests whether the get_mongodb_link function works."""

        with open(self.config_path, "w") as f_config:
            f_config.write(get_configuration_file_form())

        expected_value = "database_link"

        self.assertEqual(self.read_handler.get_mongodb_uri(), expected_value)
        self.assertNotEqual(self.read_handler.get_mongodb_uri(), "cake")

    def test_get_rabbitmq_address(self):
        """Tests whether the get_rabbitmq_address function works."""

        with open(self.config_path, "w") as f_config:
            f_config.write(get_configuration_file_form())

        expected_value = "localhost"

        self.assertEqual(self.read_handler.get_rabbitmq_address(),
                         expected_value)
        self.assertNotEqual(self.read_handler.get_flask_address(), "nougat")

    def test_get_rabbitmq_port(self):
        """Tests whether the get_rabbitmq_port function works."""

        with open(self.config_path, "w") as f_config:
            f_config.write(get_configuration_file_form())

        expected_value = "5672"

        self.assertEqual(self.read_handler.get_rabbitmq_port(), expected_value)
        self.assertNotEqual(self.read_handler.get_rabbitmq_port(), "pancake")

    def test_get_flask_address(self):
        """Tests whether the get_flask_address function works."""

        with open(self.config_path, "w") as f_config:
            f_config.write(get_configuration_file_form())

        expected_value = "localhost"

        self.assertEqual(self.read_handler.get_flask_address(), expected_value)
        self.assertNotEqual(self.read_handler.get_flask_address(), "coffee")

    def test_get_flask_port(self):
        """Tests whether the get_flask_port function works."""

        with open(self.config_path, "w") as f_config:
            f_config.write(get_configuration_file_form())

        expected_value = "500"

        self.assertEqual(self.read_handler.get_flask_port(), expected_value)
        self.assertNotEqual(self.read_handler.get_flask_port(), "not tea")

    def test_get_supported_metrics(self):
        """Tests whether the get_supported_metrics function works."""

        metrics_path = os.path.join(self.root_path, "files\\metrics.txt")

        with open(metrics_path, "w") as f_metrics:
            f_metrics.write(get_metrics_file_form())

        expected_value = ['Disk_Usage',
                          'Cpu_Percent',
                          'Memory_Info',
                          'Cpu_Stats']

        self.assertEqual(self.read_handler.get_supported_metrics(),
                         expected_value)
        self.assertNotEqual(self.read_handler.get_supported_metrics(), "taco")
