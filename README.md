# Zadania Python

Skrypty do dwóch zadań w języku Python. 

Treść pierwszego zadania: 

Write a program that reads a text file and then makes a copy of it,
in which the order of the letters in each word is randomly changed except for
first and last letter of the word.


Treść drugiego zadania:

Write a program to validate the PESEL number according to the official
format specification. Prepare unit tests that check several data
incorrect data and at least one correct pesel number.


## Zadanie 1 
Zadanie znajduje się w folderze "Zadanie1".
Uruchomienie odbywa się za pomocą linii komend w folderze, w którym znajduje się skrypt "zadanie1.py"
```python
python zadanie1.py x y
```
Gdzie: x - plik wejściowy txt; y - plik wyjściowy txt (Opcjonalnie, domyślnie - Sample.txt)
       
## Zadanie 2 
Zadanie znajduje się w folderze "Zadanie2".
Uruchomienie odbywa się za pomocą linii komend w folderze, w którym znajduje się skrypt "zadanie2.py"
```python
python zadanie2.py x
```
Gdzie: x - numer pesel

W przypadku uruchomienia predefiniowanych testów, również można uruchomić je za pomocą linii komend
```python
python -m pytest tests.py
```
## Potrzebne biblioteki
Lista niezbędnych bibliotek do uruchomienia skryptów, znajduje się w folderze requirements.txt, a zainstalować można je za pomocą komendy
```
pip install -r requirements.txt
