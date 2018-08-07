# Supercalifragilisticexpialidocius-Monitoring-System-Server
This is the server part of the project.
Using RabbitMQ, the sent metric packets will be added to a MongoDB database using the database name and database link.
Using Flask, the packets are taken from the database and displayed in html format.
To change database name and database link, instead of default, write them in config.txt file.
To display information, check the main page of html.
