from .export_model_python import generate_python_language_model
from .export_model_profitchart import generate_profitchart_language_model


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
