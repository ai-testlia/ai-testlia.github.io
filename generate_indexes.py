import os

base_dir = r"C:\Users\balpo\HappyBin\ai-testlia.github.io"
folders = {
    "Alson": {
        "title": "子睿 的學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "語文基礎與修辭": [
                {"file": "s3_rhetoric_fianl.html", "title": "修辭學總複習", "desc": "語文基礎強化"}
            ],
            "說話與寫作技巧": [
                {"file": "四格看圖說故事.html", "title": "四格看圖說故事", "desc": "看圖說話訓練"}
            ]
        }
    },
    "Anson": {
        "title": "楊逸 的DSE中文科學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "閱讀與範文": [
                {"file": "DSE 中文閱讀卷高分作戰藍圖.html", "title": "中文閱讀卷高分作戰藍圖", "desc": "DSE 閱讀策略"},
                {"file": "《逍遙遊》DSE應試極致筆記_潘SIR中文教室.html", "title": "《逍遙遊》應試極致筆記", "desc": "DSE 範文深造"},
                {"file": "中六閱讀：〈廢墟與記憶的辯證〉分析.html", "title": "〈廢墟與記憶的辯證〉分析", "desc": "中六課外閱讀"}
            ],
            "寫作進階技巧": [
                {"file": "抒情文進階：從「觸景生情」到「意象重構」.html", "title": "抒情文進階", "desc": "觸景生情與意象重構"},
                {"file": "記敘文進階：細節的溫度與情感的留白.html", "title": "記敘文進階", "desc": "細節溫度與情感留白"}
            ]
        }
    },
    "Himson": {
        "title": "Himson 的學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "記敘文寫作": [
                {"file": "《那次，我流下了悔恨的淚水》寫作教學筆記.html", "title": "《那次，我流下了悔恨的淚水》", "desc": "寫作教學筆記"}
            ],
            "實用文寫作": [
                {"file": "實用文_便條_書信.html", "title": "便條與書信", "desc": "實用文格式與應用"},
                {"file": "寫作教學筆記_勸導信（小五）_潘SIR中文教室.html", "title": "勸導信寫作", "desc": "小五實用文教學"}
            ]
        }
    },
    "Timothy": {
        "title": "Timothy 的學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "綜合與聆聽訓練": [
                {"file": "中文能力強化練習_卷三・專業對弈_潘SIR中文教室.html", "title": "卷三・專業對弈", "desc": "中文能力強化練習"}
            ],
            "語文適應與翻譯": [
                {"file": "文白適應訓練.html", "title": "文白適應訓練", "desc": "文言與白話轉換"}
            ]
        }
    },
    "ga_him": {
        "title": "家謙 的DSE中文科學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "DSE 考試策略": [
                {"file": "DSE 中文閱讀卷高分作戰藍圖.html", "title": "中文閱讀卷高分作戰藍圖", "desc": "DSE 閱讀策略"}
            ],
            "寫作進階技巧": [
                {"file": "抒情文進階：從「觸景生情」到「意象重構」.html", "title": "抒情文進階", "desc": "觸景生情與意象重構"},
                {"file": "記敘文進階：細節的溫度與情感的留白.html", "title": "記敘文進階", "desc": "細節溫度與情感留白"}
            ]
        }
    },
    "ho_dyun": {
        "title": "可端 的學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "語文基礎與成語": [
                {"file": "句意辨析攻略（小六TSA強化篇）_潘SIR中文教室.html", "title": "句意辨析攻略", "desc": "小六TSA強化篇"},
                {"file": "小五成語專題工作紙_成語運用_潘SIR中文教室.html", "title": "成語專題工作紙", "desc": "成語運用"},
                {"file": "小五成語專題練習_掌握語義與應用（五年級）_潘SIR中文教室.html", "title": "成語專題練習", "desc": "掌握語義與應用"},
                {"file": "成語填充練習（小五）_潘SIR中文教室.html", "title": "成語填充練習", "desc": "小五程度"},
                {"file": "成語教學與填充練習（小五）_潘SIR中文教室.html", "title": "成語教學與填充", "desc": "小五程度"}
            ],
            "說話與寫作技巧": [
                {"file": "四格看圖說故事.html", "title": "四格看圖說故事", "desc": "看圖說話訓練"}
            ]
        }
    },
    "hok_wai": {
        "title": "學維 的DSE中文科學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "中文科應試與寫作": [
                {"file": "DSE 中文閱讀卷高分作戰藍圖.html", "title": "中文閱讀卷高分作戰藍圖", "desc": "DSE 閱讀策略"},
                {"file": "抒情文進階：從「觸景生情」到「意象重構」.html", "title": "抒情文進階", "desc": "觸景生情與意象重構"},
                {"file": "記敘文進階：細節的溫度與情感的留白.html", "title": "記敘文進階", "desc": "細節溫度與情感留白"}
            ],
            "中國歷史": [
                {"file": "晚明政局_清朝統一與清初盛衰.html", "title": "晚明政局與清初盛衰", "desc": "中史研讀筆記"}
            ]
        }
    },
    "zeon_lok": {
        "title": "浚樂 的DSE中文科學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "DSE 考試策略": [
                {"file": "DSE 中文閱讀卷高分作戰藍圖.html", "title": "中文閱讀卷高分作戰藍圖", "desc": "DSE 閱讀策略"}
            ],
            "寫作技巧": [
                {"file": "《那次，我流下了悔恨的淚水》寫作教學筆記.html", "title": "《那次，我流下了悔恨的淚水》", "desc": "寫作教學筆記"},
                {"file": "抒情文進階：從「觸景生情」到「意象重構」.html", "title": "抒情文進階", "desc": "觸景生情與意象重構"},
                {"file": "記敘文進階：細節的溫度與情感的留白.html", "title": "記敘文進階", "desc": "細節溫度與情感留白"}
            ],
            "語文基礎與修辭": [
                {"file": "比喻手法教學筆記_潘SIR中文教室.html", "title": "比喻手法教學筆記", "desc": "修辭手法應用"}
            ]
        }
    },
    "zeng_han": {
        "title": "政行 的DSE中文科學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "DSE 考試策略": [
                {"file": "DSE 中文閱讀卷高分作戰藍圖.html", "title": "中文閱讀卷高分作戰藍圖", "desc": "DSE 閱讀策略"}
            ],
            "寫作進階技巧": [
                {"file": "抒情文進階：從「觸景生情」到「意象重構」.html", "title": "抒情文進階", "desc": "觸景生情與意象重構"},
                {"file": "記敘文進階：細節的溫度與情感的留白.html", "title": "記敘文進階", "desc": "細節溫度與情感留白"}
            ],
            "語文基礎與修辭": [
                {"file": "筆記_常用修辭手法.html", "title": "常用修辭手法", "desc": "小五深進篇"}
            ]
        }
    },
    "DSE_HTML_Notes": {
        "title": "中六・文憑試十二篇範文深造系列",
        "tag": "文言教學筆記目錄",
        "categories": {
            "十二篇範文精讀": [
                {"file": "DSE_出師表_精讀筆記.html", "title": "《出師表》", "desc": "諸葛亮"},
                {"file": "DSE_六國論_精讀筆記.html", "title": "《六國論》", "desc": "蘇洵"},
                {"file": "DSE_勸學_精讀筆記.html", "title": "《勸學》", "desc": "荀子"},
                {"file": "DSE_唐詩三首_精讀筆記.html", "title": "《唐詩三首》", "desc": "王維、李白、杜甫"},
                {"file": "DSE_始得西山宴遊記_精讀筆記.html", "title": "《始得西山宴遊記》", "desc": "柳宗元"},
                {"file": "DSE_宋詞三首_精讀筆記.html", "title": "《宋詞三首》", "desc": "蘇軾、李清照、辛棄疾"},
                {"file": "DSE_岳陽樓記_精讀筆記.html", "title": "《岳陽樓記》", "desc": "范仲淹"},
                {"file": "DSE_師說_精讀筆記.html", "title": "《師說》", "desc": "韓愈"},
                {"file": "DSE_廉頗藺相如列傳_精讀筆記.html", "title": "《廉頗藺相如列傳》", "desc": "司馬遷"},
                {"file": "DSE_論仁論孝論君子_精讀筆記.html", "title": "論仁、論孝、論君子", "desc": "《論語》"},
                {"file": "DSE_逍遙遊_精讀筆記.html", "title": "《逍遙遊》", "desc": "莊子"},
                {"file": "DSE_魚我所欲也_精讀筆記.html", "title": "《魚我所欲也》", "desc": "孟子"}
            ]
        }
    }
}

html_template = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}｜學習筆記目錄</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --color-text-primary: #1a1a1a;
    --color-text-secondary: #444444;
    --color-background-primary: #ffffff;
    --color-background-secondary: #f6f6f4;
    --color-border-tertiary: rgba(0,0,0,0.15);
    --border-radius-md: 8px;
    --border-radius-lg: 12px;
  }}

  @media (prefers-color-scheme: dark) {{
    :root {{
      --color-text-primary: #f5f5f5;
      --color-text-secondary: #cccccc;
      --color-background-primary: #121212;
      --color-background-secondary: #1e1e1c;
      --color-border-tertiary: rgba(255,255,255,0.2);
    }}
  }}

  body {{
    font-family: 'Noto Sans TC', sans-serif;
    color: var(--color-text-primary);
    background: var(--color-background-secondary);
    line-height: 1.8;
    font-size: 14px;
    margin: 0;
    padding: 20px;
  }}

  .wrap {{
    max-width: 850px;
    margin: 0 auto;
    background: var(--color-background-primary);
    padding: 45px;
    border-radius: var(--border-radius-lg);
    box-shadow: 0 4px 24px rgba(0,0,0,0.06);
  }}

  .hero {{
    padding: 3rem 2rem 2.5rem;
    text-align: center;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    border-radius: var(--border-radius-lg);
  }}
  .hero-tag {{
    display: inline-block;
    font-size: 11px;
    letter-spacing: 0.12em;
    padding: 0.25rem 0.9rem;
    border-radius: 20px;
    margin-bottom: 1rem;
    font-family: 'Noto Sans TC', sans-serif;
  }}
  .hero h1 {{
    font-family: 'Noto Serif TC', serif;
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    margin-bottom: 0.7rem;
    color: inherit;
    line-height: 1.4;
  }}
  .hero p {{ font-size: 13px; margin: 0; }}

  .hero.classical {{ background: #D5D8C5; color: #1A2015; }}
  .hero.classical .hero-tag {{
    border: 1px solid rgba(26,32,21,0.3);
    color: rgba(26,32,21,0.65);
  }}
  .hero.classical p {{ color: rgba(26,32,21,0.5); }}

  .section-header {{
    display: flex;
    align-items: center;
    margin: 3.5rem 0 1.5rem;
    padding-bottom: 0.6rem;
    border-bottom: 2px solid var(--color-border-tertiary);
  }}
  .section-icon {{
    font-size: 1.6rem;
    margin-right: 0.8rem;
  }}
  .section-header h2 {{
    font-family: 'Noto Serif TC', serif;
    font-size: 1.6rem;
    margin: 0;
    color: var(--color-text-primary);
  }}

  .nav-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin: 1.5rem 0;
  }}

  @media (max-width: 600px) {{
    .nav-grid {{
      grid-template-columns: 1fr;
    }}
  }}

  .nav-card {{
    background: var(--color-background-secondary);
    border: 1px solid var(--color-border-tertiary);
    border-radius: var(--border-radius-md);
    padding: 1.8rem;
    text-decoration: none;
    color: var(--color-text-primary);
    transition: all 0.2s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }}

  .nav-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border-color: #6b705c;
  }}

  .nav-card h3 {{
    margin: 0 0 0.5rem 0;
    font-family: 'Noto Serif TC', serif;
    font-size: 1.2rem;
    color: var(--color-text-primary);
  }}

  .nav-card .dot {{
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: #6b705c;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-bottom: 1rem;
    font-size: 14px;
  }}

  .nav-card p {{
    margin: 0;
    color: var(--color-text-secondary);
    font-size: 0.95rem;
  }}
</style>
</head>
<body>

<div class="wrap">
  
  <div class="hero classical">
    <div class="hero-tag">{tag}</div>
    <h1>{title}</h1>
    <p>潘SIR中文教室編撰</p>
  </div>

{content}

  <footer style="margin-top:3rem; padding:1.2rem 1.5rem; background:var(--color-background-primary); border:0.5px solid var(--color-border-tertiary); border-radius:var(--border-radius-lg); text-align:center;">
    <div style="font-size:12px; color:var(--color-text-secondary); line-height:1.9;">
      <span style="font-weight:500; color:var(--color-text-primary);">©2026 潘SIR中文教室</span><br>
      版權歸潘SIR中文教室所有，未經允許，嚴禁以任何形式進行複製、印刷、轉載、轉售、營利或分享。<br>如需使用，請事先取得潘SIR中文教室的書面同意。
    </div>
  </footer>

</div>

</body>
</html>"""

icons = ["📚", "🧭", "🔥", "⚡", "⚖️"]

for folder_name, data in folders.items():
    content_html = ""
    has_dse = False
    if folder_name == "zeng_han":
        has_dse = True
    for category, items in data["categories"].items():
        if "DSE" in category:
            has_dse = True
        for item in items:
            if "DSE" in item.get("file", "") or "DSE" in item.get("title", "") or "DSE" in item.get("desc", ""):
                has_dse = True

    icon_idx = 0
    for category, items in data["categories"].items():
        icon = icons[icon_idx % len(icons)]
        icon_idx += 1
        content_html += f'''  <div class="section-header">
    <div class="section-icon">{icon}</div>
    <h2>{category}</h2>
  </div>
  <div class="nav-grid">
'''
        for idx, item in enumerate(items):
            content_html += f'''    <a href="{item["file"]}" class="nav-card">
      <div class="dot">{idx + 1}</div>
      <h3>{item["title"]}</h3>
      <p>{item["desc"]}</p>
    </a>
'''
        content_html += '  </div>\n'

    if folder_name != "DSE_HTML_Notes" and has_dse:
        dse_banner = """  <div class="nav-grid" style="grid-template-columns: 1fr; margin-bottom: 1.5rem;">
    <a href="../DSE_HTML_Notes/index.html" class="nav-card" style="margin-bottom: 0;">
      <div class="dot">🔥</div>
      <h3>DSE 12篇範文精讀筆記</h3>
      <p>中六・文憑試十二篇範文深造系列目錄</p>
    </a>
  </div>
"""
        content_html = dse_banner + content_html
    
    final_html = html_template.format(title=data["title"], tag=data["tag"], content=content_html)
    
    out_path = os.path.join(base_dir, folder_name, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Generated {out_path}")
