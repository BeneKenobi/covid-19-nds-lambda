**Disclaimer: This is just a hobby-project to play with GitHubActions, AWS Lambda/ECR and finally JavaScript/Scriptable (see https://gist.github.com/BeneKenobi/340a99e202f52c1d28d4d8095aabb0ab). There are a couple of easier, direct approaches to do this (like handling everything just in the Scriptable JavaScript).**
# covid-19-nds-lambda
AWS Lambda function to parse the covid-19 data of the state Niedersachsen (Germany).

Takes the `GKZ` as only (query-)parameter and returns the recent 8 values for `7-Tagesinzidenz pro 100.000 Einwohner` using AWS API-Gateway.

You may use `list_gkz.py` to find your `GKZ`.

[![CI/CD](https://github.com/BeneKenobi/covid-19-nds-lambda/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/BeneKenobi/covid-19-nds-lambda/actions/workflows/main.yml)
