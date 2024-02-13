# Python : Tout est objet

[![Image de présentation](https://github.com/Mottais/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/Python.PNG?raw=true "Image de présentation")](https://github.com/Mottais/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/Python.PNG?raw=true "Image de présentation")
## Introduction :
 Python est un langage de programmation populaire et puissant, apprécié pour sa simplicité et sa flexibilité.
Une caractéristique fondamentale de Python est que tout y est considéré comme un objet.
Dans cet article,  j'explique la nature des objets mutables et immuables en Python, comment ils sont stockés en mémoire, et comment Python gère les valeurs des variables lorsqu'elles sont passées à des fonctions.

## I ) En Python, tout est un objet, y compris les variables :
 Exemple : les variables de type int sont des instances d'un objet de la classe int.
Illustration :
```python
x = -63
print("Nombre de bit pour définir :", x, "est",x.bit_length())
print("----------------------")
print(x.__doc__)
print("----------------------")
print(x.__repr__())
print(x.__abs__())
print(x.__add__(10))
 
  # Output:
Nombre de bit pour définir : -63 est 6
----------------------
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
----------------------
-63
63
-53
```
Remarque : x = -63  est l'équivalent à  x = int(-63)


## II )  Identification (id) et Type :
 En Python, chaque objet possède un identifiant unique, accessible via la fonction `id()`.
Cet identifiant est l'adresse mémoire de l'objet.
Par exemple :
```python
x = 5
print(id(x)) # Affiche 140455139066224

```
 Chaque objet a un type, qui définit les opérations possibles sur cet objet et comment il est stocké en mémoire.
Le type d'un objet peut être obtenu à l'aide de la fonction `type()`.

Exemple de création d'une chaine de caracteres :
```python
string = "hello"
print(type(string))  # Affiche <class 'str'>
```
Exemple de création de tuple :
```python
tup = (1, 2, 3)
print(type(tup))  # Affiche <class 'tuple'>
```
Exemple de création de set :
```python
s = {1, 2, 3}
print(type(s))  # Affiche <class 'set'>
```
Exemple de création de byte array :
```python
arr = bytearray(b"hello")
print(type(arr))  # Affiche <class 'bytearray'>
```
Exemple de création de dictionnaire :
```python
dict = {"key": "value", "name": "John"}
print(type(dict))  # Affiche <class 'dict'>
```
Exemple de création de nombre complexe :
```python
comp = 3 + 4j
print(type(comp))  # Affiche <class 'complex'>
```


## III)  En Python, les objets peuvent être classés en 2 catégories :

### Objets Mutables :
 Les objets mutables peuvent être modifiés après leur création.
##### Objets mutables : listes, dictionnaires, ensembles, tableaux d'octets.
```python
mon_dictionnaire = {'a': 1, 'b': 2}
print(id(mon_dictionnaire), ":", mon_dictionnaire) 

mon_dictionnaire['c'] = 3
print(id(mon_dictionnaire), ":", mon_dictionnaire)

  # Output:
140699864735744 : {'a': 1, 'b': 2}
140699864735744 : {'a': 1, 'b': 2, 'c': 3}
```


### Objets  Immuables :
Les objets immuables ne peuvent pas être modifiés après leur création..
##### Objets immuables : nombres (int, float, complexe), chaînes de caractères, tuples, ensembles figés (frozen sets), octets (bytes).
Lorsque vous effectuez une opération qui semble modifier un objet immuable, en réalité, Python crée un nouvel objet avec la valeur modifiée.
Illustration :
```python
x = 1
print(id(x), ' : x = ',x)

x = 2
print(id(x), ' : x = ',x)

  # Output:
140574289461488  : x =  1
140574289461520  : x =  2
```

#### Stockage en mémoire des objets immuables :
 Les objets immuables sont stockés en mémoire de manière optimisée.
Les petits entiers et certaines chaînes de caractères sont pré-alloués lors du démarrage de l'interpréteur Python pour améliorer les performances et économiser de la mémoire.

#### Pré-allocation des entiers :
 Python pré-alloue des entiers compris entre les variables **NSMALLPOSINTS**  et **NSMALLNEGINTS**  (de -5 à 256 par défaut) pour éviter de les recréer à chaque utilisation. Cela réduit la consommation de mémoire et améliore les performances lors de la manipulation de nombres entiers courants.

Illustration:
```python
x = 256
x += 1
y = 257
print(id(x))
print(id(y))

# output
139790061919152
139790061919024
```

```python
x = 255
x += 1
y = 256
print(id(x))
print(id(y))

# output
140419464154480
140419464154480
```

#### Cas particulier des Tuples et des Frozen Sets :
 Les tuples et les ensembles figés sont immuables, mais ils peuvent contenir des objets mutables.
Cela signifie que la structure de données ne peut pas être modifiée, mais les objets qu'elle contient peuvent l'être.


## IV) Assignation vs Référencement :
 En Python, l'assignation crée une référence vers l'objet plutôt que de  copier sa valeur.
Cela signifie que plusieurs variables peuvent référencer le même objet. 
Lorsque plusieurs variables référencent le même objet, elles sont appelées des **alias**.
Modifier l'objet via l'un de ces **alias** affectera toutes les références.

Par exemple :
```python
a = [1, 2, 3]
b = a  
b.append(4)
print(a)  # Affiche [1, 2, 3, 4]
```


## V) Comment les arguments sont transmis aux fonctions et ce que cela implique pour les objets mutables et immuables
En Python, les arguments sont transmis aux fonctions de manière référentielle.

Lorsqu' un objet mutable est passé à une fonction, toute modification de cet objet à l'intérieur de la fonction affectera également l'objet à l'extérieur de la fonction.

```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

# output
[1, 2, 3, 4]
```


Lorsqu' un objet immuable est passé  à une fonction,   l'objet original reste inchangé
**Rappel** : lorsque vous effectuez une opération qui semble modifier un objet immuable, en réalité, Python crée un nouvel objet avec la valeur modifiée.
```python
def increment(n):
    n += 1

n = 1
increment(n)
print(n)

# output
1
```


## En conclusion :
Comprendre le concept selon lequel "tout est objet" en Python est essentiel pour écrire un code efficace et évolutif.
En maîtrisant les notions d'identification, de type, de mutabilité et d'immuabilité des objets, ainsi que les subtilités de la gestion de la mémoire et du passage d'arguments aux fonctions, les développeurs peuvent éviter des erreurs et tirer pleinement parti de la puissance et de la flexibilité de Python.