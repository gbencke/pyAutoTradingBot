from .create_ast_from_xgboost_dump import create_ast_from_xgboost_dump, get_features_from_ast


def indent(str, ident_to_apply):
    return (' ' * (ident_to_apply * 4)) + str


def process_ast_node_for_profitchart(current_node, current_booster, path, generated_trees, current_indent):
    if current_node['node_type'] == 'node':
        process_ast_node_for_profitchart(
            current_booster['nodes'][current_node['result']['yes']],
            current_booster,
            path + [{'result': 'yes', 'condition': current_node['condition']}], generated_trees, current_indent)
        process_ast_node_for_profitchart(
            current_booster['nodes'][current_node['result']['no']],
            current_booster,
            path + [{'result': 'no', 'condition': current_node['condition']}], generated_trees, current_indent)
    if current_node['node_type'] == 'leaf':
        current_line = ''
        for current_condition in path:
            condition_py = ''
            if current_condition['result'] == 'no':
                condition_py += 'not '
            condition_py += '('
            condition_py += current_condition['condition']['variable']
            condition_py += current_condition['condition']['operator']
            cur_value = str(current_condition['condition']['value'])
            condition_py += cur_value if not 'e-' in cur_value else '0.0'
            condition_py += ') and '
            current_line += condition_py
        current_line = current_line[:-5]
        cur_res = str(current_node['result'])
        cur_res = cur_res if not 'e-' in cur_res else '0.0'
        current_line = indent(
            f"if {current_line} then final_res:=final_res + ({cur_res});", current_indent + 1)
        generated_trees.append(current_line)


def transverse_tree_for_profitchart(current_booster, generated_code, current_indent):
    process_ast_node_for_profitchart(
        current_booster['nodes'][0], current_booster, [], generated_code, current_indent)


def export_model(ast, model_name, output_file_name, initial_bias, decision_boundary, generated_code, current_indent):
    generated_code += ['', indent(f"function {model_name}: Boolean;", current_indent),
                       indent("var", current_indent),
                       indent("final_res: Float;", current_indent + 1)]

    generated_code += [indent(f'{x} : Float;', current_indent + 1)
                       for x in get_features_from_ast(ast)]

    generated_code += [indent("begin", current_indent),
                       indent(f"final_res:={initial_bias};", current_indent + 1)]

    for current_booster in ast:
        generated_code.append(
            indent(f"{{ Processing Booster:{current_booster['booster']}}}", current_indent + 1))
        transverse_tree_for_profitchart(
            current_booster, generated_code, current_indent)
        generated_code.append(indent('\n', current_indent))

    generated_code.append(
        indent(f"Result:=(final_res > {decision_boundary});", current_indent + 1))
    generated_code.append(indent("end;\n", current_indent))


def generate_header(generated_code):
    pass


def generate_global_variables(generated_code, current_indent):
    generated_code.append('var')
    generated_code.append(indent('Resultado: Integer;', current_indent + 1))


def export_model_profitchart(ast_short, ast_long, output_file_name, initial_bias, decision_boundary):
    generated_code = []

    generate_header(generated_code)

    generate_global_variables(generated_code, 0)

    export_model(ast_short, "ShouldShort", output_file_name,
                 initial_bias, decision_boundary,
                 generated_code, 1)

    export_model(ast_long, "ShouldLong", output_file_name,
                 initial_bias, decision_boundary,
                 generated_code, 1)

    generated_code.append('begin')

    generated_code.append('end;')

    with open(output_file_name, 'w') as out:
        out.writelines([x + '\n' for x in generated_code])


def generate_profitchart_language_model(args):
    ast_short = create_ast_from_xgboost_dump(args.modelshort)
    ast_long = create_ast_from_xgboost_dump(args.modellong)
    export_model_profitchart(ast_short, ast_long, args.savemodelto, 0.5, 0.4)
