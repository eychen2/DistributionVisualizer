from math import dist
from sre_constants import SUCCESS
from flask import Flask, render_template
from Forms import DistributionForm

app = Flask(__name__)
app.config['SECRET_KEY']='f3907285dd73b27a155dd423614e0d3a'
@app.route("/", methods=['GET','POST'])
def home():
    form=DistributionForm()
    if form.validate_on_submit():
        dist=form.distribution.data
        return render_template('home.html',form=form,dist=dist)
    return render_template('home.html',form=form,dist=0)
@app.route("/visualization", methods=['GET','POST'])
def visualization():
    return render_template('visualization.html')
@app.route("/about")
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)