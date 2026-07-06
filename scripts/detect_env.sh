#!/usr/bin/env bash
# detect_env.sh — report which visual-capture tools are available.
# Output: one line per tool, "yes"/"no", plus a suggested capture tier.

check() { command -v "$1" >/dev/null 2>&1 && echo "yes" || echo "no"; }

PY=$(check python3)
GIT=$(check git)
NODE=$(check node)
DOCKER=$(check docker)
SHOTSCRAPER=$(check shot-scraper)
VHS=$(check vhs)
ASCIINEMA=$(check asciinema)
AGG=$(check agg)
FFMPEG=$(check ffmpeg)
MMDC=$(check mmdc)
PLAYWRIGHT="no"
if [ "$PY" = "yes" ]; then
  python3 -c "import playwright" 2>/dev/null && PLAYWRIGHT="yes"
fi

echo "python3:      $PY"
echo "git:          $GIT"
echo "node:         $NODE"
echo "docker:       $DOCKER"
echo "playwright:   $PLAYWRIGHT"
echo "shot-scraper: $SHOTSCRAPER"
echo "vhs:          $VHS"
echo "asciinema:    $ASCIINEMA"
echo "agg:          $AGG"
echo "ffmpeg:       $FFMPEG"
echo "mermaid-cli:  $MMDC"
echo "---"

if [ "$SHOTSCRAPER" = "yes" ] || [ "$PLAYWRIGHT" = "yes" ]; then
  echo "web-capture:  REAL SCREENSHOTS available"
else
  echo "web-capture:  fallback (install: pip install shot-scraper && shot-scraper install)"
fi
if [ "$VHS" = "yes" ]; then
  echo "cli-capture:  VHS GIF recording available"
elif [ "$ASCIINEMA" = "yes" ] && [ "$AGG" = "yes" ]; then
  echo "cli-capture:  asciinema+agg GIF available"
else
  echo "cli-capture:  static code blocks only (install: https://github.com/charmbracelet/vhs)"
fi
echo "diagrams:     Mermaid always available (GitHub renders natively)"
