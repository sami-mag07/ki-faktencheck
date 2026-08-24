# KI-Faktencheck

Checks an AI answer claim by claim via web search and writes a
report with sources and a corrected version.

Made for teachers: if ChatGPT, Claude, or Gemini wrote a text for you,
run this tool over it once before you use it. AI models hallucinate:
they invent numbers, dates, names, and sources while sounding completely
confident. This tool uses a second AI with real web search that checks
every verifiable claim against sources.

## What you get

From `meine-ki-antwort.md` you get `meine-ki-antwort.bericht.md` with:

1. **Summary**: how many claims were checked, confirmed, refuted
2. **Individual checks**: a table with a verdict and source URL per claim
3. **Corrected version**: the text with sourced corrections
4. **Source list**: all URLs used, so you can read them yourself

Verdicts are only given with a concrete source. Anything that cannot be
backed up is honestly labeled "Not verifiable", not "probably fine".

## Setup (one time, 5 minutes)

1. Install Python 3 if you don't have it (already included on the Mac)
2. In the terminal:

```
pip install anthropic
```

3. Get an API key at [console.anthropic.com](https://console.anthropic.com)
   (add credit; one check costs about 10 to 50 cents depending on text length)
4. Copy the file `.env.example` to `.env` and enter the key:

```
cp .env.example .env
```

The key stays in the `.env` on your machine. Never write the key itself
into files you share or upload.

## Usage

Save the AI answer as a text file (e.g. `antwort.md`), then:

```
python3 faktencheck.py antwort.md
```

After 1 to 5 minutes, `antwort.bericht.md` appears next to it.

## Use as a Claude skill

If you work with Claude (Code, Desktop, or Cowork), you don't need the script:
copy the `SKILL.md` from this repo into your own skills folder
(e.g. `~/.claude/skills/faktencheck/SKILL.md`), then a simple
"check this for hallucinations" in the chat is enough and Claude checks
by the same rules, with web search and mandatory sources.

## Related projects

- [fact-check-skill](https://github.com/FuturizeRush/fact-check-skill): claim verification for technical texts
- [claude-skill-citation-checker](https://github.com/PHY041/claude-skill-citation-checker): checks bibliographies against CrossRef, Semantic Scholar, and OpenAlex
- [anthropic-anti-hallucinate-skills](https://github.com/instantX-research/anthropic-anti-hallucinate-skills): behavioral rules against hallucinations

## Limits

The checker is an AI too. It works with real web search and is not allowed
to give a verdict without a source, which makes it far more reliable than the
unchecked first answer, but not infallible. For anything with consequences
(grades, letters to parents, legal matters), open the linked sources yourself.
The report is a preliminary check, not a substitute for your own judgment.
