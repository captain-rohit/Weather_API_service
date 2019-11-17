# Weather_API_service
Differnent APIs for CRUD operations

Instructions for Using the Service:
First of all you need to have Python 3.7 installed in your system. Clone the repository with the Default named folder.

Go inside the Repository:
cd Weather_API_service/

Setting up of Virtual Environment:
python3 -m venv .
    or,
python -m venv .

Going inside the Environment:
Deactivate your current Python Environment or Base Environment and activate the new Virtual Environment by using:
source bin/activate [for Linux only]

Installing the Required Packages:
Install the required Libraries/Framework required by using:
pip3 install -r requirements.txt
         or,
pip install -r requirements.txt

After all the Installations are complete Create a new Superuser by running:

cd src/

manage.py createsuperuser

Enter the required Credentials and now you are done.

Make the Migrations in Database and start the remote server.

