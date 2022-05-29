from flask import json, jsonify, request, Flask
import pandas as pd
# from flask_executor import Executor
app = Flask(__name__)
from sqlalchemy import create_engine
engine = create_engine('postgresql://ucjwemyiugimlp:9e712414af84c32436e99f16b18eba7fbd7b040e605830a389452e48faa843a9@ec2-52-212-228-71.eu-west-1.compute.amazonaws.com:5432/dbh3cjjfj4g2jq')
# create local postgresql instance
# engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')

@app.route('/api/branch',methods = ["GET"])
def searchBranch():
    v = request.args
    print(v)
    offset = int(v.get('offset') or 0)
    limit = int(v.get('limit') or 10)
    # fetch data from database
    sql_query = "SELECT * FROM bank_branches where branch like"+ "'%%"+ v.get('q') +"%%'"+ "ORDER BY branch LIMIT "+ str(limit) + " OFFSET "+ str(offset)
    df = engine.execute(sql_query).fetchall()
    print(df)
    data = []
    for i in df:
        temp = {'ifsc':i[0],'bank_id':i[1],'branch':i[2],'address':i[3],'city':i[4],'district':i[5],'state':i[6],'bank_name':i[7]}
        data.append(temp)
    return jsonify({'branches': data})

@app.route('/api/search',methods = ["GET"])
def searchQuery():
    v = request.args
    print(v)
    offset = int(v.get('offset') or 0)
    limit = int(v.get('limit') or 10)
    # fetch data from database
    sql_query = "SELECT * FROM bank_branches where branch like"+ "'%%"+ v.get('q') +"%%'"+ "ORDER BY branch LIMIT "+ str(limit) + " OFFSET "+ str(offset)
    df = engine.execute(sql_query).fetchall()
    print(df)
    data = []
    for i in df:
        temp = {'ifsc':i[0],'bank_id':i[1],'branch':i[2],'address':i[3],'city':i[4],'district':i[5],'state':i[6],'bank_name':i[7]}
        data.append(temp)
    return jsonify({'branches': data})

if __name__ == '__main__':
    app.run(debug=True)