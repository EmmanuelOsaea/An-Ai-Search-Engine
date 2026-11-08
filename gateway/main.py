from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Distributed Search Engine API")

# Enable CORS so your frontend UI can talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Vector DB Data for instantaneous setup
MOCK_VECTOR_DB = [
    {"id": 1, "title": "Trunk-Based Automated Release Pipeline", "category": "DevOps", "score": 0.98},
    {"id": 2, "title": "Multi-Tenant Kubernetes Cluster Isolation via Cilium", "category": "Security", "score": 0.91},
    {"id": 3, "title": "Single Source of Truth Declarative GitOps via ArgoCD", "category": "GitOps", "score": 0.88},
    {"id": 4, "title": "Autonomous Self-Healing Platform Operator via LangGraph", "category": "AI Agents", "score": 0.85}
]

@app.get("/api/search")
async def search(q: str = Query(..., description="The search query string")):
    # Simulating a semantic vector similarity search
    if not q:
        return {"results": []}
    
    # Simple mock filtering to mimic vector search match scores
    filtered_results = [
        item for item in MOCK_VECTOR_DB 
        if q.lower() in item["title"].lower() or q.lower() in item["category"].lower()
    ]
    
    return {
        "query": q,
        "engine": "Vector-Native (Qdrant/AzureAI-Mock)",
        "results": filtered_results if filtered_results else MOCK_VECTOR_DB[:2]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "pipeline": "passing"}
