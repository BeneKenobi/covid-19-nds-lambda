# covid-19-nds-lambda
AWS Lambda function to parse the covid-19 data of the state Niedersachsen (Germany).

Takes the `GKZ` as only (query-)parameter and returns the recent 8 values for `7-Tagesinzidenz pro 100.000 Einwohner` using AWS API-Gateway.

You may use `list_gkz.py` to find your `GKZ`.

[![CI/CD](https://github.com/BeneKenobi/covid-19-nds-lambda/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/BeneKenobi/covid-19-nds-lambda/actions/workflows/main.yml)