#!/usr/bin/env python3
import re

files = [
    'cobranca-empresarial-especializada.html',
    'cobranca-empresarial-personalizada.html',
    'empresas-cobranca-terceirizada.html'
]

for filename in files:
    print(f"Processing {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update WhatsApp modal form
    content = re.sub(
        r'<p>Informe o nome da sua empresa</p>\s*</div>\s*<form id="whatsappForm">',
        r'''<p>Preencha seus dados para contato</p>
            </div>
            <form id="whatsappForm" name="whatsapp_contact_form">''',
        content
    )
    
    content = re.sub(
        r'<form id="whatsappForm">\s*<div class="whatsapp-form-group">\s*<label for="empresaNome">Nome da Empresa \*</label>\s*<input type="text" id="empresaNome" name="empresaNome"',
        r'''<form id="whatsappForm" name="whatsapp_contact_form">
                <div class="whatsapp-form-group">
                    <label for="whatsappNome">Seu Nome *</label>
                    <input type="text" id="whatsappNome" name="full_name" required placeholder="Digite seu nome completo">
                </div>
                <div class="whatsapp-form-group">
                    <label for="whatsappEmail">Seu E-mail *</label>
                    <input type="email" id="whatsappEmail" name="email" required placeholder="seu@email.com">
                </div>
                <div class="whatsapp-form-group">
                    <label for="empresaNome">Nome da Empresa *</label>
                    <input type="text" id="empresaNome" name="company_name"''',
        content
    )
    
    # 2. Update form submission handlers
    # Replace leadFormHero
    old_hero = r"document\.getElementById\('leadFormHero'\)\.addEventListener\('submit', function\(e\) \{\s*e\.preventDefault\(\);\s*const formData = \{[^}]+\};"
    new_hero = """document.getElementById('leadFormHero').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const form = e.target;
            const formData = new FormData(form);
            
            const dataToSend = {
                name: formData.get('full_name'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                empresa: formData.get('company_name'),
                plataforma: 'Campanha Empresas +1M - Hero',
                question: `Inadimplência: ${form.querySelector('[name="valor_inadimplencia"]').options[form.querySelector('[name="valor_inadimplencia"]').selectedIndex].text}`,
                source: 'AMCC - Empresas +1M | Recupere 5-10% do Faturamento Perdido',
                tags: ['AMCC', 'Empresas +1M', 'Alto Faturamento', 'Grandes Carteiras', 'Form Hero']
            };"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {filename} updated")

print("\nDone!")
