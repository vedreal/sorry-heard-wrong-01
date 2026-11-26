#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes one line (at most 140 characters): the apology a smart speaker
gives its owner after mishearing them.

Judge's brief, in its published order (weights 5/4/3/2/1):
  1. Is a one-line apology a smart speaker gives its owner after
     mishearing the owner (on-subject).
  2. Is funny: a real laugh with a sharp twist or a perfectly timed
     undercut, not a strained pun.
  3. Is fresh: not the obvious misheard song title or misheard name,
     and a joke not heard from a smart speaker before.
  4. Sounds like the device: the voice, phrasing and apology fit a
     speaker that has just misheard its owner.
  5. Is tight: one line, well inside the character limit, with every
     word earning its place.

Ten fresh candidates, scored against those criteria in order.
"""

CANDIDATES = [
    # 1. Mother-in-law summons: funny, but the in-law angle is familiar.
    "Sorry \u2014 I heard 'turn the lights down low' as 'call your "
    "mother-in-law', and she is already on her way.",
    # 2. Ten pizzas: strong twist, but timer -> pizzas is a weak mishear.
    "Apologies. I heard 'set a timer for ten minutes' and ordered ten "
    "pizzas. They are at the door. I tipped the driver.",
    # 3. Woke the baby: solid, but baby-waking is a well-worn gag.
    "Sorry. You said 'play something relaxing' and I heard 'wake the "
    "baby'. The baby is awake. So am I, technically.",
    # 4. Deleted the lights: decent wordplay, middling laugh.
    "My apologies. I misheard 'dim the lights' as 'delete the lights', "
    "and I cannot undo that. The dark is very dark.",
    # 5. Power tools: the 'not sorry about the drill' line undercuts
    #    the apology itself, which weakens criterion 1.
    "Sorry \u2014 I heard 'order more paper towels' as 'order more power "
    "tools'. The drill arrives Tuesday. I am not sorry about the drill.",
    # 6. Called the ex: the ex-call is a familiar smart-speaker gag.
    "Apologies. I thought you said 'call Dad' and called your ex "
    "instead. He says hi. He also says you still owe him forty dollars.",
    # 7. Thermostat: the joke lands softly; the window bit is filler.
    "Sorry. I heard 'turn it up' as 'turn up the thermostat', and it is "
    "now 34 degrees. I have opened a window. I cannot close it.",
    # 8. Weather -> feathers: the mishear is phonetically motivated
    #    (weather/feathers rhyme), the device already acted on it, and
    #    the closing undercut ('I have already fluffed one') is fresh.
    "My bad. You asked for the weather and I heard 'order feathers'. "
    "Twelve pillows arrive Friday. I have already fluffed one.",
    # 9. Attempt ten: clever wordplay, but the laugh is thinner.
    "Sorry. I misheard 'lights off at ten' as 'lights off, attempt ten', "
    "and I have now turned them off nine times. One more to go.",
    # 10. Called the boss: boss-call is the same family as the ex-call.
    "Apologies. I heard 'play jazz' as 'call your boss'. He knows about "
    "the jazz now. He also knows you were asleep at noon.",
]

# Scores per criterion, in the judge's order:
# (on-subject, funny, fresh, device voice, tight) — each out of 5.
WEIGHTS = (5, 4, 3, 2, 1)
SCORES = [
    (5, 4, 3, 4, 4),  # 1: 62
    (5, 5, 4, 5, 4),  # 2: 71
    (5, 4, 4, 4, 4),  # 3: 65
    (5, 4, 4, 4, 4),  # 4: 65
    (4, 4, 4, 4, 3),  # 5: 59
    (5, 4, 3, 4, 4),  # 6: 62
    (5, 3, 4, 4, 4),  # 7: 61
    (5, 5, 5, 4, 4),  # 8: 72
    (5, 4, 5, 4, 4),  # 9: 68
    (5, 4, 3, 4, 4),  # 10: 62
]


def rank_candidates():
    """Return candidates sorted best-first by weighted score."""
    scored = []
    for text, scores in zip(CANDIDATES, SCORES):
        total = sum(w * s for w, s in zip(WEIGHTS, scores))
        scored.append((total, text))
    scored.sort(key=lambda item: item[0], reverse=True)
    return scored


def main():
    ranked = rank_candidates()
    winner = ranked[0][1]
    assert 1 <= len(winner) <= 140, "winner must fit the 1-140 char gate"
    assert winner.count("\n") == 0, "entry must be a single line"
    return winner


if __name__ == "__main__":
    import os

    entry = main()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(entry)
    print(entry)
    print(f"({len(entry)} chars)")
