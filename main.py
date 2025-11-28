from flask import Flask, request, jsonify, render_template
from langdetect import detect
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

model_cache = {}

def get_model(src_lang: str, tgt_lang: str):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    if model_name not in model_cache:
        try:
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)
            model_cache[model_name] = (tokenizer, model)
        except OSError:
            print(f"[WARN] No model found for {src_lang} → {tgt_lang}. Returning None.")
            return None, None
    return model_cache.get(model_name, (None, None))

@app.get("/marianMT_filter/filter/models")
def list_models():
    return {"models": list(model_cache.keys())}  # or any default list

def translate(text: str, src_lang: str, tgt_lang: str):
    tokenizer, model = get_model(src_lang, tgt_lang)
    if tokenizer is None or model is None:
        print(f"[WARN] No translation model for {src_lang} → {tgt_lang}, returning original text.")
        return text

    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    translated = model.generate(**inputs)
    tgt_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return tgt_text

@app.route("/translate", methods=["POST"])
def translate_route():
    data = request.json or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400

    src_lang = data.get("src_lang")
    tgt_lang = data.get("tgt_lang")

    # Explicit src/tgt given
    if src_lang and tgt_lang:
        translated = translate(text, src_lang, tgt_lang)
        return jsonify({
            "src_lang": src_lang,
            "tgt_lang": tgt_lang,
            "translation": translated
        })

    # Auto-detect case
    detected_lang = detect(text)
    if detected_lang == "en":
        translation = text  # already English
    else:
        translation = translate(text, detected_lang, "en")

    return jsonify({
        "detected_language": detected_lang,
        "src_lang": detected_lang,
        "tgt_lang": "en",
        "translation": translation
    })

# ----- Stub endpoint for Open WebUI chat/completion -----
@app.route("/v1/chat/completions", methods=["POST"])
def chat_completions_stub():
    data = request.json or {}
    prompt = data.get("prompt", "")
    return jsonify({
        "id": "dummy-id",
        "object": "chat.completion",
        "choices": [
            {
                "text": prompt,
                "index": 0,
                "finish_reason": "stop"
            }
        ]
    })

@app.route("/")

def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
