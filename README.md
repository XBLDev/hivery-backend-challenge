This backend is hosted on: 13.210.70.130

Install:
pip install -r requirements.txt

Run api:
python app.py

First api:
http://127.0.0.1:5000/companyemployees?name=SOMECOMPANYNAME

Second api:
http://127.0.0.1:5000/commonfriends?person1=PERSON1NAME&person2=PERSON2NAME

Third api:
http://127.0.0.1:5000/fruitsvegetables?person=PERSONNAME

Run test:
pytest test.py
