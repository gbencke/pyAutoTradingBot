import sys
import os
from pyautotrader.utils.model_export import create_ast_from_xgboost_dump, export_model_python

if __name__ == '__main__':
    ast = create_ast_from_xgboost_dump(sys.argv[1])
    python_script_name = 'process_long'
    export_model_python(ast, python_script_name, os.path.join(
        os.path.dirname(__file__), python_script_name + '.py'), 0.5)

    ast = create_ast_from_xgboost_dump(sys.argv[2])
    python_script_name = 'process_short'
    export_model_python(ast, python_script_name, os.path.join(
        os.path.dirname(__file__), python_script_name + '.py'), 0.5)
