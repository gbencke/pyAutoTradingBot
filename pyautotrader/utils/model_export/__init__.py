import sys
from .export_model_python import generate_python_language_model, export_model_python
from .export_model_profitchart import generate_profitchart_language_model
from .create_ast_from_xgboost_dump import create_ast_from_xgboost_dump


def add_generate_language_args(command_parser):
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


def generate_language_model(args):
    if args.language is None:
        print('Missing language to export the model to')
        sys.exit(1)
    if args.savemodelto is None:
        print('Missing the destination file for the language model.')
        sys.exit(1)
    if args.language == 'python':
        if args.model is None:
            print(
                'Missing source XGBoost model dump, to generate the language model from.')
            sys.exit(1)
        if args.pythonfunctionname is None:
            print('Missing the python function name...')
            sys.exit(1)
        generate_python_language_model(args)
    if args.language == 'profitchart':
        if args.modelshort is None:
            print(
                'Missing source XGBoost model dump for the short trades, to generate the language model from.')
            sys.exit(1)
        if args.modellong is None:
            print(
                'Missing source XGBoost model dump for the long trades, to generate the language model from.')
            sys.exit(1)
        generate_profitchart_language_model(args)
