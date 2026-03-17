#!/usr/bin/env python3
"""
Gera versões Google Ads e Meta Ads das 4 Landing Pages.
- Ajusta caminhos de assets (../logo amcc/, ../videos/, etc.)
- Altera mensagem WhatsApp para referenciar a campanha correta
- Salva em /google/ e /meta/
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mapeamento dos 4 arquivos LP originais
LP_FILES = {
    "recupere-faturamento-perdido.html": "recupere-faturamento-perdido.html",
    "cobranca-empresarial-especializada.html": "cobranca-empresarial-especializada.html",
    "cobranca-empresarial-personalizada.html": "cobranca-empresarial-personalizada.html",
    "empresas-cobranca-terceirizada.html": "empresas-cobranca-terceirizada.html",
}

# Assets paths to fix (relative -> one level up)
ASSET_PREFIXES = [
    'favicon.png',
    'logo amcc/',
    'fotos-equipe/',
    'capas/',
    'videos/',
    'parceiros/',
]


def fix_asset_paths(html):
    """Adjust asset paths to go one level up (../)"""
    for prefix in ASSET_PREFIXES:
        # Handle src="prefix" and href="prefix" and url('prefix')
        # Avoid double-fixing already relative paths
        # src="logo amcc/..." -> src="../logo amcc/..."
        html = html.replace(f'src="{prefix}', f'src="../{prefix}')
        html = html.replace(f"src='{prefix}", f"src='../{prefix}")
        html = html.replace(f'href="{prefix}', f'href="../{prefix}')
        html = html.replace(f"href='{prefix}", f"href='../{prefix}")
        html = html.replace(f"url('{prefix}", f"url('../{prefix}")
        html = html.replace(f'url("{prefix}', f'url("../{prefix}')
        html = html.replace(f'url({prefix}', f'url(../{prefix}')
        # srcset
        html = html.replace(f'srcset="{prefix}', f'srcset="../{prefix}')
        html = html.replace(f"srcset='{prefix}", f"srcset='../{prefix}")
        # poster
        html = html.replace(f'poster="{prefix}', f'poster="../{prefix}')
    return html


def set_campaign_source(html, source):
    """
    Change the WhatsApp message campaign source.
    Original: 'vim pela campanha do Google Ads - Landing Page Empresas AMCC'
    """
    if source == "google":
        campaign_text = "Google Ads"
    else:
        campaign_text = "Meta Ads (Facebook/Instagram)"

    # Pattern 1: template literal with \n\n
    html = re.sub(
        r"vim pela campanha do [^.\\]+",
        f"vim pela campanha do {campaign_text} - Landing Page Empresas AMCC",
        html
    )
    return html


def set_webhook_plataforma(html, source):
    """Change the webhook plataforma field from 'organico' to google/meta"""
    html = html.replace("plataforma: 'organico'", f"plataforma: '{source}'")
    return html


def add_utm_comment(html, source):
    """Add a HTML comment identifying the campaign source"""
    marker = "<!-- End Meta Pixel Code -->"
    comment = f"\n    <!-- Campaign Source: {source.upper()} ADS -->"
    html = html.replace(marker, marker + comment, 1)
    return html


def fix_obrigado_link(html):
    """Fix any links to obrigado (sem .html) to go one level up"""
    html = html.replace('href="obrigado"', 'href="../obrigado"')
    html = html.replace("href='obrigado'", "href='../obrigado'")
    html = html.replace('action="obrigado"', 'action="../obrigado"')
    # Fix JavaScript redirect to obrigado
    html = html.replace("window.location.href = 'obrigado'", "window.location.href = '../obrigado'")
    html = html.replace('window.location.href = "../obrigado"', 'window.location.href = "../obrigado"')
    return html


def process_lp(source_file, output_dir, campaign_source):
    """Process a single LP file for a given campaign source"""
    source_path = os.path.join(BASE_DIR, source_file)
    
    if not os.path.exists(source_path):
        print(f"  ⚠️  Arquivo não encontrado: {source_file}")
        return False
    
    with open(source_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Apply transformations
    html = fix_asset_paths(html)
    html = set_campaign_source(html, campaign_source)
    html = set_webhook_plataforma(html, campaign_source)
    html = add_utm_comment(html, campaign_source)
    html = fix_obrigado_link(html)
    
    # Save to output directory
    output_path = os.path.join(output_dir, source_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✅ {campaign_source.upper()}/{source_file}")
    return True


def main():
    print("🚀 Gerando versões Google Ads e Meta Ads das Landing Pages...\n")
    
    google_dir = os.path.join(BASE_DIR, "google")
    meta_dir = os.path.join(BASE_DIR, "meta")
    
    os.makedirs(google_dir, exist_ok=True)
    os.makedirs(meta_dir, exist_ok=True)
    
    count = 0
    
    print("📁 GOOGLE ADS (/google/):")
    for lp_file in LP_FILES.values():
        if process_lp(lp_file, google_dir, "google"):
            count += 1
    
    print(f"\n📁 META ADS (/meta/):")
    for lp_file in LP_FILES.values():
        if process_lp(lp_file, meta_dir, "meta"):
            count += 1
    
    print(f"\n✨ Total: {count} páginas geradas com sucesso!")
    print(f"   📂 /google/ - {len(os.listdir(google_dir))} arquivos")
    print(f"   📂 /meta/   - {len(os.listdir(meta_dir))} arquivos")


if __name__ == "__main__":
    main()
