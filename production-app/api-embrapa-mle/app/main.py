from fastapi import FastAPI
from app.routes.production_routes import router as production_router
from app.routes.commercialization_routes import router as commercialization_router
from app.routes.processing_routes import router as processing_router
from app.routes.user_routes import router as user_router
from app.routes.exportation_routes import router as exportation_router
from app.routes.importation_routes import router as importation_router

app = FastAPI(
    title="Tech Challenge 1 - API Dados de Vitivinicultura - Embrapa",

    description="A API foi desenvolvida como parte do trabalho do curso de pós-graduação em Engenharia de Machine Learning da FIAP. Ela fornece acesso a dados detalhados sobre produção, processamento, comercialização, exportação e importação de produtos vitivinícolas, com foco na análise e monitoramento do setor.",
    version="1.0.0",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)


app.include_router(production_router)
app.include_router(commercialization_router)
app.include_router(processing_router)
app.include_router(exportation_router)
app.include_router(importation_router)
app.include_router(user_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}