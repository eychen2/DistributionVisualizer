from tokenize import String
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,SubmitField
class DistributionForm(FlaskForm):
    distribution = SelectField(u'Distribution', choices=[('0','Bernoulli'),('1','Binomial'),('2','Geometric'),
    ('3','Hypergeometric'),('4','Negative Binomial'),('5','Poisson')])
    submit=SubmitField('Visualize')

class ParameterForm(FlaskForm):
    param=StringField(u'Parameter')
