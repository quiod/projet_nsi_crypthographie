class Graphe:
    
    def __init__(self):
        self.adj = {}
    
    def ajouter_sommet(self,s):
        if s not in self.adj:
            self.adj[s] = set()
            
    def ajouter_arc(self,s1,s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)
    
    def arc(self, s1,s2):
        return s2 in self.adj[s1]
    
    def sommets(self):
        return list(self.adj)
    
    def voisins(self,s):
        return self.adj[s]
    
    def nb_sommets(self):
        return len(self.adj)
    
    def degre(self,s):
        return len(self.adj[s])
    
    def nb_arcs(self):
        n = 0
        for i in self.adj:
            n+=degre(self.adj[i])
        return n
    
    def afficher(self):
        for i in self.adj.keys():
            print(i,"|",self.adj[i])
            
def parcours(g,vus,s):
    if s not in vus:
        vus.add(s)
        for i in g.voisins(s):
            parcours(g,vus,i)
            
def existe_chemin(g,u,v):
    vus = set()
    parcours(g,vus,u)
    return v in vus
BLANC, GRIS, NOIR = 1,2,3
def parcours_cy(g,couleur,s):
    if couleur[s] == GRIS:
        return True
    if couleur[s] == NOIR:
        return False
    couleur[s] = GRIS
    for v in g.voisins(s):
        if parcours_cy(g,couleur,v):
            return True
    return False

def cycle(g):
    couleur = {}
    for s in g.sommets():
        couleur[s] = BLANC
    for s in g.sommets():
        if parcours_cy(g,couleur,s):
            return True
    return False

g = Graphe()
for i in range(10):    
    g.ajouter_sommet(i)
for i in range(9):
    g.ajouter_arc(i, (i+1)%10)
g.ajouter_arc(9, 4)

g.afficher()
print(cycle(g))

            
    



    
