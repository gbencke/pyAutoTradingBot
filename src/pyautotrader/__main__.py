import sys
import os
import argparse
from pyautotrader.utils.data_import import import_data_from_profit_chart_into_metatrader

command_parser = argparse.ArgumentParser(
    description='pyAutoTrader - Universal Python Automatic Trading Bot - Utils CLI')
command_parser.add_argument('command',
                            metavar='command',
                            type=str,
                            choices=['import_data_from_profit_chart_into_metatrader',
                                     'generate_code'],
                            help='Command to be performed by CLI, can be: [import_data_from_profit_chart_into_metatrader, generate_code]')

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

command_parser.add_argument('--language',
                            metavar='language',
                            dest='language',
                            type=str,
                            required=False,
                            choices=['python', 'profitchart'],
                            help='Language to generate the source files from the XGBoost Model. Can be:[python, profitchart].\n(Required for generate_code command)')

command_parser.add_argument('--model',
                            metavar='model',
                            dest='model',
                            type=str,
                            required=False,
                            help='Model to use in order to generate the source files. (Required for generate_code command)')
command_parser.add_argument('--initial-date',
                            metavar='initialdate',
                            dest='initialdate',
                            type=str,
                            required=False,
                            help='Initial Date for the source CSV file')


args = command_parser.parse_args()

if __name__ == '__main__':
    if args.command == 'import_data_from_profit_chart_into_metatrader':
        if args.destination is None:
            print("Missing --destination parameter")
            sys.exit(1)
        if args.source is None:
            print("Missing --source parameter")
            sys.exit(1)
        import_data_from_profit_chart_into_metatrader(
            args.source, args.destination, args.initialdate)
