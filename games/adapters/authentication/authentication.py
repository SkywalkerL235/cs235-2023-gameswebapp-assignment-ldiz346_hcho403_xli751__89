from flask import Blueprint, render_template, redirect, url_for, session, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from password_validator import PasswordValidator


@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    user_name_not_unique = None

    if form.validate_on_submit():
        try:
            services.add_uesr(form.user_name.data, form.password.data repo.repo_instance)
            #passed (redirect to login page)
            return redirect(url_for('authentication_bp.login'))
        except sevices.NameNotUniqueException:
            user_name_not_unique = 'Your user name is already taken!'

    return render_template(
        'authentication/credentials.html',
        title='Register',
        form=form,
        user_name_error_message=user_name_not_unique,
        handler_url=url_for('authentication_bp.register'),
        #add more here (e.g. selected_games)
    )

