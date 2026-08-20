# KI-Faktencheck

Prüft eine KI-Antwort Behauptung für Behauptung per Websuche und schreibt einen
Bericht mit Quellen und einer korrigierten Fassung.

Gedacht für Lehrkräfte: Wenn ChatGPT, Claude oder Gemini euch einen Text
geschrieben hat, lasst dieses Werkzeug einmal drüberlaufen, bevor ihr ihn
verwendet. KI-Modelle halluzinieren, sie erfinden Zahlen, Daten, Namen und
Quellen und klingen dabei völlig sicher. Dieses Werkzeug nutzt eine zweite KI
mit echter Websuche, die jede prüfbare Behauptung gegen Quellen abgleicht.

## Was rauskommt

Aus `meine-ki-antwort.md` wird `meine-ki-antwort.bericht.md` mit:

1. **Kurzfazit**: wie viele Behauptungen geprüft, bestätigt, widerlegt
2. **Einzelprüfung**: Tabelle mit Urteil und Quellen-URL pro Behauptung
3. **Korrigierte Fassung**: der Text mit belegten Richtigstellungen
4. **Quellenliste**: alle verwendeten URLs zum Selbst-Nachlesen

Urteile gibt es nur mit konkreter Quelle. Was sich nicht belegen lässt, heißt
ehrlich "Nicht belegbar", nicht "stimmt schon".

## Einrichtung (einmalig, 5 Minuten)

1. Python 3 installieren, falls nicht vorhanden (auf dem Mac schon dabei)
2. Im Terminal:

```
pip install anthropic
```

3. API-Key holen auf [console.anthropic.com](https://console.anthropic.com)
   (Guthaben aufladen, eine Prüfung kostet je nach Textlänge etwa 10 bis 50 Cent)
4. Die Datei `.env.example` zu `.env` kopieren und den Key eintragen:

```
cp .env.example .env
```

Der Key bleibt in der `.env` auf eurem Rechner. Niemals den Key selbst in
Dateien schreiben, die ihr weitergebt oder hochladet.

## Benutzung

KI-Antwort als Textdatei speichern (z.B. `antwort.md`), dann:

```
python3 faktencheck.py antwort.md
```

Nach 1 bis 5 Minuten liegt `antwort.bericht.md` daneben.

## Grenzen

Auch der Prüfer ist eine KI. Er arbeitet mit echter Websuche und darf ohne
Quelle kein Urteil fällen, das macht ihn deutlich zuverlässiger als die
ungeprüfte Erstantwort, aber nicht unfehlbar. Bei allem, was Konsequenzen hat
(Noten, Elternbriefe, Rechtliches), die verlinkten Quellen selbst öffnen. Der
Bericht ist eine Vorprüfung, kein Ersatz für den eigenen Blick.
