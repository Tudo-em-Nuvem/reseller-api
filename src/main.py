import uvicorn

from fastipy import Fastipy
from controller.sheet import sheetRoutes

app = Fastipy().cors()

app.register(sheetRoutes, {"prefix": "/omie"})
if __name__ == "__main__":
  uvicorn.run("main:app", host='0.0.0.0', port=80, reload=True, loop="asyncio")