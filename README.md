# Raziskava korelacije med različnimi objavami na spletu ter nihanjem kripto valut. 


Projekt, vsebuje podatke in metode, ki smo jih uporabili, da smo analizerali podatke.

## Člani

Člani skupine smo: Gal Mrvar, Avguštin Kastelic, Gregor Novak, Jure Mohar

## Cilji

Iz podatkov, bi radi ugotovili, kaj je vplivalo na ceno kriptovalut v preteklosti.
Zanima nas ali na ceno vplivajo:

* pozitivni / negativni tweeti znanih twitter oseb
* ali je kakšna povezava med število všečkov, retweetov in ceno?

## Kriterij uspešnost

Iz naloge, bi na koncu radi imeli potrditev, če se je naša hipoteza (da socialna omrežja vplivajo na ceno) potrdila. Zadovoljni bi bili

## Podatki

Podatke smo črpali iz večih delov. Vzeli smo obdobje med 1.1.2017 in 1.1.2019

1. Tweeti iz twitterja od vplivnih oseb.

S pomočjo twitter API, ki pa žal pri zastonjski verziji seže le do 1. tedna nazaj si nismo mogli pomagati, zato smo napisali program, ki preko query searchi na twitterju bere twitte. Za začetek smo izbrali nekaj prepoznavnejših oseb kot so:

* vitalikbuterin (začetnik ETH)
* SatoshiLite (začenik LTC)

pa nekaj znanih novinarjev v kripto družbi

* lopp
* fluffypony

in pa nekaj znanih kripto "exchangov"

* binance
* bittrex

2. Podatki o kriptovalutah

Zaenkrat smo se osredotočili na Bitcoin in s pomočjo CryptoCompare API pridobili dnevne podatke v izbranem obdobju o ceni in volumnu. Pridobljene podatke v JSON formatu smo pretvorili v CSV format za lažje branje iz datoteke. Podatki vključujejo:

* čas v obliki timestamp
* close
* high
* low
* open
* volumefrom
* volumeto

Vrednosti so v valuti USD.

3. yyyyyyyyy

## Analize
