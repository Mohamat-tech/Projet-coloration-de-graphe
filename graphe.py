import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

class GrapheConflits:
    def __init__(self, ues, etudiants):
        self.ues = [ue["id"] for ue in ues]
        self.n = len(self.ues)
        self.ue_index = {ue["id"]: i for i, ue in enumerate(ues)}
        self.mat_adj = [[0]*self.n for _ in range(self.n)]
        self.liste_adj = {ue["id"]: [] for ue in ues}
        self.construire(ues, etudiants)

    def construire(self, ues, etudiants):
        # Créer un mapping étudiant -> liste d'UE
        for etudiant in etudiants:
            ues_etudiant = etudiant["ues"]
            for u1, u2 in combinations(ues_etudiant, 2):
                self.ajouter_arete(u1, u2)

    def ajouter_arete(self, u1, u2):
        i, j = self.ue_index[u1], self.ue_index[u2]
        if not self.mat_adj[i][j]:
            self.mat_adj[i][j] = self.mat_adj[j][i] = 1
            self.liste_adj[u1].append(u2)
            self.liste_adj[u2].append(u1)

    def degre(self, ue):
        return len(self.liste_adj[ue])

    def degres_tous(self):
        return {ue: self.degre(ue) for ue in self.ues}

    def stats(self):
        nb_aretes = sum(self.degre(ue) for ue in self.ues) // 2
        return {
            "sommets": self.n,
            "aretes": nb_aretes,
            "degres": self.degres_tous()
        }

    def visualiser(self, coloration=None, titre="Graphe des conflits"):
        G = nx.Graph()
        G.add_nodes_from(self.ues)
        for u1 in self.liste_adj:
            for u2 in self.liste_adj[u1]:
                if u1 < u2:
                    G.add_edge(u1, u2)

        pos = nx.spring_layout(G)
        if coloration:
            couleurs = [coloration[ue] for ue in self.ues]
            nx.draw(G, pos, node_color=couleurs, with_labels=True, cmap=plt.cm.tab20, node_size=800)
        else:
            nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800)
        plt.title(titre)
        plt.show()
