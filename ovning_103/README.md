# Övning 3 - Numerisk derivering

Du känner säkert till derivatans definition. För en given funktion $f$ och ett
givet värde på $x$ ger denna lutningen i punkten $x$ på den graf som $f(x)$
representerar.

$$
\frac{d}{dx}f(x)=\lim_{h\rightarrow 0} \frac{f(x+h)-f(x)}{h}
$$

I Python finns ingen inbyggd funktionalitet att derivera funktioner, det får man
skriva själv. Till den här övningen tillhandahåller jag en sådan funktion i filen
[derivata.py](derivata.py), och exempel på hur den används finns i filen
[newton-raphson.py](newton-raphson.py). För att det ska fungera att använda
deriveringsfunktionen måste dessa två filer ligga i samma katalog på
lagringsmediet.

**OBS!** Filen `derivata.py` ska du inte förändra alls i nedanstående övningar.

## Uppgifter

1. Pröva att ändra deriveringspunkten på den givna funktionen i filen
   [newton-raphson.py](newton-raphson.py). Kontrollera att resultatet stämmer med
   hjälp av deriveringsregler. Pröva också att ändra värdet på _h_ (det är ju den
   som ska gå mot noll enligt definitionen).

2. Pröva att ändra funktionen till andra funktioner (en i taget, naturligtvis).
   Pröva en exponentialfunktion, en potensfunktion (t ex en kubikrot) och en
   logaritmisk funktion.

## Newton-Rapshons metod för ekvationslösning

Derivata är användbart i många sammanhang. Ett sådant sammanhang du kanske inte
kommit kontakt med ännu är att lösa ekvationer numeriskt. Det finns en metod som
heter _Newton-Raphsons metod_. Den går till så att man

- Gissar ett värde på en funktions nollställe

- Detta värde sätts in i en metodens formel, varpå man får ut ett bättre värde

- Detta bättre värde sätts in i formeln igen, vilket ger ett ännu bättre värde
  på lösningen. Så fortsätter man tills värdet inte förändras särskilt mycket.

Om en ekvation är skriven på formen
$f(x)=0$,
så kan man få ut en approximativ lösning med Newton-Raphsons, vars formel kan
skrivas

$$
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
$$

Här är $x_n$ gissningen och $x_{n+1}$ är det
beräknade värde som kommer att bli bättre än gissningen. Sedan sätts detta
beräknade värde in som ett nytt $x_n$, varpå man får ut ett
ännu bättre värde på lösningen. Så fortsätter man som sagt till det att värdet
inte förändras så mycket, man säger att formeln **itereras**.

Ett exempel på beräkning finns [på denna Wikipedia-sida](https://sv.wikipedia.org/wiki/Newtons_metod#Exempel).
Newton-Raphsons metod fungerar med de flesta funktioner, men inte med alla
gissningar. Numerisk lösning är inte något vi ska fördjupa oss i, men som
vi kommer att se i programmeringsövningen nedan att vissa gissningar inte
alls kommer att fungera.

3. Utgå från filen [newton-raphson.py](newton-raphson.py) och implementera
   formeln för Newton-Raphsons metod för en funktion $f$. Skriv in formeln
   i en `for`-loop som gör att den kan itereras ett godtyckligt antal gånger.
   Lös ekvationerna nedan och få fram respektive lösning(ar) med fem korrekta
   decimaler (du måste pröva hur många iterationer som ska göras).

**a**.
$\ln x+x^2=0$ med $x_0=0$

Som du ser i filen så är modulen `math` importerad som `m`, och då erhålls den
naturliga logaritmen $\ln x$ som `m.log(x)`.

**b**.
$3\lg x-2.5=0$. Även här kan $x_0=1$
användas som startvärde. Logaritmen med basen 10 erhålls med `m.log10(x)`

**c**.
$x^2-2x=0$, pröva även här $x_0=1$.

**d**.
$x^2+(\sqrt{10}-\sqrt{5})x-5\sqrt{2}=0$.
Rita den aktuella funktionsgrafen och hitta lämpliga värden som kan användas
som gissning.

**e**.
$\ln p=p-2$. Hitta lämpliga startvärden grafiskt.

**f**.
$x^3=-1$. Denna ekvation har förstås en lösning $x=-1$, men det finns två
andra lösningar som är komplexa. För att få en komplex lösning måste
gissningen anges som ett komplext tal, ansätt $x_0=1-i$. I Python anges
detta tal som `1-1j`. Kan du även hitta den tredje lösningen?
