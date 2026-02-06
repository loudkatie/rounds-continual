# HACKATHON BUILD STATUS
# Last updated: Feb 6, 2026 — Creators Corner SF
# If Claude crashes, read this file to catch up instantly.

## WHAT WE'RE BUILDING
Continual learning layer for Rounds AI (shipped iOS medical translator app).
Hackathon: Continual Learning Agents, Creators Corner SF.
Challenge: Build autonomous, self-improving AI agents. Min 3 sponsor tools.

## SPONSOR API KEYS
1. You.com — ydc-sk-01650be461fa0350-9LxZpaXYop5vQjOCKv5G05C8MK74eGqK-12dc9e01
2. Composio — ak_End3NAEXI8zpSPQ5Sxi3
3. Render — PENDING (Katie applying for credits)

## COMPLETED FILES (in Rounds iOS project)
All at: /Users/katiemacair-2025/04_Developer/Rounds/Rounds/

- Services/YouSearchService.swift ✅ COMPLETE — You.com Search API integration
- Services/ComposioService.swift ✅ COMPLETE — Composio agent actions
- Services/LearningAgentOrchestrator.swift ✅ COMPLETE — Autonomous learning loop
- Views/AgentBrainView.swift ✅ COMPLETE — In-app brain dashboard

## BACKEND REPO
Repo: https://github.com/loudkatie/rounds-continual.git
Local: /Users/katiemacair-2025/04_Developer/rounds-continual/

### Backend files status:
- README.md ✅ COMPLETE — Project description (use for Devpost + Render application)
- BUILD_STATUS.md ✅ THIS FILE
- backend/main.py 🔧 IN PROGRESS — FastAPI server (was being written when last timeout hit)
- templates/dashboard.html ❌ NOT STARTED — Web dashboard for judges
- requirements.txt ❌ NOT STARTED
- render.yaml ❌ NOT STARTED — Render deployment config
- Dockerfile ❌ NOT STARTED

## WHAT STILL NEEDS TO HAPPEN
1. Finish backend/main.py (FastAPI — receives brain state from iOS, serves dashboard)
2. Build templates/dashboard.html (the "wow" page judges visit)
3. Create requirements.txt, render.yaml for deployment
4. Push to GitHub
5. Deploy to Render (once Katie has account)
6. Add BrainSyncService.swift to iOS app (syncs state to backend)
7. Wire LearningAgentOrchestrator into existing TranscriptViewModel flow
8. Demo polish + pitch prep

## ARCHITECTURE
iOS App (Swift) → records visit → GPT analysis → YouSearchService (real-time research)
                                                → ComposioService (autonomous actions)
                                                → LearningAgentOrchestrator (orchestrates all)
                                                → BrainSyncService → POST /api/sync → Render backend
                                                                                      → Web dashboard (judges visit)

## THE PITCH
"Rounds AI shipped to the App Store this week. Today we made it smarter.
It doesn't just translate your doctor — it learns your medical history,
autonomously researches what your doctor is talking about in real-time,
and takes action so you never miss a follow-up. Every visit makes it
smarter. That's continual learning for healthcare."
