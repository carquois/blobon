[BlobOn](http://blobon.com)
=================

La création de Blobon en tant que nouveau leader de la recherche internet comporte plusieurs défis technologiques.

Pour présenter des résultats de recherche du Web, nous devons donc inventer un outil qui va répertorier les pages et y retourner souvent pour voir les nouvelles pages. 

Normalement, ces outils s'appellent des "crawlers". Par contre, les crawlers qui existent actuellement ne permettent pas de créer une base de donée à partir du fichier texte qu'il génèrent. Notre premier défi technologique sera donc de créer une application autonomne qui pourra répertorier le Web. 

Crawler open-source : Lynx.

Moteurs de recherche connus : Google, Bing

Botins : Yahoo

-------

Ensuite, les résultats doivent être sauvegardés en quelque part qui permettra de les traiter. En ce moment, aucune base de donnée accessible ne permet de traiter cette quantité de résultats de manière efficace. 

Liste des bases de données :

SQLite est un fichier texte qui est particulièrement adapté pour des très petites base de données.

*MySQL* est une base de donnée transactionelle qui comporte une limite de 1 000 000 de lignes avant de devenir inefficace et la base de donnée devient complètement non-fonctionnelle à partir de 10 000 000 de lignes. Bien que ce soit la base de donnée la plus utilisée, elle est surtout utilisée pour des petits et moyens sites informatifs. Sa grande popularité est en partie dûe au fait que c'est la base de donnée utilisée par l'outil de gestion de contenu *Wordpress*  

*POSTGRE* est une version améliorée de *MySQL*, open-source et transactionnelle. Le traitement des informations se fait de manière efficace, mais la limite de lignes que peux contenir cette base de donnée reste de beaucoup trop limitée pour contenir l'internet au complet.

*Oracle* est la meilleure solution de base de donnée. Elle est utilisée par la plupart des grandes implémentations comment les services transactionnels banquaire, les gouvernements et les universités. Par contre, le code source est fermé et donc aucune modification n'est possible. Cette solution n'est donc pas adaptée non plus. 

Il ne reste qu'une seule option, coder notre propre outil de base de donnée pour contenir toutes ces données. L'outil de base de donnée serait donc codé avec les dernières technologies et les meilleurs language de programmation. 


TRUC À AJOUTER : 

* Le nombre de pages sur le Web


Auteur
-------

**Gabriel Dancause**

+ http://facebook.com/GabrielDancause
+ http://twitter.com/GabrielDancause
+ http://github.com/GabrielDancause


Copyright and license
---------------------

Copyright 2013 Blobon, Inc.

