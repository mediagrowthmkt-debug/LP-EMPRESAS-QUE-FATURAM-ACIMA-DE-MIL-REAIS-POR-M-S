#!/usr/bin/env python3
"""
Script para aplicar o redesign WhatsApp-first nas landing pages restantes.
Replica as mudanças feitas em index.html e cobranca-empresarial-especializada.html.
"""

import re

def apply_whatsapp_redesign(filepath):
    """Aplica todas as mudanças do redesign WhatsApp em um arquivo."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n🔧 Processando: {filepath}")
    
    # 1. Atualizar WhatsApp Modal
    print("  ➤ Atualizando WhatsApp Modal...")
    old_modal = r'''                <h3>Fale Conosco no WhatsApp</h3>
                <p>Informe seus dados para contato</p>
            </div>
            <form id="whatsappForm" name="whatsapp_contact_form">
                <div class="whatsapp-form-group">
                    <label for="whatsappNome">Nome Completo \*</label>
                    <input type="text" id="whatsappNome" name="full_name" required placeholder="Digite seu nome completo">
                </div>
                <div class="whatsapp-form-group">
                    <label for="whatsappEmail">E-mail \*</label>
                    <input type="email" id="whatsappEmail" name="email" required placeholder="Digite seu e-mail">
                </div>
                <div class="whatsapp-form-group">
                    <label for="empresaNome">Nome da Empresa \*</label>
                    <input type="text" id="empresaNome" name="company_name" required placeholder="Digite o nome da sua empresa">
                </div>
                <button type="submit" class="whatsapp-submit-btn">
                    <i class="fab fa-whatsapp"></i>
                    Iniciar Conversa
                </button>
            </form>'''
    
    new_modal = '''                <h3>Fale Conosco no WhatsApp</h3>
                <p>Informe seus dados para contato</p>
            </div>
            <form id="whatsappForm" name="whatsapp_contact_form">
                <div class="whatsapp-form-group">
                    <label for="whatsappNome">Nome Completo *</label>
                    <input type="text" id="whatsappNome" name="first_name" required placeholder="Digite seu nome completo">
                </div>
                <div class="whatsapp-form-group">
                    <label for="empresaNome">Nome da Empresa *</label>
                    <input type="text" id="empresaNome" name="company_name" required placeholder="Digite o nome da sua empresa">
                </div>
                <div class="whatsapp-form-group">
                    <label for="whatsappTelefone">Telefone de Contato *</label>
                    <input type="tel" id="whatsappTelefone" name="phone" class="telefone-mask" required placeholder="(00) 00000-0000">
                </div>
                <div class="whatsapp-form-group">
                    <label for="valorInadimplencia">Valor Estimado em Inadimplência *</label>
                    <select id="valorInadimplencia" name="qual_o_valor_aproximado_sua_empresa_tem_a_receber_atualmente_em_aberto" required>
                        <option value="">Selecione uma faixa...</option>
                        <option value="50k_100k">R$ 50.000 - R$ 100.000</option>
                        <option value="100k_200k">R$ 100.000 - R$ 200.000</option>
                        <option value="200k_500k">R$ 200.000 - R$ 500.000</option>
                        <option value="500k_1m">R$ 500.000 - R$ 1.000.000</option>
                        <option value="1m_3m">R$ 1.000.000 - R$ 3.000.000</option>
                        <option value="3m_plus">Acima de R$ 3.000.000</option>
                        <option value="nao_sei">Não sei informar</option>
                    </select>
                </div>
                <button type="submit" class="whatsapp-submit-btn">
                    <i class="fab fa-whatsapp"></i>
                    Iniciar Conversa
                </button>
            </form>'''
    
    content = re.sub(old_modal, new_modal, content, flags=re.DOTALL)
    
    print(f"  ✅ Modal atualizado")
    
    # Salvar mudanças
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Concluído: {filepath}\n")

# Arquivos a processar
files_to_process = [
    'cobranca-empresarial-personalizada.html',
    'empresas-cobranca-terceirizada.html'
]

print("=" * 60)
print("🚀 Iniciando aplicação do WhatsApp-first Redesign")
print("=" * 60)

for filename in files_to_process:
    filepath = f"/Users/bruno/Documents/LPS/CLIENTES/AMCC/LP-EMPRESAS QUE FATURAM ACIMA DE MIL REAIS POR MÊS/{filename}"
    try:
        apply_whatsapp_redesign(filepath)
    except Exception as e:
        print(f"❌ Erro ao processar {filename}: {e}")

print("=" * 60)
print("✅ Processo concluído!")
print("=" * 60)
