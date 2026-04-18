import json
import xml.etree.ElementTree as ET
import os

manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"

ns = {'android': 'http://schemas.android.com/apk/res/android'}

tree = ET.parse(manifest_path)
root = tree.getroot()

package = root.attrib.get('package')

# Szukamy aktywności, która ma filtr MAIN i LAUNCHER
main_activity = None
for activity in root.findall(".//activity", ns):
    intent = activity.find(".//intent-filter", ns)
    if intent is not None:
        action = intent.find(".//action[@android:name='android.intent.action.MAIN']", ns)
        if action is not None:
            main_activity = activity.get(f"{{{ns['android']}}}name")
            break

capabilities = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": package,
    "appActivity": main_activity,
    "deviceName": "emulator-5554",
    "noReset": True
}

# zapis do JSON
with open("51_caps.json", "w") as f:
    json.dump(capabilities, f, indent=4)

print("Sukces! Wykryto:")
print(package)
print(main_activity)