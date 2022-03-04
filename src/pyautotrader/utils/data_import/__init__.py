from .import_data_from_profit_chart_into_metatrader import import_data_from_profit_chart_into_metatrader
from .import_data_from_csv import import_data_from_csv
from .aggregate_data_from_csv import aggregate_data_from_csv


def import_data_from_profit_chart(args):
    if args.destination is None:
        print("Missing --destination parameter")
        sys.exit(1)
    if args.source is None:
        print("Missing --source parameter")
        sys.exit(1)
    import_data_from_profit_chart_into_metatrader(
        args.source, args.destination, args.initialdate)


def add_data_import_args(command_parser):
    command_parser.add_argument('--source',
                                metavar='source',
                                dest='source',
                                type=str,
                                help='CSV source file to import data from. (Required for import_data_from_profit_chart_into_metatrader command)')

    command_parser.add_argument('--destination',
                                metavar='destination',
                                dest='destination',
                                type=str,
                                required=False,
                                help='CSV destination file for imported data. (Required for import_data_from_profit_chart_into_metatrader command')

    command_parser.add_argument('--asset',
                                metavar='asset',
                                dest='asset',
                                type=str,
                                help='Asset that the Data belongs to...')

    command_parser.add_argument('--exchange',
                                metavar='exchange',
                                dest='exchange',
                                type=str,
                                help='Exchange that the Data belongs to...')

    command_parser.add_argument('--timeframe',
                                metavar='timeframe',
                                dest='timeframe',
                                type=str,
                                help='TimeFrame that the Data belongs to...')
