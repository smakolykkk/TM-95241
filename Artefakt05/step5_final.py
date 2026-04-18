import json

caps_path = "51_caps.json"
selectors_path = "53_selectors.json"

with open(caps_path, "r", encoding="utf-8") as f:
    caps_data = json.load(f)

with open(selectors_path, "r", encoding="utf-8") as f:
    ui_map = json.load(f)

feedback_report = []

current_pkg = caps_data.get("appPackage")

# 1. Weryfikacja Pakietu
if current_pkg == "io.appium.android.apis":
    feedback_report.append({
        "feature": "Identyfikacja Aplikacji",
        "status": "ZGODNY",
        "message": f"Pakiet {current_pkg} poprawnie zmapowany."
    })
else:
    feedback_report.append({
        "feature": "Identyfikacja Aplikacji",
        "status": "DO POPRAWY",
        "message": f"Niezgodność pakietu. Wykryto {current_pkg}, sprawdź konfigurację manifestu."
    })

# 2. Weryfikacja Dostępności Elementów
target_element = "ACCESSIBILITY"

if target_element in ui_map["selectors"]:
    feedback_report.append({
        "feature": "Dostępność UI",
        "status": "ZGODNY",
        "message": f"Element {target_element} jest dostępny w layoutach."
    })
else:
    feedback_report.append({
        "feature": "Dostępność UI",
        "status": "INFORMACJA",
        "message": f"Nie odnaleziono ID '{target_element}'. Sugestia: Zweryfikuj czy element nie zmienił nazwy na jedną z dostępnych: {list(ui_map['selectors'].keys())[:3]}."
    })

# XML
tests = len(feedback_report)
failures = sum(1 for item in feedback_report if item["status"] == "DO POPRAWY")

xml_lines = [f'<testsuite name="ConsistencyTest" tests="{tests}" failures="{failures}">']

for item in feedback_report:
    xml_lines.append(f'  <testcase name="{item["feature"]}">')
    if item["status"] == "DO POPRAWY":
        xml_lines.append(f'    <failure message="{item["message"]}"/>')
    else:
        xml_lines.append(f'    <system-out>{item["status"]}: {item["message"]}</system-out>')
    xml_lines.append('  </testcase>')

xml_lines.append('</testsuite>')

with open("55_result.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(xml_lines))

print("=== ZADANIE 5.5 ===")
for item in feedback_report:
    print(f"[{item['status']}] {item['feature']} - {item['message']}")

print("\nZapisano do 55_result.xml")