import os
import sys
from datetime import datetime

base_dir = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\balpo\HappyBin\ai-testlia.github.io"
data_version = datetime.now().strftime('%Y%m%d%H%M%S')
folders = {
    "Alson": {
        "title": "子睿 的學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "閱讀理解特訓": [
                {"file": "閱讀理解全攻略.html", "title": "閱讀理解全攻略", "desc": "《森林裏的哭聲》篇章剖析"},
                {"file": "閱讀理解必殺技閱讀六步尋寶法.html", "title": "閱讀理解必殺技", "desc": "閱讀六步尋寶法"}
            ],
            "語文基礎與修辭": [
                {"file": "s3_rhetoric_fianl.html", "title": "修辭學總複習", "desc": "語文基礎強化"},
                {"file": "Zirui_Chinese_Basics_Final.html", "title": "語文基礎 Final 練習", "desc": "綜合語文基礎練習"}
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
                {"file": "《逍遙遊》DSE應試極致筆記_潘SIR中文教室.html", "title": "《逍遙遊》應試極致筆記", "desc": "DSE 範文精讀"},
                {"file": "中六閱讀：〈廢墟與記憶的辯證〉分析.html", "title": "〈廢墟與記憶的辯證〉分析", "desc": "DSE 課外閱讀"}
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
            "特定題目寫作指導": [
                {"file": "《那次，我流下了悔恨的淚水》寫作教學筆記.html", "title": "《那次，我流下了悔恨的淚水》", "desc": "特定題目寫作指導"},
                {"file": "寫作教學筆記_我終於明白了他的用心.html", "title": "《我終於明白了他的用心》", "desc": "特定題目寫作指導"},
                {"file": "寫作教學筆記_生命生命.html", "title": "《生命，生命》", "desc": "特定題目寫作指導"},
                {"file": "寫作教學筆記_勸導信（小五）_潘SIR中文教室.html", "title": "勸導信寫作", "desc": "特定題目寫作指導"},
                {"file": "記敘文寫作教學_沒有互聯網的一天.html", "title": "《沒有互聯網的一天》", "desc": "特定題目寫作指導"},
                {"file": "抒情記敘文寫作_課室裏的空座位.html", "title": "《課室裏的空座位》", "desc": "抒情記敘文寫作指導"},
                {"file": "小六進階作文教學筆記_那夜窗外下著大雨.html", "title": "《那夜，窗外下著大雨》", "desc": "特定題目寫作指導"},
                {"file": "寫作教學筆記_原來我沒有想像中勇敢.html", "title": "《原來我沒有想像中勇敢》", "desc": "特定題目寫作指導"}
            ],
            "寫作與修辭手法教學": [
                {"file": "實用文_便條_書信.html", "title": "便條與書信", "desc": "實用文格式與應用"},
                {"file": "記敘文寫作筆記（小五）_潘SIR中文教室.html", "title": "記敘文寫作筆記", "desc": "小五結構與技巧"},
                {"file": "比喻手法教學筆記（小四）_潘SIR中文教室.html", "title": "比喻手法教學筆記", "desc": "小四修辭手法"},
                {"file": "筆記_比喻法.html", "title": "比喻法", "desc": "常用修辭手法"},
                {"file": "筆記_借喻與借代的分別.html", "title": "借喻與借代的分別", "desc": "修辭手法進階"},
                {"file": "筆記_襯托法.html", "title": "襯托法", "desc": "寫作手法與修辭"}
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
            "語文與寫作強化": [
                {"file": "中文能力強化練習_學校生活與社交.html", "title": "中文能力強化——學校生活與社交", "desc": "學校生活與社交"},
                {"file": "中文能力強化練習_日常生活.html", "title": "中文能力強化——日常生活", "desc": "日常生活"},
                {"file": "中文能力強化練習_深_生活與校園篇.html", "title": "語文能力強化——生活與校園篇（深進）", "desc": "生活與校園寫作（深進）"}
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
                {"file": "記敘文進階：細節的溫度與情感的留白.html", "title": "記敘文進階", "desc": "細節溫度與情感留白"},
                {"file": "寫作教學_褪色的舊車票.html", "title": "寫作教學：車票與陪伴", "desc": "車票與陪伴"}
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
                {"file": "四格看圖說故事.html", "title": "四格看圖說故事", "desc": "看圖說話訓練"},
                {"file": "圖片故事寫作七步成文法及全方位實戰_潘SIR中文教室.html", "title": "圖片故事寫作", "desc": "七步成文法及全方位實戰"}
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
    "sam_laam": {
        "title": "心嵐 的學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "經典課文與深造": [
                {"file": "課文教學筆記_愛蓮說.html", "title": "《愛蓮說》深層賞析", "desc": "實用文言精讀"},
                {"file": "課文教學筆記_桃花源記.html", "title": "《桃花源記》全面解析", "desc": "全面解析與深層研讀"},
                {"file": "課文教學筆記_楊柳.html", "title": "《楊柳》深層賞析", "desc": "散文賞析"},
                {"file": "課文教學筆記_為學一首示子姪.html", "title": "《為學一首示子姪》深度分析", "desc": "課文深度分析"},
                {"file": "課文教學筆記_說勤.html", "title": "《說「勤」》深度分析", "desc": "課文深度分析"},
                {"file": "課文教學筆記_風箏.html", "title": "《風箏》深度分析", "desc": "課文深度分析"},
                {"file": "課文教學筆記_黃山.html", "title": "《黃山》深度分析", "desc": "課文深度分析"}
            ],
            "寫作與修辭手法教學": [
                {"file": "比喻手法教學筆記_潘SIR中文教室.html", "title": "比喻手法教學筆記", "desc": "修辭手法應用"},
                {"file": "筆記_比喻法.html", "title": "比喻法", "desc": "常用修辭手法"},
                {"file": "筆記_借喻與借代的分別.html", "title": "借喻與借代的分別", "desc": "修辭手法進階"},
                {"file": "筆記_襯托法.html", "title": "襯托法", "desc": "寫作與修辭手法"}
            ]
        }
    },
    "DSE_HTML_Notes": {
        "title": "文憑試十二篇範文精讀系列",
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
    },
    "ka_hin": {
        "title": "嘉軒 的學習筆記",
        "tag": "學生個人專屬",
        "categories": {
            "學習筆記": []
        }
    },
}

html_template = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}｜學習筆記目錄</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --color-bg-main: #f8f6f2; /* 品牌輕透米白 */
    --color-bg-card: #ffffff;
    --color-text-primary: #2e2d2e; /* 深炭灰 */
    --color-text-secondary: #5a5a5a;
    --color-accent-teal: #0097b2; /* 品牌亮青 */
    --color-accent-teal-hover: #007a91;
    --color-brand-green: #007A87; /* 品牌主色：土耳其藍 */
    --color-brand-gold: #C5A059; /* 品牌副色：古典金 */
    --color-border: rgba(0, 122, 135, 0.1);
    --shadow-sm: 0 2px 6px rgba(0, 122, 135, 0.03);
    --shadow-md: 0 4px 15px rgba(0, 122, 135, 0.04);
    --shadow-lg: 0 10px 24px rgba(0, 122, 135, 0.06);
    --border-radius: 12px;
  }}

  @media (prefers-color-scheme: dark) {{
    :root {{
      --color-bg-main: #1a2225; /* 深色模式主背景 */
      --color-bg-card: #12181a; /* 深色模式卡片背景 */
      --color-text-primary: #f8f6f2;
      --color-text-secondary: #a3b8cc;
      --color-border: rgba(197, 160, 89, 0.2);
    }}
  }}

  body {{
    font-family: 'Inter', 'Noto Sans TC', sans-serif;
    background-color: var(--color-bg-main);
    color: var(--color-text-primary);
    margin: 0;
    padding: 20px;
    line-height: 1.6;
  }}

  .wrap {{
    max-width: 850px;
    margin: 0 auto;
    background: var(--color-bg-card);
    padding: 45px;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-lg);
    border: 1px solid var(--color-border);
  }}

  .hero {{
    background: linear-gradient(135deg, var(--color-brand-green), #004d55);
    color: #f8f6f2;
    padding: 3.5rem 2rem 3rem;
    text-align: center;
    border-bottom: 4px solid var(--color-brand-gold);
    position: relative;
    box-shadow: var(--shadow-md);
    border-radius: var(--border-radius);
    overflow: hidden;
    margin-bottom: 2rem;
  }}

  .hero-tag {{
    display: inline-block;
    font-size: 11px;
    letter-spacing: 0.15em;
    background: rgba(197, 160, 89, 0.15);
    color: var(--color-brand-gold);
    border: 1px solid rgba(197, 160, 89, 0.35);
    padding: 0.3rem 1.2rem;
    border-radius: 30px;
    margin-bottom: 1rem;
    font-weight: 600;
    text-transform: uppercase;
  }}

  .hero h1 {{
    font-family: 'Noto Serif TC', serif;
    font-size: 2.4rem;
    margin: 0 0 0.6rem;
    font-weight: 700;
    letter-spacing: 1px;
    line-height: 1.4;
  }}

  .hero p {{
    font-size: 0.95rem;
    opacity: 0.8;
    max-width: 700px;
    margin: 0 auto;
  }}

  .section-header {{
    display: flex;
    align-items: center;
    margin: 3.5rem 0 1.5rem;
    padding-bottom: 0.6rem;
    border-bottom: 2px solid var(--color-border);
  }}

  .section-icon {{
    font-size: 1.6rem;
    margin-right: 0.8rem;
  }}

  .section-header h2 {{
    font-family: 'Noto Serif TC', serif;
    font-size: 1.5rem;
    margin: 0;
    color: var(--color-brand-green);
  }}

  @media (prefers-color-scheme: dark) {{
    .section-header h2 {{
      color: var(--color-brand-gold);
    }}
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
    background-color: var(--color-bg-card);
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius);
    padding: 1.8rem;
    text-decoration: none;
    color: var(--color-text-primary);
    transition: all 0.2s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    border-left: 4px solid var(--color-brand-gold);
  }}

  .nav-card:hover {{
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
    border-color: var(--color-brand-gold);
  }}

  .nav-card h3 {{
    margin: 0 0 0.5rem 0;
    font-family: 'Noto Serif TC', serif;
    font-size: 1.2rem;
    color: var(--color-brand-green);
  }}

  @media (prefers-color-scheme: dark) {{
    .nav-card h3 {{
      color: var(--color-text-primary);
    }}
  }}

  .nav-card .dot {{
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: var(--color-brand-green);
    color: var(--color-brand-gold);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-bottom: 1rem;
    font-size: 14px;
    border: 1px solid var(--color-brand-gold);
  }}

  .nav-card p {{
    margin: 0;
    color: var(--color-text-secondary);
    font-size: 0.95rem;
  }}

  /* ===== 新版分類 index（五格＋最近加入） ===== */
  .recent-box {{
    margin: 2rem 0 0.5rem;
    padding: 1.4rem 1.6rem 1.6rem;
    background: linear-gradient(135deg, rgba(0,122,135,0.06), rgba(197,160,89,0.10));
    border: 1px solid var(--color-border);
    border-left: 4px solid var(--color-brand-gold);
    border-radius: var(--border-radius);
  }}
  .recent-box h2 {{
    font-family: 'Noto Serif TC', serif;
    font-size: 1.25rem;
    margin: 0 0 1rem;
    color: var(--color-brand-green);
  }}
  .recent-list {{ display: flex; flex-direction: column; gap: 0.6rem; }}
  .recent-item {{
    display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap;
    padding: 0.75rem 1rem;
    background: var(--color-bg-card);
    border: 1px solid var(--color-border);
    border-radius: 10px;
    text-decoration: none;
    color: var(--color-text-primary);
    transition: all 0.2s ease;
  }}
  .recent-item:hover {{ border-color: var(--color-brand-gold); transform: translateX(3px); }}
  .recent-item .r-title {{ flex: 1; min-width: 12rem; font-family: 'Noto Serif TC', serif; font-weight: 600; font-size: 1rem; }}
  .recent-item .r-meta {{ font-size: 12px; color: var(--color-text-secondary); white-space: nowrap; }}
  .section-count {{
    margin-left: auto; font-size: 12px; color: var(--color-text-secondary);
    border: 1px solid var(--color-border); border-radius: 20px; padding: 0.1rem 0.7rem;
  }}
  .note-card {{
    background-color: var(--color-bg-card);
    border: 1px solid var(--color-border);
    border-left: 4px solid var(--color-brand-gold);
    border-radius: var(--border-radius);
    padding: 1.2rem 1.3rem 1.1rem;
    text-decoration: none;
    color: var(--color-text-primary);
    transition: all 0.2s ease;
    display: flex; flex-direction: column; gap: 0.4rem;
  }}
  .note-card.is-ex {{ border-left-color: var(--color-brand-green); }}
  .note-card:hover {{ transform: translateY(-3px); box-shadow: var(--shadow-md); border-color: var(--color-brand-gold); }}
  .note-card h3 {{
    margin: 0; font-family: 'Noto Serif TC', serif; font-size: 1.1rem; line-height: 1.45;
    color: var(--color-brand-green);
  }}
  @media (prefers-color-scheme: dark) {{ .note-card h3, .recent-box h2 {{ color: var(--color-text-primary); }} }}
  .note-card p {{ margin: 0; color: var(--color-text-secondary); font-size: 0.9rem; line-height: 1.5; }}
  .note-badges {{ display: flex; align-items: center; gap: 0.4rem; }}
  .badge {{
    display: inline-block; font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
    padding: 0.1rem 0.6rem; border-radius: 20px; line-height: 1.6; white-space: nowrap;
  }}
  .badge-note {{ background: rgba(197,160,89,0.15); color: #8a6a2c; border: 1px solid rgba(197,160,89,0.45); }}
  .badge-ex {{ background: rgba(0,122,135,0.10); color: var(--color-brand-green); border: 1px solid rgba(0,122,135,0.35); }}
  .badge-new {{ background: #be3e54; color: #fff; border: 1px solid #be3e54; }}
  .note-date {{ margin-left: auto; font-size: 11.5px; color: var(--color-text-secondary); }}
</style>
</head>
<body>

<div class="wrap">
  
  <div class="hero">
    <div class="hero-tag">{tag}</div>
    <h1>{title}</h1>
    <p>潘SIR中文教室編撰</p>
  </div>

  <!-- 備忘區塊 (僅在有備忘數據時顯示) -->
  <div id="memoSection" style="display: none; margin-bottom: 2rem; padding: 22px 25px; background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--border-radius); box-shadow: var(--shadow-sm); border-left: 4px solid var(--color-brand-green);">
    <div style="font-family: 'Noto Serif TC', serif; font-size: 1.15rem; font-weight: 700; color: var(--color-brand-green); margin-bottom: 14px; display: flex; align-items: center; gap: 8px;">
      📋 本週功課 & 溫習目標
    </div>
    <div id="memoList" style="display: flex; flex-direction: column; gap: 10px;"></div>
  </div>

  <!-- 學術成長曲線區塊 (僅在有成績數據時顯示) -->
  <div id="chartSection" style="display: none; margin-bottom: 2.5rem; padding: 25px; background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--border-radius); box-shadow: var(--shadow-sm); border-left: 4px solid var(--color-brand-gold);">
    <div style="font-family: 'Noto Serif TC', serif; font-size: 1.25rem; font-weight: 700; color: var(--color-brand-green); margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">
      📈 個人學術成長曲線
    </div>
    <div style="position: relative; height: 260px; width: 100%;">
      <canvas id="growthChart"></canvas>
    </div>
    
    <!-- 成績明細表格 -->
    <div style="margin-top: 25px; overflow-x: auto;">
      <table style="width: 100%; border-collapse: collapse; font-size: 13.5px; text-align: left;">
        <thead>
          <tr style="border-bottom: 2px solid var(--color-border); color: var(--color-text-secondary); font-weight: 600;">
            <th style="padding: 10px 5px;">測驗日期</th>
            <th style="padding: 10px 5px;">測驗名稱</th>
            <th style="padding: 10px 5px; text-align: right;">得分 / 總分</th>
            <th style="padding: 10px 5px; text-align: right;">答對率</th>
            <th style="padding: 10px 5px; text-align: left; padding-left: 20px;">評語 / 備註</th>
          </tr>
        </thead>
        <tbody id="gradesTableBody">
          <!-- JS 動態插入 -->
        </tbody>
      </table>
    </div>
  </div>

  <!-- 引入 Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <!-- 引入學生專屬成績數據檔 -->
  <script src="data_grades.js?v={data_version}" onerror="console.log('未偵測到學生成績數據')"></script>
  <!-- 引入學生備忘數據檔 -->
  <script src="data_memo.js?v={data_version}" onerror="console.log('未偵測到備忘數據')"></script>

  <script>
    document.addEventListener("DOMContentLoaded", function() {{

      // 備忘區塊
      if (typeof studentMemo !== 'undefined' && Array.isArray(studentMemo) && studentMemo.length > 0) {{
        document.getElementById("memoSection").style.display = "block";
        const memoList = document.getElementById("memoList");
        const memoIcons = {{'功課': '📝', '溫習目標': '🎯', '其他': '📌'}};
        studentMemo.forEach(function(m) {{
          const div = document.createElement("div");
          div.style.cssText = "display:flex;align-items:flex-start;gap:12px;padding:12px 14px;background:var(--color-bg-main);border-radius:8px;border:1px solid var(--color-border);";
          const icon = memoIcons[m.type] || '📌';
          const dueHtml = m.due ? '<span style="font-size:11px;color:var(--color-text-secondary);margin-top:4px;display:block;">截止：' + m.due + '</span>' : '';
          div.innerHTML = '<span style="font-size:1.1rem;flex-shrink:0;">' + icon + '</span>'
            + '<div><span style="font-size:11px;font-weight:600;color:var(--color-brand-green);text-transform:uppercase;letter-spacing:0.05em;">' + m.type + '</span>'
            + '<p style="margin:3px 0 0;font-size:14px;color:var(--color-text-primary);line-height:1.5;">' + m.content + '</p>'
            + dueHtml + '</div>';
          memoList.appendChild(div);
        }});
      }}

      // 檢查是否有學生成績數據
      if (typeof studentGrades !== 'undefined' && Array.isArray(studentGrades) && studentGrades.length > 0) {{
        document.getElementById("chartSection").style.display = "block";
        
        // 1. 填充成績表格
        const tbody = document.getElementById("gradesTableBody");
        tbody.innerHTML = "";
        
        const dates = [];
        const percentages = [];
        
        studentGrades.forEach(g => {{
          const pct = Math.round((g.score / g.max_score) * 100);
          dates.push(g.date);
          percentages.push(pct);
          
          const tr = document.createElement("tr");
          tr.style.borderBottom = "1px solid var(--color-border)";
          tr.style.color = "var(--color-text-primary)";
          tr.innerHTML = `
            <td style="padding: 12px 5px;">${{g.date}}</td>
            <td style="padding: 12px 5px; font-weight: 500; font-family: 'Noto Serif TC', serif;">${{g.test_name}}</td>
            <td style="padding: 12px 5px; text-align: right;">${{g.score}} / ${{g.max_score}}</td>
            <td style="padding: 12px 5px; text-align: right; font-weight: bold; color: ${{pct >= 60 ? 'var(--color-brand-green)' : '#be3e54'}}">${{pct}}%</td>
            <td style="padding: 12px 5px; padding-left: 20px; color: var(--color-text-secondary); font-size: 12.5px;">${{g.remarks || ''}}</td>
          `;
          tbody.appendChild(tr);
        }});
        
        // 2. 渲染 Chart.js 折線圖
        const ctx = document.getElementById('growthChart').getContext('2d');
        
        // 檢測是否為深色模式
        const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        const gridColor = isDark ? 'rgba(248, 246, 242, 0.1)' : 'rgba(0, 122, 135, 0.1)';
        const textColor = isDark ? '#f8f6f2' : '#2e2d2e';
        const brandGold = '#C5A059';
        const brandGreen = '#007A87';
        
        new Chart(ctx, {{
          type: 'line',
          data: {{
            labels: dates,
            datasets: [{{
              label: '答對率 (%)',
              data: percentages,
              borderColor: brandGold,
              backgroundColor: isDark ? 'rgba(197, 160, 89, 0.15)' : 'rgba(197, 160, 89, 0.08)',
              borderWidth: 3,
              pointBackgroundColor: brandGreen,
              pointBorderColor: brandGold,
              pointRadius: 6,
              pointHoverRadius: 8,
              fill: true,
              tension: 0.3
            }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{
              legend: {{
                display: false
              }},
              tooltip: {{
                callbacks: {{
                  label: function(context) {{
                    const idx = context.dataIndex;
                    const g = studentGrades[idx];
                    return ` ${{g.test_name}}: ${{g.score}}/${{g.max_score}} (${{context.raw}}%)`;
                  }}
                }}
              }}
            }},
            scales: {{
              x: {{
                grid: {{
                  color: gridColor
                }},
                ticks: {{
                  color: textColor,
                  font: {{
                    family: 'Inter'
                  }}
                }}
              }},
              y: {{
                min: 0,
                max: 100,
                grid: {{
                  color: gridColor
                }},
                ticks: {{
                  color: textColor,
                  callback: function(value) {{
                    return value + "%";
                  }}
                }}
              }}
            }}
          }}
        }});
      }}
    }});
  </script>

{content}

  <footer style="margin-top:4rem; padding:3rem 2rem; background:var(--color-brand-green); border-top:2.5px solid var(--color-brand-gold); border-radius:var(--border-radius); text-align:center; color:#f8f6f2;">
    <div style="font-size:12px; line-height:1.9;">
      <span style="font-weight:600; color:var(--color-brand-gold); font-size:13px;">©2026 潘SIR中文教室</span><br>
      <span style="opacity:0.8;">版權歸潘SIR中文教室所有，未經允許，嚴禁以任何形式進行複製、印刷、轉載、轉售、營利或分享。<br>如需使用，請事先取得潘SIR中文教室的書面同意。</span>
    </div>
  </footer>

</div>

</body>
</html>"""

icons = ["📚", "🧭", "🔥", "⚡", "⚖️"]

SKIP_FILES = {"index.html", "data_grades.js", "data_memo.js"}

# =====================================================================
# 新版分類 index（2026-11 試行）：五格（閱讀、文言、寫作、語文基礎、測驗溫習）
# ＋「筆記／練習」標籤＋最近加入＋「新」標記。只套用於 NEW_LAYOUT 入面嘅學生。
# 分類次序：筆記 <meta name="pansir-category"> → NOTE_OVERRIDES → hero-tag／標題關鍵字
# =====================================================================
import re
import subprocess
from datetime import date, timedelta

NEW_LAYOUT = {"Hei_yu", "Himson", "Yat_Hong"}

CATEGORY_ORDER = ["閱讀", "文言", "寫作", "語文基礎", "測驗溫習"]
CATEGORY_ICON = {"閱讀": "📖", "文言": "📜", "寫作": "✍️", "語文基礎": "🧩", "測驗溫習": "📝"}
NEW_DAYS = 14      # 幾多日內加入算「新」
RECENT_COUNT = 3   # 「最近加入」顯示幾多份

# 自動分錯先喺度改：檔名 → {"category": ..., "type": "筆記"/"練習"}（全部學生通用）
NOTE_OVERRIDES = {
    "S1_02_語基與評估教學筆記.html": {"category": "語文基礎", "type": "筆記"},
    "閱讀語基評估_筆記.html": {"category": "測驗溫習", "type": "練習"},
}

_CAT_RULES = [
    ("測驗溫習", r"測驗|首測|考試|模擬|試卷|評估|總複習|闖關|IGCSE"),
    ("文言", r"文言|範文|DSE_|一字多音|一詞多義|語譯|愛蓮說|桃花源|岳陽樓|廉頗|逍遙遊|出師表|師說|勸學|六國論|陳太丘"),
    ("寫作", r"寫作|作文|批改|評改|評分報告|記敘文|記敍文|抒情文|實用文|看圖|圖片故事|立意"),
    ("語文基礎", r"語文運用|語基|字詞|詞語|生詞|成語|句子|句意|修辭|比喻|借喻|借代|襯托|標點|語法|文白"),
    ("閱讀", r"閱讀|導讀|講讀|段義|課文"),
]
_RHETORIC = r"修辭|比喻|借喻|借代|襯托|擬人|誇張|排比|對偶"
# hero-tag 用嘅次序：寫作排喺文言前面（例如「文言/白話寫作教學筆記」應該入寫作）
_HERO_RULES = [r for r in _CAT_RULES[1:] if r[0] == "寫作"] + [r for r in _CAT_RULES[1:] if r[0] != "寫作"]
_EX_WORDS = r"練習|工作紙|模擬|試卷|評估|測驗|闖關|總複習|quiz"
_NOTE_WORDS = r"筆記|教學|導讀|講讀|攻略|精讀|補帖"


def _read_head(path):
    try:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            return fh.read(60000)
    except Exception:
        return ""


def _meta(html, name):
    m = re.search(r'<meta\s+name="%s"\s+content="([^"]*)"' % re.escape(name), html)
    return m.group(1).strip() if m else ""


def _note_title(html, filename):
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    t = m.group(1).strip() if m else clean_title(filename)
    t = re.sub(r"\s*[｜|—–-]\s*潘SIR中文教室\s*$", "", t).strip()
    return t or clean_title(filename)


def _hero_tag(html):
    m = re.search(r'class="hero-tag"[^>]*>([^<]*)<', html)
    return m.group(1).strip() if m else ""


_CN_NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}


def _series_no(text):
    m = re.search(r"(?:練習|第|卷|單元|\(|（)([一二三四五六七八九十]|\d+)", text)
    if not m:
        return 0
    v = m.group(1)
    return int(v) if v.isdigit() else _CN_NUM.get(v, 0)


_added_dates = None


def _git_added_dates():
    """一次過讀 git log，攞每個檔第一次加入 repo 嘅日期。冇 git 就回傳空 dict。"""
    global _added_dates
    if _added_dates is not None:
        return _added_dates
    _added_dates = {}
    try:
        out = subprocess.run(
            ["git", "-c", "core.quotepath=false", "log", "--no-renames", "--diff-filter=A",
             "--name-only", "--format=@@%as"],
            cwd=base_dir, capture_output=True, text=True, encoding="utf-8", timeout=60,
        ).stdout
        cur = None
        for line in out.splitlines():
            if line.startswith("@@"):
                cur = line[2:]
            elif line.strip() and cur:
                _added_dates[line.strip()] = cur   # log 由新到舊，最後寫入嘅係最早日期
    except Exception:
        pass
    return _added_dates


def _classify(filename, html, title):
    ov = NOTE_OVERRIDES.get(filename, {})
    cat = _meta(html, "pansir-category") or ov.get("category")
    typ = _meta(html, "pansir-type") or ov.get("type")
    hero = _hero_tag(html)
    if not typ:
        is_ex = re.search(_EX_WORDS, title) and not re.search(_NOTE_WORDS, title)
        typ = "練習" if is_ex else "筆記"
    if not cat and re.search(r"評估|模擬|測驗|試卷", hero) and "筆記" not in hero:
        cat, typ = "測驗溫習", (ov.get("type") or _meta(html, "pansir-type") or "練習")
    if not cat:
        if typ == "練習" and re.search(_CAT_RULES[0][1], title + hero):
            cat = "測驗溫習"
        elif re.search(_RHETORIC, title):
            cat = "語文基礎"
        else:
            for name, pat in _HERO_RULES:
                if re.search(pat, hero):
                    cat = name
                    break
            if not cat:
                for name, pat in _CAT_RULES:
                    if re.search(pat, title + " " + filename):
                        cat = name
                        break
    if cat not in CATEGORY_ORDER:
        cat = "閱讀"
    return cat, typ


def _fmt_date(d):
    try:
        y, m, dd = d.split("-")
        return f"{int(m)}月{int(dd)}日"
    except Exception:
        return ""


def _badges(n):
    b = ('<span class="badge badge-ex">練習</span>' if n["type"] == "練習"
         else '<span class="badge badge-note">筆記</span>')
    if n["is_new"]:
        b += '<span class="badge badge-new">新</span>'
    return b


def build_new_layout(folder_name, folder_path):
    dates = _git_added_dates()
    today = date.today()
    notes = []
    for f in os.listdir(folder_path):
        if not f.endswith(".html") or f in SKIP_FILES:
            continue
        full = os.path.join(folder_path, f)
        html = _read_head(full)
        title = _note_title(html, f)
        cat, typ = _classify(f, html, title)
        added = dates.get(f"{folder_name}/{f}")
        if not added:
            added = datetime.fromtimestamp(os.path.getmtime(full)).strftime("%Y-%m-%d")
        parts_ = re.split(r"\s*(?:：|｜|——|──|\s—\s)\s*", title, maxsplit=1)
        main, sub = (parts_ + [""])[:2]
        # 「寫作教學筆記｜《題目》」：題目做主標題，筆記類別做副標題
        if sub and re.search(r"(筆記|教學)$", main.strip()) and not re.search(r"(筆記|教學)$", sub.strip()):
            main, sub = sub, main
        is_new = False
        try:
            is_new = (today - date.fromisoformat(added)) <= timedelta(days=NEW_DAYS)
        except Exception:
            pass
        notes.append({"file": f, "title": main.strip(), "desc": sub.strip(), "category": cat,
                      "type": typ, "added": added, "is_new": is_new, "no": _series_no(f) or _series_no(title)})

    if not notes:
        return ""

    # 新嘅排頭；同一日加入就按編號（練習一、二、三）
    notes.sort(key=lambda n: (n["added"], -n["no"], n["title"]), reverse=True)

    parts = []
    if len(notes) > RECENT_COUNT:
        parts.append('  <div class="recent-box">\n    <h2>🆕 最近加入</h2>\n    <div class="recent-list">\n')
        for n in notes[:RECENT_COUNT]:
            parts.append(
                '      <a class="recent-item" href="%s">%s<span class="r-title">%s</span>'
                '<span class="r-meta">%s・%s</span></a>\n'
                % (n["file"], _badges(n), n["title"], n["category"], _fmt_date(n["added"])))
        parts.append('    </div>\n  </div>\n')

    for cat in CATEGORY_ORDER:
        items = [n for n in notes if n["category"] == cat]
        if not items:
            continue
        parts.append(
            '  <div class="section-header">\n'
            '    <div class="section-icon">%s</div>\n'
            '    <h2>%s</h2>\n'
            '    <span class="section-count">%d 份</span>\n'
            '  </div>\n  <div class="nav-grid">\n' % (CATEGORY_ICON[cat], cat, len(items)))
        for n in items:
            cls = "note-card is-ex" if n["type"] == "練習" else "note-card"
            desc = '\n      <p>%s</p>' % n["desc"] if n["desc"] else ""
            parts.append(
                '    <a href="%s" class="%s">\n'
                '      <div class="note-badges">%s<span class="note-date">%s</span></div>\n'
                '      <h3>%s</h3>%s\n    </a>\n'
                % (n["file"], cls, _badges(n), _fmt_date(n["added"]), n["title"], desc))
        parts.append('  </div>\n')
    return "".join(parts)


# Auto-register any student folder that isn't hardcoded above. This prevents
# students added via tutor_erp from being silently skipped (they'd otherwise
# get data_grades.js/data_memo.js written but no index.html at all).
db_path = os.path.join(os.path.dirname(base_dir), "tutor_erp", "classroom.db")


def _lookup_display_name(folder_name):
    try:
        import sqlite3
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT display_name FROM students WHERE name = ?", (folder_name,))
        row = cur.fetchone()
        conn.close()
        return row[0] if row else None
    except Exception:
        return None


for entry in sorted(os.listdir(base_dir)):
    entry_path = os.path.join(base_dir, entry)
    if entry in folders or not os.path.isdir(entry_path):
        continue
    has_data_files = any(
        os.path.exists(os.path.join(entry_path, f)) for f in ("data_grades.js", "data_memo.js")
    )
    if not has_data_files:
        continue
    display_name = _lookup_display_name(entry) or entry
    folders[entry] = {
        "title": f"{display_name} 的學習筆記",
        "tag": "學生個人專屬",
        "categories": {"學習筆記": []}
    }
    print(f"Auto-registered new student folder: {entry}")

def clean_title(filename):
    name = filename.replace(".html", "")
    for suffix in ["_潘SIR中文教室", "（潘SIR中文教室）"]:
        name = name.replace(suffix, "")
    return name.strip()

for folder_name, data in folders.items():
    content_html = ""
    has_dse = False
    if folder_name == "zeng_han":
        has_dse = True

    # Collect all files already listed in categories
    listed_files = set()
    for category, items in data["categories"].items():
        if "DSE" in category:
            has_dse = True
        for item in items:
            listed_files.add(item["file"])
            if "DSE" in item.get("file", "") or "DSE" in item.get("title", "") or "DSE" in item.get("desc", ""):
                has_dse = True

    # Auto-scan for unlisted .html files in the folder
    folder_path = os.path.join(base_dir, folder_name)
    if os.path.isdir(folder_path):
        scanned = [
            f for f in os.listdir(folder_path)
            if f.endswith(".html") and f not in SKIP_FILES and f not in listed_files
        ]
        if scanned:
            data["categories"]["學習筆記"] = [
                {"file": f, "title": clean_title(f), "desc": "學習筆記"} for f in sorted(scanned)
            ]

    icon_idx = 0
    if folder_name in NEW_LAYOUT and os.path.isdir(folder_path):
        content_html = build_new_layout(folder_name, folder_path)
        data["categories"] = {}
    for category, items in data["categories"].items():
        if not items:
            continue
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
        dse_banner = """  <div class="nav-grid" style="margin-bottom: 1.5rem;">
    <a href="../DSE_HTML_Notes/index.html" class="nav-card" style="margin-bottom: 0;">
      <div class="dot">🔥</div>
      <h3>DSE 12篇範文精讀筆記</h3>
      <p>文憑試十二篇範文精讀系列目錄（按此進入）</p>
    </a>
    <a href="../S6_HTML_Notes/index.html" class="nav-card" style="margin-bottom: 0;">
      <div class="dot">🧭</div>
      <h3>文言文教學庫</h3>
      <p>文言文基礎與模擬練習（按此進入）</p>
    </a>
  </div>
"""
        content_html = dse_banner + content_html
    
    final_html = html_template.format(title=data["title"], tag=data["tag"], content=content_html, data_version=data_version)
    
    out_path = os.path.join(base_dir, folder_name, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Generated {out_path}")
