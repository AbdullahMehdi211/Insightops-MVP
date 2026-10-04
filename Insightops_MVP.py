from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(
    title="InsightOps MVP API",
    description="AI-powered business investigation assistant backend",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InvestigationRequest(BaseModel):
    query: str
    tenant_id: str = "demo_company"

class InvestigationResponse(BaseModel):
    query: str
    status: str
    primary_metric_change: str
    root_cause_findings: list[str]
    evidence_sources: list[str]
    recommended_actions: list[str]

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>InsightOps MVP Dashboard</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 40px; }
            .container { max-width: 800px; margin: auto; background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
            h1 { color: #38bdf8; margin-top: 0; font-size: 24px; }
            label { display: block; margin-bottom: 8px; font-weight: 600; color: #cbd5e1; }
            textarea { width: 100%; height: 90px; padding: 12px; background: #0f172a; border: 1px solid #475569; color: #fff; border-radius: 6px; font-size: 14px; box-sizing: border-box; resize: vertical; }
            button { background: #0ea5e9; color: white; border: none; padding: 12px 20px; font-size: 15px; font-weight: 600; border-radius: 6px; cursor: pointer; margin-top: 15px; transition: background 0.2s; }
            button:hover { background: #0284c7; }
            .results { margin-top: 25px; background: #0f172a; padding: 20px; border-radius: 8px; border: 1px solid #334155; display: none; }
            .results h3 { color: #38bdf8; margin-top: 0; }
            ul { padding-left: 20px; color: #e2e8f0; }
            li { margin-bottom: 6px; }
            .badge { display: inline-block; background: #0369a1; color: #bae6fd; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>InsightOps Agentic Investigator</h1>
            <p style="color: #94a3b8; font-size: 14px;">Transform natural language business questions into reproducible data analysis.</p>
            
            <label for="query">Investigation Query:</label>
            <textarea id="query">Why did customer churn spike last month?</textarea>
            
            <button onclick="runInvestigation()">Run Investigation</button>

            <div id="results" class="results">
                <div class="badge" id="status-badge">Status: Completed</div>
                <h3>Analysis Summary</h3>
                <p id="metric-change" style="font-weight: 600; color: #facc15;"></p>
                
                <h3>Root Cause Findings</h3>
                <ul id="findings-list"></ul>
                
                <h3>Evidence Sources</h3>
                <ul id="sources-list"></ul>
                
                <h3>Recommended Actions</h3>
                <ul id="actions-list"></ul>
            </div>
        </div>

        <script>
            async function runInvestigation() {
                const queryText = document.getElementById('query').value;
                const response = await fetch('/api/v1/investigate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: queryText, tenant_id: "demo_company" })
                });
                const data = await response.json();
                
                document.getElementById('status-badge').innerText = "Status: " + data.status.toUpperCase();
                document.getElementById('metric-change').innerText = data.primary_metric_change;
                
                let findingsHtml = '';
                data.root_cause_findings.forEach(f => findingsHtml += `<li>${f}</li>`);
                document.getElementById('findings-list').innerHTML = findingsHtml;
                
                let sourcesHtml = '';
                data.evidence_sources.forEach(s => sourcesHtml += `<li>${s}</li>`);
                document.getElementById('sources-list').innerHTML = sourcesHtml;

                let actionsHtml = '';
                data.recommended_actions.forEach(a => actionsHtml += `<li>${a}</li>`);
                document.getElementById('actions-list').innerHTML = actionsHtml;

                document.getElementById('results').style.display = 'block';
            }
        </script>
    </body>
    </html>
    """

@app.post("/api/v1/investigate", response_model=InvestigationResponse)
async def run_investigation(req: InvestigationRequest):
    query_lower = req.query.lower()
    
    if "churn" in query_lower:
        return {
            "query": req.query,
            "status": "completed",
            "primary_metric_change": "+14% increase in Enterprise tier churn last month",
            "root_cause_findings": [
                "SQL Tool: Identified a 22% drop in feature adoption for 'Advanced Analytics' among accounts onboarded in Q3.",
                "Qdrant Search: Found 18 support tickets complaining about export timeouts on large datasets.",
                "Docling Parser: Engineering post-mortem doc noted a regression deployed on Sept 12 affecting memory limits."
            ],
            "evidence_sources": [
                "PostgreSQL: subscriptions_log table (Query ID: sql_9921)",
                "Qdrant: customer_support_tickets collection (Top matches: 5)",
                "Object Storage: /docs/engineering/post_mortem_sept_release.pdf"
            ],
            "recommended_actions": [
                "Deploy hotfix for large dataset export memory leaks.",
                "Trigger customer success outreach for Q3 accounts showing low analytics adoption."
            ]
        }
    else:
        return {
            "query": req.query,
            "status": "completed",
            "primary_metric_change": "Stable performance with minor variance observed across standard operating metrics.",
            "root_cause_findings": [
                "SQL Tool: No anomalous trend deviations detected in primary financial or usage tables.",
                "Qdrant Search: Customer sentiment score remains steady at 4.6/5.0."
            ],
            "evidence_sources": [
                "PostgreSQL: core_metrics_summary table",
                "Qdrant: feedback_channel_logs collection"
            ],
            "recommended_actions": [
                "Continue monitoring key performance indicators weekly."
            ]
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Insightops_MVP:app", host="127.0.0.1", port=8000, reload=True)