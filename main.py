# Gra napisana w Pythonie - Projekt zaliczeniowy

import random

def game():
    print("--- Witaj w grze Zgadnij Liczbę! ---")
    print("Wybierz poziom trudności: 1 (Łatwy), 2 (Średni), 3 (Trudny)")
    
    levels = {"1": 15, "2": 10, "3": 5}
    choice = input("Twój wybór: ")
    attempts = levels.get(choice, 10)
    
    secret_number = random.randint(1, 100)
    used_attempts = 0

    while used_attempts < attempts:
        try:
            guess = int(input(f"Próba {used_attempts + 1}/{attempts}. Podaj liczbę: "))
        except ValueError:
            print("To nie jest liczba! Spróbuj ponownie.")
            continue

        used_attempts += 1

        if guess < secret_number:
            print("Za mało!")
        elif guess > secret_number:
            print("Za dużo!")
        else:
            print(f"Brawo! Odgadłeś w {used_attempts} próbie.")
            return

    print(f"Koniec prób! Myślałem o liczbie {secret_number}.")

if __name__ == "__main__":
    while True:
        game()
        if input("Chcesz zagrać jeszcze raz? (t/n): ").lower() != 't':
            break
