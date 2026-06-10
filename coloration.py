from collections import defaultdict
import time

class Coloration:
    @staticmethod
    def welsh_powell(graphe):
        sommets_tries = sorted(graphe.ues, key=lambda ue: graphe.degre(ue), reverse=True)
        couleur = {}
        for ue in sommets_tries:
            utilisées = {couleur[v] for v in graphe.liste_adj[ue] if v in couleur}
            for c in range(len(sommets_tries)):
                if c not in utilisées:
                    couleur[ue] = c
                    break
        return couleur

    @staticmethod
    def dsatur(graphe):
        couleur = {}
        saturation = defaultdict(int)
        degres = {ue: graphe.degre(ue) for ue in graphe.ues}

        while len(couleur) < len(graphe.ues):
            non_colores = [ue for ue in graphe.ues if ue not in couleur]
            ue_a_colorer = max(non_colores, key=lambda ue: (saturation[ue], degres[ue]))

            utilisées = {couleur[v] for v in graphe.liste_adj[ue_a_colorer] if v in couleur}
            for c in range(len(graphe.ues)):
                if c not in utilisées:
                    couleur[ue_a_colorer] = c
                    break

            # Mise à jour saturation voisins
            for v in graphe.liste_adj[ue_a_colorer]:
                if v not in couleur:
                    saturation[v] = len({couleur[voisin] for voisin in graphe.liste_adj[v] if voisin in couleur})
        return couleur

    @staticmethod
    def comparer(graphe):
        start = time.time()
        c_wp = Coloration.welsh_powell(graphe)
        t_wp = time.time() - start

        start = time.time()
        c_ds = Coloration.dsatur(graphe)
        t_ds = time.time() - start

        print("Welsh-Powell :", len(set(c_wp.values())), "créneaux, temps =", round(t_wp, 5))
        print("DSATUR :", len(set(c_ds.values())), "créneaux, temps =", round(t_ds, 5))
        return c_wp, c_ds, t_wp, t_ds
