from app import app, db
from app.models import User, Char_sheet

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Char_sheet': Char_sheet}