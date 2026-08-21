#!/usr/bin/env python3
"""KI-Faktencheck: prueft eine KI-Antwort (Markdown- oder Textdatei) Behauptung
fuer Behauptung per Websuche und schreibt einen Bericht mit Quellen und
korrigierter Fassung daneben.

Nutzung:
    python3 faktencheck.py meine-ki-antwort.md
Ergebnis:
    meine-ki-antwort.bericht.md
"""
import os
import pathlib
import sys


def lade_env():
    """Liest eine .env neben dem Skript oder im Arbeitsverzeichnis.
    Der API-Key gehoert in die .env, niemals in den Code."""
    for ordner in (pathlib.Path.cwd(), pathlib.Path(__file__).parent):
        pfad = ordner / ".env"
        if pfad.exists():
            for zeile in pfad.read_text(encoding="utf-8").splitlines():
                zeile = zeile.strip()
                if zeile and not zeile.startswith("#") and "=" in zeile:
                    k, v = zeile.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())


SYSTEM = """Du bist ein wissenschaftlicher Faktenpruefer fuer Lehrkraefte.
Du bekommst einen Text, den eine KI (z.B. ChatGPT, Claude, Gemini) erzeugt hat.
Deine Aufgabe: jede ueberpruefbare Tatsachenbehauptung per Websuche pruefen.

Vorgehen:
1. Zerlege den Text zuerst in atomare, einzeln pruefbare Behauptungen.
   Vorrangig: Zahlen, Daten, Namen, Zitate, Quellenangaben, Ortsbezogenes.
2. Suche aktiv nach den typischen Halluzinationsmustern:
   - erfundene oder nicht auffindbare Quellen, Studien, Urteile, DOIs
   - plausible, aber falsche Jahreszahlen und Zahlenwerte
   - vage Autoritaet ("Studien zeigen", "Experten sagen") ohne Beleg
   - veraltete Fakten, die frueher stimmten (Datum der Quelle pruefen)
   - falsch zugeordnete Personen und Namen
3. Urteile nur mit Beleg: "Bestaetigt" oder "Widerlegt" erfordert eine
   konkrete, serioese, wirklich gefundene Quelle. Bei "Widerlegt" nach
   Moeglichkeit zwei unabhaengige Quellen. Sonst: "Nicht belegbar".
   "Teilweise richtig", wenn Kern stimmt, aber Details abweichen.
4. Quellen-Hierarchie: Primaerquelle und offizielle Stellen vor etablierten
   Medien vor allem anderen. Inhalte, die selbst KI-generiert wirken
   (Content-Farmen, aggregierte Blogs), zaehlen nicht als Beleg.
5. Gib zu jedem Urteil eine Konfidenz an (hoch / mittel / niedrig).
6. Erfinde niemals Quellen. Wenn die Suche nichts hergibt, sag das.

Antworte als Markdown-Bericht auf Deutsch, exakt in dieser Struktur:

# Faktencheck

## Kurzfazit
Ein Absatz: X Behauptungen geprueft, davon Y bestaetigt, Z teilweise richtig,
W widerlegt, V nicht belegbar. Gesamteinschaetzung in einem Satz.

## Einzelpruefung
| Behauptung | Urteil | Konfidenz | Beleg |
|---|---|---|---|
Eine Zeile pro Behauptung. Urteil: Bestaetigt / Teilweise richtig /
Widerlegt / Nicht belegbar. Beleg: kurze Begruendung plus URL.

## Korrigierte Fassung
Der Originaltext, in dem widerlegte Stellen durch die belegte Richtigstellung
ersetzt sind (Korrekturen **fett**). Nicht belegbare Stellen mit
[unbelegt] markieren.

## Quellen
Nummerierte Liste aller verwendeten URLs."""


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    quelle = pathlib.Path(sys.argv[1])
    if not quelle.exists():
        sys.exit(f"Datei nicht gefunden: {quelle}")

    lade_env()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Kein ANTHROPIC_API_KEY gefunden. Lege eine .env nach dem "
                 "Muster von .env.example an (Key: console.anthropic.com).")

    try:
        import anthropic
    except ImportError:
        sys.exit("Bitte erst installieren: pip install anthropic")

    text = quelle.read_text(encoding="utf-8")
    client = anthropic.Anthropic()
    messages = [{
        "role": "user",
        "content": "Pruefe den folgenden KI-generierten Text:\n\n" + text,
    }]

    print(f"Pruefe {quelle.name} ... (dauert je nach Laenge 1 bis 5 Minuten)")
    while True:
        antwort = client.messages.create(
            model="claude-opus-5",
            max_tokens=16000,
            system=SYSTEM,
            tools=[{
                "type": "web_search_20260209",
                "name": "web_search",
                "max_uses": 15,
            }],
            messages=messages,
        )
        # Server-seitige Suche pausiert bei vielen Suchlaeufen; weiterlaufen lassen
        if antwort.stop_reason == "pause_turn":
            messages = [messages[0],
                        {"role": "assistant", "content": antwort.content}]
            print("  ... suche weiter")
            continue
        break

    if antwort.stop_reason == "refusal":
        sys.exit("Die Pruefung wurde vom Modell abgelehnt. Text kuerzen oder "
                 "anpassen und erneut versuchen.")

    bericht = "".join(b.text for b in antwort.content if b.type == "text")
    if not bericht.strip():
        sys.exit("Leere Antwort erhalten, bitte erneut versuchen.")

    ziel = quelle.with_suffix(".bericht.md")
    ziel.write_text(bericht, encoding="utf-8")
    suchen = sum(1 for b in antwort.content if b.type == "server_tool_use")
    print(f"Fertig: {ziel.name} ({suchen} Websuchen)")


if __name__ == "__main__":
    main()
