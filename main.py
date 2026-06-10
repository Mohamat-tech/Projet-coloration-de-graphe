from ue_data import ues, etudiants, salles, interdictions
from graphe import GrapheConflits
from coloration import Coloration
from affectation import AffectationSalles
from planning import exporter_csv

# Partie 1
g = GrapheConflits(ues, etudiants)
stats = g.stats()
print("Statistiques :", stats)
g.visualiser(titre="Graphe des conflits (avant coloration)")

# Partie 2
c_wp, c_ds, t_wp, t_ds = Coloration.comparer(g)

# Partie 3
affect = AffectationSalles(ues, salles)
planning_wp = affect.affecter(c_wp)
affect.audit(c_wp, interdictions)
exporter_csv(planning_wp, "planning_welsh_powell.csv")

# Bonus : visualisation colorée
g.visualiser(coloration=c_wp, titre="Coloration Welsh-Powell")
