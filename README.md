# pyAutoTrader

The program aims to function as an automated trading bot with capabilities for training ML models and executing trades. It operates in two modes: training and inference. In the training mode, it runs a series of Python notebooks to clean, normalize, and train data using the XGBoost algorithm (Boosted Gradient Trees). In the inference mode, it operates as a web server where features can be posted, and it returns whether it's a Long or Short operation.

# Training Models

## Data Model

For both training and inference, we utilize the "DataFrame" model, consisting of a candlestick, its previous 11 candles, and corresponding indicators (previous trading day OHLC, Moving Averages, etc.).

During XGBoost model training, we prepare this dataframe for each candle. Additionally, when inferring whether a certain candle represents a Long or Short Trade Signal, we POST this dataframe to the FastAPI server.

Below is a graphical representation of the data within the dataframe.

![Alt text](./ML.Frame.Example.png)

Furthermore, below are the fields used to represent the aforementioned dataframe:

```python
FULL_FEATURE_LIST = list(
{'x0_roc', 'x0_previous_high', 'x0_previous_low', 'x0_previous_close', 'x0_previous_open', 'x0_ema9_close',
'x0_ema21_close', 'x0_ema55_close', 'x0_ema144_close', 'x0_ema233_close', 'x1_roc', 'x1_previous_high',
'x1_previous_low', 'x1_previous_close', 'x1_previous_open', 'x1_ema9_close', 'x1_ema21_close', 'x1_ema55_close',
'x1_ema144_close', 'x1_ema233_close', 'x1_x0_close', 'x1_x0_high', 'x1_x0_low', 'x2_roc', 'x2_previous_high',
'x2_previous_low', 'x2_previous_close', 'x2_previous_open', 'x2_ema9_close', 'x2_ema21_close', 'x2_ema55_close',
'x2_ema144_close', 'x2_ema233_close', 'x2_x1_close', 'x2_x1_high', 'x2_x1_low', 'x3_roc', 'x3_previous_high',
'x3_previous_low', 'x3_previous_close', 'x3_previous_open', 'x3_ema9_close', 'x3_ema21_close', 'x3_ema55_close',
'x3_ema144_close', 'x3_ema233_close', 'x3_x2_close', 'x3_x2_high', 'x3_x2_low', 'x4_roc', 'x4_previous_high',
'x4_previous_low', 'x4_previous_close', 'x4_previous_open', 'x4_ema9_close', 'x4_ema21_close', 'x4_ema55_close',
'x4_ema144_close', 'x4_ema233_close', 'x4_x3_close', 'x4_x3_high', 'x4_x3_low', 'x5_roc', 'x5_previous_high',
'x5_previous_low', 'x5_previous_close', 'x5_previous_open', 'x5_ema9_close', 'x5_ema21_close', 'x5_ema55_close',
'x5_ema144_close', 'x5_ema233_close', 'x5_x4_close', 'x5_x4_high', 'x5_x4_low', 'x6_roc', 'x6_previous_high',
'x6_previous_low', 'x6_previous_close', 'x6_previous_open', 'x6_ema9_close', 'x6_ema21_close', 'x6_ema55_close',
'x6_ema144_close', 'x6_ema233_close', 'x6_x5_close', 'x6_x5_high', 'x6_x5_low', 'x7_ema9', 'x7_ema21', 'x7_ema55',
'x7_ema144', 'x7_ema233', 'x7_ema9', 'x7_ema21', 'x7_ema55', 'x7_ema144', 'x7_ema233', 'x7_open', 'x7_high',
'x7_low', 'x7_close', 'x7_volume', 'x7_open', 'x7_high', 'x7_low', 'x7_close', 'x7_height', 'x7_body', 'x7_roc',
'x7_previous_high', 'x7_previous_low', 'x7_previous_close', 'x7_previous_open', 'x7_ema9_close', 'x7_ema21_close',
'x7_ema55_close', 'x7_ema144_close', 'x7_ema233_close', 'x7_x6_close', 'x7_x6_high', 'x7_x6_low', 'x8_roc',
'x8_previous_high', 'x8_previous_low', 'x8_previous_close', 'x8_previous_open', 'x8_ema9_close', 'x8_ema21_close',
'x8_ema55_close', 'x8_ema144_close', 'x8_ema233_close', 'x8_x7_close', 'x8_x7_high', 'x8_x7_low', 'x9_roc',
'x9_previous_high', 'x9_previous_low', 'x9_previous_close', 'x9_previous_open', 'x9_ema9_close', 'x9_ema21_close',
'x9_ema55_close', 'x9_ema144_close', 'x9_ema233_close', 'x9_x8_close', 'x9_x8_high', 'x9_x8_low', 'x10_roc',
'x10_previous_high', 'x10_previous_low', 'x10_previous_close', 'x10_previous_open', 'x10_ema9_close',
'x10_ema21_close', 'x10_ema55_close', 'x10_ema144_close', 'x10_ema233_close', 'x10_x9_close', 'x10_x9_high',
'x10_x9_low', 'x11_roc', 'x11_previous_high', 'x11_previous_low', 'x11_previous_close', 'x11_previous_open',
'x11_ema9_close', 'x11_ema21_close', 'x11_ema55_close', 'x11_ema144_close', 'x11_ema233_close', 'x11_x10_close',
'x11_x10_high', 'x11_x10_low', 'previous_close', 'previous_high', 'previous_low', 'previous_open', 'x0_ema55',
'x0_ema144', 'x0_ema233', 'x1_ema55', 'x1_ema144', 'x1_ema233', 'x2_ema55', 'x2_ema144', 'x2_ema233', 'x3_ema55',
'x3_ema144', 'x3_ema233', 'x4_ema55', 'x4_ema144', 'x4_ema233', 'x5_ema55', 'x5_ema144', 'x5_ema233', 'x6_ema55',
'x6_ema144', 'x6_ema233', 'x7_ema55', 'x7_ema144', 'x7_ema233', 'x8_ema55', 'x8_ema144', 'x8_ema233', 'x9_ema55',
'x9_ema144', 'x9_ema233', 'x10_ema55', 'x10_ema144', 'x10_ema233', 'x11_ema55', 'x11_ema144', 'x11_ema233',
'x0_body', 'x0_close', 'x0_ema21', 'x0_ema9', 'x0_height', 'x0_high', 'x0_low', 'x0_open', 'x0_volume', 'x10_body',
'x10_close', 'x10_ema21', 'x10_ema9', 'x10_height', 'x10_high', 'x10_low', 'x10_open', 'x10_volume', 'x11_body',
'x11_close', 'x11_close_slope', 'x11_ema21', 'x11_ema9', 'x11_height', 'x11_high', 'x11_high_slope', 'x11_low',
'x11_low_slope', 'x11_open', 'x11_volume', 'x11_volume_slope', 'x1_body', 'x1_close', 'x1_ema21', 'x1_ema9',
'x1_height', 'x1_high', 'x1_low', 'x1_open', 'x1_volume', 'x2_body', 'x2_close', 'x2_ema21', 'x2_ema9',
'x2_height', 'x2_high', 'x2_low', 'x2_open', 'x2_volume', 'x3_body', 'x3_close', 'x3_ema21', 'x3_ema9',
'x3_height', 'x3_high', 'x3_low', 'x3_open', 'x3_volume', 'x4_body', 'x4_close', 'x4_ema21', 'x4_ema9',
'x4_height', 'x4_high', 'x4_low', 'x4_open', 'x4_volume', 'x5_body', 'x5_close', 'x5_ema21', 'x5_ema9',
'x5_height', 'x5_high', 'x5_low', 'x5_open', 'x5_volume', 'x6_body', 'x6_close', 'x6_ema21', 'x6_ema9',
'x6_height', 'x6_high', 'x6_low', 'x6_open', 'x6_volume', 'x7_body', 'x7_close', 'x7_ema21', 'x7_ema9',
'x7_height', 'x7_high', 'x7_low', 'x7_open', 'x7_volume', 'x8_body', 'x8_close', 'x8_ema21', 'x8_ema9',
'x8_height', 'x8_high', 'x8_low', 'x8_open', 'x8_volume', 'x9_body', 'x9_close', 'x9_ema21', 'x9_ema9',
'x9_height', 'x9_high', 'x9_low', 'x9_open', 'x9_volume', 'current_bar_in_date', "x0_vwap", "x1_vwap", "x2_vwap",
"x3_vwap", "x4_vwap", "x5_vwap", "x6_vwap", "x7_vwap", "x8_vwap", "x9_vwap", "x10_vwap", "x11_vwap"})
```

Please notice that the quotes have been normalized, so instead of having a quote with the absolute price, we use the percentual variation in relation to the close price of the target candlestick

## Hyperparameters and Model Output

XGBoost is a algorithm that generates a decision tree that tries to predict if when certain numerical features are within a certain range, they present a "probability"  that a certain outcome is possible or not, so, something like the model generated below:

```python
def process_long(cond):
    final_res=0.5

    final_res+=(0.0972686261 if (cond['x9_previous_high']<1.76160121) and (cond['x11_height']<0.148379788) and (cond['x11_height']<-0.145042777) and (cond['x11_height']<-0.21536532) and (cond['x3_previous_low']<-1.71445251) else 0.0 )
    final_res+=(-0.123476721 if (cond['x9_previous_high']<1.76160121) and (cond['x11_height']<0.148379788) and (cond['x11_height']<-0.145042777) and (cond['x11_height']<-0.21536532) and not (cond['x3_previous_low']<-1.71445251) else 0.0 )
    final_res+=(-0.0554996096 if (cond['x9_previous_high']<1.76160121) and (cond['x11_height']<0.148379788) and (cond['x11_height']<-0.145042777) and not (cond['x11_height']<-0.21536532) and (cond['x7_height']<-0.173613116) else 0.0 )
    final_res+=(-0.295924634 if (cond['x9_previous_high']<1.76160121) and (cond['x11_height']<0.148379788) and (cond['x11_height']<-0.145042777) and not (cond['x11_height']<-0.21536532) and not (cond['x7_height']<-0.173613116) else 0.0 )
    final_res+=(-0.421801716 if (cond['x9_previous_high']<1.76160121) and (cond['x11_height']<0.148379788) and not (cond['x11_height']<-0.145042777) and (cond['x2_previous_close']<-0.232456565) and (cond['x4_ema55_close']<-0.313315094) else 0.0 )

    return final_res
```

Where we can see that each range of values in the features, add or subtract possibilities for the final response be positive ( > 0 ) or negative ( < 0 )

In order for us to run the training, we need some parameters to be set as env. parameters which will inform the location of the input and output data, the accepted target and loss of the model and many other parameters:

```bash
TRADE_DAY_START=900 # The Time in which the trading day starts, in this case: 09:00 AM
MINIMUM_TIME=930 # When it is safe to start to execute trading operations ( Avoid Opening Orders )
MAXIMUM_TIME=1350 # When we should stop the trading day, in this case: 1:50 PM
MINIMUM_DATE_DATAFRAME=20180301 # The Minimun date to start the trading day, ( in this case, 2018-03-01 )
MINIMUM_DATE_TRADE=20180315 # When we should start training? ( in this case, 2018-03-15 )
MAX_TRAIN_DATE=20210830 # When we should stop training? ( in this  case, 2021-08-30 )
MAX_TRADE_DURATION=24 # The Max duration of a trade operation ( in candles )
CURRENT_TARGET=0.8 # The Current Gain Target, in percent
CURRENT_STOP=0.4 # The Current Maximum Loss, in percent
DECISION_BOUNDARY=0.4 # The score from the XGBoost Model, from which we should consider a Long or Short Signal
CURRENT_EXCHANGE='B3' # The Exchange Code, right now it is only supported Brazilian B3 
CURRENT_ASSET='WDO' # The Asset Code, Dollar Futures mini-contracts
CURRENT_TIMEFRAME='5Min' # The current time frame 
NUM_TREES=120 # The Max number of Decision trees in the XGBoost 
TREE_DEPTH=5 # The Maximum Depth for each decision tree
WEIGHT_RATIO=0.8 # These is used to balance the target classes
CURRENT_DAILY_FILE_CSV='WDO$Daily.csv' # The daily input file with the quotes in OHLC format
CURRENT_5MIN_FILE_CSV='WDO$M5.csv' # The 5min input file with the quotes in OHLC format
DATA_INPUT_DIR=../00.data/input # The folder containing input data
DATA_OUTPUT_DIR=../00.data/output # The folder for the output data
IS_HYPER_PARAMETER_SEARCH=False # Are we going to use hyper parameter search?
NUM_FOLDS_CROSSVALIDATION=10 # How many times should we shuffle the input data and cross fold it between train and validation?
DATA_HYPERPARAMETERS_DIR=../00.data/hyperparameters # The folder for the hyperparameters search result
```
After the environment variables have been set, we can then run training with the following command in the root folder:

```shell
poetry run python -m pyautotrader run_scenarios --minimum-interactions 1 
```

This will run all the training notebooks below, which are available in ```models/strategies/B3/WDOL/02.candle_strategy```

* **02.candle_strategy_0100_create_dataframe.ipynb**: This notebook takes the raw OHLC quotes from ```models/strategies/B3/WDOL/00.data/input``` and generates the dataframes that will be used during training
* **02.candle_strategy_0200_create_xgbooster.ipynb**: From the dataframes generated in the previous step, we create the XGBoost Models.
* **02.candle_strategy_0300_find_decision_boundary.ipynb**: With the generated models, we test them against the training data
* **02.candle_strategy_0400_forward_testing.ipynb**: And after the testing with the training data, we test then with the test data ( not yet seen by the model), and generate the python file which is the model itself
* **02.candle_strategy_0500_check_predict.ipynb**: After we created the python file, we can then use the API Server to test it against the data that we have, in order to check if the API and 
* **02.candle_strategy_0600_analyse_test_trades.ipynb**: This is a simple analytics notebook with several charts regarding the best trading hours, day of the week and so on.

and generate several artefacts which will be available in the directory indicated by ```DATA_OUTPUT_DIR```:

| Artefact                                                                                                                                                                 | Description                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [B3.WDO.5Min.80.40.check_model.xlsx](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.check_model.xlsx)                     | XLSX file summarising the signals generated                                               |
| [B3.WDO.5Min.80.40.hist_long.png](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.hist_long.png)                           | Histogram of predicted XGBoost scores for each candlestick for Long trades                |
| [B3.WDO.5Min.80.40.hist_short.png](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.hist_short.png)                         | Histogram of predicted XGBoost scores for each candlestick for Long trades                |
| [B3.WDO.5Min.80.40.hyperparameters_long.xlsx](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.hyperparameters_long.xlsx)   | Most significant features for the long model                                              | 
| [B3.WDO.5Min.80.40.hyperparameters_short.xlsx](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.hyperparameters_short.xlsx) | Most significant features for the short model                                             |
| [B3.WDO.5Min.80.40.long.train.score.txt](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.long.train.score.txt)             | The score of the model generated for the long operations                                  |
| [B3.WDO.5Min.80.40.parameters.pickle](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.parameters.pickle)                   | A pickle file containing the python parameters dictionary                                 |
| [B3.WDO.5Min.80.40.predicts.xlsx](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.predicts.xlsx)                           | XLSX file containing the predicts for the test dataset                                    |
| [B3_WDO_5Min_80_40_process_long.py](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3_WDO_5Min_80_40_process_long.py)                       | A python file that implements the long model                                              |
| [B3_WDO_5Min_80_40_process_short.py](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3_WDO_5Min_80_40_process_short.py)                     | A python file that implements the short model                                             |
| [B3.WDO.5Min.80.40.raw.pickle](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.raw.pickle)                                 | A pickle file containing a list of python dictionaries containing ALL the dataframes data |
| [B3.WDO.5Min.80.40.short.train.score.txt](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.short.train.score.txt)           | The score of the model generated for the short operations                                 |
| [B3.WDO.5Min.80.40.test_trades.xlsx](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.test_trades.xlsx)                     | The trades executed during the test dataset                                               |
| [B3.WDO.5Min.80.40.trades.xlsx](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.trades.xlsx)                               | The trades executed during the train dataset                                              |
| [B3.WDO.5Min.80.40.xgboostlongmodel.pickle](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.xgboostlongmodel.pickle)       | The XGBoost long model in pickle format                                                   |
| [B3.WDO.5Min.80.40.xgboostlongmodel.txt](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.xgboostlongmodel.txt)             | A text dump of the XGBoost long model                                                     |
| [B3.WDO.5Min.80.40.xgboostshortmodel.pickle](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.xgboostshortmodel.pickle)     | The XGBoost short model in pickle format                                                  |
| [B3.WDO.5Min.80.40.xgboostshortmodel.txt](https://s3.amazonaws.com/gbencke.pyautocrypto.example/20240220230332.266159/B3.WDO.5Min.80.40.xgboostshortmodel.txt)           | A text dump of the XGBoost short model                                                    |

After the artefacts above have been generated, we can then serve them using the inference API that can be seen below.

## Generating and evaluating multiple models with different hyperparameters

It is important to notice that the models might vary a lot depending on the hyperparameters, so it is extremely important to tune those hyperparameters and verify which ones are the most performative.

We can run train several models at the same time, the script:```run_scenarios.sh``` is a good example of that. When the scenarios are finished, we can then summarize all the generated models and plot a chart of the best models.

We can see here the summary of the strategies: [strategy_summary.xlsx](https://s3.amazonaws.com/gbencke.pyautocrypto.example/strategy_summary.xlsx)

And a chart with the accumulated P/L of the best model:

![P/L Chart](https://s3.amazonaws.com/gbencke.pyautocrypto.example/002018.20240318080231.47817.png)

# Serving and inferring models

At these point, we have run several models, with several different hyperparameters and now we need to use it in a bot.

Despite its name, this repo does not contain a full trading bot that can receive real time quotes, infer them and send sell / buy orders to a real exchange. This role in our case was assigned to the [ProfitChartBot](https://github.com/gbencke/ProfitChartBot) project which scraps the screen of a real trading software: ProfitChart and then sends the quote and calculate a signal from the provided quote.

We can see below a image of the [ProfitChartBot](https://github.com/gbencke/ProfitChartBot) working: 

![Alt text](./ProfitDemoBot.png)

And we can also check this video demo: [ProfitChartBot Demo](https://s3.amazonaws.com/gbencke.pyautocrypto.example/2022.04.07.ProfitChartBotDemo.mp4)

We can start the inference api using the ```run_server.sh``` script or just running:
```bash
poetry run python -m pyautotrader  start_server --sqlalchemy-connection-string sqlite:///data//pyautotrader.db  --xgboost-model $PYAUTOTRADER_MODEL
```
where $PYAUTRADER_MODEL is the model that is going to be served through the API.

The API has 3 endpoints:

#### GET - "/predict/{exchange}/{asset}/{timeframe}/{date}/{time}/"
This endpoint returns the score from the model for a certain candle in a certain date / time / asset / exchange. It is important to notice that it is required that the data for this candle should already be posted in the database that is being served.

#### GET - "/parameters/"
This endpoint returns the dictionary of parameters that is being used by the model.

#### POST "/quotes/{exchange}/{asset}/{timeframe}/"
This endpoint writes to the database the data regarding a certain candlestick in a certain exchange / asset / timeframe

# Instalation

This project uses poetry, and after the repo has been cloned, it is necessary to run ```poetry install``` to create the virtual environment and install all dependencies on it.

# Pending Improvements

There are many improvements to be made, including, but not limited to:
* Add an API in order to perform automatic training of new models
* Create a database for the generated model artefacts, instead of relying on the filesystem.
* Allow dynamic indicators and define the length of relevant previous candlesticks during runtime
And many more...