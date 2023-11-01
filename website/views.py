from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Serverconfig
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # serverConfig = Serverconfig.query.all()
    # print(serverConfig)
    currServerConfig = Serverconfig.query.filter_by(serverName='nodered').first()
    if request.method == 'POST':
        nrIp = request.form.get('nrIp')
        if nrIp == "":
            nrIp = currServerConfig.nrIp
        apiUrl = request.form.get('apiUrl')
        if apiUrl == "":
            apiUrl = currServerConfig.apiUrl
        payloadMsg = request.form.get('payloadMsg')
        if payloadMsg == "":
            payloadMsg = currServerConfig.payloadMsg
        print(currServerConfig)
        currServerConfig.nrIp = nrIp
        currServerConfig.apiUrl = apiUrl
        currServerConfig.payloadMsg = payloadMsg
        db.session.commit()
        print(Serverconfig.query.all()[0].nrIp)
        flash("New server configuration set successfully!", category='success')

    return render_template("home.html", user=current_user, nrIp=currServerConfig.nrIp, apiUrl=currServerConfig.apiUrl, payloadMsg=currServerConfig.payloadMsg)