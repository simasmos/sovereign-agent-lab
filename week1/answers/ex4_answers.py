"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = " I searched for venues that can accommodate at least 300 people with vegan options available, but unfortunately there are no venues in Edinburgh that meet both of these requirements.\n\nWould you like me to:\n1. **Search for venues with 300+ capacity** (without the vegan requirement) to see what's available, or\n2. **Search for venues with vegan options** at a lower capacity to see what the maximum capacity is for vegan-friendly venues?\n\nLet me know which option you'd prefer, or if you have different requirements in mind!"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Only mcp_venue_server.py needed to be updated to modify the availablity of 
the Albanach venue and make it full. The model then returned The Haymarket Vaults
at 1 Dalry Road, Edinburgh instead.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 6   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 2   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
Using MCP allows defining tools in one place and using them in multiple
agents. It also allows dynamic tools discovery, so new tools can be added
without modifying the agent code.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The Headless Automator is best suited for the research task as it's not
interactive and can run in the background for extended periods of time.
Kimi-2 was finishing the tasks in 10 seconds, but when I previously tried
DeepSeek R1, it was taking around 70 seconds overall.

The Digital Employee is best for handling the calls as it can provide
answers in real time and follow the defined conversation flow.
Allows better handling of edge cases as in the scenario with train times.
The Digital Employee stick to the conversation, but Automator comes up with
some not validated answers.

Swapping feels wrong as then the caller would wait for the Automator to finish
thinking, and the conversation would sound weird. 
The other way around, the Digital Employee would require defining the researh
flow in advance, which should be more exploratory.
"""
