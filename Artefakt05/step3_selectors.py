import json
import os
import xml.etree.ElementTree as ET

layout_dir = os.path.join("..", "Artefakt02", "decompiled_apk", "res", "layout")

ui_map = {"selectors": {}}

# Iterujemy po plikach layoutów
for file_name in os.listdir(layout_dir):
    if file_name.endswith(".xml"):
        try:
            tree = ET.parse(os.path.join(layout_dir, file_name))
            root = tree.getroot()

            # Szukamy wszystkich elementów z atrybutem id
            for element in root.iter():
                res_id = element.attrib.get('{http://schemas.android.com/apk/res/android}id')

                if res_id:
                    # Oczyszczamy ID (np. @id/button → button)
                    clean_id = res_id.split("/")[-1]

                    # Tworzymy nazwę biznesową (np. LOGIN_BTN)
                    business_name = clean_id.upper()

                    ui_map["selectors"][business_name] = clean_id

        except:
            continue

# zapis do JSON
with open("53_selectors.json", "w", encoding="utf-8") as f:
    json.dump(ui_map, f, indent=4, ensure_ascii=False)

# wynik
count = len(ui_map["selectors"])

print("=== ZADANIE 5.3 ===")
print(f"Zmapowano {count} unikalnych elementów UI")
print("Zapisano do 53_selectors.json")