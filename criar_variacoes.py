#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para criar 3 variações da landing page otimizadas para diferentes palavras-chave
"""

import os

# Ler o arquivo original
with open('index.html', 'r', encoding='utf-8') as f:
    conteudo_original = f.read()

# Definir as variações com suas palavras-chave e otimizações
variacoes = [
    {
        'nome_arquivo': 'cobranca-empresarial-especializada.html',
        'keyword': 'cobrança empresarial especializada',
        'title': 'Cobrança Empresarial Especializada | AMCC - Recupere até 85% dos Créditos',
        'meta_description': 'Cobrança empresarial especializada para empresas que faturam +1M/mês. Equipe especializada, tecnologia avançada e jurídico integrado. Zero custo antecipado.',
        'h1': 'Cobrança Empresarial <span class="highlight">Especializada</span> para Grandes Negócios',
        'hero_subtitle': '<strong>Cobrança empresarial especializada</strong> com 30+ anos de experiência. O Grupo AMCC oferece solução completa com tecnologia avançada, jurídico integrado e <strong>zero custo antecipado</strong>.',
        'section_title': 'Por Que Escolher Nossa <span class="highlight">Cobrança Empresarial Especializada</span>?'
    },
    {
        'nome_arquivo': 'cobranca-empresarial-personalizada.html',
        'keyword': 'cobrança empresarial personalizada',
        'title': 'Cobrança Empresarial Personalizada | AMCC - Soluções Sob Medida',
        'meta_description': 'Cobrança empresarial personalizada para cada tipo de negócio. Estratégias customizadas, atendimento humanizado e 85% de taxa de sucesso. Análise gratuita.',
        'h1': 'Cobrança Empresarial <span class="highlight">Personalizada</span> para Seu Negócio',
        'hero_subtitle': '<strong>Cobrança empresarial personalizada</strong> que respeita sua marca e clientes. O Grupo AMCC desenvolve estratégias sob medida com abordagem humanizada e <strong>zero custo antecipado</strong>.',
        'section_title': 'Vantagens da Nossa <span class="highlight">Cobrança Empresarial Personalizada</span>'
    },
    {
        'nome_arquivo': 'empresas-cobranca-terceirizada.html',
        'keyword': 'empresas de cobrança terceirizada',
        'title': 'Empresas de Cobrança Terceirizada | AMCC - Líder há 30+ Anos',
        'meta_description': 'Entre as melhores empresas de cobrança terceirizada do Brasil. R$ 2Bi+ recuperados, 85% de sucesso. Solução completa para grandes carteiras.',
        'h1': 'Líder Entre as <span class="highlight">Empresas de Cobrança Terceirizada</span>',
        'hero_subtitle': 'Destaque entre as <strong>empresas de cobrança terceirizada</strong> do Brasil. O Grupo AMCC une 30+ anos de experiência, tecnologia avançada e jurídico integrado com <strong>zero custo antecipado</strong>.',
        'section_title': 'O Que Nos Diferencia das Demais <span class="highlight">Empresas de Cobrança Terceirizada</span>?'
    }
]

# Criar cada variação
for variacao in variacoes:
    print(f"\n🔧 Criando variação: {variacao['nome_arquivo']}")
    
    # Fazer uma cópia do conteúdo original
    novo_conteudo = conteudo_original
    
    # 1. Substituir o TITLE
    novo_conteudo = novo_conteudo.replace(
        '<title>AMCC - Empresas +1M | Recupere 5-10% do Faturamento Perdido</title>',
        f'<title>{variacao["title"]}</title>'
    )
    
    # 2. Substituir a META DESCRIPTION
    novo_conteudo = novo_conteudo.replace(
        '<meta name="description" content="Sua empresa fatura acima de 1 milhão por mês? 5-10% vira prejuízo por inadimplência. Recupere grandes carteiras com abordagem humanizada e zero custo antecipado.">',
        f'<meta name="description" content="{variacao["meta_description"]}">'
    )
    
    # 3. Substituir o H1
    novo_conteudo = novo_conteudo.replace(
        '''<h1 class="hero-title fade-in">
                            Sua empresa perde até
                            <span class="highlight">R$ 100 mil/mês</span>
                            em inadimplência
                        </h1>''',
        f'''<h1 class="hero-title fade-in">
                            {variacao["h1"]}
                        </h1>'''
    )
    
    # 4. Substituir o Hero Subtitle
    novo_conteudo = novo_conteudo.replace(
        '''<p class="hero-subtitle fade-in">
                            <strong>5% a 10% do seu faturamento vira prejuízo</strong> silenciosamente. 
                            O Grupo AMCC recupera grandes carteiras com tecnologia avançada, 
                            jurídico integrado e <strong>zero custo antecipado</strong>.
                        </p>''',
        f'''<p class="hero-subtitle fade-in">
                            {variacao["hero_subtitle"]}
                        </p>'''
    )
    
    # 5. Substituir o Section Title (primeira seção de problema)
    novo_conteudo = novo_conteudo.replace(
        '''<h2 class="section-title fade-in">
                        A <span class="highlight">Taxa Silenciosa</span> que Drena seu Lucro
                    </h2>''',
        f'''<h2 class="section-title fade-in">
                        {variacao["section_title"]}
                    </h2>'''
    )
    
    # 6. Adicionar keywords no conteúdo (adicionar após o hero-subtitle)
    # Adicionar menção da keyword no primeiro parágrafo da seção problema
    novo_conteudo = novo_conteudo.replace(
        '''<p class="section-subtitle fade-in">
                        Empresas que faturam acima de 1 milhão por mês carregam um custo invisível: 
                        a inadimplência que pode chegar a <strong>10% do faturamento</strong>.
                    </p>''',
        f'''<p class="section-subtitle fade-in">
                        Com {variacao["keyword"]}, empresas que faturam acima de 1 milhão por mês 
                        recuperam o custo invisível da inadimplência que pode chegar a <strong>10% do faturamento</strong>.
                    </p>'''
    )
    
    # Salvar o novo arquivo
    with open(variacao['nome_arquivo'], 'w', encoding='utf-8') as f:
        f.write(novo_conteudo)
    
    print(f"✅ Arquivo criado: {variacao['nome_arquivo']}")
    print(f"   - Title: {variacao['title']}")
    print(f"   - Keyword: {variacao['keyword']}")

print("\n" + "="*70)
print("✅ TODAS AS 3 VARIAÇÕES FORAM CRIADAS COM SUCESSO!")
print("="*70)
print("\nArquivos criados:")
for variacao in variacoes:
    print(f"  • {variacao['nome_arquivo']}")
print("\n📌 Cada arquivo está otimizado para sua palavra-chave específica")
print("📌 Title, meta description, H1 e conteúdo foram adaptados")
print("📌 As variações mantêm toda a estrutura e funcionalidade da página original")
