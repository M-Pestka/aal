# Projekt AAL

Michał Pestka

## Opis problemu

(Numer zadania 9)

Treść zadania: 

> Tutaj idzie treść zadania. 

Problem postawiony w zadaniu polega więc na stworzeniu specyficznego rodzaju drzewa rozpinającego. 

**Klasyczne drzewo rozpinające** 
Problem drzewa rozpinającego polega na znalezieniu sieci połączneń nie zawierającej cykli która łączy wszystkie wierzchołki, dodatkowo spełniając pewnie kryterium.  Zwykle szukamy drzewa o jaknajniższej sumie wag krawędzi.

**Nasze drzewo rozpinające**
W zadaniu chodzi o znalezienie drzewa rozpinającego które maksymalizuje wagę krawędzi o najniższej wadze. 

**Algorytm Kruskala**

Okazuje się że Algorytm kruskala, który służy do znajdowania klasycznego drzewa rozpinającego, rozwiązuje problem dokładnie odwrotny do zadanego. Wystarczy więc zamienić znajdowanie najtańszej krawędzi na szukanie najdroższej.

## Metody rozwiązania

Rozwiązanie zostało napisane w języku Python3. Dzieli się na 2 części:

* Cześć zawieracjąca algorytm
* Część zawierająca algorytm

### Algorytm rozwiązania

Zgodnie z tym, co zostało napisane powyżej, użyłem niznacznie zmodyfikowanego algorytmu Kruskala.

**Algorytm Kruskala**
Algortm Kruskala jest bardzo prosty. Kroki algorytmu:

* Utworzenie lasu (zbioru drzew) w którym każdy z wierzchołków jest osobnym drzewem.
* Iteracja po zbiorze krawędzi zaczynając od krawędzi o najmniejszej wadze:
  * Wybranie pierwszej krawędzi oraz usunięcie jej ze zbioru krawędzi.
  * Sprawdznie do ilu drzew należy krawędź:
    * Jeśli do 1 -> odrzucamy krawędź.
    * Jeśli do 2 -> łączymy te dwa drzewa w jedno oraz dołączamy krawędź.
  * Wyjdź z pętli jeśli istnieje tylko jedno drzewo (jest ono rozpinające)

**Mój Algorytm**

Nie różni się zbytnio od wyżej wymienionego algorytmu. Jedne różnice to odwrócenie sortowania oraz dynamiczne dodawanie drzew kiedy zajdzie taka potrzeba.

Kroki algorytmu:

* Utworzenie pustej listy przeznaczonej na drzewa.
* Iteracja po zbiorze krawędzi zaczynając od krawędzi o najmniejszej wadze:
  * Wybranie pierwszej krawędzi oraz usunięcie jej ze zbioru krawędzi.
  * Sprawdznie do ilu drzew należy krawędź:
    * Jeśli do 0 -> tworzymy nowe drzewo zawierające 2 wierzchołki krawędzi oraz dodajemy je do listy drzew.
    * Jeśli do 1 -> odrzucamy krawędź.
    * Jeśli do 2 -> łączymy te dwa drzewa w jedno oraz dołączamy krawędź.





### Algorytmy generatora danych

Powstały dwa generatory danych. 

**Generator1**
Zadaniem generatora 1 jest stworzenie zadania o zadanych parametrach którego wynik znamy. 



**Generator2**
Generator drugi znajduje zastosowanie w profilowaniu algorytmu. Zasada działania opiera się na wylosowaniu macierzy gęstej. Po otrzymaniu macierzy losowej o rozmiarach podyktowanych przez zadane rozmiary grafu, obliczany jest punkt odcięcia $x_{ths}$. Wyznaczany jest tak, aby w macierzy znajdowała się określona liczba liczb mniejszych od $x_{ths}$. Ponieważ znamy rozkład liczb (jest on jednorodny), możemy ustalić $X_{ths}$ "na oko", czyli tak żeby liczba liczb zgadzała się mniej więcej z zadaną wartością. Następnie zapewniana jest jednolitość grafu poprzez dodanie krawędzi. 



## Analiza złożoności

Niech zbiór $E$ stanowi zbiór krawędzi, a zbiór $V$ zbiór wierzchołków. 

Złożoność poszczególnych kroków jest następująca:

* Sortowanie - $ O(|E|*log(|E|))$ 
* znalezienie wierzchołka w podrzewie  - Dzięki implementacji na podstawie hashsetu - $O(1)$
* połącznienie zbiorów ze sobą - $O(len(x_1) + len(x_2))$ . Ponieważ te zbiory mogą sumować się maksymalnie do $???$ , złożoność to $???$

Dodatkowo po kroku sortowania wszyskie operacje działają w pętli o ilości powtóżeń równej $|E|$

Wynika z tego że całkowita złożoność algorytmu to:
$$
O(|E|log(|E|)) + |E|*(O(1) + O(log(|V|)) = O(|E|log(|E|))+O(|E|log(|V|)) \\
$$
Wiemy również że $O(|E|) = O(|V|^2)$ dlatego możemy stwierdzić że pesymistyczna zlożoność algorytmu to
$$
O(|E|log(|E|))
$$


## Testowanie



## Badanie 

