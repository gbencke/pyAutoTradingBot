
def add_server_args(command_parser):
    command_parser.add_argument('--sqlalchemy-connection-string',
                                metavar='sqlalchemy_connection_string',
                                dest='sqlalchemy_connection_string',
                                type=str,
                                required=False,
                                help='String for the connection of the SQLAlchemy Engine')
    command_parser.add_argument('--server-port',
                                metavar='server_port',
                                dest='server_port',
                                type=int,
                                required=False,
                                help='Port for connection to the server')
    command_parser.add_argument('--listening-ip',
                                metavar='listening_ip',
                                dest='listening_ip',
                                type=str,
                                required=False,
                                help='IP for the listening of the server')
