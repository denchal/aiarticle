import openai
import os

def load_article(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Plik '{file_path}' nie istnieje.")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_html(output_path, content):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def generate_html(article_content, api_key, engine="gpt-4o"):
    openai.api_key = api_key

    prompt = (
    """Przekształć poniższą treść artykułu w strukturalny kod HTML. 

    1. Kod HTML powinien zawierać wyłącznie zawartość do wstawienia pomiędzy tagami <body> i </body>. 
    Nie dołączaj znaczników <html>, <head> ani <body>. Kod powinien zawierać wyłącznie zawartość do wstawienia pomiędzy tagami <body> i </body>
    2. Użyj odpowiednich tagów HTML, takich jak <h1>, <h2>, <p>, <ul>, <li>, aby właściwie strukturyzować treść.
    3. W miejscach, gdzie warto dodać grafiki, co najmniej raz na podrozdział wstaw tag <img> z atrybutem src="image_placeholder.jpg". 
    Dodaj do niego atrybut alt z dokładnym, szczegółowym opisem zawartości obrazka, 
    który może zostać łatwo wygenerowany przez AI. Prompty muszą być szczegółowe, zawierać informacje o:
    - scenerii lub otoczeniu,
    - kluczowych elementach widocznych na obrazku,
    - stylu wizualnym (jeśli jest istotny),
    - kontekście użycia obrazka.
    Nie twórz promptów które wymagają wygenerowania tekstu, schematów, tabeli. Skup się na abstrakcji.
    4. Pod każdą grafiką dodaj opis w osobnym tagu HTML, takim jak <figcaption> Opisy powinny być w tym samym języku co artykuł.
    5. Zachowaj spójność i poprawność kodu HTML. Upewnij się, że cała struktura jest logiczna i zgodna z treścią artykułu.

    Oto treść artykułu do przekształcenia: 
    """
        + article_content
    )

    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=4000,
            temperature=0.7
        )

        html_content = response.choices[0].text.strip()
        return html_content
    except openai.error.AuthenticationError:
        raise Exception("Nieprawidłowy klucz API OpenAI.")
    except openai.error.OpenAIError as e:
        raise Exception(f"Wystąpił błąd podczas komunikacji z API OpenAI: {str(e)}")

def main():
    input_file = "artykul.txt"
    output_file = "artykul.html"
    api_key = "your_openai_api_key"
    engine = "gpt-4o"

    try:
        article_content = load_article(input_file)

        html_content = generate_html(article_content, api_key, engine)

        save_html(output_file, html_content)
        print(f"Plik HTML został zapisany jako {output_file}")
    except FileNotFoundError as e:
        print(f"Wystąpił błąd z plikiem: {str(e)}")
    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")

if __name__ == "__main__":
    main()
