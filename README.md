# Sieć Kohonena - Wizualizacja Uczenia

## Program
Aplikacja została napisana w **Pythonie**, głównie przy użyciu bilbiotek *numpy* i *pygame*. 
Pozwala na nałożenie punktów na ekran, wybrania parametrów **mapy SOM**, a następnie zwizualizowania uczenia Sieci Kohonena na zadanych punktach.



https://github.com/DarkArbiterr/Siec-Kohonena/assets/75552617/8542e914-c907-414c-af66-7721ff94bc31



> [!NOTE]
> **Mapa SOM (Self-Organizing Map)**: znana również jako sieć Kohonena, to rodzaj sztucznej sieci neuronowej używanej w nienadzorowanym uczeniu maszynowym.
> Jest to technika klastrowania danych, która pomaga zredukować wymiarowość danych i odzwierciedlić ich strukturę w dwuwymiarowej lub trójwymiarowej przestrzeni.

## Algorytm Sieci Kohonena
**Inicjalizacja**: Parametry to wysokość (*height*), szerokość (*width*) i wymiar (*dimension*) mapy SOM, 
współczynniki uczenia *alpha* i *sigma* (można je zmienić w funkcji *main*, domyślnie ustawione na **0.6 i 1.2**).

**Funkcja znajdująca neuron**: znajduje neuron najbliższy do danego punktu (start) na mapie SOM. 
Oblicza odległość między punktem a każdym neuronem i zwraca współrzędne najbliższego neuronu.

**Funkcja Gaussa**: używana do obliczania wpływu sąsiadujących neuronów podczas aktualizacji wag. 
Parametr distance to odległość między neuronem a punktem danych.

**Funkcja Alpha**: funkcja aktualizacji współczynnika uczenia w czasie. Parametr t to aktualny krok czasowy.
