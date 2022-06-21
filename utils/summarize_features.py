import glob
import os
import sys
import pandas as pd

if not 'PYAUTOTRADER_MODEL' in os.environ:
    print('There is a need to define the model in PYAUTOTRADER_MODEL.')
    sys.exit(-1)

model = os.environ['PYAUTOTRADER_MODEL']


current_long_features = ""
current_short_features = ""

SEARCH_PATH = os.path.join(model, "*.hyperparameters_long.xlsx")

for current_file in glob.glob(SEARCH_PATH):
    current_long_features = current_file

SEARCH_PATH = os.path.join(model, "*.hyperparameters_short.xlsx")

for current_file in glob.glob(SEARCH_PATH):
    current_short_features = current_file


long_features = pd.read_excel(current_long_features)
long_features_list = long_features.to_dict('records')
short_features = pd.read_excel(current_short_features)
short_features_list = short_features.to_dict('records')

total_features = long_features_list + short_features_list

cleaned_features = {}
columns_needed = {}

for current_feature in total_features:
    name = current_feature['feature']

    if name.startswith('x') and "_" in name:
        feature_type = "_".join(current_feature['feature'].split("_")[1:])
        column_type = "_".join(current_feature['feature'].split("_")[:1])
        feature_weigth = current_feature['value']
        if feature_type.startswith("x"):
            continue
        if not feature_type in cleaned_features:
            cleaned_features[feature_type] = feature_weigth
        else:
            cleaned_features[feature_type] += feature_weigth
        if not column_type in columns_needed:
            columns_needed[column_type] = feature_weigth
        else:
            columns_needed[column_type] += feature_weigth
        continue

    if not name.startswith('x'):
        feature_weigth = current_feature['value']
        if not name in cleaned_features:
            cleaned_features[name] = feature_weigth
        else:
            cleaned_features[name] += feature_weigth
        continue

    print("erro:" + name)

cleaned_features = [{"feature": x, "weight": cleaned_features[x]}
                    for x in list(cleaned_features.keys())]

columns_needed = [{"feature": x, "weight": columns_needed[x]}
                  for x in list(columns_needed.keys())]

cleaned_features.sort(reverse=True, key=lambda x: x["weight"])
columns_needed.sort(reverse=True, key=lambda x: x["weight"])

df_cleaned_features = pd.DataFrame(cleaned_features)
df_columns_needed = pd.DataFrame(columns_needed)

current_features = current_long_features.replace(
    "hyperparameters_long", "hyperparameters_summarized")

writer = pd.ExcelWriter(current_features, engine='xlsxwriter')

df_cleaned_features.to_excel(writer, sheet_name='features')
df_columns_needed.to_excel(writer, sheet_name='columns')

writer.save()
