# covid-19-nds-lambda
AWS Lambda function to parse the covid-19 data of the state Niedersachsen (Germany).

Takes the `GKZ` as only (query-)parameter and returns the recent 8 values for `7-Tagesinzidenz pro 100.000 Einwohner` using AWS API-Gateway.

You may use `list_gkz.py` to find your `GKZ`.

## Create Lambda with docker
1. Build the docker image:
   ```
   docker build -t covid-19-nds-lambda .
   ```
2. Using the AWS CLI (https://aws.amazon.com/cli/):
   ```
   aws ecr create-repository --repository-name covid-19-nds-lambda --image-scanning-configuration scanOnPush=true
   ```
   Note the `repositoryUri` from the result.
3. Tag the docker image for AWS ECR using the `repositoryUri`:
   ```
   docker tag covid-19-nds-lambda:latest repositoryUri:latest
   ```
4. Login to AWS ECR using the `repositoryUri` without the path component (`/covid-19-nds-lambda`):
   ```
   aws ecr get-login-password | docker login --username AWS --password-stdin repositoryUriWithoutPath
   ```
5. Push the docker image to AWS ECR:
   ```
   docker push repositoryUri:latest
   ```
6. Create the AWS Lamda function using the AWS Console by selecting the just uploaded image from ECR.