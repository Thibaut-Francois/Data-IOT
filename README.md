"# Data-IOT" 

Notre projet est simple : sélectionner un nombre, une couleur et un pays sur un site web
et faire clignoter une led autant de fois que le nombre indiqué et de la couleur 
précédemment sélectionnée, ainsi que faire apparaitre sur un panneau led le drapeau du
pays sélectionné.

Pour ce faire nous utilisons un serveur fait sur NodeJs, des requêtes envoyées via Axios
et le urequest de Python sur un raspberry pi pour utiliser des GET pour récupérer les
informations.

Le panneau led affiche bien le pays demandé et la led clignote le bon nombre de fois
mais ils nous a manquer un peu de temps pour faire briller le led RGB de la couleur
séléctionnée.

Schéma technique dans le repo
Vidéo dans le repo (désolé pour le son en fond). Moments clés :
    0:02 entrée du chiffre 5 et du pays "France"
    0:11 verification de l'envoie des infromations dans le serveur Node
    0:15 lancement du programe python
    0:20 le panneau led brille aux couleurs de la France
    0:24 la led brille 5 fois d'affilées et recommence après quelques secondes

Membres du groupe : Thibaut François et Mehdi Bellam