"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
70B model correctly answered all three conditions, although the XML and
SANDWICH answers returned the venue that appeared first in the list,
while PLAIN returned the one closer to the end. 
This shows that structured input overcomes recency bias.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Albanach"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = True

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
When running the experiment with provided list of distractors, the results were
similar to PART A and can be found in ex1_results_original.json file. But when
running the experiment several times the output of PART B XML condition was
malformed sometimes. It contained both correct venue names separated by a new line.
I've added a new script exercise1_context_loop.py to run the experiment 100 times
to check for consistency. There's ex1_results_loop.json file that has additional
flag "different_from_first": true for 6 experiments where this reproduced.
This might happen because the querry isn't strict enough about providing a single
venue name. Using 'Reply with exactly one venue name, nothing else' fixes the issue.

I also modified the list with distractors by adding two additional passing pub
names for PART C. It led to PART B providing a similar answer for all 3 conditions,
negating the recency bias in plain format due to stronger signal density and 
going for primacy 
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Guilford Arms"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
With the original list of distractors all 3 conditions were answered correctly
by the small model.
Interestingly, it was addition of two passing venues to the list that made
PLAIN condition fail and use a venue without vegan options. It was passing fine
when adding venues with come constraint violated.
The plain format is the one where the small model failed as The Guilford Arms 
is 3rd venue in the list of 11, also the model fixates on big capacity and misses
vegan constraint without any structural guardrails.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when accuracy is important, context is long,
model is small or specific output format is required.

XML format changes the model processing from narrative to data processing mode,
allowing to filter data more effectively as seen in PART A of the exercise.

Being more strict with the prompts also helps to remove unexpected outputs
which happened in PART B.

Increasing the context length can lead to model, especially a small one,
making mistakes, as demonstrated in PART C. Providing structural guardrails
is required to keep the model on track and avoid it dropping important details.

Signal density changes bias direction. With sparce answers plain format shows
recency bias and primacy bias with dense answers. This can be seen in PART B
change from "The Haymarket Vaults" when using the original list (2/9 passing venues)
to "The Albanach" (4/11).

Although we tried to achieve deterministic results, PART B output was inconsistent.
In some of the experiments running the same prompt in a loop provided long
consecutive streaks of a malformed answer. This might be due to the load balancer
routing requests to a different model replica that caused results to flip.
"""
