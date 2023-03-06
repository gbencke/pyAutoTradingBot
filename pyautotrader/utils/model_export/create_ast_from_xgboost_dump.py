def process_ast_node_for_features(current_node, current_booster, path, generated_features):
    if current_node['node_type'] == 'node':
        process_ast_node_for_features(
            current_booster['nodes'][current_node['result']['yes']],
            current_booster,
            path + [{'result': 'yes', 'condition': current_node['condition']}], generated_features)
        process_ast_node_for_features(
            current_booster['nodes'][current_node['result']['no']],
            current_booster,
            path + [{'result': 'no', 'condition': current_node['condition']}], generated_features)
    if current_node['node_type'] == 'leaf':
        current_line = ''
        for current_condition in path:
            generated_features.append(
                current_condition['condition']['variable'])


def get_features_from_ast(ast):
    features_to_return = []
    for current_booster in ast:
        process_ast_node_for_features(current_booster['nodes']
                                      [0], current_booster, [], features_to_return)
    features_to_return = list(set(features_to_return))
    features_to_return.sort()
    return features_to_return


def create_ast_from_xgboost_dump(file_to_read):
    current_booster = None
    generated_boosters = []

    def read_dump_file():
        with open(file_to_read) as f:
            return f.readlines()

    def process_booster(current_booster):
        nodes = {}
        for current_line in current_booster['raw_lines']:
            c_line = current_line.strip()
            c_line = c_line.split(':')
            node_number = int(c_line[0])
            c_line = c_line[1]
            if ' ' in c_line:
                node_type = 'node'
                c_line = c_line.split(" ")

                condition = c_line[0]
                condition = condition.strip('[')
                condition = condition.strip(']')
                operator = '<' if '<' in condition else '>'
                condition = condition.split(operator)
                variable = condition[0]
                value = condition[1]
                condition = {
                    'variable': variable,
                    'operator': operator,
                    'value': float(value)
                }

                result = c_line[1]
                result = result.replace('yes=', '')
                result = result.replace('no=', '')
                result = result.replace('missing=', '')
                result = result.split(',')
                result = {
                    'yes': int(result[0]),
                    'no': int(result[1]),
                    'missing': int(result[2]),
                }
            else:
                condition = None
                node_type = 'leaf'
                result = float(c_line.replace('leaf=', ''))
            nodes[node_number] = {
                'node_type': node_type,
                'result': result,
                'condition': condition,
            }
        current_booster['nodes'] = nodes
        generated_boosters.append(current_booster)

    def create_booster(current_line):
        booster_number = int(current_line.replace(
            "booster[", "").replace("]:", ""))
        new_booster = dict()
        new_booster = {"booster": booster_number, 'raw_lines': []}
        return new_booster

    dump_file_lines = read_dump_file()
    dump_file_lines = [x.strip() for x in dump_file_lines]
    for current_line in dump_file_lines:
        if current_booster is None and not current_line.startswith('booster'):
            raise ValueError('Incorrect format for XGBoost dump file...')
        if current_booster is None:
            current_booster = create_booster(current_line)
            continue
        if not current_booster is None:
            if current_line.startswith('booster'):
                process_booster(current_booster)
                current_booster = create_booster(current_line)
            else:
                current_booster['raw_lines'].append(current_line)

    process_booster(current_booster)
    return generated_boosters
