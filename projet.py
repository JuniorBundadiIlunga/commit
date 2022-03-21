fonction tri()

    entier: tableauA[],tableauB[]tableauFussion[],tailleTabA,tailleTabB,tailleTabFussion,i,j,m,temp
    debut
        ecrire "entrer la taille du tableau A"
        lire tailleTabA
        ecrire "entrer la taille du tableau B"
        lire tableauB
        pour i d 0 a tailleTabA-1:
            ecrire "entrer l'element du tableau"
            lire tableauA[i]
        finpour
        pour i de 0 a tailleTabB-1 faire:
            ecrire "entrer l'element du tableau"
            lire tableauB[i]
        finpour
        pour i de 0 tableauA[] faire:
            tableauFussion=tableauA[i]
            j=i
        finpour
        j=j+1
        i=0
        pour i de 0 a tableauB faire:
            tableauFussion[j]=tableauB[i]
            j++
        finpour
        pour de 0 a tableauFussion faire:
            tailleTabFussion++
        j=0
        i=0
        pour i de 0 a tailleTabFussion-2 faire:
            m=i
            pour j de i+1 a tailleTabFussion-1 faire:
                si tableauFussion[j]<tableauFussion[m] alors
                m=j
                finsi
            finpour
            temp=tableauFussion[m]
            tailleTabFussion=tailleTabFussion[i]
            tab[i]temp
        finpour

               return tableauFussion
fin

B) la complexité
temps O(n3)
espace O(1)i,j,m,temp
////////////////////////////////////////////////////////////////////////////////////////

fonction cercle():
    entier:x_cercleA,y_cercleA,r_cercleA,x_cercleB,y_cercleB,r_cercleB,


    debut  
        ecrire "entrer la coordonnée x"
        lire x_cercleA
        ecrire "entrer la coordonnée y"
        lire y_cercleA
        ecrire "entrer la valeur du rayon"
        lire r_cercleA
        //
         ecrire "entrer la coordonnée x"
        lire x_cercleB
        ecrire "entrer la coordonnée y"
        lire y_cercleB
        ecrire "entrer la valeur du rayon"
        lire r_cercleB

        si r_cercleA == r_cercleB:
            ecrire " ils sont en intersections"
            return vrai
        sinon
            ecrire " ils ne sont pas en intersections"
            return vrai
        finsi


/////
B) le complexité
O(n)