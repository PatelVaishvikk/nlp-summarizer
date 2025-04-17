from transformers import pipeline

# Load summarization model (T5-small for CPU efficiency)
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

# Load paraphrasing model (pegasus-xsum)
paraphraser = pipeline("text2text-generation", model="tuner007/pegasus_paraphrase")

def summarize(text, max_length=130):
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def paraphrase(text, num_return_sequences=1):
    paraphrased = paraphraser(text, num_return_sequences=num_return_sequences)
    return [p['generated_text'] for p in paraphrased]