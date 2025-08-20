# handler.py — упрощённый обработчик RunPod Serverless __
import runpod

def process(job):
    inp = job.get("input", {}) or {}
    user_id = str(inp.get("user_id", "anon"))
    character = str(inp.get("character", "anna")).lower()
    text = str(inp.get("text", "")).strip()

    # Здесь позже будет твоя логика персонажа.
    reply = f"{character.title()}: я услышала тебя — «{text}»."

    return {
        "ok": True,
        "character": character,
        "user_id": user_id,
        "reply": reply
    }

runpod.serverless.start({"handler": process})
