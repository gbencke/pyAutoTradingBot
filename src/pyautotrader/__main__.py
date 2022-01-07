import sys
import os
import argparse
from pyautotrader.utils.data_import import import_data_from_profit_chart_into_metatrader, import_data_from_profit_chart
from pyautotrader.utils.model_export import generate_language_model

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

command_parser.add_argument('--model-short',
                            metavar='modelshort',
                            dest='modelshort',
                            type=str,
                            required=False,
                            help='Short Model to use in order to generate the source files. (Required for generate_code command)')

command_parser.add_argument('--model-long',
                            metavar='modellong',
                            dest='modellong',
                            type=str,
                            required=False,
                            help='Long Model to use in order to generate the source files. (Required for generate_code command)')

command_parser.add_argument('--python-function-name',
                            metavar='pythonfunctionname',
                            dest='pythonfunctionname',
                            type=str,
                            required=False,
                            help='Name of the python function to generate the code model (Required for generate_code command)')

command_parser.add_argument('--initial-date',
                            metavar='initialdate',
                            dest='initialdate',
                            type=str,
                            required=False,
                            help='Initial Date for the source CSV file')

command_parser.add_argument('--save-model-to',
                            metavar='savemodelto',
                            dest='savemodelto',
                            type=str,
                            required=False,
                            help='File to save the generated code model ( profit or python language')


args = command_parser.parse_args()

if __name__ == '__main__':
    if args.command == 'import_data_from_profit_chart_into_metatrader':
        import_data_from_profit_chart(args)
    if args.command == 'generate_code':
        generate_language_model(args)
