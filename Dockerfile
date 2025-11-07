# --- 1. Build Angular ---
FROM node:24.11.0 AS frontend-build
WORKDIR /app/frontend

# Copy package files and install dependencies
COPY frontend/package*.json ./
RUN npm install

# Copy all source files and build for production
COPY frontend/ ./
RUN rm -rf dist || true
RUN npm run build --prod

# --- 2. Build FastAPI ---
FROM python:3.13-slim AS backend-build

# Install curl & uv
RUN apt-get update && \
    apt-get install -y curl && \
    curl -LSf https://astral.sh/uv/install.sh | sh && \
    rm -rf /var/lib/apt/lists/*

# Add uv binary to PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy dependency files and install backend dependencies
COPY backend/pyproject.toml backend/uv.lock ./
RUN uv sync --locked

# Copy backend source code
COPY backend/ ./backend

# Copy built frontend assets into backend/static
RUN rm -rf ./backend/static || true
COPY --from=frontend-build /app/frontend/dist/frontend ./backend/static

WORKDIR /app/backend

# Expose the FastAPI port
EXPOSE 8000

# Start FastAPI using uvicorn
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]