import datetime
from flask_wtf import FlaskForm
import wtforms as wf


class HistoryForm(FlaskForm):
    name_client = wf.SelectField(label='Имя клиента')
    name_doctor = wf.SelectField(label='Имя доктора')
    diagnosis = wf.StringField(label='Диагноз')


class ClientForm(FlaskForm):
    name = wf.StringField(label='ФИО клиента')
    date_of_birth = wf.DateField(label='Дата рождения')
    inn = wf.IntegerField(label='ИНН клиента')
    gender = wf.SelectField(label='Пол клиента', choices=['Мужской', 'Женский', 'Другой'])
    number = wf.StringField(label='Номер телефона', validators=[
        wf.validators.Length(min=13, max=13)
    ])
    address = wf.StringField(label='Адрес проживания')
    date_of_application = wf.DateField(label='Дата обращения')

    def validate_name(self, field):
        if ' ' not in field.data:
            raise wf.validators.ValidationError('Введите ФИО на кириллице!')

    def validate_date_of_birth(self, field):
        if (datetime.date.today().year - field.data.year) < 18:
            raise wf.validators.ValidationError('Вам должно исполниться 18 лет!')

    # def validate_inn(self, field):
    #     if field.data[1:3] != self.date_of_birth.data.day and\
    #             field.data[3:5] != self.date_of_birth.data.month and\
    #             field.data[5:9] != self.date_of_birth.data.year:
    #         raise wf.validators.ValidationError('ИНН не совпадает с датой рождения!')

    def validate_number(self, field):
        if field.data[0] != '+':
            raise wf.validators.ValidationError('Номер телефона должен начинаться с +')

    def validate_date_of_application(self, field):
        if field.data > datetime.date.today():
            raise wf.validators.ValidationError('Дата не может быть выше сегодняшней')


class DoctorForm(FlaskForm):
    name = wf.StringField(label='ФИО доктора')
    date_of_birth = wf.DateField(label='Дата рождения')
    specialization = wf.StringField(label='Специальность')
    experience = wf.IntegerField(label='Стаж')

    def validate_name(self, field):
        if ' ' not in field.data:
            raise wf.validators.ValidationError('Введите ФИО на кириллице!')

    def validate_date_of_birth(self, field):
        if (datetime.date.today().year - field.data.year) < 25:
            raise wf.validators.ValidationError('Вам должно исполниться 25 лет!')

    def validate_experience(self, field):
        if (datetime.date.today().year - self.date_of_birth.data.year - 25) < field.data:
            raise wf.validators.ValidationError('Стаж должен быть минимум 5 лет')
