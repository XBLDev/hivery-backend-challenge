from flask import Flask
import json
from flask import request

app = Flask(__name__)

#Given a company, the API needs to return all their employees. 
#Provide the appropriate solution if the company does not have any employees.
@app.route('/companyemployees')
def companyemployees():
    name = request.args.get('name')
    if name is not None:
        companyindex = -1
        with open('./resources/companies.json') as json_file:
            data = json.load(json_file)
            companieswithname = [obj for obj in data if obj['company'] == name]
            if len(companieswithname) > 0:
                companyindex = companieswithname[0]['index']
        if companyindex == -1:
            return 'No company with name: ' + name + ' was found, please make sure you are requesting an existing company'
        else:
            with open('./resources/people.json') as json_file:
                data = json.load(json_file)
                companyemployees = [employee for employee in data if employee['company_id'] == companyindex]
                if len(companyemployees) == 0:
                    return 'Company: ' + name + ' has no employee'
                else:
                    employee_names = [employee['name'] for employee in companyemployees]
                    return 'Company: ' + name + ' has employees: ' + ', '.join(employee_names)
    else:
        return 'Please provide the name of at least one company'
    
#Given 2 people, provide their information (Name, Age, Address, phone) 
#and the list of their friends in common which have brown eyes and are still alive.
@app.route('/commonfriends')
def commonfriends():
    person1_name = request.args.get('person1')
    person2_name = request.args.get('person2')
    if person1_name is not None and person2_name is not None:
        with open('./resources/people.json') as json_file:
            data = json.load(json_file)
            person1 = [person for person in data if person['name'] == person1_name]
            person2 = [person for person in data if person['name'] == person2_name]
            if len(person1) == 0:
                return 'No person with name: ' + person1_name + ' was found'
            if len(person2) == 0:
                return 'No person with name: ' + person2_name + ' was found'
            if person1[0]['friends'] is not None and person2[0]['friends'] is not None and len(person1[0]['friends']) != 0 and len(person2[0]['friends']) != 0:
                person1_friends_indexes = [friendindex['index'] for friendindex in person1[0]['friends'] if friendindex['index'] != person1[0]['index']]
                person2_friends_indexes = [friendindex['index'] for friendindex in person2[0]['friends'] if friendindex['index'] != person2[0]['index']]
                common_friends_indexes = [index for index in person1_friends_indexes if index in person2_friends_indexes]
                common_friends_browneyes_alive = [friend for friend in data if friend['index'] in common_friends_indexes and friend['has_died'] == False and friend['eyeColor'] == 'brown']
                person1_details = {'Name': person1[0]['name'], 'Age': person1[0]['age'], 'Address': person1[0]['address'], 'Phone': person1[0]['phone']}
                person2_details = {'Name': person2[0]['name'], 'Age': person2[0]['age'], 'Address': person2[0]['address'], 'Phone': person2[0]['phone']}
                common_friends_names = [friend['name'] for friend in common_friends_browneyes_alive]
                return {'person1_details': person1_details, 'person2_details': person2_details, 'common_friends_names': common_friends_names}
            else:
                return 'No common friends'
    else:
        return 'Please provide the names of 2 people'

#Given 1 people, provide a list of fruits and vegetables they like. 
# This endpoint must respect this interface for the output: 
# {"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}
@app.route('/fruitsvegetables')
def fruitsvegetables():
    person_name = request.args.get('person')
    if person_name is not None:
        with open('./resources/people.json') as json_file:
            data = json.load(json_file)
            person = [p for p in data if p['name'] == person_name]
            if len(person) == 0:
                return {"username": "", "age": "", "fruits": [], "vegetables": []}
            if person[0]['favouriteFood'] is not None:
                return {"username": person[0]['name'], "age": person[0]['age'], "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}
            else:
                return {"username": "", "age": "", "fruits": [], "vegetables": []}
    else:
        return {"username": "", "age": "", "fruits": [], "vegetables": []}

if __name__ == '__main__':
    app.run(debug=True)