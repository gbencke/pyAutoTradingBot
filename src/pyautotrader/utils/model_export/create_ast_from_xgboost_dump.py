def create_ast_from_xgboost_dump(file_to_read):
    current_booster = None
    generated_boosters = []

    def read_dump_file():
        with open(file_to_read) as f:
            return f.readlines()

    def process_booster():
        generated_boosters.append(current_booster)

    def create_booster(current_line):
        new_booster = {
            "booster": current_line.replace("booster[", "").replace("]:", "")
        }
        new_booster['raw_lines'] = []
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
                process_booster()
                current_booster = create_booster(current_line)
            else:
                current_booster['raw_lines'].append(current_line)

    return generated_boosters
