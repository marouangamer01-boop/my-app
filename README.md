# Colab Model Runner 🚀

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/colab-model-runner/blob/main/runner.ipynb)

A turnkey solution to host open-source GGUF Large Language Models (Mistral, LLaMA, Qwen, DeepSeek, Gemma, Phi) directly on Google Colab using GPU acceleration (`llama-cpp-python`). It creates an OpenAI-compatible API endpoint secured with dynamic API keys and exposes a public URL via tunneling.

---

## 🇸🇦 الوصف بالعربية (Arabic Overview)

أداة لتشغيل نماذج الذكاء الاصطناعي مفتوحة المصدر بصيغة GGUF سحابياً عبر Google Colab، والاستفادة من معالجات الرسوميات (Nvidia T4 / V100 / A100)، مع توليد مفتاح API سري ورابط عام آمن متوافق تماماً مع صيغة واجهة برمجة تطبيقات OpenAI (`/v1/chat/completions`).

### المميزات الرئيسية:
- **دعم تسريع العتاد GPU**: تجميع `llama-cpp-python` مع دعم كامل لـ CUDA.
- **واجهة متوافقة مع OpenAI**: يعمل بسلاسة مع أي مكتبة تدعم OpenAI SDK مثل LangChain و LlamaIndex وتطبيقات الويب.
- **حفظ النماذج في Google Drive**: خيار اختياري لحفظ الملفات لتفادي إعادة التحميل عند كل جلسة.
- **حماية بمفتاح Bearer Token**: توليد مفتاح آمن بصيغة `sk-colab-xxxx` للتحقق من هوية الطلبات.
- **نفق عام (Tunneling)**: إتاحة عنوان URL عام للربط المباشر مع تطبيقاتك ومواقعك خارج Colab.

---

## 🇬🇧 English Overview & Quickstart

### Prerequisites
- Google Account with access to [Google Colab](https://colab.research.google.com/)
- Optional: Free [ngrok auth token](https://dashboard.ngrok.com/get-started/your-authtoken) (or localtunnel)
- A GGUF model download URL (e.g. Hugging Face direct link)

### Step-by-Step Usage Guide

1. **Open the Notebook**:
   Click the **Open in Colab** badge above or open `runner.ipynb` in Colab.
2. **Enable GPU**:
   Go to `Runtime` > `Change runtime type` > Select `T4 GPU` (or better) > `Save`.
3. **Run Cell 1 (Setup)**:
   Validates CUDA detection and installs `llama-cpp-python`, `fastapi`, `uvicorn`, and `pyngrok`.
4. **Configure Parameters (Cell 2)**:
   - `MODEL_URL`: Direct link to your `.gguf` file (e.g. Hugging Face `resolve/main/...gguf`).
   - `USE_GOOGLE_DRIVE`: Check if you want to store the model permanently in your Google Drive.
   - `NGROK_AUTHTOKEN`: Your ngrok token for stable tunneling (recommended).
   - `N_GPU_LAYERS`: Number of layers to offload to GPU (`-1` for all layers).
5. **Download Model (Cell 3)**:
   Streams the model with progress tracking and validates disk integrity.
6. **Start Server (Cell 4)**:
   Spins up FastAPI on background threads, establishes the public tunnel, and prints your **Base URL**, **API Key**, and a copy-paste ready `cURL` request.

---

## 🔌 API Testing & Integration

### cURL Example
```bash
curl -X POST "https://<YOUR-TUNNEL-URL>/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-colab-xxxxxxxxxxxxxxxx" \
  -d '{
    "messages": [
      {"role": "system", "content": "You are a helpful and concise AI assistant."},
      {"role": "user", "content": "Explain quantum computing in one sentence."}
    ],
    "temperature": 0.7,
    "max_tokens": 150
  }'
```

### Python OpenAI SDK Example
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://<YOUR-TUNNEL-URL>/v1",
    api_key="sk-colab-xxxxxxxxxxxxxxxx"
)

response = client.chat.completions.create(
    model="colab-gguf-model",
    messages=[
        {"role": "user", "content": "Hello, what model are you?"}
    ]
)

print(response.choices[0].message.content)
```

---

## 📁 Repository Structure

```
colab-model-runner/
├── runner.ipynb           # Complete Colab interactive notebook
├── requirements.txt       # Python dependencies
├── client_example.py      # Python script to test the remote endpoint
├── .gitignore             # Standard git exclusions
└── README.md              # Project documentation
```

## 📄 License
MIT License - free for personal and commercial usage.