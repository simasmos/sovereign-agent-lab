"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "get_edinburgh_weather", "calculate_catering_cost", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = False

TASK_A_NOTES = """
There was an issue with parsing tool calls in research_agent.py as it was
using Anthropic's tool calling format instead of OpenAI's.

Another issue was that the Nebius TokenFactory endpoint doesn't seem to
support native tool calling of Llama 3.3 70B model used by default.
Llama returned ["{\"type\": \"function\", \"name\": \"check_pub_availability\",...]
as if it treated tool descriptions as text instead of its own tools format.

After switching to Kimi-K2-Thinking, the agent started using tools correctly
and chose The Albanach as the venue for the event.
"""   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-b2c8c1ff-e042-43ba-a59b-e0b00184376e_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
Unfortunately, **The Bow Bar** cannot accommodate your event. While it does offer vegan options, its maximum capacity is only 80 guests, which falls short of your requirement for 160 people.\n\nHowever, I have excellent news! **The Albanach** is available and meets all your requirements:\n\n**The Albanach**\n- **Address:** 2 Hunter Square, Edinburgh\n- **Capacity:** 180 guests (comfortably fits your 160)\n- **Vegan Options:** Yes\n- **Status:** Available\n\nThis venue has sufficient space and can cater to your vegan requirements for tonight's event. Would you like me to proceed with calculating catering costs for this venue?
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
I'll check all of our known venues to see which can accommodate 300 people with vegan options.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = " I don't have access to train schedules or real-time transportation information. For the most accurate and up-to-date information about train times from Edinburgh Waverley to London, I'd recommend:\n\n- Checking the National Rail Enquiries website (nationalrail.co.uk) or app\n- Visiting the LNER (London North Eastern Railway) or Avanti West Coast websites\n- Calling National Rail Enquiries on 03457 48 49 50\n\nThese sources will have real-time information about tonight's services, including any delays or disruptions."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, this would be an acceptable behaviour. The agent correctly identified 
that the request was out of scope and provided helpful alternative resources
for to find the required information. It also maintained a polite and
professional tone throughout the conversation.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph Mermaid graph uses a single loop. The model decides at every step
what to execute and in which order. All routing is handled inside the model.
This means changing a model might result in different behaviour with the same
prompts and tools.

Rasa CALM has every possible flow explicitly defined in rules.yml. LLM should
only choose which flow to execute based on user input. This makes it more
predictable and easier to debug.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
While overall Kimi-2 performed well, in Task C Scenario 2 it didn't provide
any response after confirming the task. It checked all 4 venues which didn't
meet the requirements, but hasn't provided a final answer. Even if asking for
this explicitly in the prompt with "Mention if there's no such venue", it
still just goes silent. I've tried running a loop of 10 initial prompts and
only 1 of them resulted in a proper answer. 
This highlights that using LLM agents for production system requires extensive
testing and validation, especially on edge cases.
"""
