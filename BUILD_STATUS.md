# HACKATHON BUILD STATUS
# Last updated: Feb 6, 2026 ~4:30pm — Creators Corner SF
# If Claude crashes, read this file to catch up instantly.

## WHAT WE'RE BUILDING
Continual learning layer for Rounds AI (shipped iOS medical translator app).
Hackathon: Continual Learning Agents, Creators Corner SF.
Challenge: Build autonomous, self-improving AI agents. Min 3 sponsor tools.

## SPONSOR API KEYS
1. You.com ✅ — ydc-sk-01650be461fa0350-9LxZpaXYop5vQjOCKv5G05C8MK74eGqK-12dc9e01
2. Composio ✅ — ak_End3NAEXI8zpSPQ5Sxi3
3. Render — PENDING (Katie applying for credits)

## COMPLETED — iOS FILES (in Rounds Xcode project)
Path: /Users/katiemacair-2025/04_Developer/Rounds/Rounds/

- Services/YouSearchService.swift ✅ — You.com Search API integration
- Services/ComposioService.swift ✅ — Composio agent actions  
- Services/LearningAgentOrchestrator.swift ✅ — Autonomous learning loop
- Views/AgentBrainView.swift ✅ — In-app brain dashboard

## COMPLETED — BACKEND (rounds-continual repo)
Repo: https://github.com/loudkatie/rounds-continual
Local: /Users/katiemacair-2025/04_Developer/rounds-continual/
PUSHED TO GITHUB ✅

- README.md ✅ — Full project description (use for Devpost + Render form)
- BUILD_STATUS.md ✅ — This file
- backend/main.py ✅ — FastAPI server with brain sync API + demo seed
- templates/dashboard.html ✅ — Live web dashboard (dark, auto-refreshing)
- requirements.txt ✅ — Python dependencies
- render.yaml ✅ — Render deployment config
- .gitignore ✅

## WHAT STILL NEEDS TO HAPPEN
1. ❌ Deploy to Render (waiting on Katie's account/credits)
2. ❌ Add BrainSyncService.swift to iOS app (sends state to backend)
3. ❌ Wire LearningAgentOrchestrator into TranscriptViewModel
4. ❌ Add Config.plist with API keys to iOS project
5. ❌ Test the full loop: Record → Analyze → Research → Act → Sync → Dashboard
6. ❌ Demo polish + pitch prep

## DEMO FLOW
1. Visit Render URL → dashboard shows empty brain
2. Hit POST /api/demo/seed → dashboard fills with 10-day patient journey
3. Show how knowledge grows: Day 1 (3 facts) → Day 10 (47 facts)
4. Show vital trends with color-coded progression
5. Show autonomous research with citations
6. Show agent actions (calendar reminders, alerts)
7. Pitch: "Shipped this week. Made it smarter today."

## THE PITCH
"Rounds AI shipped to the App Store this week. Today we made it smarter.
It doesn't just translate your doctor — it learns your medical history,
autonomously researches what your doctor is talking about in real-time,
and takes action so you never miss a follow-up. Every visit makes it
smarter. That's continual learning for healthcare."
