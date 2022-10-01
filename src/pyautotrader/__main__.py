import argparse
from utils.data_import import import_data_from_profit_chart, add_data_import_args, import_data_from_csv, aggregate_data_from_csv
from utils.model_export import generate_language_model, add_generate_language_args
from utils.run_scenarios import run_scenarios, add_run_scenarios_args, summarize_scenarios
from utils.run_scenarios import rerun_scenarios
from server import start_server, add_server_args
from models import migrate_tables

command_parser = argparse.ArgumentParser(
    description='pyAutoTrader - Universal Python Automatic Trading Bot - Utils CLI')

command_parser.add_argument('command',
                            metavar='command',
                            type=str,
                            choices=['import_data_from_profit_chart_into_metatrader',
                                     'generate_code',
                                     'run_scenarios',
                                     'migrate_tables',
                                     'import_data_from_csv',
                                     'summarize_scenarios',
                                     'start_server',
                                     'aggregate_data_from_csv',
                                     'rerun_scenarios'],
                            help="""
                            Command to be performed by CLI, can be: 
                                 [import_data_from_profit_chart_into_metatrader, 
                                  generate_code, 
                                  run_scenarios,
                                  migrate_tables,
                                  import_data_from_csv, 
                                  summarize_scenarios,
                                  start_server,
                                  aggregate_data_from_csv]""")

add_data_import_args(command_parser)
add_generate_language_args(command_parser)
add_run_scenarios_args(command_parser)
add_server_args(command_parser)

args = command_parser.parse_args()

if __name__ == '__main__':
    if args.command == 'import_data_from_profit_chart_into_metatrader':
        import_data_from_profit_chart(args)
    if args.command == 'generate_code':
        generate_language_model(args)
    if args.command == 'run_scenarios':
        run_scenarios(args)
    if args.command == 'summarize_scenarios':
        summarize_scenarios(args)
    if args.command == 'start_server':
        start_server(args)
    if args.command == 'migrate_tables':
        migrate_tables(args)
    if args.command == 'import_data_from_csv':
        import_data_from_csv(args)
    if args.command == 'aggregate_data_from_csv':
        aggregate_data_from_csv(args)
    if args.command == 'rerun_scenarios':
        rerun_scenarios()
