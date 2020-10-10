# https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from random import randint
from backend.database.database_check import DBchcek
from backend.database.database_requests import DBrequests

DEBUG=True
# Only work with tables that we are sure are in our database
TABLES=[table.upper() for table in DBchcek.findTableNames()]     


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
cors = CORS(app, 
            resources={r'/api/*': {'originis': '*'}})

# To know if the server is up
@app.route("/")
def serverRunning():
    return "Backend Server is Running!"

@app.route('/api/<table>/random')
def randomRecommendation(table):
    """
    This routing is done when a request is made to retrieve an item from one of the
    available database.
    """
    connection=DBrequests(table=table)
    recommendation=connection.accidentalRecommendation()
    return recommendation 

@app.route('/api/<table>/contents')
def findContents(table):
    """
    Routing that helps check all entries in the database in order to grasph what information is
    being worked with.
    """
    connection=DBrequests(table=table)
    contents=connection.retrieveFullDatabase()
    return contents

@app.route('/api/<table>/<content>')
def findContent(table, content):
    """
    A route that helps find information for only 1 instance of notes
    """
    connection=DBrequests(table=table)
    content=connection.retrieveOneInstance(idx=content)
    return content

@app.route('/api/tables')
def findTables():
    """
    This routing is done on the initiation of the front-end creation, in order to confirm
    how many tables are currently available in the database that is being worked with.
    This is accessed only once.
    """
    collection_check={}
    tables_check=[table for table in DBchcek.findTableNames()]

    #populate information in such way that it could be read as a json object
    for table in tables_check:
        collection_check[table] = table
    return collection_check

@app.route('/api/<table>/<content>/delete', methods=['DELETE'])
def deleteContent(table, content):
    """
    A route that allows for deletion of an item from a specific table
    """
    response_msg = {'status': 'success'}
    connection = DBrequests(table=table)
    connection.deleteOneInstance(idx=content)
    return jsonify(response_msg)

@app.route('/api/<table>/<content>/edit', methods=['PUT'])
def updateContent(table, content):
    """
    Update one entry of information.
    """
    response_msg = {'status': 'success'}
    post_data = request.get_json()
    connection = DBrequests(table=table)
    connection.updateOneInstance(idx=post_data.get('prod_name'),
                                 year=post_data.get('prod_year'),
                                 img=post_data.get('prod_img'),
                                 description=post_data.get('prod_description'))
    return response_msg

@app.route('/api/<table>/<content>/add', methods=['POST'])
def addContent(table, content):
    response_msg = {'status': 'success'}
    post_data = request.get_json()
    connection = DBrequests(table=table)
    connection.addOneInstance(idx=post_data.get('prod_name'),
                              year=post_data.get('prod_year'),
                              img=post_data.get('prod_img'),
                              description=post_data.get('prod_description'))
    return response_msg
        

if __name__ == "__main__":
    app.run(debug=DEBUG)