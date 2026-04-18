from BasePage import BasePage

class MainPage(BasePage):

    def __init__(self):
        super().__init__()
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")

    def click_add_button(self):
        selector = self.get_selector("ADD")
        if selector:
            return f"SUKCES: Wykonano kliknięcie w element UI o ID: '{selector}'"
        return "ERROR: Selector ADD not found in map!"

    def check_title_visibility(self):
        selector = self.get_selector("TITLE")
        if selector:
            return f"SUKCES: Odnaleziono nagłówek strony (ID: {selector}). Status: Widoczny."
        return "ERROR: Selector TITLE not found in map!"