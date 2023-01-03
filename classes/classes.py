import json

class CandidatManager:
    def __init__(self, path):
        self.path = path
        
    
    def candidat_json(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
        return data
    
    
    def get_candidat_id(self,id_candidat):
        candidat_id = self.candidat_json()
        
        for candidat in candidat_id:
            if candidat['id'] == id_candidat:
                return candidat
            
            
    def get_candidat_position(self, id):
        candidat_id = self.candidat_json()
        
        for candidat in candidat_id:
            if candidat['id'] == id:
                return candidat["position"]
            
            
    def get_candidat_name(self, id):
        candidat_id = self.candidat_json()
        
        for candidat in candidat_id:
            if candidat['id'] == id:
                return candidat["name"]
            
            
    def get_candidat_skill(self, id):
        candidat_id = self.candidat_json()
        
        for candidat in candidat_id:
            if candidat['id'] == id:
                return candidat["skills"]
            
            
    def get_candidat_picture(self, id):
        candidat_id = self.candidat_json()
        
        for candidat in candidat_id:
            if candidat['id'] == id:
                return candidat["picture"]
            
            
    def  search_skill(self,skills_candidat):
        candidat_id = self.candidat_json()
        candidat_skill = []
        for candidat in candidat_id:
            if skills_candidat.lower() in candidat['skills'].lower():
                candidat_skill.append(candidat)
        
        return candidat_skill
            
            
   
        
        
