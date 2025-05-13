from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import user, item  # 각 라우터 임포트
from app.core.config import settings

app = FastAPI(
    title="My FastAPI Application",
    description="FastAPI 백엔드 베스트 프랙티스 구조 예제",
    version="1.0.0",
)

# CORS 설정 (프론트엔드와 통신을 위한 허용 설정)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영환경에서는 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(item.router, prefix="/api/v1/items", tags=["Items"])


@app.get("/")
def read_root():
    return {"message": "Welcome to My FastAPI App"}
