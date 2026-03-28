
# Overview

## One-page Executive Brief — Groq Pricing Model

Groq prices AI services by aligning cost with the natural unit of work for each modality:

- **LLMs:** tokens
- **Text to speech (TTS):** characters
- **Speech to text (STT):** audio hours
- **Tools (search, browser, code):** requests or time

This keeps pricing predictable, comparable, and easy to model in downstream financial planning.

---

## 1. Large Language Models (LLMs)

**Billing unit:**

- Per 1M input tokens
- Per 1M output tokens
- Optional per 1M cached input tokens (discounted)

**Key levers:**

- *Input vs. output split*: Enables cost control by constraining generation length while allowing rich prompts.
- *Caching*: Repeated prompts (or shared system prompts) can be billed at a lower cached input rate, materially reducing cost for high reuse workloads.
- *Performance disclosure*: Tokens per second (TPS) and context window are surfaced so teams can trade off latency vs. cost vs. capability.

**Executive implication:** LLM workloads are straightforward to forecast:

$$
	ext{Cost} \approx (\text{input tokens} \times P_{in}) + (\text{output tokens} \times P_{out}) - \text{cached savings}
$$

---

## 2. Text to Speech (TTS) Models

**Billing unit:**

- Per 1M characters generated

**Performance metric:**

- Characters per second

**Rationale:** TTS models don’t operate on tokens in the user-visible sense; they emit characters. Billing per character directly reflects the volume of synthesized speech.

**Executive implication:** TTS cost scales linearly with text length. It’s easy to budget for fixed content libraries (e.g., IVR scripts, training content, product copy).

---

## 3. Speech to Text (STT) Models

**Billing unit:**

- Per hour of audio processed
- Typically with a minimum billable duration per request (e.g., 10 seconds)

**Performance metric:**

- Speed factor (how many times faster than real time)

**Rationale:** Transcription cost is driven by audio duration, not textual complexity. Hour-based billing is the most intuitive and industry standard approach.

**Executive implication:** STT cost is predictable from media inventory (hours of calls, meetings, or content). Speed factor informs infra planning and user experience (near real time vs. batch).

---

## 4. Platform Tools (Search, Browsing, Code Execution)

**Billing units:**

- Per 1,000 requests for search and web tools
- Per hour for code execution and browser automation

These are metered independently of model usage and can be treated as adjacent line items in cost models.

**Executive implication:** Tooling costs are small but important for complex agents and RAG systems. They should be modeled as separate drivers in unit economics analyses (e.g., cost per workflow, cost per ticket, cost per customer interaction).

---

## 5. Strategic Takeaways

- **Modality-aligned billing:** Tokens, characters, and hours map cleanly to how each model is used.
- **Forecast ability:** Clear per unit pricing enables robust cost modeling and scenario analysis.
- **Optimization levers:**
  - Prompt design and max tokens for LLMs
  - Text length for TTS
  - Audio duration and batching for STT
  - Tool call frequency and time-boxed execution for platform tools
- **Enterprise fit:** The structure is compatible with internal chargeback models, per product P&L, and margin tracking at the feature or workflow level.
