from fastipy import FastipyInstance, Request, Reply
from service.sheet import SheetService

sheetService = SheetService()


async def sheetRoutes(app:FastipyInstance, options:dict):

  @app.get("/concluded")
  def get_tables(_, reply: Reply):
    try:
      return sheetService.get_tables(), 200
    except Exception as e:
      return str(e), 500

  @app.post("/concluded")
  async def append_table(req: Request, reply: Reply):
    try:
      itens = req.body.json
      sheetService.append_table([itens['domain'], itens['updatedAt']])
      await reply.send_code(200)
    except Exception as e:
      print(e)
      await reply.send_code(500)
