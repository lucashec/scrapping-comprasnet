from flask import Flask, request
import os
import json
from scrapping import obter_situacoes
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

app = Flask(__name__)

os.environ['GH_TOKEN'] = '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'
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

@app.route("/situacoes", methods=['GET'])
def get_situacoes():
    args = request.args
    results = []
    try:
        for i in range(0,3):
            results += obter_situacoes(driver, i, args.get("uasg"))
        results_json = json.dumps(results, ensure_ascii=False).encode()
        return results_json
    except:
        return json.dumps({"failed": "true"}), 400