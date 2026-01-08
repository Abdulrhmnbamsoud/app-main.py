from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="MetaView API", version="1.0.0")

class SearchRequest(BaseModel):
    query: str
    top_k: int = 20
    domain: Optional[str] = None
    country: Optional[str] = None
    source: Optional[str] = None
    min_date: Optional[str] = None
    max_date: Optional[str] = None

@app.get("/health")
def health():
    return {"status": "ok", "service": "metaview"}

# مبدئيًا endpoint بسيط للتأكد إن السيرفر شغال
@app.post("/semantic-search")
def semantic_search_api(body: SearchRequest):
    return {
        "query": body.query,
        "top_k": body.top_k,
        "filters": {
            "domain": body.domain,
            "country": body.country,
            "source": body.source,
            "min_date": body.min_date,
            "max_date": body.max_date,
        },
        "count": 0,
        "results": []
    }
