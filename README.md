# Module pathfinder 2 pour Foundry VTT

Ce dépôt est un module pour foundry VTT (https://foundryvtt.com/).
Le module améliore le système pathfinder2 pour le français.

Expérimentations en cours pour:
* Actions

## Traducteurs

* Les fichiers à traduire se trouvent dans le répertoire [data](data/)
* Chaque fichier correspond à une entrée à traduire
  * Pour chaque fichier, il faut inscrire le nom et la description en se basant sur les textes d'origine (en anglais)
  * Ne pas supprimer les textes d'orgine!
  * Voir [data/instructions.md](data/instructions.md) pour plus d'instructions concernant les fichiers de traduction

## Utilisation

Pour appliquer les traductions, il faut installer le module Babele et pointer vers le répertoire [babele](babele/). Instructions détaillées
* Télécharger une release de dépôt: [Releases](https://github.com/SvenWerlen/foundryvtt-pathfinder2-fr/releases)
* Désarchiver le tout dans un répertoire accessible depuis Foundry VTT, par exemple `[Foundry]/resources/app/public/`
* Installer le module [Babele](https://gitlab.com/riccisi/foundryvtt-babele)
* Activer le module depusi Foundry VTT
* Configurer le module et pointer les traductions vers le répertoire `babele/`
