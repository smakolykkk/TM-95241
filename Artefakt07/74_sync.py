import sys
import os
import time

sys.path.append(os.path.abspath("../Artefakt06"))
from MainPage import MainPage


class SyncManager(MainPage):
    """
    MODUŁ SYNCHRONIZACJI: Explicit Wait / WebDriverWait.
    """

    def wait_for_element_and_click(self, business_key, timeout=10):
        print(f"[SYNC] Rozpoczynam oczekiwanie na element: {business_key}")
        print(f"[SYNC] Maksymalny timeout: {timeout}s")
        print("[WebDriverWait] Symulacja inteligentnego oczekiwania...")

        start_time = time.time()

        if business_key == "ADD":
            time.sleep(1.5)
            duration = round(time.time() - start_time, 2)
            return f"SUKCES: Element '{business_key}' odnaleziony i kliknięty po {duration}s."

        time.sleep(2)
        duration = round(time.time() - start_time, 2)
        return f"TIMEOUT: Element '{business_key}' nie pojawił się po {duration}s."


if __name__ == "__main__":
    sm = SyncManager()

    print(">>> ZADANIE 7.4: TESTY SYNCHRONIZACJI DYNAMICZNEJ <<<")
    print("-" * 50)

    print(sm.wait_for_element_and_click("ADD", timeout=10))
    print(sm.wait_for_element_and_click("NON_EXISTENT_BUTTON", timeout=3))

    print("-" * 50)