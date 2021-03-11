# covid-19-nds-lambda
AWS Lambda function to parse the covid-19 data of the state Niedersachsen (Germany).

Takes the `GKZ` as only parameter and returns the recent 8 values for `7-Tagesinzidenz pro 100.000 Einwohner`.

You may use `list_gkz.py` to find your `GKZ`.