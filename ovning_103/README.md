# Övning 3 - Numerisk derivering

Du känner säkert till derivatans definition. För en given funktion ![](https://latex.codecogs.com/png.image?\dpi{100}&space;\bg_white&space;f) och ett givet värde på ![](https://latex.codecogs.com/png.image?\dpi{100}&space;\bg_white&space;x) ger denna lutningen i punkten ![](https://latex.codecogs.com/png.image?\dpi{100}&space;\bg_white&space;x) på den graf som ![](https://latex.codecogs.com/png.image?\dpi{100}&space;\bg_white&space;f) representerar.
<p align="center">
<img src="https://latex.codecogs.com/png.download?%5Cdpi%7B120%7D%20%5Cbg_white%20%5Csmall%20%5Cfrac%7Bd%7D%7B%7Bdx%7D%7Df%5Cleft%28%20x%20%5Cright%29%20%3D%20%5Cmathop%20%7B%5Clim%20%7D%5Climits_%7Bh%20%5Cto%200%7D%20%5Cfrac%7B%7Bf%5Cleft%28%20%7Bx%20+%20h%20%7D%20%5Cright%29%20-%20f%5Cleft%28%20x%20%5Cright%29%7D%7D%7Bh%20%7D"
</p>
<p align="center"><i>Derivatans definition</i></p>

I Python finns ingen inbyggd funktionalitet att derivera funktioner, det får man skriva själv. Till den här övningen tillhandahåller jag en sådan funktion i filen [derivata.py](derivata.py), och exempel på hur den används finns i filen [newton-raphson.py](newton-raphson.py). För att det ska fungera att använda deriveringsfunktionen måste dessa två filer ligga i samma katalog på lagringsmediet.

**OBS!** Filen `derivata.py` ska du inte förändra alls i nedanstående övningar.

## Uppgifter
1. Pröva att ändra deriveringspunkten på den givna funktionen i filen [newton-raphson.py](newton-raphson.py). Kontrollera att resultatet stämmer med hjälp av deriveringsregler. Pröva också att ändra värdet på ![](https://latex.codecogs.com/png.image?\dpi{100}&space;\bg_white&space;h) (det är ju den som ska gå mot noll enligt definitionen).

2. Pröva att ändra funktionen till andra funktioner (en i taget, naturligtvis). Pröva en exponentialfunktion, en potensfunktion (t ex en kubikrot) och en logaritmisk funktion.

### Newton-Rapshons metod för ekvationslösning
Derivata är användbart i många sammanhang. Ett sådant sammanhang du kanske inte kommit kontakt med ännu är att lösa ekvationer numeriskt. Det finns en metod som heter *Newton-Raphsons metod*. Den går till så att man 

* Gissar ett värde på en funktions nollställe

* Detta värde sätts in i en metodens formel, varpå man får ut ett bättre värde

* Detta bättre värde sätts in i formeln igen, vilket ger ett ännu bättre värde på lösningen. Så fortsätter man tills värdet inte förändras särskilt mycket.

Om en ekvation är skriven på formen
![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20f%28x%29%3D0), t ex ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x%5Ccdot%5Csin%28x%29+2%3D0),
så kan man få ut en approximativ lösning med Newton-Raphsons, vars formel kan skrivas

<p align="center">
<img src="https://latex.codecogs.com/png.download?%5Cdpi%7B120%7D%20%5Cbg_white%20%5Csmall%20x_%7Bn+1%7D%3Dx_n-%5Cfrac%7Bf%28x_n%29%7D%7Bf%27%28%7Bx_n%7D%29%7D">
</p>
<p align="center"><i>Newton-Raphsons formel</i></p>

Här är ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x_n) gissningen och ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x_%7Bn+1%7D) är det beräknade värde som kommer att bli bättre än gissningen. Sedan sätts detta beräknade värde in som ett nytt ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x_n), varpå man får ut ett ännu bättre värde på lösningen. Så fortsätter man som sagt till det att värdet inte förändras så mycket, man säger att formeln **itereras**.

Ett exempel på beräkning finns [på denna Wikipedia-sida](https://sv.wikipedia.org/wiki/Newtons_metod#Exempel). Newton-Raphsons metod fungerar med de flesta funktioner, men inte med alla gissningar. Numerisk lösning är inte något vi ska fördjupa oss i, men som vi kommer att se i programmeringsövningen nedan att vissa gissningar inte alls kommer att fungera.

3. Utgå från filen [newton-raphson.py](newton-raphson.py) och implementera formeln för Newton-Raphsons metod för en funktion ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20f%28x%29). Skriv in formeln i en `for`-loop som gör att den kan itereras ett godtyckligt antal gånger. Lös ekvationerna nedan och få fram respektive lösning(ar) med fem korrekta decimaler (du måste pröva hur många iterationer som ska göras).
   
    **a**. ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20%5Cln%7Bx%7D+x%5E2%3D0) med  ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x_0%3D1). Som du ser i filen så är modulen `math` importerad som `m`, och då erhålls den naturliga logaritmen
    ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20%5Cln%7Bx%7D)
    som `m.log(x)`.
    
    **b**. ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%203%5Clg%7Bx%7D-2.5%3D0). Även här kan ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x_0%3D1) användas som startvärde. Logaritmen med basen 10 erhålls med `m.log10(x)`

    **c**. ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x%5E2-2x%3D0), pröva även här ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x_0%3D1).

    **c**. ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x%5E2+%28%5Csqrt%7B10%7D-%5Csqrt%7B5%7D%29x-5%5Csqrt%7B2%7D%3D0). Rita den aktuella funktionsgrafen och hitta lämpliga värden som kan användas som gissning.

    **d**. ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20%5Cln%7Bp%7D%3Dp-2). Hitta lämpliga startvärden grafiskt.

    **e**. ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x%5E3%3D-1). Denna ekvation har förstås en lösning ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x%3D-1), men det finns två andra lösningar som är komplexa. För att få en komplex lösning måste gissningen anges som ett komplext tal, ansätt ![](https://latex.codecogs.com/png.download?%5Cbg_white%20%5Csmall%20x_0%3D1-i). I Python anges detta tal som `1-1j`. Kan du även hitta den tredje lösningen?

