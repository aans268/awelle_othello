# Awalé & Othello - IA de jeux

## 📋 Description
Implémentation d'intelligences artificielles pour les jeux de plateau **Awalé** et **Othello**. Développé dans le cadre d'une UE Intelligence Artificielle. Le projet compare différents algorithmes de décision (MinMax, Alpha-Beta, algorithme génétique) et mesure leurs performances.

**Contexte**: Projet académique - Intelligence Artificielle

## 🚀 Technologies
- **Langage**: Python 3
- **Algorithmes**: MinMax, Alpha-Beta, Algorithme génétique
- **Architecture**: Moteur de jeu modulaire avec joueurs pluggables

## 📁 Structure
```
LU2IN013/
├── game.py                    # Moteur de jeu générique
├── Awele/
│   ├── awele.py              # Règles du jeu Awalé
│   ├── main.py               # Point d'entrée + benchmarks
│   └── Joueurs/              # Stratégies d'IA
│       ├── joueur_humain.py
│       ├── joueur_aleatoire.py
│       ├── joueur_min_max.py
│       ├── jab.py            # IA avec apprentissage
│       └── oracle.py         # IA optimale
└── Othello/
    ├── othello.py            # Règles du jeu Othello
    ├── main.py               # Point d'entrée + benchmarks
    └── Joueurs/              # Stratégies d'IA
        ├── joueur_humain.py
        ├── joueur_aleatoire.py
        ├── joueur_min_max.py
        └── joueur_alpha_beta.py
```

## ⚙️ Installation & Usage

### Prérequis
```bash
python3
```

### Lancer une partie d'Awalé
```bash
cd LU2IN013/Awele
python3 main.py
```

### Lancer une partie d'Othello
```bash
cd LU2IN013/Othello
python3 main.py
```

### Configuration
Modifier les joueurs dans `main.py`:
```python
game.joueur1 = joueur_alpha_beta  # IA Alpha-Beta
game.joueur2 = joueur_humain      # Joueur humain
```

## 🎯 Fonctionnalités principales

### Moteur de jeu générique
- Architecture modulaire permettant de brancher différents jeux
- Gestion des coups valides, scores, fin de partie
- Interface terminal avec affichage coloré

### IA implémentées
- **Joueur aléatoire**: Coups aléatoires (baseline)
- **MinMax**: Exploration exhaustive avec profondeur configurable
- **Alpha-Beta**: Élagage pour optimiser MinMax
- **Algorithme génétique**: Optimisation des poids par évolution face à l'oracle (Awalé uniquement)

### Système de benchmark
- Fonction `nparties(n)`: Fait jouer n parties et calcule le winrate
- Alternance des joueurs pour équité
- Mesure du temps d'exécution

## 📊 Résultats
- **MinMax vs Aléatoire**: ~90% de victoires (profondeur 3)
- **Alpha-Beta vs MinMax**: Performances équivalentes, temps divisé par ~3
- **Algo génétique vs Oracle**: Évolution des poids pour améliorer le winrate

## 📝 Notes
- Limite de 100 tours pour Awalé (éviter parties infinies)
- Limite de 50 tours pour Othello
- Profondeur d'exploration configurable selon temps de calcul souhaité
