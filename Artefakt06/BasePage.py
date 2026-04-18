import json
import os

class BasePage:
    def __init__(self, selectors_file="53_selectors.json"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        local_path = os.path.join(current_dir, selectors_file)
        fallback_path = os.path.join(current_dir, "..", "Artefakt05", selectors_file)

        if os.path.exists(local_path):
            path_to_use = local_path
        elif os.path.exists(fallback_path):
            path_to_use = fallback_path
        else:
            raise FileNotFoundError(f"Nie znaleziono pliku z selektorami: {selectors_file}")

        with open(path_to_use, "r", encoding="utf-8") as f:
            self.selectors = json.load(f)["selectors"]

        print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(self.selectors)} elementów.")

    def get_selector(self, business_name):
        return self.selectors.get(business_name, None)

if __name__ == "__main__":
    page = BasePage()
    print(f"Weryfikacja klucza 'ADD': {page.get_selector('ADD')}")