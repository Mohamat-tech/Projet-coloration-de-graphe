"""Module d'optimisation avec recuit simulé"""

import random
import math
import time

class RecuitSimule:
    def __init__(self, graphe, k_max=1000, t0=100, alpha=0.99):
        self.graphe = graphe
        self.k_max = k_max
        self.t0 = t0
        self.alpha = alpha
    
    def energie(self, coloration):
        """Calcule le coût d'une coloration (nombre de conflits + nombre de couleurs)"""
        conflits = 0
        for ue in self.graphe.ues:
            for voisin in self.graphe.liste_adj[ue]:
                if coloration.get(ue) == coloration.get(voisin):
                    conflits += 1
        nb_couleurs = len(set(coloration.values()))
        # Pénaliser fortement les conflits
        return conflits * 1000 + nb_couleurs
    
    def perturbation(self, coloration, k):
        """Génère une nouvelle coloration par perturbation"""
        nouvelle = coloration.copy()
        # Changer la couleur d'un sommet aléatoire
        ue = random.choice(self.graphe.ues)
        # Nouvelle couleur aléatoire
        max_couleur = max(coloration.values()) + 1
        nouvelle[ue] = random.randint(0, max_couleur)
        return nouvelle
    
    def optimiser(self, coloration_initiale):
        """Algorithme de recuit simulé"""
        courant = coloration_initiale.copy()
        E_courant = self.energie(courant)
        
        meilleur = courant.copy()
        E_meilleur = E_courant
        
        t = self.t0
        
        for k in range(self.k_max):
            # Générer un voisin
            voisin = self.perturbation(courant, k)
            E_voisin = self.energie(voisin)
            
            # Accepter ou rejeter
            if E_voisin < E_courant:
                courant = voisin
                E_courant = E_voisin
            else:
                delta = E_voisin - E_courant
                p = math.exp(-delta / t)
                if random.random() < p:
                    courant = voisin
                    E_courant = E_voisin
            
            # Mettre à jour le meilleur
            if E_courant < E_meilleur:
                meilleur = courant.copy()
                E_meilleur = E_courant
            
            # Refroidissement
            t *= self.alpha
        
        # Recolorer pour avoir des couleurs consécutives
        meilleur = self.recolorer(meilleur)
        return meilleur
    
    def recolorer(self, coloration):
        """Re-numérote les couleurs pour qu'elles soient consécutives"""
        mapping = {}
        nouvelle = {}
        for ue, c in coloration.items():
            if c not in mapping:
                mapping[c] = len(mapping)
            nouvelle[ue] = mapping[c]
        return nouvelle

def optimiser_avec_recuit(graphe, coloration_initiale):
    """Fonction wrapper pour l'optimisation par recuit"""
    print("\n" + "="*60)
    print("OPTIMISATION PAR RECUIT SIMULÉ (BONUS)")
    print("="*60)
    
    start = time.time()
    recuit = RecuitSimule(graphe, k_max=2000, t0=100, alpha=0.995)
    coloration_opt = recuit.optimiser(coloration_initiale)
    temps = time.time() - start
    
    nb_creneaux = len(set(coloration_opt.values()))
    print(f"Créneaux après optimisation: {nb_creneaux}")
    print(f"Temps d'optimisation: {temps:.4f} secondes")
    
    return coloration_opt
