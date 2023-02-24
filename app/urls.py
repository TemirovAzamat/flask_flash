from . import app

from .views import get_client_doctor, client_create, doctor_create

app.add_url_rule('/', view_func=get_client_doctor)
app.add_url_rule('/client/create', view_func=client_create, methods=['GET', 'POST'])
app.add_url_rule('/doctor/create', view_func=doctor_create, methods=['GET', 'POST'])

