# Where to go - Moscow through the eyes of Artyom 

[Website](http://countzero12394.pythonanywhere.com/) about the most interesting places in Moscow. Artyom's project. 

## Run 
Requires python version >=3.6 to work 
- Download the code 
- Install dependencies with `pip install -r requirements.txt` 
- Create a database file and apply all migrations with `python3 manage.py migrate` 
- Start the server with ` python3 manage.py runserver` 

## Environment Variables 

Some project settings are taken from environment variables. To define them, create a `.env` file next to `manage.py` and write data there in the following format: `VARIABLE=value`. 

There are 4 variables available:
- `DEBUG` - debug mode. Set to True to see debug information in case of an error. 
- `SECRET_KEY` - secret key of the project 
- `ALLOWED_HOSTS` - see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts). 
- `DATABASE_URL` — one-line address to the database, for example: `sqlite:///db.sqlite3`. More info in [documentation](https://github.com/jacobian/dj-database-url) 

## Adding locations 

To add locations use `python3 manage.py load_place <link>`
where `link` is a link to json with a description of the object, [example](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D1%80%D1%82-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%BE%20%C2%AB%D0%91%D1%83%D0%BD%D0%BA%D0%B5%D1%80%20703%C2%BB.json)   

## Project Goals 

Code written for educational purposes — this is a lesson in the Python and web development 