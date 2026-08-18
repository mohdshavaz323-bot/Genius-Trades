# Production Dockerfile for Genius Traders AI SaaS
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package definition
COPY package*.json ./

# Install production dependencies
RUN npm ci --only=production || npm install --production

# Copy application source code
COPY . .

# Expose server port
EXPOSE 8080

# Environment Defaults
ENV PORT=8080
ENV NODE_ENV=production

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/api/health || exit 1

# Start production server
CMD ["node", "server.js"]
