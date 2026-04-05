#!/bin/bash

# ============================================================
# Cursor Otonom Geliştirme Ajanı — Otomatik Kurulum Scripti
# ============================================================

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo -e "${BLUE}╔════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   Cursor Otonom Geliştirme Ajanı Kurulum  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════╝${NC}"
echo ""

# Kurulum türünü sor
echo -e "${YELLOW}Kurulum türünü seçin:${NC}"
echo "  1) Global  — Tüm projelerinizde çalışır (~/.cursor/)"
echo "  2) Yerel   — Yalnızca belirttiğiniz projede çalışır"
echo ""
read -p "Seçiminiz (1/2): " choice

case $choice in
  1)
    # Global kurulum
    CURSOR_COMMANDS_DIR="$HOME/.cursor/commands"
    CURSOR_RULES_DIR="$HOME/.cursor/rules"
    
    echo ""
    echo -e "${YELLOW}→ Global kurulum başlatılıyor...${NC}"
    
    mkdir -p "$CURSOR_COMMANDS_DIR"
    mkdir -p "$CURSOR_RULES_DIR"
    
    cp .cursor/commands/*.md "$CURSOR_COMMANDS_DIR/"
    cp .cursor/rules/*.md "$CURSOR_RULES_DIR/"
    
    echo -e "${GREEN}✅ Global kurulum tamamlandı!${NC}"
    echo -e "   Komutlar: ${BLUE}$CURSOR_COMMANDS_DIR${NC}"
    echo -e "   Kurallar: ${BLUE}$CURSOR_RULES_DIR${NC}"
    ;;
    
  2)
    # Proje bazlı kurulum
    echo ""
    read -p "Proje klasör yolunu girin: " project_path
    
    if [ ! -d "$project_path" ]; then
      echo -e "${RED}❌ Hata: Klasör bulunamadı: $project_path${NC}"
      exit 1
    fi
    
    echo ""
    echo -e "${YELLOW}→ Proje bazlı kurulum başlatılıyor...${NC}"
    
    mkdir -p "$project_path/.cursor/commands"
    mkdir -p "$project_path/.cursor/rules"
    
    cp .cursor/commands/*.md "$project_path/.cursor/commands/"
    cp .cursor/rules/*.md "$project_path/.cursor/rules/"
    
    echo -e "${GREEN}✅ Proje kurulumu tamamlandı!${NC}"
    echo -e "   Komutlar: ${BLUE}$project_path/.cursor/commands/${NC}"
    ;;
    
  *)
    echo -e "${RED}❌ Geçersiz seçim. Çıkılıyor.${NC}"
    exit 1
    ;;
esac

echo ""
echo -e "${BLUE}┌────────────────────────────────────────────┐${NC}"
echo -e "${BLUE}│            Kullanılabilir Komutlar          │${NC}"
echo -e "${BLUE}├────────────────────────────────────────────┤${NC}"
echo -e "${BLUE}│${NC}  /proje_incele  → Döküman analizi          ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_basla   → Tam otomatik geliştirme  ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_durum   → İlerleme raporu          ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_calistir → Geliştirme sunucusu     ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_docker  → Docker / Compose kurulumu ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_test    → Test & uyum kontrolü     ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_bitir   → Proje sonlandırma        ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_sifirla → Temizle & sıfırla        ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_eksik_tara → Eksik ve öneri tara   ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_devam   → Eksiklerden devam et      ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_tasarim → Tasarım profili uygula    ${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_kalite_kapisi → Kurumsal kalite kapısı${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /proje_guvenlik_tara → Güvenlik/uyum tarama${BLUE}│${NC}"
echo -e "${BLUE}│${NC}  /git_agent_update → Gitten komut güncelle   ${BLUE}│${NC}"
echo -e "${BLUE}└────────────────────────────────────────────┘${NC}"
echo ""
echo -e "${GREEN}🚀 Cursor IDE'yi açın, Ctrl+L ile chat'i başlatın ve / yazın!${NC}"
echo ""
