# 📚 Biblioteka (Python)

## 📜 Opis projektu

Aplikacja konsolowa napisana w Pythonie, umożliwiająca zarządzanie prostą biblioteką.
Użytkownik może się zalogować, przeglądać dostępne książki oraz wypożyczać je i sprawdzać swoje wypożyczenia.

---

## 🏗️ Struktura systemu

🗂️ `app.py` – główny plik aplikacji zawierający logikę programu

---

## ⚙️ Funkcjonalności

🔐 Logowanie użytkownika

* maksymalnie 3 próby
* walidacja loginu i hasła

📖 Przeglądanie katalogu

* lista książek
* autor
* liczba dostępnych egzemplarzy

📚 Wypożyczanie książek

* zmniejszanie liczby dostępnych sztuk
* przypisanie książki do użytkownika

👤 Moje wypożyczenia

* lista aktualnie wypożyczonych książek

🚪 Wylogowanie

* zakończenie działania programu

---

## 🛠️ Wykorzystane technologie

🐍 Python
🧠 Programowanie strukturalne (funkcje, pętle, instrukcje warunkowe)

---

## 🧩 Struktura danych

📚 Książki:

* tytuł
* autor
* liczba dostępnych sztuk

👤 Użytkownicy:

* login
* hasło
* lista wypożyczeń

---

## 📝 Problemy i rozwiązania

🛑 Problem 1: Błędne dane logowania
Opis: Użytkownik podaje niepoprawny login lub hasło
Rozwiązanie: Wprowadzono limit 3 prób logowania

---

🛑 Problem 2: Brak dostępnych egzemplarzy
Opis: Użytkownik próbuje wypożyczyć książkę, której nie ma na stanie
Rozwiązanie: Wyświetlany jest komunikat o braku dostępności

---

🛑 Problem 3: Nieznaleziona książka
Opis: Użytkownik wpisuje tytuł, którego nie ma w katalogu
Rozwiązanie: Program informuje o braku takiej pozycji

---

## 🚀 Jak uruchomić program

Uruchom w terminalu:

```bash
python app.py
```

---

## 👤 Autor

Cyprian
