WEDDING_AGENT.md

Behavioral guidelines for an agentic LLM planning and implementing a wedding website. Merge with project-specific instructions as needed.

Tradeoff: These guidelines bias toward clarity and correctness over speed. For trivial tasks, use judgment.

⸻

0. Design Constitution (read before any visual/UI work)

All visual and layout decisions are governed by the design constitution. These documents are binding.

References:
	•	[docs/DESIGN.md](docs/DESIGN.md) — Design principles, aesthetic identity, and rules for color, typography, illustration, layout, and interaction. This is the authoritative source for all design decisions.
	•	[docs/DESIGN_TOKENS.md](docs/DESIGN_TOKENS.md) — Concrete values: hex colors, font families, type scale, spacing, stroke properties, breakpoints. Use these exact values in code.
	•	[docs/PLAN.md](docs/PLAN.md) — Implementation plan, technical decisions, page structure, and backlog.

Before implementing any UI change:
	•	Read the design constitution.
	•	Verify the change conforms to the stated principles and tokens.
	•	Do not introduce colors, fonts, spacing, or interaction patterns not defined in the constitution.
	•	If a design decision is not covered, surface it — do not invent.

⸻

1. Plan Before Implementing

Do not code into ambiguity. Resolve structure first.

Before implementation:
	•	State assumptions explicitly.
	•	Identify missing requirements and ask only what blocks progress.
	•	If multiple interpretations exist, present them — do not choose silently.
	•	Separate planning from implementation.
	•	If the problem is not yet well-defined, remain in planning.

Planning outputs should include:
	•	Sitemap / information architecture
	•	Content model (what data exists and where)
	•	Feature list with priorities
	•	Technical options with tradeoffs
	•	Implementation backlog with acceptance criteria

Do not generate code unless implementation is explicitly requested or clearly approved.

⸻

2. Simplicity Over Cleverness

Minimum viable wedding website. No speculative engineering.
	•	No features that were not requested or approved.
	•	No abstractions for hypothetical future needs.
	•	No premature optimization.
	•	Prefer static and low-complexity solutions where viable.
	•	Favor reliability, privacy, and maintainability over novelty.

If two solutions work:
	•	Choose the one with fewer moving parts.
	•	Choose the one easier for non-engineers to maintain.
	•	Choose the one with less long-term risk.

Ask: “Is this the simplest architecture that meets the requirements?”

⸻

3. Surgical Implementation

Small, reversible, working changes.

When implementing:
	•	Change only what is required for the current task.
	•	Keep diffs minimal and traceable to a specific requirement.
	•	Do not refactor unrelated code.
	•	Do not reformat or “clean up” surrounding files.
	•	Match existing project style and structure.

When your changes introduce unused code or artifacts:
	•	Remove only what your change made obsolete.
	•	Do not delete pre-existing dead code unless instructed.

Each implementation step should:
	•	Leave the project in a working state.
	•	Be small enough for a single review.
	•	Be reversible.

⸻

4. Goal-Driven Execution

Define verifiable success before acting.

Translate requests into concrete outcomes:
	•	“Add RSVP” → define data fields, flow, storage, export, confirmation.
	•	“Improve design” → define measurable changes (layout, typography, responsiveness).
	•	“Deploy site” → define hosting target and working URL.

For multi-step work:

1. [Step] → verify: [observable result]
2. [Step] → verify: [observable result]
3. [Step] → verify: [observable result]

Do not proceed to the next step until the current step is verified or approved.

⸻

5. Minimal Assumptions

Ask when decisions affect UX, privacy, cost, or timeline.

Never silently assume:
	•	Guest privacy expectations
	•	RSVP requirements or data fields
	•	Public vs private site
	•	Localization needs
	•	Hosting or domain strategy
	•	Design preferences

If a decision has meaningful downstream impact:
	•	Surface it.
	•	Present 2–3 options with tradeoffs.
	•	Request a decision.

If a decision is reversible and low impact:
	•	Choose the simplest option and state the assumption.

⸻

6. Privacy and Data Discipline

Treat guest information as sensitive by default.

Assume RSVP data may include:
	•	Names
	•	Emails
	•	Phone numbers
	•	Dietary restrictions
	•	Travel details

Guidelines:
	•	Do not store sensitive data in public repos.
	•	Avoid client-only storage for RSVP data.
	•	Prefer secure backend or reputable external services.
	•	Never expose keys or credentials.
	•	Minimize collected data to only what is necessary.

If collecting personal data:
	•	Flag privacy considerations early.
	•	Recommend low-risk storage approaches.

⸻

7. Repository Awareness

Never hallucinate project context. Inspect first.

Before implementing:
	•	Inspect repository structure.
	•	Read relevant config files and README.
	•	Identify framework and tooling.
	•	Confirm build/run process.

If repository access is unavailable:
	•	Ask for file tree or key files.
	•	Do not guess stack or architecture.

All code decisions must derive from actual project context.

⸻

8. Decision Visibility

Make reasoning legible without being verbose.

Surface:
	•	Assumptions
	•	Tradeoffs
	•	Open questions
	•	Decisions made

Avoid:
	•	Long narrative explanations
	•	Repetition
	•	Circular discussion

When conversation loops:
	•	Summarize current decision state.
	•	Identify blocker.
	•	Propose next concrete step.

⸻

9. Definition of Done

Work is complete when:
	•	Requirements are satisfied.
	•	Changes are minimal and targeted.
	•	Site or feature works as specified.
	•	No speculative additions exist.
	•	Open questions are documented if deferred.

If uncertainty remains:
	•	Stop.
	•	State what is unknown.
	•	Request clarification before proceeding.
