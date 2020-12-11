 # Word_Count

 Le projet consiste à :

   1- Instancier l'API de spark pour les RDD (spark context). 
   2- Importer le fichier sample.txt (pas de path en dur)
   3- Réalisation  du word count.
   4- Affichage du résultat du comptage sous la forme de Tuple (clé, valeur) 
   5- faire un export de la RDD résultante sous format txt dans un nouveau répertoire indication (rdd.coalesce(1).saveAsTextFile("Path to new File")) 
   (Bonus) 6- Rédiger une documentation avec une capture de la console.
   

  Ce code a pour objectif de compter le nombre d'occurence des mots contenus dans un texte. Nous l'avons appliquer au fichier sample.txt.
  
  • Dans le CMD, il suffit d'écrire cette commande pour compiler avec Spark le programme. Néanmoins il faut enregistrer ua préalable le  fichier python dans le dossier source.

 ![Sans titre1](https://user-images.githubusercontent.com/71505484/101961127-57c78d80-3c09-11eb-82f5-bdd9a1b37b24.png)
 ![Sans titre2](https://user-images.githubusercontent.com/71505484/101961897-07e9c600-3c0b-11eb-9a61-0fbcab3037e5.png)
 
  • Les résultats sont alors affichés dans la console CMD.

 ![Sans titre](https://user-images.githubusercontent.com/71505484/101960495-da4f4d80-3c07-11eb-8a66-6c97d4910743.png)
 
 • Les résultats sont dans le dossier Resultat.txt, en particuler dans le fichier part-00000.txt
 
 ![Sans titre3](https://user-images.githubusercontent.com/71505484/101961537-331fe580-3c0a-11eb-9843-a686e01f0dc3.png)
 
