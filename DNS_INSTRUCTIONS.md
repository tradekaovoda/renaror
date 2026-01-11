# DNS-instruktioner för Rena Rör

**Datum:** 2026-01-11
**Domän:** renaroristockholm.se (OBS: "ö" i "rör" fungerar inte i DNS)
**Vercel URL:** https://renaror-b8e84s2mg-tradekaovoda-1523s-projects.vercel.app

---

## Problem med "ö" i domännamn

**Viktigt:** Domänen kan INTE vara "renaröristockholm.se" eftersom svenska tecken (å, ä, ö) inte fungerar korrekt i DNS-system. Domänen måste vara:
- `renaroristockholm.se` (utan ö)

---

## DNS-poster att lägga till hos domänleverantör

Logga in på er domänleverantör (Loopia, Binero, One.com, etc.) och lägg till följande DNS-poster:

### 1. A Record (för huvuddomänen)
```
Type: A
Name: @ (eller tomt fält)
Value: 76.76.21.21
TTL: 3600
```

### 2. CNAME Record (för www)
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
TTL: 3600
```

---

## Steg-för-steg instruktioner

### Steg 1: Ta bort befintliga A/CNAME-poster
- Logga in hos er domänleverantör
- Gå till DNS-inställningar för `renaroristockholm.se`
- Ta bort alla befintliga A-poster och CNAME-poster som pekar på @ eller www

### Steg 2: Lägg till nya poster
- Lägg till A-posten: `@ → 76.76.21.21`
- Lägg till CNAME-posten: `www → cname.vercel-dns.com`
- Spara ändringarna

### Steg 3: Vänta på DNS-propagering
- DNS-ändringar tar 5 minuter - 48 timmar att spridas
- Oftast fungerar det inom 1-2 timmar
- Testa med: https://dnschecker.org

### Steg 4: Lägg till domän i Vercel
1. Gå till Vercel Dashboard: https://vercel.com/tradekaovoda-1523s-projects/renaror
2. Klicka på "Settings" → "Domains"
3. Lägg till: `renaroristockholm.se`
4. Lägg till: `www.renaroristockholm.se`
5. Vercel kommer automatiskt verifiera DNS-posterna

---

## Vanliga domänleverantörer - Var hittar man DNS-inställningar?

### Loopia
1. Logga in på loopia.se
2. Gå till "Mina sidor" → "Domäner"
3. Klicka på domänen → "DNS"

### Binero
1. Logga in på binero.se
2. Gå till "Domäner" → Välj domän
3. Klicka på "DNS-inställningar"

### One.com
1. Logga in på one.com
2. Gå till "Kontrollpanel" → "DNS"
3. Välj domänen

### GoDaddy
1. Logga in på godaddy.com
2. Gå till "My Products" → "Domains"
3. Klicka på "DNS" bredvid domänen

---

## Verifiering

När DNS-posterna är aktiva, verifiera att allt fungerar:

1. **Kolla DNS-propagering:**
   - Gå till: https://dnschecker.org
   - Sök på: `renaroristockholm.se`
   - Kontrollera att A-posten visar: `76.76.21.21`

2. **Kolla www-subdomain:**
   - Sök på: `www.renaroristockholm.se`
   - Kontrollera att CNAME visar: `cname.vercel-dns.com`

3. **Testa webbplatsen:**
   - Öppna: https://renaroristockholm.se
   - Öppna: https://www.renaroristockholm.se
   - Båda ska visa Rena Rör-webbplatsen

---

## Kontakt vid problem

Om ni får problem med DNS-konfigurationen:
- Kontakta N3O Vision: info@n3ovision.com
- Eller kontakta er domänleverantör direkt

---

## Teknisk information

**Vercel IP-adress:** 76.76.21.21
**Vercel CNAME:** cname.vercel-dns.com
**SSL/HTTPS:** Aktiveras automatiskt av Vercel efter DNS-verifiering
**Deployment URL:** https://renaror-b8e84s2mg-tradekaovoda-1523s-projects.vercel.app
