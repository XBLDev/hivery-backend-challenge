from app import app
from flask import json
import json

url = 'http://127.0.0.1:5000'

class Tests(object):
    def test_companyemployees(self):
        #Tests for /companyemployees
        response_nocompanyname = app.test_client().get(url+ '/companyemployees')
        data_nocompanyname = json.loads(response_nocompanyname.get_data(as_text=True))
        assert len(data_nocompanyname['employees']) == 0

        response_wrongcompanyname = app.test_client().get(url + '/companyemployees?name=adsfadsfsad')
        data_wrongcompanyname = json.loads(response_wrongcompanyname.get_data(as_text=True))
        assert len(data_wrongcompanyname['employees']) == 0

        response_companynoemployee = app.test_client().get(url + '/companyemployees?name=NETBOOK')
        data_companynoemployee = json.loads(response_companynoemployee.get_data(as_text=True))
        assert len(data_companynoemployee['employees']) == 0

        response_companymanyemployees = app.test_client().get(url + '/companyemployees?name=STRALUM')
        data_companymanyemployees = json.loads(response_companymanyemployees.get_data(as_text=True))
        assert len(data_companymanyemployees['employees']) == 11
        
        #Tests for /commonfriends
        response_nopeoplenames = app.test_client().get(url + '/commonfriends')
        data_nopeoplenames = json.loads(response_nopeoplenames.get_data(as_text=True))
        assert data_nopeoplenames['person1_details'] == {} 
        assert data_nopeoplenames['person2_details'] == {} 
        assert len(data_nopeoplenames['common_friends_names']) == 0

        response_noperson2name = app.test_client().get(url + '/commonfriends?person1=Joy Alvarado')
        data_noperson2name = json.loads(response_noperson2name.get_data(as_text=True))
        assert data_noperson2name['person1_details']['Name'] == 'Joy Alvarado' 
        assert data_noperson2name['person2_details'] == {} 
        assert len(data_noperson2name['common_friends_names']) == 0

        response_noperson1name = app.test_client().get(url + '/commonfriends?person2=Joy Alvarado')
        data_noperson1name = json.loads(response_noperson1name.get_data(as_text=True))
        assert data_noperson1name['person1_details'] == {}
        assert data_noperson1name['person2_details']['Name'] == 'Joy Alvarado' 
        assert len(data_noperson1name['common_friends_names']) == 0

        response_wrongperson1name = app.test_client().get(url + '/commonfriends?person1=Jdfbgoy Alvaradfdaso&person2=Weeks Knox')
        data_wrongperson1name = json.loads(response_wrongperson1name.get_data(as_text=True))
        assert data_wrongperson1name['person1_details'] == {}
        assert data_wrongperson1name['person2_details']['Name'] == 'Weeks Knox' 
        assert len(data_wrongperson1name['common_friends_names']) == 0

        response_wrongperson2name = app.test_client().get(url + '/commonfriends?person1=Joy Alvarado&person2=Weefdks Knofsdggx')
        data_wrongperson2name = json.loads(response_wrongperson2name.get_data(as_text=True))
        assert data_wrongperson2name['person1_details']['Name'] == 'Joy Alvarado' 
        assert data_wrongperson2name['person2_details'] == {}
        assert len(data_wrongperson2name['common_friends_names']) == 0

        response_havecommonfriends = app.test_client().get(url + '/commonfriends?person1=Joy Alvarado&person2=Weeks Knox')
        data_havecommonfriends = json.loads(response_havecommonfriends.get_data(as_text=True))
        assert data_havecommonfriends['person1_details']['Name'] == 'Joy Alvarado' 
        assert data_havecommonfriends['person2_details']['Name'] == 'Weeks Knox' 
        assert data_havecommonfriends['common_friends_names'][0] == 'Decker Mckenzie'
        assert data_havecommonfriends['common_friends_names'][1] == 'Mindy Beasley'

        response_havenocommonfriends = app.test_client().get(url + '/commonfriends?person1=Carmella Lambert&person2=Decker Mckenzie')
        data_havenocommonfriends = json.loads(response_havenocommonfriends.get_data(as_text=True))
        assert data_havenocommonfriends['person1_details']['Name'] == 'Carmella Lambert' 
        assert data_havenocommonfriends['person2_details']['Name'] == 'Decker Mckenzie' 
        assert len(data_havenocommonfriends['common_friends_names']) == 0

        #Tests for /fruitsvegetables
        response_nopersonname = app.test_client().get(url + '/fruitsvegetables')
        data_nopersonname = json.loads(response_nopersonname.get_data(as_text=True))
        assert data_nopersonname['age'] == ''
        assert data_nopersonname['username'] == ''
        assert len(data_nopersonname['fruits']) == 0
        assert len(data_nopersonname['vegetables']) == 0

        response_wrongpersonname = app.test_client().get(url + '/fruitsvegetables?person=Carmlla Lamert')
        data_wrongpersonname = json.loads(response_wrongpersonname.get_data(as_text=True))
        assert data_wrongpersonname['age'] == ''
        assert data_wrongpersonname['username'] == ''
        assert len(data_wrongpersonname['fruits']) == 0
        assert len(data_wrongpersonname['vegetables']) == 0

        response_rightpersonname = app.test_client().get(url + '/fruitsvegetables?person=Carmella Lambert')
        data_rightpersonname = json.loads(response_rightpersonname.get_data(as_text=True))
        assert data_rightpersonname['age'] == 61
        assert data_rightpersonname['username'] == 'Carmella Lambert'
        assert len(data_rightpersonname['fruits']) == 4
        assert len(data_rightpersonname['vegetables']) == 0

        response_rightpersonname = app.test_client().get(url + '/fruitsvegetables?person=Bonnie Bass')
        data_rightpersonname = json.loads(response_rightpersonname.get_data(as_text=True))
        assert data_rightpersonname['age'] == 54
        assert data_rightpersonname['username'] == 'Bonnie Bass'
        assert len(data_rightpersonname['fruits']) == 3
        assert len(data_rightpersonname['vegetables']) == 1

        response_rightpersonname = app.test_client().get(url + '/fruitsvegetables?person=Grace Kelly')
        data_rightpersonname = json.loads(response_rightpersonname.get_data(as_text=True))
        assert data_rightpersonname['age'] == 24
        assert data_rightpersonname['username'] == 'Grace Kelly'
        assert len(data_rightpersonname['fruits']) == 1
        assert len(data_rightpersonname['vegetables']) == 3