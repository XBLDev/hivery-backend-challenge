from app import app
from flask import json
import json

url = 'http://127.0.0.1:5000'

class Tests(object):
    def test_companyemployees(self):
        #Tests for /companyemployees
        response_nocompanyname = app.test_client().get(url+ '/companyemployees')
        data_nocompanyname = response_nocompanyname.get_data(as_text=True)
        assert data_nocompanyname == 'Please provide the name of at least one company'

        response_wrongcompanyname = app.test_client().get(url + '/companyemployees?name=adsfadsfsad')
        data_wrongcompanyname = response_wrongcompanyname.get_data(as_text=True)
        assert data_wrongcompanyname == 'No company with name: adsfadsfsad was found, please make sure you are requesting an existing company'

        response_companynoemployee = app.test_client().get(url + '/companyemployees?name=NETBOOK')
        data_companynoemployee = response_companynoemployee.get_data(as_text=True)
        assert data_companynoemployee == 'Company: NETBOOK has no employee'

        response_companymanyemployees = app.test_client().get(url + '/companyemployees?name=STRALUM')
        data_companymanyemployees = response_companymanyemployees.get_data(as_text=True)
        assert data_companymanyemployees == 'Company: STRALUM has employees: Kathleen Clarke, Guy Dunn, Butler Norton, Amelia Benjamin, Florence Gordon, Marguerite Frost, Avis Carter, Margery Brooks, English Nolan, Hansen Dejesus, Emily Taylor'
        
        #Tests for /commonfriends
        response_nopeoplenames = app.test_client().get(url + '/commonfriends')
        data_nopeoplenames = response_nopeoplenames.get_data(as_text=True)
        assert data_nopeoplenames == 'Please provide the names of 2 people'

        response_noperson2name = app.test_client().get(url + '/commonfriends?person1=Joy Alvarado')
        data_noperson2name = response_noperson2name.get_data(as_text=True)
        assert data_noperson2name == 'Please provide the names of 2 people'

        response_noperson1name = app.test_client().get(url + '/commonfriends?person2=Joy Alvarado')
        data_noperson1name = response_noperson1name.get_data(as_text=True)
        assert data_noperson1name == 'Please provide the names of 2 people'

        response_wrongperson1name = app.test_client().get(url + '/commonfriends?person1=Jdfbgoy Alvaradfdaso&person2=Weeks Knox')
        data_wrongperson1name = response_wrongperson1name.get_data(as_text=True)
        assert data_wrongperson1name == 'No person with name: Jdfbgoy Alvaradfdaso was found'

        response_wrongperson2name = app.test_client().get(url + '/commonfriends?person1=Joy Alvarado&person2=Weefdks Knofsdggx')
        data_wrongperson2name = response_wrongperson2name.get_data(as_text=True)
        assert data_wrongperson2name == 'No person with name: Weefdks Knofsdggx was found'

        response_havecommonfriends = app.test_client().get(url + '/commonfriends?person1=Joy Alvarado&person2=Weeks Knox')
        data_havecommonfriends = json.loads(response_havecommonfriends.get_data(as_text=True))
        assert data_havecommonfriends['common_friends_names'][0] == 'Decker Mckenzie'
        assert data_havecommonfriends['common_friends_names'][1] == 'Mindy Beasley'

        response_havenocommonfriends = app.test_client().get(url + '/commonfriends?person1=Carmella Lambert&person2=Decker Mckenzie')
        data_havenocommonfriends = json.loads(response_havenocommonfriends.get_data(as_text=True))
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
        assert len(data_rightpersonname['fruits']) == 2
        assert len(data_rightpersonname['vegetables']) == 2