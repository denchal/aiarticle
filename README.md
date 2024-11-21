# Aplikacja do generowania kodu HTML z artykułów

## Opis

Ta aplikacja w Pythonie pozwala na przekształcenie artykułów tekstowych w kod HTML, który jest odpowiednio sformatowany i zawiera tagi HTML do strukturalizacji treści. W artykule generowany jest także kod dla obrazków, które mogą być użyte w artykule, z odpowiednimi promptami dla AI do wygenerowania grafiki. 


## Wymagania

- Python 3.7+
- Biblioteki:
  - `openai` (do komunikacji z API OpenAI)
  - `os` (do operacji na plikach)
  
  Można zainstalować niezbędne biblioteki za pomocą pip:
  
  ```bash
  pip install openai
  ```

## Instalacja

1. **Pobierz repozytorium**:
   - Sklonuj repozytorium lub pobierz plik `.zip` z kodem aplikacji.

2. **Uzyskaj klucz API OpenAI**:
   Zarejestruj się na OpenAI i uzyskaj klucz API, który będzie używany do komunikacji z OpenAI.

3. **Skonfiguruj swój klucz API**:
   W kodzie aplikacji, w pliku, który będziesz uruchamiać, dodaj swój klucz API w miejscu:
   
   ```python
   api_key = "your_openai_api_key"
   ```

## Użycie

1. **Przygotuj plik tekstowy z artykułem**:
   Przygotuj plik tekstowy z artykułem, który chcesz przekształcić na HTML. Artykuł powinien być zapisany w formacie `.txt`.

2. **Uruchom aplikację**:
   Uruchom skrypt w terminalu lub IDE:

   ```bash
   python app.py
   ```

3. **Wynik**:
   Po wykonaniu aplikacji, wynikowy kod HTML zostanie zapisany w pliku `artykul.html` (lub innym, jeśli zmienisz nazwę w kodzie). Plik będzie zawierał kod HTML z artykułem, odpowiednimi tagami HTML, a także tagami `<img>` z promptami do generowania grafik.

## Struktura plików

- **app.py** - Główny plik aplikacji, który wykonuje całą logikę.
- **artykul.txt** - Plik tekstowy z artykułem do przekształcenia.
- **artykul.html** - Wynikowy plik HTML, który jest generowany przez aplikację.

## Konfiguracja

- **max_chunk_size**: Określa maksymalną liczbę tokenów, jaką API OpenAI może przetworzyć na raz.
- **api_key**: Twój klucz API OpenAI, który musisz wprowadzić w kodzie.

## Jak działa aplikacja

1. **Wczytywanie artykułu**: Aplikacja wczytuje artykuł z pliku tekstowego.
2. **Generowanie kodu HTML**: Aplikacja wysyła fragmenty artykułu do API OpenAI, które generuje odpowiedni kod HTML, strukturalizując artykuł przy użyciu tagów HTML.
3. **Generowanie promptów dla obrazków**: W miejscach, gdzie aplikacja zaleca dodanie obrazka, generowany jest prompt w atrybucie `alt`, który jest dostosowany do łatwego wygenerowania grafiki AI.
4. **Zapis do pliku HTML**: Ostateczny wygenerowany kod HTML (bez nagłówków `<html>`, `<head>`, `<body>`) jest zapisywany do pliku `.html`.

## Przykład

Załóżmy, że mamy artykuł o "Sieciach Neuronowych". Aplikacja przekształci ten tekst na odpowiednią strukturę HTML z nagłówkami, akapitami, listami, a także wygeneruje tagi `<img>` z odpowiednimi promptami, np.:

```html
<h1>Sieci Neuronowe</h1>
<p>Sieci neuronowe to...</p>
<img src="image_placeholder.jpg" alt="Scena przedstawiająca nowoczesną fabrykę z robotami pracującymi obok ludzi, którzy kontrolują procesy na ekranach komputerów. Dynamiczna interakcja między człowiekiem a maszyną w kontekście automatyzacji. Styl futurystyczny, z akcentem na technologię.">
<figcaption>Robotyka i automatyzacja w fabryce z równoczesnym udziałem ludzi w monitorowaniu procesów.</figcaption>
```
