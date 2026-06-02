# 潘SIR中文教室 ｜ 學生個人學習筆記門戶網站

本專案是 **潘SIR中文教室** 的學生個人學習筆記門戶與託管系統，基於 GitHub Pages 進行靜態網頁託管與分發。

網站網址：[https://ai-testlia.github.io](https://ai-testlia.github.io)

---

## 📂 專案目錄結構

每個學生的專屬資料夾中均包含各自的學習網頁（如修辭手法、寫作技巧等）及一個自動生成的 `index.html` 門戶目錄頁面。

```text
ai-testlia.github.io/
├── Alson/               # 學生個人學習筆記目錄 (Alson)
├── Anson/               # 學生個人學習筆記目錄 (Anson)
├── Himson/              # 學生個人學習筆記目錄 (Himson)
├── Timothy/             # 學生個人學習筆記目錄 (Timothy)
├── ga_him/              # 學生個人學習筆記目錄 (ga_him)
├── ho_dyun/             # 學生個人學習筆記目錄 (ho_dyun)
├── hok_wai/             # 學生個人學習筆記目錄 (hok_wai)
├── zeon_lok/            # 學生個人學習筆記目錄 (zeon_lok)
├── zeng_han/            # 學生個人學習筆記目錄 (zeng_han)
├── DSE_HTML_Notes/      # 中六・文憑試十二篇範文精讀系列目錄與筆記
│   ├── DSE_出師表_精讀筆記.html
│   ├── ...
│   └── index.html
├── generate_indexes.py  # 門戶目錄自動生成與更新腳本（Python）
└── README.md            # 本說明文件
```

---

## 👥 學生目錄與狀態一覽

以下為目前系統已註冊的學生與其對應的門戶配置：

| 資料夾名稱 | 門戶標題說明 | DSE 標記狀態 | 備註 / 目錄分類 |
| :--- | :--- | :---: | :--- |
| `Alson` | 個人學習筆記 | ❌ | 語文基礎與修辭、說話與寫作技巧 |
| `Anson` | DSE中文科學習筆記 | ✅ | 閱讀與範文、寫作進階技巧 |
| `Himson` | 個人學習筆記 | ❌ | 記敘文寫作、實用文寫作 |
| `Timothy` | 個人學習筆記 | ❌ | 綜合與聆聽訓練、語文適應與翻譯 |
| `ga_him` | DSE中文科學習筆記 | ✅ | DSE 考試策略、寫作進階技巧 |
| `ho_dyun` | 個人學習筆記 | ❌ | 語文基礎與成語、說話與寫作技巧 |
| `hok_wai` | DSE中文科學習筆記 | ✅ | 中文科應試與寫作、中國歷史 |
| `zeon_lok` | DSE中文科學習筆記 | ✅ | DSE 考試策略、寫作技巧、語文基礎與修辭 |
| `zeng_han` | DSE中文科學習筆記 | ✅ | DSE 考試策略、寫作進階技巧、語文基礎與修辭 |

*註：**DSE 標記狀態** 為 `✅` 的學生，其門戶最上方會自動顯示 **🔥 DSE 12篇範文精讀筆記** 的專屬連結區塊。*

---

## 🛠️ 自動化維護與更新指南

本專案使用 Python 腳本 `generate_indexes.py` 來維護所有目錄頁面，避免人工修改 HTML 造成的樣式不一致。

### 1. 新增學生 或 為學生新增筆記檔

若要為某個學生加入新的 HTML 筆記，或新增一位學生，請直接編輯 [generate_indexes.py](file:///c:/Users/ai-testlia.github.io/generate_indexes.py) 中的 `folders` 字典設定：

* **新增學生**：仿照其他學生，在 `folders` 中新增一個鍵值（如 `"new_student"`），填入 `title`、`tag` 以及 `categories` 分類。
* **新增筆記檔案**：在該學生的 `categories` 對應分類列表中，新增一個字典項，例如：

  ```python
  {"file": "新筆記檔名.html", "title": "顯示在目錄的標題", "desc": "簡短描述說明"}
  ```

### 2. 生成與套用更新

在編輯完 `generate_indexes.py` 之後，請於本機執行該腳本。腳本會自動抓取最新的配置，並重新為所有學生輸出排版美觀、格式統一的 `index.html` 門戶頁面：

```bash
python generate_indexes.py
```

### 3. 提交並發佈至 GitHub

完成生成且本機測試無誤後，請將變更提交並推送至 GitHub：

```bash
git add -A
git commit -m "更新學生目錄配置與網頁"
git push origin main
```

---

## 🎨 設計規範與視覺風格

* **經典灰綠風格 (Classical Sage Green)**：
  學生門戶首頁採用極具質感的墨綠、灰綠色調（Hero 區背景色為 `#D5D8C5`，文字與細節使用深綠色 `#1A2015` 與 `#6b705c`）。
* **卡片式佈局 (Grid Layout)**：
  筆記列表均以響應式卡片網路（Grid Card）呈現，並在深色模式下支援自動色彩切換。
* **DSE 特色區塊**：
  任何分類或筆記標題中包含「DSE」字眼的學生，頁面最上方均會自動注入獨立寬度的「🔥 DSE 12篇範文精讀筆記」快速入口卡片。
