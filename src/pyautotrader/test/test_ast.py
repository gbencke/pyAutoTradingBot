import sys
from pyautotrader.utils.model_export import create_ast_from_xgboost_dump

if __name__ == '__main__':
    print(create_ast_from_xgboost_dump(sys.argv[1]))
