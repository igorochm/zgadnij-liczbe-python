# 🎯 Gra: Zgadnij Liczbę (Guess The Number)

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## 📝 Opis Projektu
Interaktywna gra konsolowa, w której gracz zmaga się z algorytmem losującym. Celem jest odgadnięcie liczby przy minimalnej liczbie prób, korzystając z podpowiedzi systemu.

---

## 📋 Wymagania Funkcjonalne

Poniższa tabela przedstawia kluczowe funkcjonalności podzielone na kategorie:

| ID | Kategoria | Opis Funkcjonalności | Priorytet |
|:---|:---|:---|:---|
| **01** | Rdzeń gry | Losowanie liczby z zakresu **1 - 100** | Krytyczny |
| **02** | Mechanika | System podpowiedzi: `Za mało` / `Za dużo` | Krytyczny |
| **03** | Trudność | 3 poziomy trudności (Łatwy, Średni, Trudny) | Wysoki |
| **04** | UX | Walidacja danych (odporność na wpisanie liter) | Wysoki |
| **05** | Wyniki | Licznik pozostałych prób widoczny dla gracza | Średni |
| **06** | Sesja | Możliwość restartu gry po wygranej/przegranej | Średni |

---

## 🛠 Lista zadań (Checklista do Trello)

Poniższe punkty zostały przeniesione na tablicę Kanban jako zadania do wykonania:

- [x] **Logika Losowania**: Użycie biblioteki `random` do generowania liczby.
- [x] **Pętla Główna**: Mechanizm pozwalający na wielokrotne zgadywanie.
- [x] **System Walidacji**: Obsługa błędów `ValueError` przy `input()`.
- [x] **Poziomy Trudności**: Słownik definiujący liczbę prób dla każdego poziomu.
- [x] **Interfejs**: Czytelne i kolorowe komunikaty w konsoli.
- [x] **High Score**: Zapamiętywanie najlepszego wyniku w danej sesji.
- [x] **Obsługa Wyjścia**: Możliwość zamknięcia gry w dowolnym momencie.
- [x] **Podsumowanie**: Wyświetlenie komunikatu końcowego z wynikiem.
- [x] **Instrukcja**: Krótki samouczek wyświetlany na starcie.
- [x] **CI/CD**: Konfiguracja automatycznych testów na GitHubie.

---

## 🚀 Instalacja i Uruchomienie

Aby uruchomić grę lokalnie, wykonaj poniższe kroki:

1. **Sklonuj repozytorium**:
   ```bash
   git clone [https://github.com/TWOJA-NAZWA/zgadnij-liczbe-python.git](https://github.com/TWOJA-NAZWA/zgadnij-liczbe-python.git)
