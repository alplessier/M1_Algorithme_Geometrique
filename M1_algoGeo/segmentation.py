import halfedge_mesh
import math

# .off are supported
# mesh = maillage 

mesh = halfedge_mesh.HalfedgeMesh("tests/data/cube_seg.off")
filename = "tests/data/cube_seg2.off"
filename2 = "tests/data/cube_seg3.off"
filename3 = "tests/data/cube_seg4.off"

def moyenne_angle():

    list = [] 

    for f in mesh.facets:
        st1 = f.halfedge.get_angle_normal()
        nd2 = f.halfedge.next.get_angle_normal()
        rd3 = f.halfedge.next.next.get_angle_normal()

        result = (st1 + nd2 + rd3) / 3
        list.append(result)
        
    return list

def mettre_degre(l):

    for i in l:
        print((i/math.pi)*180)

def moyenne_angle_min_max(l):

    l2 = []
    
    for i in l:
      j = (i-min(l))/(max(l)-min(l))
      l2.append(truncate(j))
    
    return l2

def truncate(num):
    temp = str(num)
    temp2 = ""
    if temp == "0.0":
      temp2 = "0.000"
    elif temp == "1.0":
      temp2 = "1.000"
    else:
      for i in range(5):
        temp2 += temp[i]
    return temp2

def truncate2(num, seuil):
  if (num < seuil):
    return "1.000"
  else:
    return "0.000"

def colorier(filename, l, type):
    mesh.save_vertices(filename, l, type)

def coloriertwoClass(l):

    l2 = []

    #valeur déjà entre 0 et 1
    moyenne = 0.0
    for j in l:
      moyenne += float(j)
    moyenne = moyenne / len(l)
    
    for j in l:
      l2.append(truncate2(float(j), moyenne))

    return l2

#Mediane
def coloriertwoClass2(l):
     
    l2 = []
    lCopy = []
    lCopy = l.copy()
    lCopy.sort()
    
    if(len(lCopy)%2 == 1):
        mediane = float(lCopy[round(len(lCopy)/2)])
    else:
        for i in range(len(lCopy)):
          if(i == int(len(lCopy)/2)):
            mediane = (float(lCopy[i]) + float(lCopy[i+1]))/2
        

    for j in l:
        l2.append(truncate2(float(j), mediane))
    
    return l2

def colorier2(filename, l, type):
    mesh.save_vertices(filename, l, type)
    


valeurs = moyenne_angle()
valeurs = moyenne_angle_min_max(valeurs)

# Moyenne angles
#colorier(filename, valeurs, "firstSeg")

# 2 classes avec Seuil = Moyenne
#valeurs2 = coloriertwoClass(valeurs)
#colorier2(filename2, valeurs2, "TwoClassSeg")

# 2 classes avec Seuil = Mediane
valeurs3 = coloriertwoClass2(valeurs)
colorier2(filename3, valeurs3, "TwoClassSeg")




