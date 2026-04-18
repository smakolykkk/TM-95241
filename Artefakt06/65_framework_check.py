import os
from MainPage import MainPage

results = []

# 1. Sprawdzenie instancji POM
try:
    page = MainPage()
    results.append(("POM_Initialization", "PASSED", "Klasy BasePage i MainPage działają poprawnie."))
except Exception as e:
    results.append(("POM_Initialization", "FAILED", str(e)))

# 2. Sprawdzenie raportu Markdown (6.4)
if os.path.exists("64_audit_report.md"):
    results.append(("Documentation_Check", "PASSED", "Raport inżynierski MD został odnaleziony."))
else:
    results.append(("Documentation_Check", "FAILED", "Brak pliku 64_audit_report.md!"))

# 3. Sprawdzenie selektorów (blok 5)
try:
    if len(page.selectors) > 0:
        results.append(("Data_Layer_Connection", "PASSED", f"Wczytano {len(page.selectors)} selektorów z Bloku 5."))
    else:
        results.append(("Data_Layer_Connection", "FAILED", "Mapa selektorów jest pusta!"))
except:
    results.append(("Data_Layer_Connection", "FAILED", "Nie udało się odczytać selektorów."))

# === GENEROWANIE XML ===
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += f'<testsuite name="POM_Framework_Audit" tests="{len(results)}">\n'

print("\n--- WYNIKI AUDYTU ARCHITEKTURY ---")

for name, status, msg in results:
    print(f"[{status}] {name}: {msg}")

    xml_content += f'  <testcase name="{name}" status="{status.lower()}">\n'
    xml_content += f'    <system-out>{msg}</system-out>\n'
    xml_content += f'  </testcase>\n'

xml_content += '</testsuite>'

with open("65_final_report.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)

print("\n[ZAKOŃCZONO] Blok 6 zweryfikowany. Raport: 65_final_report.xml")