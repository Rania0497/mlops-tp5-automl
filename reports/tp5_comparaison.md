# Modele manuel ou modele AutoML ?

| Critere                    | Manuel (rf 500/16)                                   | AutoML (FLAML 90 s)                                  |
|----------------------------|------------------------------------------------------|------------------------------------------------------|
| Famille de modele          | foret aleatoire                                      | xgboost                                              |
| F1 sur le jeu de test      | 0.8669                                               | 0.8582                                               |
| Temps de recherche machine | 1.9 s (entrainement)                                 | 90.7 s                                               |
| Temps humain (estimation)  | environ 30 min (choix et essais des reglages)        | environ 5 min (lancer le script)                     |
| Latence mediane (ms)       | 71                                                   | 33                                                   |
| Latence p95 (ms)           | 121                                                  | 49                                                   |
| Taille du fichier (Mo)     | 13.37                                                | 0.29                                                 |
| Explicabilite              | importance des variables, 500 arbres, profondeur 16  | importance des variables, arbres boostes (parametres | 
|                            |                                                      |   cfg_ visibles dans le run MLflow)                  |

## Decision : quel modele mettre en production, et pourquoi ?

Je mettrais le modele AutoML (xgboost) en production.
Son F1 est legerement inferieur (0.8582 contre 0.8669), un ecart faible mesure sur un seul decoupage test.
Il repond environ deux fois plus vite (33 ms contre 71 ms en mediane, 49 ms contre 121 ms en p95).
Il est environ 46 fois plus leger (0.29 Mo contre 13.37 Mo), donc plus facile a conteneuriser et a deployer.
Les deux modeles restent explicables par l'importance des variables, et l'AutoML demande beaucoup moins de temps humain.