from flask_wtf import FlaskForm
from wtforms import (
StringField, 
PasswordField, 
TextAreaField, 
BooleanField, 
DateField, 
TimeField, 
SelectField, 
IntegerField,
RadioField,
widgets, 
SelectMultipleField,
)
from wtforms.validators import DataRequired
from .api_requests import get_agents
import json

callPolicyChoices = ['CIRCULAR', 'UNIFORM', 'REGULAR', 'SIMULATANEOUS', 'WAITED']
booleanSelector = ['True', 'False']
BooleanField.false_values = {False, 'false', ''}
agentSelector = [(agent['id'], agent['emails'][0]) for agent in get_agents()['items']]
languagecodeSelector = ['pt-br', 'pt-pt', 'pl-pl', 'fr-fr', 'gr-gr']

class HuntGroupForm(FlaskForm):
    #General settings
    name = StringField('Hunt Group name', validators=[DataRequired()])
    phoneNumber = StringField('Phone number', validators=[DataRequired()])
    extension = IntegerField('Hunt Group number', widget = widgets.Input(input_type="tel"))
    languagecode = SelectField('Languagecode', choices=languagecodeSelector, validators=[DataRequired()])
    firstName = StringField('First Name')
    lastName = StringField('Last Name')
    timezone = StringField('Timezone')
    #Agents
    agents= SelectMultipleField('Agents to associate', choices=agentSelector)
    #Enabling Hunt Group
    enabled = BooleanField('Enable Hunt Group')

class CallPoliciesForm(FlaskForm):
    policy = SelectField('Call Policy', choices=callPolicyChoices, validators=[DataRequired()])
    waitingEnabled = BooleanField('Advance when busy')

class NoAnswerForm(FlaskForm):
    nextAgentEnabled = BooleanField('Advance to next agent')
    nextAgentRings = SelectField('Number of rings', choices=range(1,10), validators=[DataRequired()])
    forwardEnabled = BooleanField('Enable forwarding')
    numberOfRings = SelectField('Number of rings', choices=range(1,10), validators=[DataRequired()])
    destination = StringField('Forward destination', validators=[DataRequired()])
    destinationVoicemailEnabled = BooleanField('Enable forwarding to Voice Mail')

class BusinessConForm(FlaskForm):
    #BusinessContinuity settings
    enabled = BooleanField('Enable Business Continuity')
    destination = StringField('Business continuity destination', validators=[DataRequired()])
    destinationVoicemailEnabled = BooleanField('Enable Business Continuity Voicemail')





