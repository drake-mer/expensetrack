cd ..

# clean up
rm -rf demo
# clone the repo
git clone david-kremer demo
# move into folder

cd demo
# move to 8080 port
sed -i s/"localhost:8000"/"localhost:8080"/g ui-js/js/client.js

cd extrack
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver localhost:8080 


