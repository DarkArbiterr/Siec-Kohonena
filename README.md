# Sieć Kohonena - Wizualizacja Uczenia

## Program
Aplikacja została napisana w **Pythonie**, głównie przy użyciu bilbiotek *numpy* i *pygame*. 
Pozwala na nałożenie punktów na ekran, wybrania parametrów **mapy SOM**, a następnie zwizualizowania uczenia Sieci Kohonena na zadanych punktach.

![pygamewindow2024-02-0316-30-42-ezgif com-video-to-gif-converter](https://github.com/DarkArbiterr/Siec-Kohonena/assets/75552617/61db6aa0-1657-4ed4-9724-1436af796192)

> [!NOTE]
> **Mapa SOM (Self-Organizing Map)**: znana również jako sieć Kohonena, to rodzaj sztucznej sieci neuronowej używanej w nienadzorowanym uczeniu maszynowym.
> Jest to technika klastrowania danych, która pomaga zredukować wymiarowość danych i odzwierciedlić ich strukturę w dwuwymiarowej lub trójwymiarowej przestrzeni.

## Algorytm Sieci Kohonena
**Inicjalizacja**: Parametry to wysokość (*height*), szerokość (*width*) i wymiar (*dimension*) mapy SOM, 
współczynniki uczenia *alpha* i *sigma* (można je zmienić w funkcji *main*, domyślnie ustawione na **0.6 i 1.2**).

**Funkcja znajdująca neuron**: znajduje neuron najbliższy do danego punktu (*start*) na mapie SOM. 
Oblicza odległość między punktem a każdym neuronem i zwraca współrzędne najbliższego neuronu.

**Funkcja Gaussa**: używana do obliczania wpływu sąsiadujących neuronów podczas aktualizacji wag. 
Parametr *distance* to odległość między neuronem a punktem danych.

**Funkcja Alpha**: funkcja aktualizacji współczynnika uczenia w czasie. Parametr *t* to aktualny krok czasowy.

**Aktualizacja wag neuronu**: aby zbliżyć je do punktu danych. Parametry to indeks neuronu (*record*), punkt danych (*dataPoint*), aktualny krok czasowy (*st*) i odległość między neuronem a punktem (*distance*).

**Aktualizacja sieci**: Aktualizacja wag wszystkich neuronów na podstawie najlepszego neuronu i punktu danych. Parametry to najlepszy neuron (*bestNeuron*), punkt danych (*dataPoint*) i aktualny krok czasowy (*step*).

**Trening**: proces treningu sieci. Wybiera losowy punkt danych, znajduje najlepszy neuron, a następnie aktualizuje wagi wszystkich neuronów na podstawie tego punktu danych.

Algorytm ten jest iteracyjny i podczas każdej iteracji aktualizuje wagi neuronów na podstawie losowo wybranego punktu danych. To prowadzi do organizacji mapy w taki sposób, aby neuronów odpowiadały różnym obszarom danych, co jest przydatne do analizy struktury danych i klasyfikacji. Algorytm jest stopniowo dostosowywany do danych wejściowych, aż do uzyskania stabilnej struktury mapy SOM.
