---
name: anki-flashcards
description: Convert notes into an Anki .apkg deck of Basic Front/Back cards using genanki.
disable-model-invocation: true
---

1. Card every fact in the notes, in order. Add no facts that aren't in the notes.
2. Write `cards.json` as `[{"front":"...","back":"..."}]`. The notes are Markdown: name the deck with the text of the first top-level heading (`# ...`), without the `#`. If there is none, use the first heading of any level; if there are no headings, use the notes' file name without `.md`. Headings are not facts; don't make cards from them.
3. Run `python3 <skill-dir>/scripts/build.py cards.json "<Deck>" "<Deck>.apkg"`, where `<skill-dir>` is the folder containing this SKILL.md (requires `pip install genanki`). Deliver the file and the card count.

Rules:
- Reword, don't copy. Rewrite each fact as a short, clear sentence that makes sense on its own: fix grammar, split long sentences, cut filler, and use standard terms where they fit. If a term the notes don't use is the answer, follow it with the notes' meaning in parentheses. Keep the meaning of the note.
- If a note is only true in some cases, add a qualifier such as "usually" so the card is true. After the deck, list the cards you qualified.
- One fact per card. The back holds only the answer, as short as possible.
- Anki shows cards as HTML, so write every line break as `<br>`, not a newline.
- Use `[...]` for the blank on the front: "The capital of France is [...]." -> "Paris"
- Two blanks: the back lists both, "hydrogen / oxygen".
- If a card is unclear on its own, start it with the topic: "Photosynthesis: ..."
- Abbreviations are a question, not a blank: "What does DNA stand for?" -> "deoxyribonucleic acid"
- Choices: "Plants [absorb/release] CO2." -> "absorb"
- Two-way: if a fact links two things and each side has only one right answer, make a card for each direction:
  "The capital of France is [...]." and "[...] is the capital of France."
  Skip the reverse if more than one answer would fit.
- Lists: show the full list one item per line and blank one item. Make one card per item.
