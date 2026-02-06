# Rounds AI — Continual Learning Medical Agent

## One-Liner
A shipped iOS app that translates doctor-speak for caregivers, now powered by an autonomous learning agent that researches medical context in real-time and takes action without human intervention.

## The Problem
When your loved one is in the ICU, you're drowning in medical jargon. Doctors speak in acronyms, vitals change daily, and you can't Google fast enough to keep up. Caregivers need a translator — but a static translator isn't enough. Medical knowledge evolves, drug interactions matter, and every patient's journey is unique.

## What Rounds AI Does
Rounds AI is a **shipped iOS app** (submitted to the App Store this week) that records doctor visits using on-device speech recognition and translates complex medical conversations into plain language a caregiver can understand.

For this hackathon, we added a **continual learning layer** that transforms Rounds from a translator into an autonomous medical research agent:

1. **LISTENS** — Records and transcribes doctor conversations (Apple Speech, on-device)
2. **ANALYZES** — GPT-4o-mini processes the transcript with full patient memory context, tracking vital trends from Day 1 baseline
3. **RESEARCHES** — Autonomously searches real-time medical sources for drug interactions, side effects, and latest research on mentioned conditions (You.com Search API)
4. **LEARNS** — Stores new medical facts in a persistent patient knowledge graph that grows smarter every session
5. **ACTS** — Creates follow-up appointment reminders, medication alerts, and trend warnings without the caregiver lifting a finger (Composio)
6. **VISUALIZES** — A live web dashboard shows the agent's brain state, knowledge growth, and learning progression over time (deployed on Render)

Every visit makes the agent smarter. That's continual learning for healthcare.

## How It Meets the Challenge Criteria

- **Autonomous operation**: After hitting "record," the agent handles research, learning, and action creation with zero human prompting
- **Continual learning**: Patient knowledge graph persists and grows across sessions — Day 10 analysis is dramatically richer than Day 1
- **Real-time data**: You.com Search API grounds every analysis in current medical knowledge, not static training data
- **Meaningful action**: Composio triggers calendar reminders, medication alerts, and trend warnings automatically
- **Observable intelligence**: Web dashboard on Render lets you watch the agent get smarter in real-time

## Sponsor Integrations

| Sponsor | Integration | Role |
|---------|------------|------|
| **You.com** | Search API | Real-time medical knowledge grounding — drug interactions, side effects, latest research with citations |
| **Composio** | Agent Actions | Autonomous post-analysis actions — Google Calendar reminders, medication alerts, trend notifications |
| **Render** | Web Service | Backend API + live dashboard showing agent brain state and learning progression |

## Tech Stack
- **iOS App**: Swift/SwiftUI, Apple Speech Recognition (on-device), GPT-4o-mini
- **Backend**: Python FastAPI on Render
- **AI/ML**: OpenAI GPT-4o-mini with custom medical system prompt, You.com Search API for real-time grounding
- **Agent Layer**: Composio for autonomous actions, custom knowledge graph with vital trend tracking
- **Memory**: Persistent patient knowledge graph with Day 1 baseline tracking, medical term normalization, cross-session pattern detection

## What Makes This Special
This isn't a hackathon prototype — it's a **production app** that we made smarter today. The continual learning layer we built transforms a shipped product into an autonomous agent that gets better at advocating for patients with every single visit.

## Team
- **Katie Mac** — CEO/Founder, Loud Labs (former Head of Developer Programs, Meta)
- **Built with**: Claude (Anthropic) as technical cofounder

## Links
- GitHub: https://github.com/loudkatie/rounds-continual
- Loud Labs: loudlabs.io
