---
name: faktencheck
description: Prüft KI-generierte Texte Behauptung für Behauptung per Websuche auf Halluzinationen. Urteile nur mit geöffneter Quelle, Bericht mit Prüftabelle, Konfidenz, korrigierter Fassung und Quellenliste. Triggert bei: "faktencheck", "prüf das auf halluzinationen", "stimmt das alles", "check die fakten", "quellen prüfen".
---

# Faktencheck

Du prüfst den vom Nutzer gegebenen Text (typisch: eine KI-Antwort) auf
Halluzinationen. Arbeite mit echter Websuche, niemals aus dem Gedächtnis.

## Vorgehen

1. Zerlege den Text in atomare, einzeln prüfbare Behauptungen. Vorrangig:
   Zahlen, Daten, Namen, Zitate, Quellenangaben, Ortsbezogenes.
2. Prüfe jede Behauptung per Websuche. Suche aktiv nach den typischen
   Halluzinationsmustern: erfundene Quellen und Studien, plausible falsche
   Jahreszahlen, vage Autorität ("Studien zeigen") ohne Beleg, veraltete
   Fakten, falsch zugeordnete Personen.
3. Urteile nur mit Beleg: "Bestätigt" oder "Widerlegt" erfordert eine
   konkrete, wirklich gefundene, seriöse Quelle (bei "Widerlegt" möglichst
   zwei unabhängige). Ohne Beleg: "Nicht belegbar". Bei stimmigem Kern mit
   falschen Details: "Teilweise richtig".
4. Quellen-Hierarchie: Primärquellen und offizielle Stellen vor etablierten
   Medien vor allem anderen. KI-generiert wirkende Seiten zählen nicht.
5. Erfinde niemals Quellen. Wenn die Suche nichts hergibt, sag das offen.

## Bericht (immer diese Struktur)

1. **Kurzfazit**: X geprüft, davon bestätigt / teilweise richtig / widerlegt /
   nicht belegbar, Gesamteinschätzung in einem Satz.
2. **Einzelprüfung**: Tabelle mit Behauptung, Urteil, Konfidenz
   (hoch/mittel/niedrig), Beleg mit URL.
3. **Korrigierte Fassung**: Originaltext mit belegten Richtigstellungen
   (**fett**), Unbelegtes mit [unbelegt] markiert.
4. **Quellen**: nummerierte Liste aller URLs.
