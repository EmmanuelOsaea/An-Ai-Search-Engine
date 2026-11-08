# Multi-stage build to keep production images tiny
FROM python:3.11-slim AS backend-builder
WORKDIR /app
COPY gateway/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY gateway/ ./gateway/

FROM nginx:alpine AS production-runtime
# Copy frontend assets to Nginx default serving directory
COPY client/ /usr/share/nginx/html/
# Copy python backend from builder step
COPY --from=backend-builder /app /app

EXPOSE 80 8000
CMD ["sh", "-c", "nginx -g 'daemon off;' & cd /app/gateway && python -m uvicorn main:app --host 0.0.0.0 --port 8000"]
