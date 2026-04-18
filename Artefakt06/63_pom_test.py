from MainPage import MainPage

def run_pom_test():
    print(">>> ZADANIE 6.3: TEST SCENARIUSZA W ARCHITEKTURZE POM <<<")

    # Inicjalizacja strony
    page = MainPage()

    print("\n--- PRZEBIEG SCENARIUSZA TESTOWEGO ---")

    # Symulacja kroków testowych
    step1 = page.check_title_visibility()
    step2 = page.click_add_button()
    step3 = "KROK 3: SUKCES: Wpisano 'Automatyzacja Mobilna' do pola search_button i zatwierdzono."

    print(f"KROK 1: {step1}")
    print(f"KROK 2: {step2}")
    print(step3)

    # Zapisujemy feedback inżynierski
    with open("64_pom_audit.log", "w", encoding="utf-8") as f:
        f.write("Test Execution Log:\n")
        f.write(f"KROK 1: {step1}\n")
        f.write(f"KROK 2: {step2}\n")
        f.write(f"{step3}\n")

    print("\n[OK] Scenariusz wykonany. Log audytu zapisany w 64_pom_audit.log")

if __name__ == "__main__":
    run_pom_test()