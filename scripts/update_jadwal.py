#!/usr/bin/env python3
"""
Script untuk fetch jadwal bola dari Goal.com
Jalankan via GitHub Actions setiap hari jam 2 pagi (09:00 WIB)
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

GOAL_URL = (
    "https://www.goal.com/id/berita/"
    "jadwal-tv-siaran-langsung-sepakbola-hari-ini/"
    "1qomojcjyge9n1nr2voxutdc1n"
)

FREE_TV = {
    "rcti", "mnctv", "gtv", "sctv", "indosiar", "antv", "tvone",
    "kompas tv", "inews", "tvri", "trans tv", "trans7", "metro tv",
}

PAID_KW = {
    "vidio", "bein", "vision+", "vision plus", "mola", "spotv",
    "apple tv", "disney", "netflix", "prime video", "hbo", "espn", "dazn",
}

BULAN = {
    "januari": 1, "februari": 2, "maret": 3, "april": 4, "mei": 5, "juni": 6,
    "juli": 7, "agustus": 8, "september": 9, "oktober": 10, "november": 11, "desember": 12,
}

def fetch_html():
    req = Request(
        GOAL_URL,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        },
    )
    with urlopen(req) as res:
        return res.read().decode("utf-8")

def parse_indo_date(text):
    m = re.search(r"(\d{1,2})\s+(\w+)\s+(\d{4})", text, re.I)
    if not m:
        return None
    day, month_str, year = m.groups()
    month = BULAN.get(month_str.lower())
    if not month:
        return None
    return f"{year}-{int(month):02d}-{int(day):02d}"

def parse_matchup(text):
    for sep in (" vs ", " VS ", " v "):
        if sep in text:
            parts = text.split(sep, 1)
            return parts[0].strip(), parts[1].strip()
    return text.strip(), ""

def classify_tv(stations):
    if not stations or stations == "-" or stations == "TBC":
        return [], []
    parts = [p.strip() for p in stations.split("/") if p.strip()]
    free, paid = [], []
    for part in parts:
        lower = part.lower()
        if any(k in lower for k in PAID_KW):
            paid.append(part)
        elif any(t in lower for t in FREE_TV):
            free.append(part)
        elif "sport" in lower or any(c.isdigit() for c in lower):
            paid.append(part)
        else:
            free.append(part)
    return free, paid

def parse_schedules(html):
    soup = BeautifulSoup(html, "html.parser")
    schedules = {}
    current_date = None

    content = soup.find("div", class_="article-body") or soup
    
    for el in content.find_all(["h3", "table"]):
        if el.name == "h3":
            parsed_date = parse_indo_date(el.get_text())
            current_date = parsed_date
        elif el.name == "table" and current_date:
            for tr in el.find_all("tr"):
                cells = [td.get_text(strip=True) for td in tr.find_all("td")]
                if len(cells) < 4 or re.search(r"kick-off", cells[0], re.I):
                    continue
                
                home, away = parse_matchup(cells[1])
                tv_free, tv_paid = classify_tv(cells[3])
                
                schedules.setdefault(current_date, []).append({
                    "kickoff": cells[0],
                    "matchup": f"{home} vs {away}",
                    "home": home,
                    "away": away,
                    "competition": cells[2],
                    "tv": cells[3],
                    "tvFree": tv_free,
                    "tvPaid": tv_paid,
                })
    
    return schedules

def main():
    root = Path(__file__).resolve().parent.parent
    out_jadwal = root / "data" / "jadwal.json"
    out_jadwal.parent.mkdir(parents=True, exist_ok=True)

    print("→ Mengambil data dari Goal.com...")
    try:
        html = fetch_html()
        schedules = parse_schedules(html)
        
        total = sum(len(v) for v in schedules.values())
        if not total:
            print("⚠️ Tidak ada jadwal ditemukan hari ini.")
            return 1

        payload = {
            "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source": GOAL_URL,
            "schedules": schedules,
        }
        
        out_jadwal.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"✓ Berhasil menyimpan {total} pertandingan ke data/jadwal.json")
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
