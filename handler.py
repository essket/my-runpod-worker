# src/handler.py
def handler(event):
    # event["input"] — это то, что ты пришлёшь в запросе
    name = (event.get("input") or {}).get("name", "world")
    return {"ok": True, "msg": f"Hello, {name}! Serverless работает."}
