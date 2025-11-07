<div align="center">

# TxtToSrt - 文字轉 SRT 字幕轉換器

[![展示頁面](./screenshots/desktop-interface.png)](https://txttosrt.onrender.com/static/)

 [**English**](./README.md) | [**繁體中文**](./README_zh-TW.md)

一個現代化的網頁應用程式，將純文字檔案轉換為 SRT (SubRip) 字幕格式。前端使用 Angular，後端使用 Python FastAPI 建置。

</div>

## ✨ 功能特色

- **智慧計時**：根據字數以及標點符號自動計算每行字幕的持續時間
- **簡易轉換**：將純文字轉換為 SRT 字幕格式
- **檔案上傳支援**：直接上傳 .txt 檔案或貼上文字內容
- **即時處理**：轉換過程有進度指示
- **響應式設計**：在桌面和手機上都能完美運行
- **現代化 UI**：乾淨的卡片式介面搭配漸層背景
- **Docker 支援**：使用多階段建置的容器化部署以優化映像大小
- **CI/CD 自動化**：使用 GitHub Actions 的自動化建置與部署流程

## 📋 目錄

- [🖼️ 螢幕截圖](#%EF%B8%8F-%E8%9E%A2%E5%B9%95%E6%88%AA%E5%9C%96)
- [🛠️ 技術棧](#%EF%B8%8F-%E6%8A%80%E8%A1%93%E6%A3%A7)
- [🚀 快速開始](#-%E5%BF%AB%E9%80%9F%E9%96%8B%E5%A7%8B)
- [🚀 部署與 Demo](#-%E9%83%A8%E7%BD%B2%E8%88%87-demo)
- [🔄 CI/CD](#-cicd)
- [📖 使用說明](#-%E4%BD%BF%E7%94%A8%E8%AA%AA%E6%98%8E)
- [📁 專案結構](#-%E5%B0%88%E6%A1%88%E7%B5%90%E6%A7%8B)
- [🤝 貢獻](#-%E8%B2%A2%E7%8D%BB)
- [📄 授權](#-%E6%8E%88%E6%AC%8A)
- [🙋‍♂️ 支援](#%E2%80%8D%EF%B8%8F-%E6%94%AF%E6%8F%B4)

## 🖼️ 螢幕截圖

### 轉換過程
![轉換演示](./screenshots/conversion-demo.png)

### 下載結果
![下載結果](./screenshots/download-result.png)

### 手機版介面
![手機介面](./screenshots/mobile-interface.png)

## 🛠️ 技術棧

### 前端
- **Angular 20** - 現代化網頁框架
- **Bootstrap 5** - 響應式 CSS 框架
- **TypeScript** - 型別安全的 JavaScript
- **SCSS** - 增強的 CSS 預處理器

### 後端
- **Python 3.13+** - 程式語言
- **FastAPI** - 現代化 Python 網頁框架
- **Uvicorn** - ASGI 伺服器
- **uv** - 快速 Python 套件管理器
- **Docker** - 容器化部署

## 🚀 快速開始

### 環境需求

- Node.js 24.11.0+ 和 npm 11.6.1+
- Python 3.13+
- uv (Python 套件管理器)
- Git

### 安裝步驟

1. **複製專案**
   ```bash
   git clone https://github.com/your-username/TxtToSrt.git
   cd TxtToSrt
   ```

2. **設定後端**
   ```bash
   cd backend
   uv sync
   ```

3. **設定前端**
   ```bash
   cd ../frontend
   npm install
   ```

### 運行應用程式

1. **啟動後端伺服器**
   ```bash
   cd backend
   uv run unicorn main:app
   ```
   後端將運行在 `http://localhost:8000`

2. **啟動前端伺服器**
   ```bash
   cd frontend
   npm start
   ```
   前端將運行在 `http://localhost:4200`

3. **開啟瀏覽器**並前往 `http://localhost:4200`

## 🚀 部署與 Demo

此應用程式已容器化並部署到 Render。

- **Docker Image**: 存放在 GitHub Container Registry (ghcr.io)
- **部署平台**: Render
- **Demo 網址**: [https://txttosrt.onrender.com/static/](https://txttosrt.onrender.com/static/)

**注意**: Render 在沒有使用 15 分鐘後會自動休眠，初次訪問可能需要等待應用程式啟動。

## 🔄 CI/CD

此專案使用 GitHub Actions 進行持續整合與部署 (CI/CD)，實現自動化建置與部署流程。

### 自動化流程

當您推送程式碼到 `main` 分支時，系統會自動執行以下步驟：

1. **觸發條件**：推送至 `main` 分支
2. **建置環境**：Ubuntu Latest
3. **權限設定**：讀取程式碼與寫入套件權限

### 建置步驟

1. **程式碼簽出**：使用 `actions/checkout@v4` 簽出最新程式碼
2. **登入容器註冊表**：使用 `docker/login-action@v3` 登入 GitHub Container Registry (ghcr.io)
3. **建置與推送映像**：使用 `docker/build-push-action@v6` 建置 Docker 映像並推送至 `ghcr.io/kokorohoshi/txt-to-srt:latest`
4. **觸發部署**：透過 HTTP POST 請求呼叫 Render 部署鉤子，自動重新部署應用程式

### 相關檔案

- **工作流程檔案**：`.github/workflows/docker-image.yml`
- **Docker 映像**：`ghcr.io/kokorohoshi/txt-to-srt:latest`
- **部署平台**：Render (https://txttosrt.onrender.com)

### 設定需求

為了使 CI/CD 正常運作，您需要設定以下 GitHub Secrets：

- `RENDER_DEPLOY_HOOK`：Render 提供的部署鉤子 URL，用於觸發重新部署

      (註) GITHUB_TOKEN 會自動提供，用於容器註冊表認證，不用設定

## 📖 使用說明

1. **文字輸入**：將文字內容直接貼上到文字框中
2. **檔案上傳**：點擊「Choose File」上傳 .txt 檔案
3. **開始轉換**：點擊「開始轉換」按鈕
4. **下載檔案**：轉換完成後，點擊「下載 SRT 檔案」下載字幕檔案

## 📁 專案結構

```
TxtToSrt/
├── backend/                 # Python FastAPI 後端
│   ├── main.py             # 主 API 伺服器
│   ├── utils.py            # 工具函數
│   ├── pyproject.toml      # Python 依賴
│   └── README.md           # 後端說明文件
├── frontend/                # Angular 前端
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   │   └── txt-to-srt/  # 主元件
│   │   │   └── app.ts
│   │   └── styles.scss
│   ├── angular.json        # Angular 設定
│   └── package.json        # Node 依賴
├── .gitignore              # Git 忽略規則
└── README.md               # 此檔案
```

## 🤝 貢獻

歡迎貢獻！請隨時提交 Pull Request。

1. Fork 此專案
2. 建立您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 📄 授權

此專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案。

## 🙋‍♂️ 支援

如果您有任何問題或需要幫助，請在 GitHub 上開啟 issue。

[(回到頂部)](#txttosrt---%E6%96%87%E5%AD%97%E8%BD%89-srt-%E5%AD%97%E5%B9%95%E8%BD%89%E6%8F%9B%E5%99%A8)
