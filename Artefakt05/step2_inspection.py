import os
import xml.etree.ElementTree as ET

manifest_path = os.path.join("..", "Artefakt02", "decompiled_apk", "AndroidManifest.xml")
ns = {'android': 'http://schemas.android.com/apk/res/android'}

if not os.path.exists(manifest_path):
    print(f"❌ Nie znaleziono pliku: {manifest_path}")
    raise SystemExit(1)

tree = ET.parse(manifest_path)
root = tree.getroot()

package = root.attrib.get('package', 'BRAK')

permissions = []
for perm in root.findall("uses-permission"):
    perm_name = perm.attrib.get('{http://schemas.android.com/apk/res/android}name')
    if perm_name:
        permissions.append(perm_name)

activities = []
for activity in root.findall(".//activity", ns):
    act_name = activity.attrib.get('{http://schemas.android.com/apk/res/android}name')
    if act_name:
        activities.append(act_name)

report_lines = []
report_lines.append("=== ARTEFAKT 5.2: RAPORT ANALIZY STATYCZNEJ ===")
report_lines.append(f"Pakiet główny: {package}")
report_lines.append(f"Liczba Activity: {len(activities)}")
report_lines.append("")
report_lines.append("Kluczowe uprawnienia (co aplikacja chce robić):")

if permissions:
    for p in permissions:
        report_lines.append(f" - {p}")
else:
    report_lines.append(" - BRAK")

report_text = "\n".join(report_lines)

with open("52_inspection.log", "w", encoding="utf-8") as f:
    f.write(report_text)

print(report_text)
print("\n[OK] Sukces! Artefakt zapisany jako: 52_inspection.log")