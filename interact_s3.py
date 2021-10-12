import boto3
import pandas as pd

s3_client = boto3.client('s3')

# s3_client.download_file(
#     "datalake-jfds-igti-edc",
#     "data/new_user_credentials.csv",
#     "data/new_user_credentials.csv"
# )

# df = pd.read_csv("data/new_user_credentials.csv", sep=",")
# print(df)

# s3_client.upload_file(
#     "data/pnadc20203.csv",
#     "datalake-jfds-igti-edc",
#     "data/pnadc20203.csv"
# )

# Resposta trabalho modulo 1
s3_client.upload_file(
    Filename="data/MICRODADOS_ENEM_2019.csv",
    Bucket="datalake-jefferson-694809588948",
    Key="raw-data/enem/year=2019/MICRODADOS_ENEM_2019.csv"
)