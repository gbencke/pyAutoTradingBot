import sys
import os
import argparse
from pyautotrader.utils.data_import import import_data_from_profit_chart, add_data_import_args
from pyautotrader.utils.model_export import generate_language_model, add_generate_language_args

command_parser = argparse.ArgumentParser(
    description='pyAutoTrader - Universal Python Automatic Trading Bot - Utils CLI')

command_parser.add_argument('command',
                            metavar='command',
                            type=str,
                            choices=['import_data_from_profit_chart_into_metatrader',
                                     'generate_code'],
                            help='Command to be performed by CLI, can be: [import_data_from_profit_chart_into_metatrader, generate_code]')

add_data_import_args(command_parser)
add_generate_language_args(command_parser)


args = command_parser.parse_args()

if __name__ == '__main__':
    if args.command == 'import_data_from_profit_chart_into_metatrader':
        import_data_from_profit_chart(args)
    if args.command == 'generate_code':
        generate_language_model(args)
