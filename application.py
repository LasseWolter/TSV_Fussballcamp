from flask import Flask
from app import application, db
from app.models import Player 

# Configure the shell context when running 'flask shell'
@application.shell_context_processor
def make_shell_context():
    return {'db':db, 'Player':Player}

# run the app.
if __name__ == "__main__":
    application.run()
