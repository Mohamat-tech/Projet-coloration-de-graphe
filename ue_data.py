# ue_data.py
ues = [
    {"id": "UE1", "effectif": 120, "type_salle": "labo", "enseignant": "ProfA", "filiere": "info"},
    {"id": "UE2", "effectif": 80, "type_salle": "standard", "enseignant": "ProfB", "filiere": "maths"},
    {"id": "UE3", "effectif": 90, "type_salle": "labo", "enseignant": "ProfA", "filiere": "info"},
    {"id": "UE4", "effectif": 200, "type_salle": "standard", "enseignant": "ProfC", "filiere": "maths"},
]

etudiants = [
    {"id": 1, "ues": ["UE1", "UE2"]},
    {"id": 2, "ues": ["UE1", "UE3"]},
    {"id": 3, "ues": ["UE2", "UE4"]},
    {"id": 4, "ues": ["UE3", "UE4"]},
]

salles = [
    {"nom": "Amphi A", "capacite": 250, "type": "standard"},
    {"nom": "Labo B", "capacite": 100, "type": "labo"},
]

interdictions = [("UE1", "UE4")]
