# Landing Page - AMCC Empresas +1M

## 📋 Descrição

Landing Page desenvolvida especificamente para empresas que faturam **acima de 1 milhão de reais por mês**, focada em recuperação de crédito de grandes carteiras.

## 🎯 Público-Alvo

- **Faturamento:** Acima de R$ 1.000.000/mês
- **Perfil:** Empresas de médio e grande porte
- **Segmentos:** Varejo, Indústria, Distribuição, Serviços, Saúde, Educação
- **Dor Principal:** 5-10% do faturamento perdido em inadimplência (até R$ 100k/mês)

## 📝 Copy Principal do Anúncio

**Texto do Anúncio:**
"Sua empresa fatura acima de um milhão de reais por mês. Saiba que ela carrega uma taxa silenciosa. 5% a 10% vira prejuízo por inadimplência. O Grupo AMCC recupera grandes carteiras com abordagem humanizada, jurídico integrado, tecnologia avançada e zero custo antecipado. Você só paga pelo resultado. Imagine transformar dívidas antigas em caixa imediato. Com previsibilidade, segurança jurídica e o cliente voltando ao ciclo de compras. Clique agora e solicite uma análise gratuita."

## 🎨 Características da LP

### Layout e Design
- **Cores:** Baseadas na LP Padrão
  - Primária: #8B0F0F (Vermelho AMCC)
  - Secundária: #05090D (Preto Moderno)
  - Destaque: #D4AF37 (Dourado Premium)
- **Estilo:** Premium, corporativo, sofisticado
- **Fonte:** Inter (Google Fonts)

### Estrutura

1. **Hero Section**
   - Badge "Para Empresas +1 Milhão/Mês"
   - Headline de impacto sobre perda de R$ 100k/mês
   - Estatísticas: +30 anos, R$ 2Bi+ recuperados, 85% taxa de sucesso
   - CTA principal: "Análise Gratuita Agora"

2. **Problema Section**
   - "A Taxa Silenciosa"
   - 3 Cards com números de impacto:
     - 5-10% de prejuízo mensal
     - R$ 1,2M de perda anual
     - 60% de clientes perdidos

3. **Solução Section**
   - 6 Diferenciais em grid:
     - Zero Custo Antecipado
     - Tecnologia Avançada
     - Jurídico Integrado
     - Abordagem Humanizada
     - Previsibilidade
     - Segurança Jurídica

4. **Diferenciais Section**
   - "Por que Grandes Empresas Escolhem a AMCC"
   - 4 Diferenciais detalhados:
     - Expertise em Grandes Volumes
     - Time Especializado
     - Integração com ERP
     - Atendimento Premium

5. **Resultados Section**
   - 3 Cases de sucesso reais
   - Métricas específicas de recuperação

6. **Parceiros Section**
   - Logos de empresas clientes
   - Diversos segmentos

7. **Formulário Section**
   - Campos específicos para empresas grandes:
     - Nome + Cargo
     - Telefone + Email corporativo
     - Empresa + Faturamento Mensal
     - Valor em Inadimplência + Segmento
   - Trust badges: LGPD, Confidencialidade, Resposta 24h

8. **Footer**
   - Logo AMCC
   - Telefone 0800
   - Compliance LGPD

## 🔧 Funcionalidades

- ✅ Design responsivo (mobile-first)
- ✅ Animações on-scroll suaves
- ✅ Botão flutuante fixo
- ✅ Smooth scroll entre seções
- ✅ Máscara de telefone automática
- ✅ Integração com webhook Make.com
- ✅ Redirecionamento para página de obrigado
- ✅ Microsoft Clarity tracking

## 📊 Integração

**Webhook:** `https://hook.us2.make.com/08wombkl1yfcab6s4jwuot97v0bfe99r`

**Dados Enviados:**
```json
{
  "name": "Nome Completo",
  "email": "email@empresa.com",
  "phone": "(11) 99999-9999",
  "empresa": "Nome da Empresa",
  "plataforma": "Campanha Empresas +1M",
  "question": "Cargo + Faturamento + Inadimplência + Segmento",
  "source": "AMCC - Empresas +1M | Recupere 5-10% do Faturamento Perdido",
  "tags": ["AMCC", "Empresas +1M", "Alto Faturamento", "Grandes Carteiras"]
}
```

## 📁 Estrutura de Arquivos

```
LP-EMPRESAS QUE FATURAM ACIMA DE MIL REAIS POR MÊS/
├── index.html          # Página principal
├── obrigado.html       # Página de agradecimento
└── README.md          # Este arquivo
```

**Nota:** As imagens e assets são referenciadas da pasta `../LP PADRÃO/`

## 🚀 Como Usar

1. Fazer upload dos arquivos para o servidor
2. Garantir que a pasta `LP PADRÃO` está no mesmo nível com:
   - `/parceiros de sucesso/` (logos)
   - `/logo amcc/` (logo branco)
   - `/primeiro bloco/` (background)
3. Testar formulário e integração com Make.com
4. Configurar campanha de anúncios apontando para esta LP

## 🎯 Otimização para Conversão

### Pontos Fortes
- ✅ Headline com número específico (R$ 100k/mês)
- ✅ Segmentação clara (empresas +1M)
- ✅ Prova social (logos de parceiros)
- ✅ Cases com números reais
- ✅ Zero fricção (sem custo antecipado)
- ✅ Urgência sutil (resposta em 24h)
- ✅ Trust signals (LGPD, compliance)

### Diferenciais vs LP Padrão
- ✅ Badge de segmentação premium
- ✅ Estatísticas corporativas no hero
- ✅ Formulário mais completo (cargo, faturamento, segmento)
- ✅ Cases específicos de grandes carteiras
- ✅ Linguagem mais corporativa/executiva
- ✅ Ênfase em previsibilidade e integração com ERP

## 📱 Compatibilidade

- ✅ Desktop (1920px+)
- ✅ Laptop (1366px - 1920px)
- ✅ Tablet (768px - 1366px)
- ✅ Mobile (< 768px)

## 🎨 Paleta de Cores

```css
--primary-color: #8B0F0F;     /* Vermelho AMCC */
--primary-dark: #7C0C0C;      /* Vermelho Escuro */
--dark-modern: #05090D;       /* Preto Moderno */
--accent-gold: #D4AF37;       /* Dourado Premium */
--light-bg: #F9F3F3;          /* Fundo Claro */
--subtle-bg: #F7EDEE;         /* Fundo Sutil */
```

## 📈 Métricas Esperadas

- **Taxa de Conversão Alvo:** 8-15%
- **Tempo na Página:** 3-5 minutos
- **Bounce Rate Esperado:** < 40%
- **Qualidade dos Leads:** Alta (empresas +1M)

## ✅ Checklist de Publicação

- [ ] Testar formulário em desktop
- [ ] Testar formulário em mobile
- [ ] Verificar integração com Make.com
- [ ] Testar página de obrigado
- [ ] Verificar carregamento de todas as imagens
- [ ] Testar responsividade em diferentes dispositivos
- [ ] Configurar Clarity tracking
- [ ] Configurar pixels de conversão (Meta Ads, Google Ads)
- [ ] Testar velocidade de carregamento
- [ ] Verificar SEO básico (title, meta description)

## 📞 Suporte

Para dúvidas ou ajustes, entre em contato com a equipe de desenvolvimento.

---

**Última atualização:** 21 de novembro de 2025
**Versão:** 1.0
**Desenvolvido para:** Grupo AMCC - Campanha Empresas +1M
