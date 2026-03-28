#!/usr/bin/env python3
"""Tech news digest collector — scrapes HN top stories + article text."""

import json
import sys
import time
import urllib.request
import urllib.error

HN_API = "https://hacker-news.firebaseio.com/v0"
HN_ITEM = f"{HN_API}/item/{{}}.json"
HN_TOP  = f"{HN_API}/topstories.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_json(url, timeout=10):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def fetch_text(url, timeout=12):
    """Best-effort plain-text extraction from an article URL."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read(200_000).decode("utf-8", errors="replace")
    except Exception:
        return ""

    # Strip scripts/styles, collapse whitespace
    import re
    raw = re.sub(r"(?s)<script[^>]*>.*?</script>", " ", raw)
    raw = re.sub(r"(?s)<style[^>]*>.*?</style>", " ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = "\n".join(
        ln.strip() for ln in raw.splitlines() if len(ln.strip()) > 60
    )
    return raw[:8000]


def hn_source(url):
    if not url:
        return "news.ycombinator.com"
    import urllib.parse
    host = urllib.parse.urlparse(url).netloc
    return host.removeprefix("www.")


def collect(n_candidates=12, n_output=9):
    print("Fetching HN top stories …", file=sys.stderr)
    try:
        top_ids = fetch_json(HN_TOP)[:60]
    except Exception as e:
        print(f"HN fetch failed: {e}", file=sys.stderr)
        top_ids = []

    stories = []
    seen_domains = {}

    for sid in top_ids:
        if len(stories) >= n_candidates:
            break
        try:
            item = fetch_json(HN_ITEM.format(sid))
        except Exception:
            continue

        if item.get("type") != "story":
            continue

        score = item.get("score", 0)
        if score < 50:
            continue

        url   = item.get("url", f"https://news.ycombinator.com/item?id={sid}")
        title = item.get("title", "")
        comments = item.get("descendants", 0)
        source = hn_source(url)

        # Limit two stories per domain
        if seen_domains.get(source, 0) >= 2:
            continue
        seen_domains[source] = seen_domains.get(source, 0) + 1

        print(f"  [{score:>4}] {title[:70]}", file=sys.stderr)
        article_text = fetch_text(url)
        time.sleep(0.3)

        stories.append({
            "title": title,
            "url": url,
            "source": source,
            "score": score,
            "comments": comments,
            "article_text": article_text,
        })

    stories.sort(key=lambda s: s["score"], reverse=True)
    output = stories[:n_output]
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return output


if __name__ == "__main__":
    collect()
