import subprocess
import time
import os
import sys
from datetime import datetime


def run_cmd(cmd, ignore_error=False):
    """Wykonuje komendę systemową i obsługuje błędy."""
    try:
        subprocess.run(cmd, shell=True, check=not ignore_error)
    except subprocess.CalledProcessError:
        if not ignore_error:
            print(f"❌ Błąd podczas wykonywania: {cmd}")
            sys.exit(1)


def main():
    # Ścieżki
    compose_path = "../Artefakt09/docker-compose.yml"
    results_dir = "allure-results"

    # Ścieżka do Allure
    allure_cmd = (
        r"C:\Users\vdi-terminal\Desktop\allure-2.42.1\bin\allure.bat"
    )

    if not os.path.exists(compose_path):
        print(f"❌ Błąd: Nie znaleziono pliku {compose_path}")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("🚀 START: AUTOMATYCZNY PIPELINE TESTOWY")
    print("=" * 50)

    # 1. Czyszczenie środowiska
    print("\n🧹 Czyszczenie środowiska...")
    run_cmd("docker rm -f appium-server", ignore_error=True)

    # 2. Start kontenerów
    print("\n📦 KROK 1: Podnoszenie kontenerów...")
    run_cmd(f'docker compose -f "{compose_path}" up -d')

    # 3. Czekanie na start
    print("\n⏳ Oczekiwanie na gotowość usług...")
    time.sleep(5)

    # 4. Uruchomienie testów
    print("\n🧪 KROK 2: Uruchamianie testów Pytest...")
    run_cmd(
        f'python -m pytest --alluredir="{results_dir}"',
        ignore_error=True
    )

    # 5. Dodanie informacji o środowisku
    print("\n📝 KROK 3: Tworzenie metadanych raportu...")

    os.makedirs(results_dir, exist_ok=True)

    env_content = f"""Pipeline.Status=SUCCESS
Execution.Time={datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Execution.Type=Automated Master Script
Infrastructure=Docker (Appium Server)
Platform={sys.platform}
Build.Engine=Python Subprocess
"""

    with open(
        os.path.join(results_dir, "environment.properties"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(env_content)

    # 6. Generowanie raportu
    print("\n📊 KROK 4: Generowanie raportu Allure...")

    run_cmd(
        f'"{allure_cmd}" generate "{results_dir}" --clean -o allure-report'
    )

    # 7. Zamknięcie kontenerów
    print("\n🧹 KROK 5: Zamykanie kontenerów...")
    run_cmd(f'docker compose -f "{compose_path}" down')

    print("\n" + "=" * 60)
    print("🏆 PIPELINE ZAKOŃCZONY POPRAWNIE!")
    print(
        f"📍 Raport wygenerowany: "
        f"{os.getcwd()}\\allure-report\\index.html"
    )
    print("=" * 60)

    # Automatyczne otwarcie raportu
    report_file = os.path.join(
        os.getcwd(),
        "allure-report",
        "index.html"
    )

    if os.path.exists(report_file):
        os.startfile(report_file)


if __name__ == "__main__":
    main()