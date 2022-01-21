from .run_scenarios import run_scenarios


def add_run_scenarios_args(command_parser):
    command_parser.add_argument('--minimum-interactions',
                                metavar='minimum_interactions',
                                dest='minimum_interactions',
                                type=str,
                                required=False,
                                help='Model to use in order to generate the source files. (Required for generate_code command)')
    command_parser.add_argument('--minimum-time',
                                metavar='minimum_time',
                                dest='minimum_time',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
    command_parser.add_argument('--maximum-time',
                                metavar='maximum_time',
                                dest='maximum_time',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
    command_parser.add_argument('--minimum-date-dataframe',
                                metavar='minimum_date_dataframe',
                                dest='minimum_date_dataframe',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
    command_parser.add_argument('--minimum-date-trade',
                                metavar='minimum_date_trade',
                                dest='minimum_date_trade',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
    command_parser.add_argument('--max-train-date',
                                metavar='max_train_date',
                                dest='max_train_date',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
    command_parser.add_argument('--max-train-duration',
                                metavar='max_train_duration',
                                dest='max_train_duration',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
    command_parser.add_argument('--current-target',
                                metavar='current_target',
                                dest='current_target',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
    command_parser.add_argument('--current-stop',
                                metavar='current_stop',
                                dest='current_stop',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
    command_parser.add_argument('--decision-boundary',
                                metavar='decision_boundary',
                                dest='decision_boundary',
                                type=str,
                                required=False,
                                help=' (Required for run_scenarios command)')
