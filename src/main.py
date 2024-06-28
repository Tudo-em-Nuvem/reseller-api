import uvicorn

from fastipy import Fastipy
from controller.sheet import sheetRoutes

app = Fastipy().cors()

app.register(sheetRoutes, {"prefix": "/omie"})
if __name__ == "__main__":
  uvicorn.run("main:app", log_level="debug", port=80, reload=True, loop="asyncio")