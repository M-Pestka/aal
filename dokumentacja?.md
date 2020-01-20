# Projekt AAL

Michał Pestka

## Opis problemu

(Numer zadania 9)

Treść zadania: 

> Tutaj idzie treść zadania. 

Problem postawiony w zadaniu polega więc na stworzeniu specyficznego rodzaju drzewa rozpinającego. 

**Klasyczne drzewo rozpinające** 
Problem drzewa rozpinającego polega na znalezieniu sieci połączneń nie zawierającej cykli która łączy wszystkie wierzchołki, dodatkowo spełniając pewnie kryterium.  Zwykle szukamy drzewa o jaknajniższej sumie wag krawędzi.

**Moje drzewo rozpinające**
W zadaniu chodzi o znalezienie drzewa rozpinającego które maksymalizuje wagę krawędzi o najniższej wadze. 

**Algorytm Kruskala**

Okazuje się że Algorytm kruskala, który służy do znajdowania klasycznego drzewa rozpinającego, rozwiązuje problem dokładnie odwrotny do zadanego. Wystarczy więc zamienić znajdowanie najtańszej krawędzi na szukanie najdroższej.

## Metody rozwiązania

Rozwiązanie zostało napisane w języku Python3. Dzieli się na 3 części:

* Cześć zawieracjąca algorytm
* Część zawierająca algorytm
* Część zawierającą strukturę danych - zbiór podzbiorów rozłącznych.

### Algorytm rozwiązania

Zgodnie z tym, co zostało napisane powyżej, użyłem niznacznie zmodyfikowanego algorytmu Kruskala.

**Algorytm Kruskala**
Algortm Kruskala jest bardzo prosty. Kroki algorytmu:

* Utworzenie lasu (zbioru drzew) w którym każdy z wierzchołków jest osobnym drzewem.
* Posortowanie krawędzi
* Dla każdej krawędzi w zbiorze zaczynając od krawędzi o najmniejszej wadze:
  * Wybranie pierwszej krawędzi oraz usunięcie jej ze zbioru krawędzi.
  * znalezienie najwyższego parenta wierzchołka 1 w poddrzewie do którego należy (operacja FIND)
  * znalezienie najwyższego parenta wierzchołka 2 w poddrzewie do którego należy (operacja FIND)
  * Porównanie parenta wierzchołka 1 oraz 2:
  	* Jeśli Parent(1) == Parent(2) -> nic nie robimy
  	* Jeśli Parent(1) != Parent(2) -> łączymy drzewa ze sobą (opracja UNION)



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
Algorytm rozwiązanie był testowany za pomocą generatora zdolnego określić jaka powinna być wynikowa wartość programu. Zostały wygenerowanie 3 grafy. Zostały one następnie wrzucone do programu rozwiązującego.


## Badanie 
Zostały również przeprowadzone empiryczne badania złożoności obliczeniowej algorytmu. Badania te były bardzo proste i składały się z następującyk kroków:
* wygenerowanie grafu
* Sprawdzenie liczby krawędzi oraz zapisanie jej
* Zapamiętanie obecnego czasu
* Rozwiązanie zadanego problemu
* Porównanie obeznego czasu z zapamiętaną wartością.

Wyniki analizy:


Wnioski z analizy:
Empiryczna analiza złożoności pokazała że złożoność czasowa jest taka sama jak zakładana.

