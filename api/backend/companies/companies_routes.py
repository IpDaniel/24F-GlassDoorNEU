from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

companies = Blueprint('companies', __name__)

#------------------------------------------------------------
# Get all companies
# 
@companies.route('/companies', methods=['GET'])
def get_companies():
    current_app.logger.info('GET /companies route')
    
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT companyID, companyName, location
                      FROM interview_prep_system.Company
    ''')
    
    companies_data = cursor.fetchall()
    
    response = make_response(jsonify(companies_data))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Add a new company
# TODO: need to test
@companies.route('/companies', methods=['POST'])
def create_company():
    current_app.logger.info('POST /companies route')
    company_info = request.json
    companyName = company_info['companyName']
    location = company_info['location']

    query = 'INSERT INTO Company (companyName, location) VALUES (%s, %s)'
    data = (companyName, location)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return 'company added!'

#------------------------------------------------------------
# Update company info for specific companyID
# TODO: Need to test
@companies.route('/companies', methods=['PUT'])
def update_company():
    current_app.logger.info('PUT /companies route')
    company_info = request.json
    companyID = company_info['companyID']
    companyName = company_info['companyName']
    location = company_info['location']
    
    cursor = db.get_db().cursor()

    query = 'UPDATE Company SET companyName = %s, location = %s WHERE companyID = %s'
    data = (companyName, location, companyID)
    cursor.execute(query, data)
    db.get_db().commit()
    return 'company updated!'

#------------------------------------------------------------
# Delete company for specific companyID
# TODO: Need to test
@companies.route('/companies/<companyID>', methods=['DELETE'])
def delete_company(companyID):
    current_app.logger.info('DELETE /companies/<companyID> route')
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Company WHERE companyID = {0}'.format(companyID))
    db.get_db().commit()
    return 'company deleted!'

#------------------------------------------------------------
# Get company info for specific companyID
# TODO: Need to test
@companies.route('/companies/<companyID>', methods=['GET'])
def get_company(companyID):
    current_app.logger.info('GET /companies/<companyID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT companyID, companyName, location FROM Company WHERE companyID = {0}'.format(companyID))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Update a specific company
# TODO: Need to test
@companies.route('/companies/<companyID>', methods=['PUT'])
def update_specific_company(companyID):
    current_app.logger.info('PUT /companies/<companyID> route')
    company_info = request.json
    companyName = company_info['companyName']
    location = company_info['location']

    cursor = db.get_db().cursor()
    
    query = 'UPDATE Company SET companyName = %s, location = %s WHERE companyID = %s'
    data = (companyName, location, companyID)
    cursor.execute(query, data)
    db.get_db().commit()
    return 'company updated successfully!'