#!/bin/bash
# ============================================
# Güvenli Hermes Paketi — Tek Komutla Kurulum
# KamuYZ APA Çalışma Grubu — Ağustos 2026
# ============================================
set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}   Güvenli Hermes Paketi Kurulumu${NC}"
echo -e "${BLUE}   KamuYZ APA Çalışma Grubu${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ---------- Adım 1: Gereksinim Kontrolü ----------
echo -e "${YELLOW}[1/6] Gereksinimler kontrol ediliyor...${NC}"

command -v docker >/dev/null 2>&1 || { echo -e "${RED}Docker bulunamadı. Lütfen Docker'ı kurun: https://docs.docker.com/get-docker/${NC}"; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo -e "${RED}Python 3 bulunamadı. Lütfen Python 3.10+ kurun.${NC}"; exit 1; }
command -v git >/dev/null 2>&1 || { echo -e "${RED}Git bulunamadı. Lütfen Git'i kurun.${NC}"; exit 1; }

echo -e "${GREEN}  ✓ Docker: $(docker --version)${NC}"
echo -e "${GREEN}  ✓ Python: $(python3 --version)${NC}"
echo -e "${GREEN}  ✓ Git: $(git --version)${NC}"

# ---------- Adım 2: Hermes Agent Klonlama ----------
echo -e "${YELLOW}[2/6] Hermes Agent indiriliyor...${NC}"

HERMES_DIR="$HOME/.hermes-paket"
mkdir -p "$HERMES_DIR"

if [ -d "$HERMES_DIR/hermes-agent" ]; then
    echo -e "${GREEN}  ✓ Hermes Agent zaten mevcut, güncelleniyor...${NC}"
    cd "$HERMES_DIR/hermes-agent" && git pull
else
    git clone https://github.com/nousresearch/hermes-agent.git "$HERMES_DIR/hermes-agent"
fi

# ---------- Adım 3: Güvenli Yapılandırma ----------
echo -e "${YELLOW}[3/6] Güvenli yapılandırma uygulanıyor...${NC}"

CONFIG_DIR="$HERMES_DIR/config"
mkdir -p "$CONFIG_DIR"

# Güvenli config.toml oluştur
cat > "$CONFIG_DIR/config.toml" << 'CONFEOF'
# Güvenli Hermes Yapılandırması — KamuYZ APA

[gateway]
host = "127.0.0.1"       # Dışarıya kapalı, sadece loopback
port = 18789
allowed_origins = ["http://127.0.0.1:18789", "http://localhost:18789"]

[memory]
enabled = true            # Öğrenme döngüsü AÇIK
skill_generation = true   # Kendi skill'ini yazabilsin
session_archive = true    # Geçmiş oturumları hatırla
memory_max_chars = 2200   # MEMORY.md karakter limiti
user_max_chars = 1375     # USER.md karakter limiti

[security]
sandbox = true            # Korumalı alan AÇIK
sandbox_mode = "isolated" # Tam izolasyon
require_approval = true   # Kritik komutlarda onay sor
approval_timeout = 300    # 5 dakika içinde onaylanmazsa iptal
max_tool_calls = 20       # Görev başı maks araç çağrısı
token_budget = 100000     # Görev başı maks token

[provider]
model = "claude-sonnet-4-20250514"
fallback_model = "gpt-4o"

[channels]
telegram_enabled = false  # Kurulum sonrası manuel açın
telegram_dm_policy = "pairing"  # Sadece onaylanan kullanıcılar
telegram_require_mention = true # Gruplarda etiketlenmeden okumaz

[logging]
level = "info"
audit_log = true          # Tüm komutlar kayıt altında
log_file = "/var/log/hermes/hermes.log"
CONFEOF

echo -e "${GREEN}  ✓ config.toml oluşturuldu (127.0.0.1, sandbox=on, pairing=on)${NC}"

# ---------- Adım 4: Docker Compose ----------
echo -e "${YELLOW}[4/6] Docker Compose dosyası hazırlanıyor...${NC}"

cat > "$HERMES_DIR/docker-compose.yml" << 'DCEOF'
version: '3.8'

services:
  hermes-agent:
    image: nousresearch/hermes-agent:latest
    container_name: hermes_secure
    restart: unless-stopped

    user: "1000:1000"     # Root değil, güvenli kullanıcı

    ports:
      - "127.0.0.1:18789:18789"  # Sadece loopback

    environment:
      - HERMES_CONFIG=/home/hermes/config/config.toml
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}

    volumes:
      - ./config:/home/hermes/config:ro      # Salt okunur config
      - ./workspace:/home/hermes/workspace   # Çalışma alanı
      - ./data/memory:/home/hermes/.hermes/memory  # Hafıza kalıcı
      - ./data/skills:/home/hermes/.hermes/skills  # Skill'ler kalıcı
      - ./logs:/var/log/hermes               # Log'lar

    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    read_only: false

    networks:
      - hermes_net

    deploy:
      resources:
        limits:
          memory: 4G
          cpus: '2.0'

networks:
  hermes_net:
    driver: bridge
    internal: true  # Dış ağa kapalı
DCEOF

echo -e "${GREEN}  ✓ docker-compose.yml oluşturuldu (non-root, no-new-privileges, internal network)${NC}"

# ---------- Adım 5: .env Dosyası ----------
echo -e "${YELLOW}[5/6] Ortam değişkenleri...${NC}"

if [ ! -f "$HERMES_DIR/.env" ]; then
    cat > "$HERMES_DIR/.env" << 'ENVEOF'
# API Anahtarları — EN AZ YETKİYLE tanımlayın
ANTHROPIC_API_KEY=buraya_kendi_anahtarinizi_yazin
OPENROUTER_API_KEY=buraya_kendi_anahtarinizi_yazin

# Telegram (opsiyonel, güvenli pakette varsayılan kapalı)
TELEGRAM_BOT_TOKEN=
ENVEOF
    echo -e "${YELLOW}  ⚠ .env dosyası oluşturuldu. Lütfen API anahtarlarınızı girin:${NC}"
    echo -e "${YELLOW}     nano $HERMES_DIR/.env${NC}"
else
    echo -e "${GREEN}  ✓ .env zaten mevcut${NC}"
fi

# ---------- Adım 6: Başlatma ----------
echo -e "${YELLOW}[6/6] Hermes başlatılıyor...${NC}"

cd "$HERMES_DIR"
mkdir -p workspace data/memory data/skills logs

docker compose up -d 2>/dev/null || echo -e "${YELLOW}  ⚠ Docker Compose başlatılamadı. API anahtarlarını .env dosyasına girdikten sonra:${NC}"
echo -e "${YELLOW}     cd $HERMES_DIR && docker compose up -d${NC}"

# ---------- Tamamlandı ----------
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}  Kurulum tamamlandı! ✓${NC}"
echo ""
echo -e "  Hermes dizini: ${BLUE}$HERMES_DIR${NC}"
echo -e "  Yapılandırma:  ${BLUE}$HERMES_DIR/config/config.toml${NC}"
echo -e ""
echo -e "  Başlatmak için:"
echo -e "    ${BLUE}cd $HERMES_DIR${NC}"
echo -e "    ${BLUE}nano .env  # API anahtarlarını gir${NC}"
echo -e "    ${BLUE}docker compose up -d${NC}"
echo -e ""
echo -e "  Durum kontrolü:"
echo -e "    ${BLUE}docker compose ps${NC}"
echo -e "    ${BLUE}docker compose logs -f${NC}"
echo -e ""
echo -e "  ${GREEN}Güvenlik varsayılanları:${NC}"
echo -e "    ✓ Sadece loopback'te çalışır (127.0.0.1)"
echo -e "    ✓ Non-root kullanıcı"
echo -e "    ✓ Sandbox izolasyonu açık"
echo -e "    ✓ Kritik komutlarda onay sorar"
echo -e "    ✓ Dış ağa kapalı (internal network)"
echo -e "    ✓ Config salt okunur"
echo -e "    ✓ Audit log aktif"
echo -e ""
echo -e "  Telegram bağlamak için:"
echo -e "    ${BLUE}docs/TELEGRAM.md${NC}"
echo -e "${BLUE}========================================${NC}"
