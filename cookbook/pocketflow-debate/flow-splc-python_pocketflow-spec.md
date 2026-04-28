## 0. High-level Description

This WORKFLOW implements a structured debate orchestration system that evaluates claims through adversarial argumentation and judicial assessment. The workflow employs three sequential CREATE FUNCTIONs: an advocate-for function that generates supporting arguments using evidence and reasoning, an advocate-against function that produces rebuttals and counterarguments, and a judge function that evaluates both cases to declare a winner with numerical scores. Each GENERATE call produces structured YAML output containing arguments and key points, with shared state (@claim, @case_for, @case_against, @verdict) flowing between functions. The control flow follows a simple sequential pattern without WHILE loops or EVALUATE branches, terminating with RETURN WITH status metadata including winner designation and scoring. The multi-model design supports both OpenAI and Gemini backends through adapter pattern LLM calls, with built-in retry logic and wait mechanisms for robustness.

## 1. Purpose

This implementation creates an automated debate system that evaluates the strength of claims by generating opposing arguments and rendering impartial judgment with scoring.

## 2. SPL ↔ Python/PocketFlow Construct Mapping

| SPL Construct | Python/PocketFlow Equivalent | Notes |
|---------------|-------------------------------|--------|
| `WORKFLOW <name>` | `Flow(start=node)` class with chained nodes | Declares the orchestration workflow |
| `CREATE FUNCTION <name>` | `Node` class with `prep/exec/post` methods | Reusable prompt templates with logic |
| `GENERATE <fn>(...) INTO @<var>` | `call_llm(prompt)` in `exec()` method | LLM calls storing results in shared state |
| `@<var>` (shared state) | `shared` dict passed between nodes | Variables accessible across workflow steps |
| `CALL <tool>(...) INTO @<var>` | File I/O operations in `post()` method | Side-effect operations like output saving |
| `RETURN @<var> WITH <k>=<v>` | Final `shared` state with metadata | Workflow termination with status info |
| `EXCEPTION WHEN <Type> THEN` | `max_retries` and `wait` parameters | Built-in retry logic for failure handling |
| Sequential execution | Node chaining with `>>` operator | Implicit control flow without explicit branches |

## 3. Logical Functions / Prompts

**AdvocateFor**
- **Name**: Argument Generation (Pro)
- **Role**: Creates supporting evidence and reasoning for the given claim
- **Key prompt conventions**: YAML output format with `argument` and `key_points` fields, 3-4 sentence constraint, evidence-based reasoning requirement

**AdvocateAgainst** 
- **Name**: Counter-Argument Generation (Con)
- **Role**: Rebuts the pro argument and presents opposing evidence
- **Key prompt conventions**: YAML output format, receives opponent's argument as context, focuses on rebuttal and counterarguments

**JudgeDebate**
- **Name**: Judicial Evaluation
- **Role**: Impartially evaluates both arguments and declares winner with numerical scoring
- **Key prompt conventions**: YAML output with `winner`, `score_for`, `score_against`, `verdict`, and `reasoning` fields, 1-10 scoring scale, winner selection from "FOR"/"AGAINST"

## 4. Control Flow

The execution follows a simple sequential path: Initial argument generation → Counter-argument with rebuttal → Judicial evaluation → Termination with verdict. There are no WHILE loop conditions or EVALUATE branch logic - each step executes exactly once in predetermined order. The workflow terminates with RETURN WITH status metadata including winner designation, numerical scores, and reasoning. The shared state flows linearly from @claim input through @case_for and @case_against intermediate results to final @verdict, @winner, and @score variables.

## 5. How to Regenerate as SPL

```bash
# Step 1 — generate SPL from this spec (Section 0 above as text2spl input)
spl3 text2spl --description "This WORKFLOW implements a structured debate orchestration system that evaluates claims through adversarial argumentation and judicial assessment. The workflow employs three sequential CREATE FUNCTIONs: an advocate-for function that generates supporting arguments using evidence and reasoning, an advocate-against function that produces rebuttals and counterarguments, and a judge function that evaluates both cases to declare a winner with numerical scores. Each GENERATE call produces structured YAML output containing arguments and key points, with shared state (@claim, @case_for, @case_against, @verdict) flowing between functions. The control flow follows a simple sequential pattern without WHILE loops or EVALUATE branches, terminating with RETURN WITH status metadata including winner designation and scoring. The multi-model design supports both OpenAI and Gemini backends through adapter pattern LLM calls, with built-in retry logic and wait mechanisms for robustness." --mode workflow

# Step 2 — compile to any target
spl3 splc compile <output.spl> --lang python/pocketflow
spl3 splc compile <output.spl> --lang python/langgraph  
spl3 splc compile <output.spl> --lang go
```