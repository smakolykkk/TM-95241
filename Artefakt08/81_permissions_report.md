# 🔐 RAPORT ANALIZY UPRAWNIEŃ APK

**Audytor:** Patryk Samołyk 95241  
**Moduł:** Blok 8 - Statyczna Analiza Bezpieczeństwa  
**Analizowany plik:** AndroidManifest.xml

---

## 1. Zawartość RiskyPermission.xml

Zidentyfikowano następujące ryzykowne elementy konfiguracji aplikacji:

* **Debuggable: true** - wysokie ryzyko, ponieważ aplikacja może być debugowana w środowisku produkcyjnym.
* **READ_CONTACTS** - dostęp do kontaktów użytkownika.
* **INTERNET** - dostęp do sieci.
* **WRITE_EXTERNAL_STORAGE** - możliwość zapisu do pamięci zewnętrznej.
* **RECORD_AUDIO** - możliwość nagrywania dźwięku.
* **CAMERA** - dostęp do kamery urządzenia.

---

## 2. Interpretacja Inżynierska

Najpoważniejszym problemem jest aktywna flaga `debuggable=true`.  
Wersja produkcyjna aplikacji nie powinna być uruchamiana z takim ustawieniem, ponieważ ułatwia ono analizę działania programu oraz może zwiększyć ryzyko ataku.

Drugim problemem jest szeroki zakres uprawnień. Aplikacja posiada dostęp do kontaktów, kamery, mikrofonu, internetu i pamięci zewnętrznej.  
Jeżeli aplikacja nie wykorzystuje tych funkcji, oznacza to zasadę nadmiarowych uprawnień, czyli **Over-privileged App**.

---

## 3. Akcja korygująca

1. Wyłączyć `debuggable=true` w konfiguracji produkcyjnej.
2. Usunąć niepotrzebne uprawnienia z `AndroidManifest.xml`.
3. Stosować zasadę minimalnych uprawnień.
4. Dodać automatyczną kontrolę manifestu w procesie CI/CD.

---

## 4. Status

**Poziom ryzyka:** WYSOKI  
**Status audytu:** WYMAGANE POPRAWKI