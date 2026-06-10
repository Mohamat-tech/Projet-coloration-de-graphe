import csv

def exporter_csv(planning, filename="planning.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Creneau", "Salle", "UE", "Effectif"])
        for creneau, salles in sorted(planning.items()):
            for salle, (ue, effectif) in salles.items():
                writer.writerow([creneau, salle, ue, effectif])
    print(f"✅ Planning exporté dans {filename}")
