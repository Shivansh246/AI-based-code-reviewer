# Security Review Prototype

A VS Code security-review prototype combining static analysis,
LLM semantic analysis, dependency/CVE checks, risk scoring,
voice interaction, adaptive feedback, multimodal experiments,
and explainable findings.

## Project Goal

Build a working prototype over 8 weeks.

The project focuses on integrating existing libraries and
pretrained models rather than training a large model from scratch.

## Week 1 — ML Foundation

# Week 2 Risk Scoring Model

## Goal

Provide a simple and transparent way to estimate vulnerability severity
using exploitability and impact.

## Inputs

Both inputs use a 0-10 scale.

### Exploitability

Measures how easily an attacker could take advantage of the vulnerability.

- 0-2: Very difficult
- 3-5: Moderate difficulty
- 6-8: Relatively easy
- 9-10: Very easy

### Impact

Measures the potential damage if the vulnerability is successfully exploited.

- 0-2: Minimal impact
- 3-5: Limited impact
- 6-8: Significant impact
- 9-10: Severe impact

## Risk Formula

Risk Score = (0.6 × Exploitability) + (0.4 × Impact)

Exploitability has a slightly higher weight because vulnerabilities
that are easy to exploit should receive additional priority.

## Severity Mapping

| Risk Score | Severity |
|------------|----------|
| 0-2.9      | Low      |
| 3-5.9      | Medium   |
| 6-7.9      | High     |
| 8-10       | Critical |

## Assumptions

1. Exploitability and impact are independent scores.
2. Both scores are normalized to 0-10.
3. The model is intentionally simple and explainable.
4. The score is a prioritization mechanism, not a replacement for
   established vulnerability scoring systems.
5. The model can be improved later using more detailed security signals.