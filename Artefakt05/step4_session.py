import json

caps_path = "51_caps.json"
selectors_path = "53_selectors.json"

# Wczytywanie Capsów
with open(caps_path, 'r') as f:
    caps_data = json.load(f)

# Wczytywanie Selektorów
with open(selectors_path, 'r') as f:
    ui_map = json.load(f)

# 2. INTELIGENTNE POBIERANIE DANYCH
# Próba pobrania z prefixem appium: lub bez
app_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
app_act = caps_data.get("appActivity") or caps_data.get("appium:appActivity")
dev_name = caps_data.get("deviceName") or caps_data.get("appium:deviceName")

# liczba elementów UI
selectors = ui_map.get("selectors", {})
ui_count = len(selectors)

# 3. WERYFIKACJA INTEGRACJI
if not app_pkg or not app_act:
    status_msg = "FAILED: Missing appPackage or appActivity in JSON!"
    color = "\033[91m"  # Red
else:
    status_msg = "READY TO CONNECT"
    color = "\033[92m"  # Green

# raport
report = f"""
=== ZADANIE 5.4 ===
Target App : {app_pkg}
Main Activity : {app_act}
Device : {dev_name}
UI Elements : {ui_count} loaded
Status : {status_msg}
"""

# zapis do pliku
with open("54_session.log", "w") as f:
    f.write(report)

# output w konsoli
print(color + report + "\033[0m")
print("Zapisano do 54_session.log")