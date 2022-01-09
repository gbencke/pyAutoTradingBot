from .create_ast_from_xgboost_dump import create_ast_from_xgboost_dump, get_features_from_ast


def initialize_variable(var_name):
    ret = ''

    current_var_name = var_name

    if var_name == 'current_bar_in_date':
        return 'current_bar_in_date:=0;'

    if var_name == 'previous_close':
        return 'previous_close:=((CloseD(1) / current_open) - 1) * 100;'

    if var_name == 'previous_high':
        return 'previous_high:=((HighD(1) / current_open) - 1) * 100;'

    if var_name == 'previous_low':
        return 'previous_low:=((LowD(1) / current_open) - 1) * 100;'

    if var_name == 'previous_open':
        return 'previous_open:=((OpenD(1) / current_open) - 1) * 100;'

    if var_name == 'x11_high_slope':
        return 'x11_high_slope:=0;'

    if var_name == 'x11_low_slope':
        return 'x11_low_slope:=0;'

    if var_name == 'x11_close_slope':
        return 'x11_close_slope:=0;'

    if var_name == 'x11_volume_slope':
        return 'x11_volume_slope:=0;'

    for x in range(12):
        i = 12-x
        if var_name == f'x{x}_body':
            ret = ''
            ret += f' if open[{i}] > close[{i}] then '
            ret += f' x{x}_body := ((open[{i}] / close[{i}]) - 1) * 100'
            ret += f' else '
            ret += f' x{x}_body := ((close[{i}] / open[{i}]) - 1) * 100;'
            return ret
        if var_name == f'x{x}_close':
            return f"x{x}_close:=((close[{i}]/current_open)-1)*100;"

        if var_name == f'x{x}_ema144':
            return f"x{x}_ema144:=(((MediaExp(144,Close)[{i}])/current_open)-1)*100;"

        if var_name == f'x{x}_ema144_close':
            return f"x{x}_ema144_close:=(((MediaExp(144,Close)[{i}])/close[{i}])-1)*100;"

        if var_name == f'x{x}_ema21':
            return f"x{x}_ema21:=(((MediaExp(21,Close)[{i}])/current_open)-1)*100;"

        if var_name == f'x{x}_ema21_close':
            return f"x{x}_ema21_close:=(((MediaExp(21,Close)[{i}])/close[{i}])-1)*100;"

        if var_name == f'x{x}_ema233':
            return f"x{x}_ema233:=(((MediaExp(233,Close)[{i}])/current_open)-1)*100;"

        if var_name == f'x{x}_ema233_close':
            return f"x{x}_ema233_close:=(((MediaExp(233,Close)[{i}])/close[{i}])-1)*100;"

        if var_name == f'x{x}_ema55':
            return f"x{x}_ema55:=(((MediaExp(55,Close)[{i}])/current_open)-1)*100;"

        if var_name == f'x{x}_ema55_close':
            return f"x{x}_ema55_close:=(((MediaExp(55,Close)[{i}])/close[{i}])-1)*100;"

        if var_name == f'x{x}_ema9':
            return f"x{x}_ema9:=(((MediaExp(9,Close)[{i}])/current_open)-1)*100;"

        if var_name == f'x{x}_ema9_close':
            return f"x{x}_ema9_close:=(((MediaExp(9,Close)[{i}])/close[{i}])-1)*100;"

        if var_name == f'x{x}_height':
            return f"x{x}_height:=(((High[{i}]/current_open)-1)*100) - (((Low[{i}]/current_open)-1)*100);"

        if var_name == f'x{x}_high':
            return f"x{x}_high:=(((High[{i}]/current_open)-1)*100);"

        if var_name == f'x{x}_low':
            return f"x{x}_low:=(((Low[{i}]/current_open)-1)*100);"

        if var_name == f'x{x}_open':
            return f"x{x}_open:=(((Open[{i}]/current_open)-1)*100);"

        if var_name == f'x{x}_previous_close':
            return f"x{x}_previous_close:=(((CloseD(1)/close[{i}])-1)*100);"

        if var_name == f'x{x}_previous_high':
            return f"x{x}_previous_high:=(((HighD(1)/close[{i}])-1)*100);"

        if var_name == f'x{x}_previous_low':
            return f"x{x}_previous_low:=(((LowD(1)/close[{i}])-1)*100);"

        if var_name == f'x{x}_previous_open':
            return f"x{x}_previous_open:=(((OpenD(1)/close[{i}])-1)*100);"

        if var_name == f'x{x}_roc':
            return f"x{x}_roc:=(((open[{i}]/close[{i}])-1)*100);"

        if var_name == f'x{x}_volume':
            return f"x{x}_volume:=(((volume[{i}] / current_volume) -1)*100);"

        if var_name == f'x{x}_vwap':
            return f"x{x}_vwap:=(((vwap(1)[{i}] / current_open) - 1) *100);"

        if var_name == f'x{x}_x{x-1}_close':
            return f"x{x}_x{x-1}_close:=(((close[{i}] / close[{i-1}]) - 1) *100);"

        if var_name == f'x{x}_x{x-1}_high':
            return f"x{x}_x{x-1}_high:=(((high[{i}] / high[{i-1}]) - 1) *100);"

        if var_name == f'x{x}_x{x-1}_low':
            return f"x{x}_x{x-1}_low:=(((low[{i}] / low[{i-1}]) - 1) *100);"

    raise ValueError(f'variable {var_name} not found... Error')


def indent(str, ident_to_apply):
    ret = '\n'.join([(' ' * (ident_to_apply * 4)) +
                    x for x in str.split('\n')])
    return ret


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
    generated_code += ['', indent(f"function {model_name}: Float;", current_indent),
                       indent("var", current_indent),
                       indent("final_res: Float;", current_indent + 1),
                       indent("current_volume: Float;", current_indent + 1),
                       indent("current_open: Float;", current_indent + 1)]

    generated_code += [indent(f'{x} : Float;', current_indent + 1)
                       for x in get_features_from_ast(ast)]

    generated_code += [indent("begin", current_indent),
                       indent(f"final_res:={initial_bias};",
                              current_indent + 1),
                       indent(f"current_volume:=volume[1];", current_indent+1),
                       indent(f"current_open:=open[1];", current_indent+1)]

    generated_code += [indent(initialize_variable(x), current_indent + 1)
                       for x in get_features_from_ast(ast)]

    counter = 0
    for current_booster in ast:
        generated_code.append(
            indent(f"{{ Processing Booster:{current_booster['booster']}}}", current_indent + 1))
        transverse_tree_for_profitchart(
            current_booster, generated_code, current_indent)
        generated_code.append(indent('\n', current_indent))
        counter += 1
        if counter > 40:
            break

    generated_code.append(
        indent(f"Result:= final_res;", current_indent + 1))
    generated_code.append(indent("end;\n", current_indent))


def generate_header(generated_code):
    pass


def generate_global_variables(generated_code, current_indent):
    generated_code.append('const')
    generated_code.append(indent('ESTADO_NEUTRO = 0;', current_indent+1))
    generated_code.append(indent('ESTADO_COMPRADO = 1;', current_indent+1))
    generated_code.append(indent('ESTADO_VENDIDO = 2;', current_indent+1))
    generated_code.append(indent('ESTADO_ZERADO = 3;', current_indent+1))
    generated_code.append('var')
    generated_code.append(indent('Resultado: Integer;', current_indent + 1))
    generated_code.append(indent('EstadoAtual: Integer;', current_indent + 1))
    generated_code.append(indent('LastPlot: Float;', current_indent + 1))


def generate_indicator_code(generated_code, minimum_time, minimum_day, decision_boundary):
    generated_code.append(indent(f'if Date = 1211116 then', 1))
    generated_code.append(indent(f'begin', 1))
    generated_code.append(
        indent(f'if (Time < {minimum_time}) then begin EstadoAtual:=ESTADO_NEUTRO; LastPlot:=0; end;', 1+1))
    generated_code.append(
        indent(f'if (Time >= {minimum_time}) then ', 1+1))
    generated_code.append(indent(f'begin', 1+1))
    generated_code.append(indent(f'Plot(ShouldShort);', 3))
    generated_code.append(indent(f'Plot2(ShouldLong);', 3))
    generated_code.append(indent(f'end;', 1+1))
    generated_code.append(indent(f'end;', 1))


def export_model_profitchart(ast_short, ast_long, output_file_name, initial_bias, decision_boundary, minimum_day, minimum_time):
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

    generate_indicator_code(generated_code, minimum_time,
                            minimum_day, decision_boundary)

    generated_code.append('end;')

    with open(output_file_name, 'w') as out:
        out.writelines([x + '\n' for x in generated_code])


def generate_profitchart_language_model(args):
    ast_short = create_ast_from_xgboost_dump(args.modelshort)
    ast_long = create_ast_from_xgboost_dump(args.modellong)
    export_model_profitchart(
        ast_short, ast_long, args.savemodelto, 0.5, 0.4, 1210921, 930)
