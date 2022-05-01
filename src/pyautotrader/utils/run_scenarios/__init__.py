from .run_scenarios import run_scenarios, summarize_scenarios
from .rerun_scenarios import rerun_scenarios


def add_run_scenarios_args(command_parser):
    command_parser.add_argument('--minimum-interactions',
                                metavar='minimum_interactions',
                                dest='minimum_interactions',
                                type=str,
                                required=False,
                                help='Model to use in order to generate the source files. (Required for generate_code command)')
