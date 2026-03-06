# 📘 Guia Completo: Integração GoHighLevel com External Tracking

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Pré-requisitos](#pré-requisitos)
3. [Passo 1: Obter o Script de Tracking](#passo-1-obter-o-script-de-tracking)
4. [Passo 2: Instalar o Script](#passo-2-instalar-o-script)
5. [Passo 3: Configurar Formulários](#passo-3-configurar-formulários)
6. [Passo 4: Mapear Custom Fields](#passo-4-mapear-custom-fields)
7. [Passo 5: Testar a Integração](#passo-5-testar-a-integração)
8. [⚠️ O Que Evitar](#️-o-que-evitar)
9. [🔧 Troubleshooting](#-troubleshooting)
10. [📊 Exemplos Práticos](#-exemplos-práticos)

---

## Visão Geral

O **External Tracking Script** do GoHighLevel permite capturar:
- ✅ Page views (visualizações de página)
- ✅ Form submissions (envios de formulários)
- ✅ Custom fields personalizados
- ✅ Dados para automações e workflows

**IMPORTANTE:** O script captura apenas formulários HTML padrão (`<form>`) que estão diretamente no DOM da página.

---

## Pré-requisitos

### ✅ Antes de começar, certifique-se de que:

1. **Domínio conectado ao GoHighLevel**
   - Vá em: GoHighLevel → Settings → Domains
   - Adicione seu domínio (ex: `lp3.grupoamcc.com.br`)

2. **Custom Fields criados no GHL**
   - Vá em: Settings → Custom Fields
   - Crie os campos personalizados que deseja capturar
   - **Anote o nome técnico** de cada campo (ex: `nome_da_sua_empresa`)

3. **Website acessível**
   - Seu site deve estar no ar
   - Você deve ter acesso ao código HTML

---

## Passo 1: Obter o Script de Tracking

### 1.1 Acessar o GoHighLevel
1. Faça login no GoHighLevel
2. Vá em **Settings** (⚙️ Configurações)
3. Clique em **External Tracking**

### 1.2 Copiar o Script
Você verá um código similar a este:

```html
<script 
  src="https://link.msgsndr.com/js/external-tracking.js" 
  data-tracking-id="tk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx">
</script>
```

⚠️ **NUNCA modifique o `data-tracking-id`** - ele é único para sua conta!

### 1.3 Habilitar Debug Mode (Recomendado)
Para facilitar testes, adicione `data-debug="true"`:

```html
<script 
  src="https://link.msgsndr.com/js/external-tracking.js" 
  data-tracking-id="tk_fe2f51e951164d39a5605589a1622f3d"
  data-debug="true">
</script>
```

---

## Passo 2: Instalar o Script

### 2.1 Onde Instalar
Coloque o script **ANTES do fechamento da tag `</body>`**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Minha Landing Page</title>
    <!-- Outros códigos do head -->
</head>
<body>
    <!-- Todo o conteúdo da página -->
    
    <!-- 👇 INSTALE O SCRIPT AQUI -->
    <script 
      src="https://link.msgsndr.com/js/external-tracking.js" 
      data-tracking-id="tk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      data-debug="true">
    </script>
</body>
</html>
```

### 2.2 Instalação via Google Tag Manager

Se você usa GTM:

1. Acesse Google Tag Manager
2. Crie uma nova **Tag HTML Personalizada**
3. Cole o script completo (incluindo as tags `<script>`)
4. Configure o acionador para **All Pages** (Todas as Páginas)
5. **IMPORTANTE:** Verifique se o atributo `data-tracking-id` permanece intacto

⚠️ **ATENÇÃO:** Alguns gerenciadores de tags podem remover atributos. Se isso acontecer, instale manualmente no código HTML.

---

## Passo 3: Configurar Formulários

### 3.1 Estrutura Básica do Formulário

Para o GHL capturar dados, seu formulário DEVE:

✅ **Ter uma tag `<form>` real**
✅ **Ter um atributo `name` no formulário**
✅ **Ter campos com atributo `name`**
✅ **Ter um campo de e-mail (obrigatório)**
✅ **Campos devem estar visíveis no DOM**

### 3.2 Exemplo de Formulário Compatível

```html
<form name="lead_form_hero" id="leadFormHero">
    <!-- Campo Nome -->
    <label for="nome">Nome Completo</label>
    <input 
      type="text" 
      id="nome" 
      name="full_name" 
      required 
      placeholder="Digite seu nome">
    
    <!-- Campo E-mail (OBRIGATÓRIO) -->
    <label for="email">E-mail</label>
    <input 
      type="email" 
      id="email" 
      name="email" 
      required 
      placeholder="seu@email.com">
    
    <!-- Campo Telefone -->
    <label for="telefone">Telefone</label>
    <input 
      type="tel" 
      id="telefone" 
      name="phone" 
      placeholder="(00) 00000-0000">
    
    <!-- Botão de Envio -->
    <button type="submit">Enviar</button>
</form>
```

### 3.3 Nomes de Campos Padrão do GHL

O GoHighLevel reconhece automaticamente estes nomes:

| Campo | Atributo `name` recomendado |
|-------|---------------------------|
| Nome Completo | `full_name` ou `name` |
| Primeiro Nome | `first_name` |
| Sobrenome | `last_name` |
| E-mail | `email` ⚠️ **OBRIGATÓRIO** |
| Telefone | `phone` |
| Empresa | `company_name` ou `company` |

---

## Passo 4: Mapear Custom Fields

### 4.1 Criar Custom Field no GoHighLevel

1. Vá em **Settings → Custom Fields**
2. Clique em **+ Add Custom Field**
3. Preencha:
   - **Field Name:** Nome da sua Empresa
   - **Field Key:** `nome_da_sua_empresa` ⚠️ **Anote este valor!**
   - **Field Type:** Text
   - **Object Type:** Contact ou Opportunity

### 4.2 Usar Custom Field no Formulário

Use o **Field Key** como valor do atributo `name`:

```html
<form name="whatsapp_contact_form" id="whatsappForm">
    <!-- Campos padrão -->
    <input type="text" name="full_name" required>
    <input type="email" name="email" required>
    
    <!-- Custom Field: Nome da Empresa -->
    <label for="empresa">Nome da Empresa</label>
    <input 
      type="text" 
      id="empresa" 
      name="nome_da_sua_empresa" 
      required>
    
    <!-- Custom Field: Pergunta personalizada -->
    <label for="pergunta">Sua Pergunta</label>
    <textarea 
      id="pergunta" 
      name="qual_o_valor_aproximado_sua_empresa_tem_a_receber_atualmente_em_aberto" 
      rows="3">
    </textarea>
    
    <button type="submit">Enviar</button>
</form>
```

### 4.3 Como Funciona o Mapeamento

O GHL usa esta ordem de prioridade para mapear campos:

1. **Field Key exato** (ex: `nome_da_sua_empresa`)
2. **Field Label** (nome de exibição do campo)
3. **Nome do campo** (case-insensitive)

✅ **Melhor prática:** Sempre use o **Field Key** exato.

---

## Passo 5: Testar a Integração

### 5.1 Abrir Console do Browser

1. Abra seu site no Chrome
2. Pressione **F12** (ou Cmd+Option+I no Mac)
3. Vá na aba **Console**

### 5.2 Verificar Inicialização do Script

Com `data-debug="true"`, você deve ver:

```
[LC Tracking] Tracker initialized successfully
[LC Tracking] Tracking ID: tk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5.3 Testar Envio de Formulário

1. Preencha todos os campos do formulário
2. Clique em **Enviar**
3. No console, você deve ver:

```
[LC Tracking] Form submission detected
[LC Tracking] Form name: lead_form_hero
[LC Tracking] Form data: { full_name: "...", email: "...", ... }
[LC Tracking] Submission sent successfully
```

### 5.4 Verificar no GoHighLevel

1. Vá em **Contacts** no GHL
2. Procure pelo e-mail que você testou
3. Abra o contato
4. Verifique se os campos foram preenchidos:
   - ✅ Nome
   - ✅ E-mail
   - ✅ Custom Fields

---

## ⚠️ O Que Evitar

### 🚫 NÃO FAÇA ISSO:

#### 1. **NÃO use `type="hidden"` para campos importantes**
```html
<!-- ❌ ERRADO - GHL NÃO captura campos hidden -->
<input type="hidden" name="empresa" value="Minha Empresa">
```

**Por quê?** O GHL ignora campos `hidden` por padrão.

**✅ Solução:** Use campos visíveis ou esconda com CSS:
```html
<!-- ✅ CORRETO - Visível no DOM, mas invisível na tela -->
<input 
  type="text" 
  name="empresa" 
  value="Minha Empresa"
  style="position: absolute; left: -9999px; width: 1px; height: 1px;"
  aria-hidden="true" 
  tabindex="-1">
```

---

#### 2. **NÃO use `e.preventDefault()` sem submeter manualmente ao GHL**

```html
<script>
document.getElementById('meuForm').addEventListener('submit', function(e) {
    e.preventDefault(); // ❌ Bloqueia o GHL de capturar!
    
    // Seu código aqui...
    fetch('/api/enviar', { ... });
});
</script>
```

**Por quê?** O `preventDefault()` impede que o formulário seja submetido, e o GHL não consegue capturar os dados.

**✅ Solução:** Chame manualmente `LCTracker.submitForm()`:
```html
<script>
document.getElementById('meuForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const form = e.target;
    
    // 👇 Enviar para GHL ANTES de fazer seu próprio processamento
    if (typeof window.LCTracker !== 'undefined') {
        try {
            await window.LCTracker.submitForm(form);
            console.log('[GHL] Form submitted successfully');
        } catch (error) {
            console.error('[GHL] Error:', error);
        }
    }
    
    // Aguardar 500ms para GHL processar
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // Agora fazer seu processamento
    fetch('/api/enviar', { ... });
});
</script>
```

---

#### 3. **NÃO esqueça o campo de E-mail**

```html
<!-- ❌ ERRADO - Sem e-mail, GHL NÃO cria contato -->
<form name="meu_form">
    <input type="text" name="full_name">
    <input type="tel" name="phone">
    <button type="submit">Enviar</button>
</form>
```

**Por quê?** O GHL exige um e-mail para criar/atualizar contatos.

**✅ Solução:** Sempre inclua um campo de e-mail:
```html
<form name="meu_form">
    <input type="text" name="full_name">
    <input type="email" name="email" required> <!-- ✅ -->
    <input type="tel" name="phone">
    <button type="submit">Enviar</button>
</form>
```

---

#### 4. **NÃO use formulários em iframes**

```html
<!-- ❌ ERRADO - GHL NÃO rastreia iframes -->
<iframe src="https://outrosite.com/formulario.html"></iframe>
```

**Por quê?** O script não consegue acessar o conteúdo dentro de iframes.

**✅ Solução:** Coloque o formulário diretamente no HTML da página.

---

#### 5. **NÃO modifique o `data-tracking-id`**

```html
<!-- ❌ ERRADO -->
<script 
  src="https://link.msgsndr.com/js/external-tracking.js" 
  data-tracking-id="meu_id_personalizado">
</script>
```

**Por quê?** O tracking ID é gerado pelo GHL e é único para sua conta.

**✅ Solução:** Use exatamente o ID fornecido pelo GoHighLevel.

---

#### 6. **NÃO redirecione imediatamente após submit**

```html
<script>
document.getElementById('meuForm').addEventListener('submit', function(e) {
    e.preventDefault();
    window.location.href = 'obrigado.html'; // ❌ Muito rápido!
});
</script>
```

**Por quê?** O GHL precisa de tempo para enviar os dados.

**✅ Solução:** Aguarde pelo menos 500ms:
```html
<script>
document.getElementById('meuForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Enviar para GHL
    if (typeof window.LCTracker !== 'undefined') {
        await window.LCTracker.submitForm(e.target);
    }
    
    // ✅ Aguardar antes de redirecionar
    await new Promise(resolve => setTimeout(resolve, 500));
    
    window.location.href = 'obrigado.html';
});
</script>
```

---

#### 7. **NÃO use atributos `name` duplicados**

```html
<!-- ❌ ERRADO - Dois campos com mesmo name -->
<form>
    <input type="text" name="empresa" placeholder="Nome">
    <input type="text" name="empresa" placeholder="CNPJ">
</form>
```

**Por quê?** O GHL captura apenas o primeiro valor encontrado.

**✅ Solução:** Use nomes únicos:
```html
<form>
    <input type="text" name="nome_da_empresa">
    <input type="text" name="cnpj_da_empresa">
</form>
```

---

## 🔧 Troubleshooting

### Problema 1: "Nenhum log aparece no console"

**Possíveis causas:**
- Script não foi instalado corretamente
- `data-debug="true"` não está presente
- AdBlocker bloqueando o script

**Solução:**
1. Verifique se o script está antes do `</body>`
2. Adicione `data-debug="true"`
3. Desative extensões de bloqueio de ads
4. Verifique a aba **Network** no DevTools se o script foi carregado

---

### Problema 2: "Formulário não está sendo capturado"

**Checklist:**
- [ ] Formulário tem tag `<form>` real?
- [ ] Formulário tem atributo `name`?
- [ ] Há um campo com `name="email"`?
- [ ] Campos têm atributos `name`?
- [ ] Formulário não está dentro de iframe?

---

### Problema 3: "Custom fields não aparecem no GHL"

**Verificar:**
1. O custom field foi criado no GoHighLevel?
2. O `name` do input corresponde ao **Field Key** exato?
3. O campo está visível (não é `type="hidden"`)?
4. O valor foi preenchido antes do submit?

---

### Problema 4: "Dados chegam em branco"

**Causa comum:** `preventDefault()` sem submissão manual

**Solução:**
```javascript
// Use async/await com LCTracker.submitForm()
document.getElementById('form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const form = e.target;
    
    // Submeter manualmente ao GHL
    if (typeof window.LCTracker !== 'undefined') {
        await window.LCTracker.submitForm(form);
    }
    
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // Seu código aqui
});
```

---

## 📊 Exemplos Práticos

### Exemplo 1: Formulário Simples

```html
<!DOCTYPE html>
<html>
<head>
    <title>Formulário de Contato</title>
</head>
<body>
    <form name="contact_form" id="contactForm">
        <input type="text" name="full_name" required placeholder="Nome">
        <input type="email" name="email" required placeholder="E-mail">
        <input type="tel" name="phone" placeholder="Telefone">
        <button type="submit">Enviar</button>
    </form>

    <!-- Script GHL -->
    <script 
      src="https://link.msgsndr.com/js/external-tracking.js" 
      data-tracking-id="tk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      data-debug="true">
    </script>
</body>
</html>
```

**Resultado no GHL:**
- ✅ Contato criado com nome, e-mail e telefone

---

### Exemplo 2: Formulário com Custom Fields

```html
<form name="lead_form" id="leadForm">
    <!-- Campos padrão -->
    <input type="text" name="full_name" required>
    <input type="email" name="email" required>
    <input type="tel" name="phone">
    
    <!-- Custom Fields -->
    <input type="text" name="nome_da_sua_empresa" required>
    
    <select name="valor_inadimplencia">
        <option value="">Selecione...</option>
        <option value="Até R$ 50.000">Até R$ 50.000</option>
        <option value="De R$ 50.001 a R$ 200.000">De R$ 50.001 a R$ 200.000</option>
        <option value="Acima de R$ 200.000">Acima de R$ 200.000</option>
    </select>
    
    <textarea name="qual_o_valor_aproximado_sua_empresa_tem_a_receber_atualmente_em_aberto" rows="3"></textarea>
    
    <button type="submit">Enviar</button>
</form>

<script 
  src="https://link.msgsndr.com/js/external-tracking.js" 
  data-tracking-id="tk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  data-debug="true">
</script>
```

**Resultado no GHL:**
- ✅ Contato criado
- ✅ Custom field "Nome da sua Empresa" preenchido
- ✅ Custom field "Valor Inadimplência" preenchido
- ✅ Custom field "Pergunta" preenchido

---

### Exemplo 3: Formulário com Redirecionamento

```html
<form name="signup_form" id="signupForm">
    <input type="text" name="full_name" required>
    <input type="email" name="email" required>
    <button type="submit">Enviar</button>
</form>

<script 
  src="https://link.msgsndr.com/js/external-tracking.js" 
  data-tracking-id="tk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  data-debug="true">
</script>

<script>
document.getElementById('signupForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const form = e.target;
    const submitBtn = form.querySelector('button[type="submit"]');
    
    // Desabilitar botão
    submitBtn.disabled = true;
    submitBtn.textContent = 'Enviando...';
    
    // Enviar para GHL
    if (typeof window.LCTracker !== 'undefined') {
        try {
            await window.LCTracker.submitForm(form);
            console.log('[GHL] Dados enviados com sucesso!');
        } catch (error) {
            console.error('[GHL] Erro ao enviar:', error);
        }
    }
    
    // Aguardar GHL processar
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // Redirecionar
    window.location.href = 'obrigado.html';
});
</script>
```

---

## 📝 Checklist Final

Antes de publicar sua landing page, verifique:

### ✅ Script Instalado
- [ ] Script colado antes do `</body>`
- [ ] `data-tracking-id` correto
- [ ] `data-debug="true"` (para testes)

### ✅ Formulário Configurado
- [ ] Tag `<form>` com atributo `name`
- [ ] Campo `email` obrigatório presente
- [ ] Todos os campos têm atributo `name`
- [ ] Nenhum campo importante é `type="hidden"`

### ✅ Custom Fields
- [ ] Custom fields criados no GHL
- [ ] Field Keys anotados
- [ ] Atributos `name` correspondem aos Field Keys

### ✅ JavaScript
- [ ] Se usa `preventDefault()`, chama `LCTracker.submitForm()`
- [ ] Aguarda 500ms antes de redirecionar
- [ ] Logs de debug funcionando

### ✅ Testes
- [ ] Console mostra inicialização do tracker
- [ ] Console mostra envio de formulário
- [ ] Contato criado no GHL
- [ ] Todos os campos preenchidos corretamente

---

## 🎯 Conclusão

Seguindo este guia, sua integração com GoHighLevel estará funcionando perfeitamente. Lembre-se:

1. **E-mail é obrigatório** para criar contatos
2. **Campos hidden não são capturados** por padrão
3. **Use `LCTracker.submitForm()`** se usar `preventDefault()`
4. **Aguarde 500ms** antes de redirecionar
5. **Use Field Keys exatos** para custom fields

---

## 📞 Precisa de Ajuda?

Se encontrar problemas:
1. Ative `data-debug="true"`
2. Verifique o console do browser
3. Confira o checklist acima
4. Revise a seção "O Que Evitar"

---

**Última atualização:** 6 de março de 2026  
**Projeto:** LP-EMPRESAS-QUE-FATURAM-ACIMA-DE-MIL-REAIS-POR-MÊS  
**Autor:** Media Growth Marketing
