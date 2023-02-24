from flask import render_template, request, redirect, url_for, flash

from . import db
from .models import Client, Doctor
from .forms import ClientForm, DoctorForm


def get_client_doctor():
    clients = Client.query.all()
    doctors = Doctor.query.all()
    return render_template('view.html', clients=clients, doctors=doctors)


def client_create():
    title = 'Добавление нового клиента'
    form = ClientForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            client = Client()
            form.populate_obj(client)
            db.session.add(client)
            db.session.commit()
            flash('Успешно добавлено!')
            return redirect(url_for('get_client_doctor'))
    return render_template('form.html', form=form, title=title)


def doctor_create():
    title = 'Добавление нового доктора'
    form = DoctorForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            doctor = Doctor()
            form.populate_obj(doctor)
            db.session.add(doctor)
            db.session.commit()
            flash('Успешно добавлено!')
            return redirect(url_for('get_client_doctor'))
    return render_template('form.html', form=form, title=title)
