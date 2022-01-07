from .create_ast_from_xgboost_dump import create_ast_from_xgboost_dump


def process_ast_node_for_python(current_node, current_booster, path, generated_trees):
    if current_node['node_type'] == 'node':
        process_ast_node_for_python(
            current_booster['nodes'][current_node['result']['yes']],
            current_booster,
            path + [{'result': 'yes', 'condition': current_node['condition']}], generated_trees)
        process_ast_node_for_python(
            current_booster['nodes'][current_node['result']['no']],
            current_booster,
            path + [{'result': 'no', 'condition': current_node['condition']}], generated_trees)
    if current_node['node_type'] == 'leaf':
        current_line = ''
        for current_condition in path:
            condition_py = ''
            if current_condition['result'] == 'no':
                condition_py += 'not '
            condition_py += '('
            condition_py += "cond['" + \
                current_condition['condition']['variable'] + "']"
            condition_py += current_condition['condition']['operator']
            condition_py += str(current_condition['condition']['value'])
            condition_py += ') and '
            current_line += condition_py
        current_line = current_line[:-5]
        current_line = f"    final_res+=({str(current_node['result'])} if {current_line} else 0.0 )  "
        generated_trees.append(current_line)


def transverse_tree_for_python(current_booster, generated_trees):
    process_ast_node_for_python(current_booster['nodes']
                                [0], current_booster, [], generated_trees)


def export_model_python(ast, code_name, output_file_name, base_score):
    generated_code = [f"def {code_name}(cond):", f"    final_res={base_score}"]
    for current_booster in ast:
        generated_code.append(
            f"# Processing Booster:{current_booster['booster']}\n")
        transverse_tree_for_python(current_booster, generated_code)
        generated_code.append('\n\n')

    generated_code.append("    return final_res")

    with open(output_file_name, 'w') as out:
        out.writelines([x + '\n' for x in generated_code])


def generate_python_language_model(args):
    ast = create_ast_from_xgboost_dump(args.model)
    export_model_python(ast, args.pythonfunctionname, args.savemodelto, 0.5)
