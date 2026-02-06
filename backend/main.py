# Rounds AI — Continual Learning Backend
# Hackathon: Creators Corner SF, Feb 6, 2026
# Sponsors: You.com, Composio, Render

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uvicorn

app = FastAPI(title="Rounds AI — Continual Learning Agent", version="1.0.0")
import pathlib

_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(_BASE_DIR / "templates"))

# ─────────────────────────────────────────────
# IN-MEMORY STORE
# ─────────────────────────────────────────────

agent_state = {
    "patient_name": "",
    "caregiver_name": "",
    "diagnosis": "",
    "sessions_analyzed": 0,
    "facts_learned": 0,
    "research_queries": 0,
    "actions_taken": 0,
    "vital_trends": {},
    "knowledge_categories": {},
    "learning_log": [],
    "research_history": [],
    "action_history": [],
    "medical_facts": [],
    "last_updated": None,
    "created_at": datetime.utcnow().isoformat(),
}

# ─────────────────────────────────────────────
# MODELS
# ─────────────────────────────────────────────

class BrainSync(BaseModel):
    patient_name: str = ""
    caregiver_name: str = ""
    diagnosis: str = ""
    sessions_analyzed: int = 0
    facts_learned: int = 0
    research_queries: int = 0
    actions_taken: int = 0
    vital_trends: dict = {}
    knowledge_categories: dict = {}
    medical_facts: list = []
    learning_log: list = []
    research_history: list = []
    action_history: list = []

class LearningEvent(BaseModel):
    event_type: str
    description: str
    details: dict = {}

class ResearchResult(BaseModel):
    query: str
    category: str
    findings: list = []
    sources: list = []
    relevance_score: float = 0.0

class AgentAction(BaseModel):
    action_type: str
    description: str
    status: str = "completed"
    details: dict = {}

# ─────────────────────────────────────────────
# API ENDPOINTS
# ─────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "state": agent_state,
    })

@app.get("/api/brain")
async def get_brain_state():
    return JSONResponse(content=agent_state)

@app.post("/api/sync")
async def sync_brain(data: BrainSync):
    global agent_state
    agent_state.update({
        "patient_name": data.patient_name,
        "caregiver_name": data.caregiver_name,
        "diagnosis": data.diagnosis,
        "sessions_analyzed": data.sessions_analyzed,
        "facts_learned": data.facts_learned,
        "research_queries": data.research_queries,
        "actions_taken": data.actions_taken,
        "vital_trends": data.vital_trends,
        "knowledge_categories": data.knowledge_categories,
        "medical_facts": data.medical_facts,
        "learning_log": data.learning_log,
        "research_history": data.research_history,
        "action_history": data.action_history,
        "last_updated": datetime.utcnow().isoformat(),
    })
    return {"status": "synced", "facts_learned": data.facts_learned}

@app.post("/api/event")
async def log_event(event: LearningEvent):
    agent_state["learning_log"].append({
        "event_type": event.event_type,
        "description": event.description,
        "details": event.details,
        "timestamp": datetime.utcnow().isoformat(),
    })
    # Trim to last 200
    if len(agent_state["learning_log"]) > 200:
        agent_state["learning_log"] = agent_state["learning_log"][-200:]
    return {"status": "logged"}

@app.post("/api/research")
async def log_research(result: ResearchResult):
    agent_state["research_history"].append({
        "query": result.query,
        "category": result.category,
        "findings": result.findings,
        "sources": result.sources,
        "relevance_score": result.relevance_score,
        "timestamp": datetime.utcnow().isoformat(),
    })
    agent_state["research_queries"] = len(agent_state["research_history"])
    return {"status": "logged"}

@app.post("/api/action")
async def log_action(action: AgentAction):
    agent_state["action_history"].append({
        "action_type": action.action_type,
        "description": action.description,
        "status": action.status,
        "details": action.details,
        "timestamp": datetime.utcnow().isoformat(),
    })
    agent_state["actions_taken"] = len(agent_state["action_history"])
    return {"status": "logged"}

@app.get("/api/health")
async def health():
    return {"status": "alive", "agent": "rounds-ai", "version": "1.0.0"}

# ─────────────────────────────────────────────
# DEMO: Pre-seed with realistic data for judges
# ─────────────────────────────────────────────

@app.post("/api/demo/seed")
async def seed_demo():
    """Pre-seeds the dashboard with a realistic 10-day patient journey."""
    global agent_state
    agent_state = {
        "patient_name": "David",
        "caregiver_name": "Katie",
        "diagnosis": "Double lung transplant",
        "sessions_analyzed": 10,
        "facts_learned": 47,
        "research_queries": 23,
        "actions_taken": 8,
        "vital_trends": {
            "Creatinine": {"readings": [1.2, 1.8, 2.4, 2.1, 2.6, 3.0, 2.8, 3.2, 2.9, 3.1], "unit": "mg/dL", "direction": "rising", "baseline": 1.2},
            "FiO2": {"readings": [100, 80, 60, 50, 45, 40, 35, 35, 30, 30], "unit": "%", "direction": "falling", "baseline": 100},
            "Tacrolimus Level": {"readings": [0, 4.2, 6.8, 8.1, 7.5, 9.2, 8.8, 10.1, 9.5, 10.0], "unit": "ng/mL", "direction": "rising", "baseline": 0},
            "WBC": {"readings": [18.5, 15.2, 12.8, 14.1, 11.5, 10.2, 9.8, 11.0, 8.5, 9.2], "unit": "K/uL", "direction": "falling", "baseline": 18.5},
            "Temperature": {"readings": [101.2, 100.8, 99.5, 98.8, 99.1, 98.6, 98.9, 98.6, 98.7, 98.6], "unit": "°F", "direction": "stable", "baseline": 101.2},
        },
        "knowledge_categories": {
            "drug_interaction": 7,
            "side_effect": 6,
            "condition": 5,
            "procedure": 3,
            "latest_research": 2,
        },
        "medical_facts": [
            "Patient received bilateral lung transplant on Day 0",
            "Tacrolimus is primary immunosuppressant — target level 8-12 ng/mL",
            "Creatinine trending upward may indicate tacrolimus nephrotoxicity",
            "FiO2 weaning from 100% to 30% indicates improving lung function",
            "Bronchoscopy on Day 3 showed no acute rejection (A0, B0)",
            "Mycophenolate 1000mg BID added Day 2 for rejection prophylaxis",
            "Prednisone taper: 125mg → 60mg → 40mg → 20mg over 10 days",
            "[Research] Tacrolimus + mycophenolate increases nephrotoxicity risk by 23%",
            "[Research] Post-transplant creatinine >2.5 within 10 days warrants nephrology consult",
            "[Research] FiO2 weaning to 30% by Day 10 is ahead of typical recovery curve",
            "Patient tolerating oral tacrolimus as of Day 4",
            "Chest tube removed Day 5 — drainage <100mL/24hr",
            "[Research] Early chest tube removal (Day 5) associated with faster mobilization",
            "Physical therapy started Day 6 — patient walked 50 feet with walker",
        ],
        "learning_log": [
            {"event_type": "transcript_analyzed", "description": "Day 1: Initial ICU rounds — 1,847 chars", "timestamp": "2026-01-27T08:30:00Z"},
            {"event_type": "research_triggered", "description": "Researched tacrolimus + mycophenolate interactions", "timestamp": "2026-01-27T08:31:00Z"},
            {"event_type": "fact_learned", "description": "Learned: Tacrolimus target level 8-12 ng/mL for lung transplant", "timestamp": "2026-01-27T08:31:30Z"},
            {"event_type": "action_taken", "description": "📅 Created reminder: Follow-up tacrolimus level check", "timestamp": "2026-01-27T08:32:00Z"},
            {"event_type": "transcript_analyzed", "description": "Day 3: Bronchoscopy results rounds — 2,103 chars", "timestamp": "2026-01-29T09:15:00Z"},
            {"event_type": "research_triggered", "description": "Researched bronchoscopy grading A0 B0 meaning", "timestamp": "2026-01-29T09:16:00Z"},
            {"event_type": "knowledge_enriched", "description": "Added 4 research findings to patient memory", "timestamp": "2026-01-29T09:16:30Z"},
            {"event_type": "pattern_detected", "description": "⚠️ Creatinine has risen for 3 consecutive sessions", "timestamp": "2026-01-31T08:45:00Z"},
            {"event_type": "action_taken", "description": "⚠️ Alert: Creatinine trending — may indicate tacrolimus nephrotoxicity", "timestamp": "2026-01-31T08:45:30Z"},
            {"event_type": "transcript_analyzed", "description": "Day 10: Discharge planning rounds — 3,215 chars", "timestamp": "2026-02-05T10:00:00Z"},
            {"event_type": "research_triggered", "description": "Researched post-transplant discharge criteria", "timestamp": "2026-02-05T10:01:00Z"},
            {"event_type": "fact_learned", "description": "Learned: FiO2 at 30% by Day 10 is ahead of typical recovery", "timestamp": "2026-02-05T10:01:30Z"},
            {"event_type": "action_taken", "description": "📅 Created reminder: Outpatient pulmonology follow-up in 7 days", "timestamp": "2026-02-05T10:02:00Z"},
        ],
        "research_history": [
            {"query": "tacrolimus mycophenolate drug interaction transplant", "category": "drug_interaction", "findings": ["Concurrent use increases nephrotoxicity risk by 23%", "Monitor creatinine closely when both drugs are used"], "sources": ["https://pubmed.ncbi.nlm.nih.gov/"], "relevance_score": 1.0, "timestamp": "2026-01-27T08:31:00Z"},
            {"query": "bronchoscopy grading A0 B0 lung transplant", "category": "procedure", "findings": ["A0 = no acute rejection, B0 = no airway inflammation", "Best possible result for surveillance bronchoscopy"], "sources": ["https://www.ishlt.org/"], "relevance_score": 0.75, "timestamp": "2026-01-29T09:16:00Z"},
            {"query": "creatinine rising tacrolimus nephrotoxicity", "category": "side_effect", "findings": ["Creatinine >2.5 mg/dL with tacrolimus suggests nephrotoxicity", "Consider dose reduction or switch to alternative immunosuppressant"], "sources": ["https://www.uptodate.com/"], "relevance_score": 1.0, "timestamp": "2026-01-31T08:45:00Z"},
        ],
        "action_history": [
            {"action_type": "calendar_reminder", "description": "📅 Reminder: Follow-up tacrolimus level check", "status": "completed", "timestamp": "2026-01-27T08:32:00Z"},
            {"action_type": "trend_alert", "description": "⚠️ Creatinine rising for 3 consecutive sessions", "status": "completed", "timestamp": "2026-01-31T08:45:30Z"},
            {"action_type": "medication_alert", "description": "💊 Drug interaction: tacrolimus + mycophenolate nephrotoxicity risk", "status": "completed", "timestamp": "2026-01-27T08:31:30Z"},
            {"action_type": "calendar_reminder", "description": "📅 Outpatient pulmonology follow-up in 7 days", "status": "completed", "timestamp": "2026-02-05T10:02:00Z"},
        ],
        "last_updated": datetime.utcnow().isoformat(),
        "created_at": "2026-01-27T08:30:00Z",
    }
    return {"status": "seeded", "sessions": 10, "facts": 47}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
