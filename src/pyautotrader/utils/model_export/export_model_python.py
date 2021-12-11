def process_ast_node(current_node, current_booster, path, generated_trees):
    if current_node['node_type'] == 'node':
        process_ast_node(
            current_booster['nodes'][current_node['result']['yes']],
            current_booster,
            path + [{'result': 'yes', 'condition': current_node['condition']}], generated_trees)
        process_ast_node(
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


def transverse_tree(current_booster, generated_trees):
    process_ast_node(current_booster['nodes']
                     [0], current_booster, [], generated_trees)


def export_model_python(ast, code_name, output_file_name):
    generated_code = [f"def {code_name}(cond):", f"    final_res=0.0"]
    for current_booster in ast:
        transverse_tree(current_booster, generated_code)

    generated_code.append("    return final_res")

    with open(output_file_name, 'w') as out:
        out.writelines([x + '\n' for x in generated_code])
