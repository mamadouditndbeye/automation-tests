# language: fr
Fonctionnalité: Recherche sur DuckDuckGo

  Plan du scénario: L'utilisateur effectue plusieurs recherches
    Étant donné je suis sur la page d'accueil de DuckDuckGo
    Quand je recherche "<terme>"
    Alors le titre de la page contient "<terme>"

    Exemples:
      | terme                      |
      | automatisation de tests QA |
      | Selenium Python            |
      | outil Xray                 |