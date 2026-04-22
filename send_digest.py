import json, urllib.request

msg = """☀️ *Good Morning — Tech Briefing for 2026-04-22*

🔵 *Tim Cook Is Out — John Ternus to Lead Apple Starting September*
Apple announced Monday that Tim Cook will step down as CEO and become executive chairman, handing the reins to John Ternus, 50, the hardware engineering chief who oversaw the iPhone, iPad, and Vision Pro. Ternus inherits a company lagging rivals on AI and facing a landmark DOJ antitrust case.
[Read more →](https://www.cnbc.com/2026/04/20/apple-names-john-ternus-ceo-replacing-tim-cook-who-becomes-chairman.html) · _CNBC, TechCrunch, Bloomberg, NBC News, ABC News_ · 📡 6+ sources

🔴 *OpenAI Hits $25B Revenue and Is Eyeing a Late-2026 IPO*
OpenAI has crossed $25 billion in annualized revenue and is reportedly taking early steps toward a public listing, potentially by late 2026. Rival Anthropic is close behind at ~$19B ARR — the two are now the most commercially successful AI labs in history.
[Read more →](https://llm-stats.com/ai-news) · _LLM Stats_

🟢 *Anthropic Releases Claude Mythos 5 — the First 10-Trillion-Parameter Model*
Anthropic released Claude Mythos 5, described as the first ten-trillion-parameter AI model, built for high-stakes work in cybersecurity and research. Separately, Anthropic's Model Context Protocol crossed 97 million installs — it's now the default standard for AI agents connecting to external tools and APIs.
[Read more →](https://www.crescendo.ai/news/latest-ai-news-and-updates) · _Crescendo AI_

🟡 *GPT-5.4 Can Now Run Your Computer Autonomously*
OpenAI says GPT-5.4 has cleared human-level performance on desktop task benchmarks and can act as a fully autonomous OS-level agent — running apps, managing files, and completing multi-step workflows without supervision. It's a meaningful shift from AI as assistant to AI as operator.
[Read more →](https://www.devflokers.com/blog/ai-news-last-24-hours-april-2026-model-releases-breakthroughs) · _devFlokers_

🟠 *This Week's Tech Layoffs Were Explicitly Blamed on AI Efficiency*
A cluster of companies disclosed headcount cuts last week, with executives directly citing AI-driven productivity gains as the cause. Roles in code review, content, and customer support are shrinking as generative tools handle more of the load — a pattern accelerating even as company revenues grow.
[Read more →](https://techstartups.com/2026/04/20/top-tech-news-today-april-20-2026/) · _Tech Startups_

🟣 *Blue Origin Reuses a New Glenn Booster for the First Time*
New Glenn's third launch on April 19 hit a milestone: its first-stage booster was recovered and is being prepped for reuse. The achievement closes a key gap with SpaceX's Falcon 9 and gives Blue Origin a path toward competitive launch economics.
[Read more →](https://techstartups.com/2026/04/20/top-tech-news-today-april-20-2026/) · _Tech Startups_

_Also worth reading:_
• [ChatGPT Was Down for 90+ Minutes on April 20](https://www.techradar.com/news/live/chatgpt-down-april-2026) · _TechRadar_ — OpenAI confirmed the partial outage; service restored same day
• [AI Training AI Spreads Hidden Biases, Nature Finds](https://www.nature.com/articles/d41586-026-01224-1) · _Nature_ — Model-to-model training propagates subtle, hard-to-detect biases
• [SoundHound Buys LivePerson for ~$250M, Shares Fall](https://www.fool.com/coverage/stock-market-today/2026/04/21/stock-market-today-april-21-soundhound-ai-falls-after-announcing-all-stock-liveperson-acquisition/) · _Motley Fool_ — All-stock deal to combine voice and conversational AI platforms
• [20% of Companies Are Capturing 75% of AI's Economic Value](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html) · _PwC_ — New study shows AI ROI is highly concentrated among top performers

_⚠️ Some news sources were unreachable today — coverage may be narrower than usual._

_@MarvinZhangTelegramableBot_"""

payload = json.dumps({
    "chat_id": "5465534784",
    "text": msg,
    "parse_mode": "Markdown",
    "disable_web_page_preview": True
}).encode()

req = urllib.request.Request(
    "https://api.telegram.org/bot8082240790:AAGTsbXS_GGtN7sEvDBbEkbm4_RveYOfEAs/sendMessage",
    data=payload,
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read().decode())
    if result.get("ok"):
        print("✅ Digest sent successfully!")
    else:
        print("❌ Error:", result)
