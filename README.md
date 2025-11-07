<div align="center">

# TxtToSrt - Text to SRT Subtitle Converter

[![Demo](./screenshots/desktop-interface.png)](https://txttosrt.onrender.com/static/)

 [**English**](./README.md) | [**繁體中文**](./README_zh-TW.md)

A modern web application that converts plain text files into SRT (SubRip) subtitle format. Built with Angular frontend and Python FastAPI backend.

</div>

## ✨ Features

- **Intelligent Timing**: Automatically calculates subtitle duration based on word count and punctuation marks
- **Simple Conversion**: Convert plain text to SRT subtitle format
- **File Upload Support**: Upload .txt files directly or paste text content
- **Real-time Processing**: Fast conversion with progress indication
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern UI**: Clean, card-based interface with gradient background

## 📋 Table of Contents

- [🖼️ Screenshots](#%EF%B8%8F-screenshots)
- [🛠️ Tech Stack](#%EF%B8%8F-tech-stack)
- [🚀 Quick Start](#-quick-start)
- [🚀 Deployment & Demo](#-deployment--demo)
- [🔄 CI/CD](#-cicd)
- [ Usage](#-usage)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙋‍♂️ Support](#%E2%80%8D%EF%B8%8F-support)

## 🖼️ Screenshots

### Conversion Process
![Conversion Demo](./screenshots/conversion-demo.png)

### Download Result
![Download Result](./screenshots/download-result.png)

### Mobile View
![Mobile Interface](./screenshots/mobile-interface.png)

## 🛠️ Tech Stack

### Frontend
- **Angular 20** - Modern web framework
- **Bootstrap 5** - Responsive CSS framework
- **TypeScript** - Type-safe JavaScript
- **SCSS** - Enhanced CSS preprocessing

### Backend
- **Python 3.13+** - Programming language
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **uv** - Fast Python package manager
- **Docker** - Containerized deployment

## 🚀 Quick Start

### Prerequisites

- Node.js 24.11.0+ and npm 11.6.1+
- Python 3.13+
- uv (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/TxtToSrt.git
   cd TxtToSrt
   ```

2. **Setup Backend**
   ```bash
   cd backend
   uv sync
   ```

3. **Setup Frontend**
   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

1. **Start Backend Server**
   ```bash
   cd backend
   uv run unicorn main:app
   ```
   Backend will run on `http://localhost:8000`

2. **Start Frontend Server**
   ```bash
   cd frontend
   npm start
   ```
   Frontend will run on `http://localhost:4200`

3. **Open your browser** and navigate to `http://localhost:4200`

## 🚀 Deployment & Demo

This application is containerized and deployed on Render.

- **Docker Image**: Hosted on GitHub Container Registry (ghcr.io)
- **Deployment Platform**: Render
- **Demo URL**: [https://txttosrt.onrender.com/static/](https://txttosrt.onrender.com/static/)

**Note**: Render automatically sleeps after 15 minutes of inactivity, so the first visit may take some time to wake up the application.

## 🔄 CI/CD

This project uses GitHub Actions for continuous integration and deployment (CI/CD), implementing automated build and deployment processes.

### Automated Workflow

When you push code to the `main` branch, the system automatically executes the following steps:

1. **Trigger Condition**: Push to `main` branch
2. **Build Environment**: Ubuntu Latest
3. **Permissions**: Read code and write packages permissions

### Build Steps

1. **Code Checkout**: Use `actions/checkout@v4` to check out the latest code
2. **Login to Container Registry**: Use `docker/login-action@v3` to log in to GitHub Container Registry (ghcr.io)
3. **Build and Push Image**: Use `docker/build-push-action@v6` to build Docker image and push to `ghcr.io/kokorohoshi/txt-to-srt:latest`
4. **Trigger Deployment**: Call Render deployment hook via HTTP POST request to automatically redeploy the application

### Related Files

- **Workflow File**: `.github/workflows/docker-image.yml`
- **Docker Image**: `ghcr.io/kokorohoshi/txt-to-srt:latest`
- **Deployment Platform**: Render (https://txttosrt.onrender.com)

### Configuration Requirements

To make CI/CD work properly, you need to set the following GitHub Secrets:

- `RENDER_DEPLOY_HOOK`: The deployment hook URL provided by Render, used to trigger redeployment

      (Note) GITHUB_TOKEN is automatically provided for container registry authentication, no need to set it

## 📖 Usage

1. **Text Input**: Paste your text content directly into the textarea
2. **File Upload**: Click "Choose File" to upload a .txt file
3. **Convert**: Click the "開始轉換" (Start Conversion) button
4. **Download**: Once conversion is complete, click "下載 SRT 檔案" to download your subtitle file

## 📁 Project Structure

```
TxtToSrt/
├── backend/                 # Python FastAPI backend
│   ├── main.py             # Main API server
│   ├── utils.py            # Utility functions
│   ├── pyproject.toml      # Python dependencies
│   └── README.md           # Backend documentation
├── frontend/                # Angular frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   │   └── txt-to-srt/  # Main component
│   │   │   └── app.ts
│   │   └── styles.scss
│   ├── angular.json        # Angular configuration
│   └── package.json        # Node dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you have any questions or need help, please open an issue on GitHub.

[(Back to top)](#txttosrt---text-to-srt-subtitle-converter)
