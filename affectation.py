class AffectationSalles:
    def __init__(self, ues, salles):
        self.ues = {ue["id"]: ue for ue in ues}
        self.salles = salles

    def affecter(self, coloration):
        planning = {}
        # On regroupe les UE par créneau
        creneaux = {}
        for ue, cr in coloration.items():
            creneaux.setdefault(cr, []).append(ue)

        for cr, ues_creneau in creneaux.items():
            planning[cr] = {}
            for ue in ues_creneau:
                ue_data = self.ues[ue]
                # Choisir salle
                salle_ok = None
                for salle in self.salles:
                    if salle["capacite"] >= ue_data["effectif"] and salle["type"] == ue_data["type_salle"]:
                        if salle["nom"] not in planning[cr]:
                            salle_ok = salle["nom"]
                            break
                if salle_ok:
                    planning[cr][salle_ok] = (ue, ue_data["effectif"])
                else:
                    print(f"⚠️  Impossible d'affecter {ue} (créneau {cr}) : pas de salle dispo.")
        return planning

    def audit(self, coloration, interdictions):
        print("\n=== AUDIT ===")
        creneaux_ues = {}
        for ue, cr in coloration.items():
            creneaux_ues.setdefault(cr, []).append(ue)

        # Vérifier interdictions même créneau
        ok = True
        for u1, u2 in interdictions:
            if coloration.get(u1) == coloration.get(u2):
                print(f"❌ Interdiction violée : {u1} et {u2} même créneau {coloration[u1]}")
                ok = False
        if ok:
            print("✓ Aucune interdiction violée.")
        print("Nombre de créneaux utilisés :", len(set(coloration.values())))
