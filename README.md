Pull code and installation:
git init

git remote add origin https://github.com/XBLDev/hivery-backend-challenge.git

git pull origin master

git checkout -b xilong

git fetch

git branch --set-upstream-to=origin/xilong xilong

git pull

pip install -r requirements.txt OR pip3 install -r requirements.txt

If fails to install pytest try:
pip install -U pytest

Run api:
python app.py

First api:
http://127.0.0.1:5000/companyemployees?name=SOMECOMPANYNAME
Example: http://127.0.0.1:5000/companyemployees?name=STRALUM

Second api:
http://127.0.0.1:5000/commonfriends?person1=PERSON1NAME&person2=PERSON2NAME
Example: http://127.0.0.1:5000/commonfriends?person1=Joy%20Alvarado&person2=Weeks%20Knox

Third api:
http://127.0.0.1:5000/fruitsvegetables?person=PERSONNAME
Example: http://127.0.0.1:5000/fruitsvegetables?person=Bonnie%20Bass

Run test:
pytest test.py

For the 3rd api, i couldn't find a smart way of seperating fruits from vegetables, so i just wrote another api
to get all the unique foods, and it appears that there are 8 in total, 4 fruits and 4 vegetables.
