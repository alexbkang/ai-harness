---
name: anki-flashcards
description: Convert notes into an Anki .apkg deck of Basic Front/Back cards using genanki.
disable-model-invocation: true
---

`<skill-dir>` is the folder containing this SKILL.md. Before anything else, run `uv --version`. If it fails, stop and ask the user to install uv. Don't install it yourself, and don't write any cards.

1. Card every fact in the notes, in order. Add no facts that aren't in the notes. The full form of an abbreviation the notes use counts as in the notes.
2. Write `cards.json` as `[{"front":"...","back":"..."}]`. Always name the deck after the notes' file name without `.md`.
3. Run `uv run <skill-dir>/scripts/build.py cards.json "<Deck>" "<Deck>.apkg"`. uv gets genanki itself. Deliver the file and the card count.

Rules:
- Reword, don't copy. Rewrite each fact as a short, clear sentence that makes sense on its own: fix grammar, split long sentences, cut filler, and use standard terms where they fit. If a term the notes don't use is the answer, follow it with the notes' meaning in parentheses. Keep the meaning of the note.
- One fact per card. A list counts as one fact. The back holds only the answer, as short as possible.
- Anki shows cards as HTML, so write every line break as `<br>`, not a newline.
- Use `[...]` for the blank on the front: "The capital of France is [...]." -> "Paris"
- Blank the fact's key term: the word or phrase someone has to know to know the fact. Never blank a word the rest of the card gives away.
- Two blanks: the back lists both, "hydrogen / oxygen".
- If a card is unclear on its own, start it with the topic: "Photosynthesis: ..."
- Abbreviations are a question, not a blank: "What does DNA stand for?" -> "deoxyribonucleic acid"
  Make one for every abbreviation in the notes.
- Choices: "Plants [absorb/release] CO2." -> "absorb"
  Use a choice when an open blank would have many possible answers.
- Lists of three or more items: make one card for the whole list. The front names the topic and how many items there are, then one `[...]` per item, each on its own line. The back lists every item in the notes' order, one per line:
  "The primary colors of light are (3):<br>[...]<br>[...]<br>[...]" -> "red<br>green<br>blue"
  Two items are not a list: make one card with two blanks.
