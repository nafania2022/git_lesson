from classes.classes import CandidatManager
from flask import Flask, render_template



PATH = "candidates.json"
candidats = CandidatManager(PATH)
app = Flask(__name__)

@app.route('/')
def name(uid):
    return candidat.get_candidat_name(uid)


@app.route('/candidat/<int:uid>')
def name(uid):
    return candidat.get_candidat_name(uid)

    
@app.route('/skill/<uid>')
def name(uid):
    candidat = []
    
    candidat.append(candidats.get_candidat_name(uid)) 
    candidat.append(candidats.get_candidat_position(uid)) 
    candidat.append(candidats.get_candidat_skill(uid)) 
    return candidat


@app.route('/candidat/<int:uid>')
def page_candidat(uid):
    candidat = []
    
    candidat.append(candidats.get_candidat_name(uid)) 
    candidat.append(candidats.get_candidat_position(uid)) 
    candidat.append(candidats.get_candidat_skill(uid)) 
    candidat.append(candidats.get_candidat_picture(uid)) 
    return render_template("page_candidat.html", candidat=candidat ) 
    


app.run()


