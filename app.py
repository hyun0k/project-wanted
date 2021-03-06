from flask  import Flask

from config import DATABASE_URI

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from database import db
    db.init_app(app)
    from models  import company

    with app.app_context():
        from views import company
        
        db.create_all()
        
        return app

