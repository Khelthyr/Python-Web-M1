# Python-Web-M1

# Commande pour lancer Application
`streamlit run file.py`

## TP1 : réalisation d'une data app 

votre mission est de construire une petite application de visualisation interactive de données avec l’outil Streamlit vu au chapitre précédent, qui contiendra les fonctionnalités suivantes :   

* Charger des jeux de données (au moins 2) présents dans votre répertoire local
	* il faudra donc que votre application pointe un chemin et sorte les fichier (dataset) du repertoire pointé. Vous utiliserez pour cela le module `os` de python.
* Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur
* Afficher le nom des colonnes du dataset 
* Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées 
* La shape du dataset, par lignes et par colonnes
* Afficher les statistiques descriptives du dataset
* Afficher plusieurs type de graphique dans une partie visualisation avec notamment : 
	* Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
	* Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)

Et enfin une dernière partie dite « visualisation personnalisable » qui permettra de : 

* Sélectionner le type de graphique à tracer
Sélectionner des colonnes dans le jeux de données afin de générer le graphique
* **(bonus)**À noter que suivant certain jeux de données il y aura des graphiques qui n’auront pas de sens capturez les dans des exceptions 🧐


## TP2 : Flask 

**Quickstart** 
Ecrire une application flask suivant le modele ci-dessus avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello DC"
* une route qui renvoie "hello name", ou name est une variable string 
	* on devra donc trouver "hello name" à la route (http:localhost:5000/ma_route/name) avec la possibilité de changer la variable name. 
* refaite la meme chose en ajoutant un template 

**Contexte**

Vous avez répondu à l'appel d'offre d'une mairie qui consiste à digitaliser la bibliothèque de la commune. Il faudra pour cela proposer un "catalogue" en ligne de leur ressources et donner la possibilité au utilisateur du site de faire des recherches de livre. On supposera que la bibliothèque nous met à disposition ces livres via un fichier `.json` ci-dessous. 
Vous devez donc construire une api (application flask) avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello my app"
* instancier une variable `book` dans votre aopplication tel que : 
```
book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
```
* faite une route `/api/books` avec une méthode `GET` qui retourne cette variable sous forme de json 
* faite une route qui retourne un book selon son `id` 
* faite une route qui retourne un book selon son titre 
* chager le fichier [books.json](https://drive.google.com/file/d/1UdRCm5d5UAPnfjGes_rHZl2kDQ9NNAsG/view?usp=sharing) et faite de même avec ce fichier
* **(bonus)** écrire un template pour le résultat de la recherche


## TP Docker & Flask 

**Quickstart Docker** 

* comprendre la différence entre images et containers et à quoi sert un `Dockerfile` 
* installer docker sur votre machine (Ubuntu de préférence, si pas de machine ubuntu vous pouvez faire un double boot ou bien installer une VM en profitant de l'accès gratuit d'un éditeur cloud GCP, Azur, AWS...) 
* lancer votre premier container ubuntu, l'équivalent du *hello-world* de docker  
* regarder si votre container est bien lancer 
* faire un résumé type `cheat sheet` des principales commandes dockers relatives aux images et containers
	* expliquer les commandes docker `build`, `run` et `exec`
	* expliquer ce qu'est un port dans un container
* vérifier en vous connectant à votre container qu'il est bien `up` et qu'il s'aggit bien 
* **(bonus)** lancer un petit container applicatif en python avec docker 

**Docker et Python**

* écrire un Dockerfile contenant : 
	* Une image ubuntu ou python 
	* installer python3, pip3 et vim 
	* une installation automatique du fichier `requirements.txt` que vous écrirez à la racine de votre application. Renseignez vous sur ce fichier `requirements.txt`, que fait il, pourquoi est il utile? 
	* un repertoire app (dans lequel se trouvera votre application flask) 
	* une exposition du port de votre choix
	* pour finir le container devra lancer votre application flask sur le port de votre choix précédemment exposé.  
	* **(bonus)** déployer votre application sur le cloud gratuit [heroku](https://www.heroku.com)

	
**Projet Bonus facultastif à rendre pour le 02/12**
Coder un site type vitrine/portfolio en flask et le déployer avec github pages 
