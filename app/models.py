from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(254), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    char_sheets = db.relationship('Char_sheet', backref='user', lazy='joined')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Char_sheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    """
    charname = db.Column(db.String(128))
    classlevel = db.Column(db.String(128))
    background = db.Column(db.String(128))
    playername = db.Column(db.String(128))
    race = db.Column(db.String(128))
    alignment = db.Column(db.String(128))
    experiencepoints = db.Column(db.String(128))
    Strengthscore = db.Column(db.Integer(128))
    strengthmod = db.Column(db.Integer)
    dexterityscore = db.Column(db.Integer)
    dexteritymod = db.Column(db.Integer)
    constitutionscore = db.Column(db.Integer)
    constitutionmod = db.Column(db.Integer)
    wisdomscore = db.Column(db.Integer)
    wisdommod = db.Column(db.Integer)
    charismascore = db.Column(db.Integer)
    charismamod = db.column(db.Integer)
    inspiration = db.column(db.Boolean)
    proficiencybonus = db.colum(db.Integer)
    strengthsave = db.column(db.Integer)
    dexteritysave = db.column(db.Integer)
    dex_prof = db.column(db.Boolean)
    constitutionsave = db.column(db.Integer)
    const_prof = db.column(db.Boolean)
    intelligencesave = db.column(db.Integer)
    int_prof = db.column(db.Boolean)
    charismasave = db.column(db.Integer)
    char_prof = db.column(db.Boolean)
    acrobatics = db.column(db.Integer)
    animalhandling = db.column(db.Integer)
    arcana = db.column(db.Integer)
    arcana = db.column(db.Integer)
    
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return '<Character sheet {}>'.format(self.char_sheet_path)