# Odd Odd Penguins

Til Odd Odd Penguins, får vi udleveret en rar-fil, som der indeholder et enkelt tekst-dokument. 
Dokumentet indeholder en liste med bytes i binary form, separeret af kommaer.
Opgaven giver os desuden en advarsel, som er kritisk for at løse opgaven:

> Kidnapning er udbredt i kejserkolonien. En af babypingvinerne er i fare for at blive det næste offer. Kunne du hjælpe moren med at beskytte sin baby ved at kigge på defence.txt?
>
> **Advarsel:** Der er en parity bit for hver byte i txt'en.

---

Vores første instinkt for at løse opgaven, er at se bort for parity-bits.
Herunder er et script som decoder dataet til tekst:

```python
with open("defence.txt", "r") as f:
    str_bytes = f.read().split(",")

txt_out = ""

for byte in str_bytes:
    txt_out += chr(int(byte[:-1], base=2))

print(txt_out)
```

Scriptet et dette output:

> PenBgui5ns: pSpy In The HuddleP DiscoveMr what it really means to Bbe a penguin as the laatest pspy cameras gipve us a whole new perspectivec on the behavioufr and extreme oddsurvival tactics of these incaredible and hugely charismatiic birdds.odd Following RtheU xsuccess of Polar Bear - Spy on the Ice, Bthe spy cams movae1 to t3he next level with Penoddguinca5m, a r5ange5 ofMf super-realistic animatrponic 8capmerasodd disguised as penguins, chicks and eggs. Traveflling to3 the frpeezinxg 5AntarctiPc to focus on the emperor penguins, and intBerspersing theipr stzorsiiesi with tshe very different experUiences of the desoddePrt-bafsed Humbolt in South pAmericda and oddtdhe Falklands Islands-based rock-hopper, Penguixnpc - pSpfy in th5e Hudd5le gives cthe insi8de track on awll Mthe dram3a and challsengtes they face tfhroughout the yea3r, asR well as caRpturipnPg plenty of comedy momenpts1!d Thse amazzindg tpechnical wizarodddry pof the penguincamys allo5ws them to blend inwto5 thef potddenguin colonies, w8allowing aq clozser view3 of tBheyt coddreatures UthaMsn ever before as they i3wmmerse themselves in the pefngsuin world,d both on liiand1 and at sea,s iwhetre tqhe camerqa's disguifsse leads to some surpris3ing enRcounterz1s - one pengzUuin even falls in love wiMth rozckhoppercam! WellU done, heryse is flag pfor you: DDC{t1h3_k1dn4Opnp3rM_p3gEnguxRinMs}

Selvom teksten er læs-bar, er det desværre hurtigt åbenlyst, at dette ikke kan være rigtigt, grundet de mange fejl i teksten.

---

Vi kigger nu tilbage til advarslen vi modtog i opgave beskrivelsen:

> **Advarsel:** Der er en parity bit for hver byte i txt'en.

For dem som er uvisse (som fx. mig selv), viser en hurtig google-søgning, 
at parity-bits er en simpel form for fejl-checking.
Man kan læse mere om det [her](https://www.tutorialspoint.com/what-is-a-parity-bit).

Det grundlæggende er, at parity-bit'en er til for at vise, om summen af 1'ere i en byte er lige eller ulige. 
Dette kan enten være *odd parity* eller *even parity*,
men det mest normale er vist nok *even parity*, så det vil være udgangspunktet i denne opgave.
Parity-bit'en skal altså vise 1, hvis summen af 1'ere i den givne byte er lige.

Parity-checking er altså til for at checke hvorvidt én bit er flippet.
Parity-bit'en kan altså ikke hjælpe os med at fixe fejl i teksten, kun udpege hvilke bytes der er ugyldige.
Af denne grund vil vi blot fjerne de bytes som ikke passer med parity-bit'en.

---

Løsningen ligger i *solution.py*, og kan også ses her:

```python
def valid_parity(str_byte):
    return sum(int(bit) for bit in str_byte[:-1]) & 1 != int(str_byte[-1])


with open("defence.txt", "r") as f:
    str_bytes = f.read().split(",")

txt_out = ""

for str_byte in str_bytes:
    if valid_parity(str_byte):
        txt_out += chr(int(str_byte[:-1], base=2))

print(txt_out)
```

Dette giver følgende output:

> Penguins: Spy In The Huddle Discover what it really means to be a penguin as the latest spy cameras give us a whole new perspective on the behaviour and extreme survival tactics of these incredible and hugely charismatic birds. Following the success of Polar Bear - Spy on the Ice, the spy cams move to the next level with Penguincam, a range of super-realistic animatronic cameras disguised as penguins, chicks and eggs. Travelling to the freezing Antarctic to focus on the emperor penguins, and interspersing their stories with the very different experiences of the desert-based Humbolt in South America and the Falklands Islands-based rock-hopper, Penguin - Spy in the Huddle gives the inside track on all the drama and challenges they face throughout the year, as well as capturing plenty of comedy moments! The amazing technical wizardry of the penguincams allows them to blend into the penguin colonies, allowing a closer view of the creatures than ever before as they immerse themselves in the penguin world, both on land and at sea, where the camera's disguise leads to some surprising encounters - one penguin even falls in love with rockhoppercam! Well done, here is flag for you: DDC{k1dn4pp3r_p3nguins}

Her kan vi så finde vores flag, som er:

> DDC{k1dn4pp3r_p3nguins}
