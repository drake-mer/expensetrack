cd ..

# clean up
rm -rf demo
# clone the repo
git clone david-kremer demo
# move into folder

cd demo

pip install -r requirements.txt --user
for folder in ${HOME}/.local/lib/python*;do 
    export PYTHONPATH=${PYTHONPATH}:${folder}/site-packages/
done

# move to 8080 port
sed -i s/"localhost:8000"/"localhost:8080"/g ui-js/js/client.js

cd extrack
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver localhost:8080 


