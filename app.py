books = [
    {"title": "Wiedźmin", "author": "Andrzej Sapkowski", "quantity": 3},
    {"title": "Pan Tadeusz", "author": "Adam Mickiewicz", "quantity": 2},
    {"title": "1984", "author": "George Orwell", "quantity": 4},
    {"title": "Projekt Hail Mary", "author": "Andy Weir", "quantity": 1},
    {"title": "Dune", "author": "Frank Herbert", "quantity": 2},
]

users = [
    {"login": "jan", "password": "1234", "borrowed": []},
    {"login": "anna", "password": "abcd", "borrowed": []},
    {"login": "marek", "password": "pass", "borrowed": []},
]


#fnkcje

def login():
    attempts = 0

    while attempts < 3:
        login_input = input("Login: ")
        password_input = input("Hasło: ")

        for user in users:
            if user["login"] == login_input and user["password"] == password_input:
                print("Zalogowano pomyślnie!\n")
                return user

        attempts += 1
        print("Błędne dane! Próba:", attempts)

    print("Przekroczono limit prób. Program zakończony.")
    return None


def show_menu():
    print("\n===== MENU =====")
    print("1. Przeglądaj katalog")
    print("2. Wypożycz książkę")
    print("3. Moje wypożyczenia")
    print("4. Wyloguj")


def show_books():
    print("\n===== KATALOG =====")
    for book in books:
        print(f'{book["title"]} - {book["author"]} (Dostępne: {book["quantity"]})')


def borrow_book(user):
    title = input("Podaj tytuł książki: ")

    for book in books:
        if book["title"].lower() == title.lower():
            if book["quantity"] > 0:
                book["quantity"] -= 1
                user["borrowed"].append(book["title"])
                print("Książka wypożyczona!")
                return
            else:
                print("Brak dostępnych sztuk!")
                return

    print("Nie znaleziono książki.")


def show_borrowed(user):
    print("\n===== MOJE WYPOŻYCZENIA =====")
    if len(user["borrowed"]) == 0:
        print("Brak wypożyczonych książek.")
    else:
        for book in user["borrowed"]:
            print(book)


def main():
    user = login()

    if user is None:
        return

    while True:
        show_menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            show_books()
        elif choice == "2":
            borrow_book(user)
        elif choice == "3":
            show_borrowed(user)
        elif choice == "4":
            print("Wylogowano.")
            break
        else:
            print("Nieprawidłowy wybór!")


main()