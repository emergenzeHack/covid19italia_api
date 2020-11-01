import yaml
import json
from fastapi import FastAPI
import sys

app = FastAPI()

with open("../data/issuesjson.json","r") as fp:
    d=json.load(fp)

dd={}
for issue in d:
    dd[issue['number']]=issue

@app.get("/")
async def root():
    return d.to_json()

@app.get("/issues/")
async def read_issues():
    return dd

@app.get("/issues/{issue_id}")
async def read_issue(issue_id):
    issue=dd[int(issue_id)]

    return issue
