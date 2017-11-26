from flask import Flask
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    
    # Update config where test parameters are fed into
    app.config.update(config_overrides)
    
    # Db setup
    db.init_app(app)
    
    # User Blueprint registration
    from user.views import user_app
    app.register_blueprint(user_app)
    
    from relationship.views import relationship_app
    app.register_blueprint(relationship_app)
    
    return app