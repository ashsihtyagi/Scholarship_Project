import flask
from flask import (render_template, url_for)
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)


@app.route('/',methods=['GET'])
def default():
    return render_template('labour.html')



@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    
    model = joblib.load('model_exp.pkl')

    education=request.args['education']
    if education=='continuing':
        edu_continue=1
        edu_finished=0
    else:
        edu_continue=0
        edu_finished=1

    age=int(request.args['age'])

    land=request.args['land']
    if land=='yes':
        land_yes=1
        land_no=0
    else:
        land_yes=0
        land_no=1

    yo=request.args['yo']
    if yo=='public':
        yo_public=1
        yo_private=0
        yo_walking=0

    elif yo=='private':
        yo_public=0
        yo_private=1
        yo_walking=0

    else:
        yo_public=0
        yo_private=0
        yo_walking=1

    ge=request.args['ge']
    if ge=='male':
        ge_male=1
        ge_female=0
    else:
        ge_male=0
        ge_female=1

    ts=request.args['ts']
    if ts=='government':
        ts_gov=1
        ts_pri=0
    else:
        ts_gov=0
        ts_pri=1

    pds=request.args['pds']
    if pds=='yes':
        pds_yes=1
        pds_no=0
    else:
        pds_yes=0
        pds_no=1

    adhar=request.args['adhar']
    if adhar=='yes':
        adhar_yes=1
        adhar_no=0
    else:
        adhar_yes=0
        adhar_no=1

    gh=request.args['gh']
    if gh=='male':
        gh_male=1
        gh_female=0
    else:
        gh_male=0
        gh_female=1

    hf=request.args['hf']
    if hf=='yes':
        hf_yes=1
        hf_no=0
    else:
        hf_yes=0
        hf_no=1
    et=request.args['et']
    if et=='self-employed':
        et_self=1
        et_salary=0
    else:
        et_self=0
        et_salary=1

    scholar = model.predict([[int(edu_continue),
                        int(edu_finished),
                        age,
                        int(land_yes),
                        int(land_no),
                        int(yo_private),
                        int(ge_male),
                        int(ge_female),
                        int(yo_walking),
                        int(ts_gov),
                        int(ts_pri),
                        int(pds_no),
                        int(adhar_no),
                        int(adhar_yes),
                        int(gh_female),
                        int(hf_yes),
                        int(hf_no),
                        int(gh_male),
                        int(pds_yes),
                        int(et_self),
                        ]])
    if scholar[0]==0:
        return str('No')
    else:
        return str('Yes')
    

app.run()