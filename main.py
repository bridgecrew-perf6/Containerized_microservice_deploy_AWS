from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer
from flask import Flask, request, render_template

app = Flask(__name__)


def translate(text):
    model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)
    translated_text = translation(text, max_length=40)[0]["translation_text"]
    return translated_text


def make_story(text, story_len):
    text_generator = pipeline("text-generation")
    story = text_generator(text, max_length=story_len, do_sample=False)
    return story


@app.route("/translate", methods=["GET", "POST"])
def do_translate():
    if request.method == "POST":
        text = request.form["text"]
        trans_text = translate(text)
        return render_template("translate.html", name=1, trans_text=trans_text)
    return render_template("translate.html", name=0)


@app.route("/tell_story", methods=["GET", "POST"])
def tell_story():
    if request.method == "POST":
        text = request.form["text"]
        text_len = request.form["story_len"]
        story_text = make_story(text, text_len)
        return render_template("tell_story.html", name=1, story_text=story_text)
    return render_template("tell_story.html", name=0)


@app.route("/")
def hello():
    return render_template("hello.html", name=0)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
