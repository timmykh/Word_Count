# Word_Count
Le projet consiste à :
1- Instancier l'API de spark pour les RDD (spark context). 
2- Importer le fichier sample.txt (pas de path en dur)
3- Réalisation  du word count.
4- Affichage du résultat du comptage sous la forme de Tuple (clé, valeur) 
5- faire un export de la RDD résultante sous format txt dans un nouveau répertoire indication (rdd.coalesce(1).saveAsTextFile("Path to new File")) 
(Bonus) 6- Rédiger une documentation avec une capture de la console.