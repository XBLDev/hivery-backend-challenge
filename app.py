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
            return {'employees': []}
        else:
            with open('./resources/people.json') as json_file:
                data = json.load(json_file)
                companyemployees = [employee for employee in data if employee['company_id'] == companyindex]
                if len(companyemployees) == 0:
                    return {'employees': []}
                else:
                    employee_names = [employee['name'] for employee in companyemployees]
                    return {'employees': employee_names}
    else:
        return {'employees': []}
    
#Given 2 people, provide their information (Name, Age, Address, phone) 
#and the list of their friends in common which have brown eyes and are still alive.
@app.route('/commonfriends')
def commonfriends():
    person1_name = request.args.get('person1')
    person2_name = request.args.get('person2')
    with open('./resources/people.json') as json_file:
        data = json.load(json_file)
        person1 = [person for person in data if person['name'] == person1_name] if person1_name is not None else {}
        person2 = [person for person in data if person['name'] == person2_name] if person2_name is not None else {}
        person1_details = {'Name': person1[0]['name'], 'Age': person1[0]['age'], 'Address': person1[0]['address'], 'Phone': person1[0]['phone']} if len(person1) > 0 else {}
        person2_details = {'Name': person2[0]['name'], 'Age': person2[0]['age'], 'Address': person2[0]['address'], 'Phone': person2[0]['phone']} if len(person2) > 0 else {}
        person1_friends_indexes = [friendindex['index'] for friendindex in person1[0]['friends'] if friendindex['index'] != person1[0]['index']] if len(person1) > 0 and person1[0]['friends'] is not None else []
        person2_friends_indexes = [friendindex['index'] for friendindex in person2[0]['friends'] if friendindex['index'] != person2[0]['index']] if len(person2) > 0 and person2[0]['friends'] is not None else []
        common_friends_indexes = [index for index in person1_friends_indexes if index in person2_friends_indexes]
        common_friends_browneyes_alive = [friend for friend in data if friend['index'] in common_friends_indexes and friend['has_died'] == False and friend['eyeColor'] == 'brown']
        common_friends_names = [friend['name'] for friend in common_friends_browneyes_alive]
        return {'person1_details': person1_details, 'person2_details': person2_details, 'common_friends_names': common_friends_names}

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
                person_fruits = [fruit for fruit in person[0]['favouriteFood'] if fruit in ['orange', 'apple', 'banana', 'strawberry']]
                person_vegetables = [vegetable for vegetable in person[0]['favouriteFood'] if vegetable in ['cucumber', 'beetroot', 'carrot', 'celery']]
                return {"username": person[0]['name'], "age": person[0]['age'], "fruits": person_fruits, "vegetables": person_vegetables}
            else:
                return {"username": "", "age": "", "fruits": [], "vegetables": []}
    else:
        return {"username": "", "age": "", "fruits": [], "vegetables": []}

#I don't really know how to seperate fruit from vegetables in this case, so this
#api is just to get all the unique food, the list is:
#['orange', 'apple', 'banana', 'strawberry', 'cucumber', 'beetroot', 'carrot', 'celery']
#with fruits being: 'orange', 'apple', 'banana', 'strawberry', 'cucumber'
#with vegetables being: 'cucumber', 'beetroot', 'carrot', 'celery'
@app.route('/getallfood')
def getallfood():
    with open('./resources/people.json') as json_file:
        data = json.load(json_file)
        allfood = []
        for person in data:
            if person['favouriteFood'] is not None:
                for food in person['favouriteFood']:
                    if food not in allfood:
                        allfood.append(food)
        return {'allfood': allfood}

if __name__ == '__main__':
    app.run(debug=True)