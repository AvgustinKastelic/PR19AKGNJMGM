# Raziskava korelacije med različnimi objavami na spletu ter nihanjem kripto valut. 


Projekt, vsebuje podatke in metode, ki smo jih uporabili, da smo analizerali podatke.

## Člani

Člani skupine smo: Gal Mrvar, Avguštin Kastelic, Gregor Novak, Jure Mohar

## Opis problema in cilji

Iz podatkov, bi radi ugotovili, ali obstaja korelacija med objavami na spletu ter nihanjem kripto valut.
Zanima nas ali na ceno oz. volumen kripto valut vplivajo naslednji faktorji:

* Količina twitter objav / člankov
* Pozitivni / negativni tweeti vplivnih twitter računov
* Število všečkov, retweetov

Poleg tega pa lahko iščemo tudi druga zanimiva odstopanja v podatkih.

## Kriterij uspešnost

Iz naloge, bi na koncu radi imeli potrditev, če se je naša hipoteza (da socialna omrežja vplivajo na ceno) potrdila. Zadovoljni bi bili

## Opis podatkov

Podatke smo črpali iz večih virov. Vzeli smo obdobje med 1.1.2017 in 1.1.2019 saj je to obdobje zaradi cen kriptovalut najbolj zanimivo za našo raziskavo.

1. Objave vplivnih oseb na Twitterju.

S pomočjo twitter API, ki pa žal pri zastonjski verziji seže le do 1. tedna nazaj si nismo mogli pomagati, zato smo napisali program, ki preko query searchi na twitterju bere twitte. Za začetek smo izbrali nekaj prepoznavnejših oseb kot so:

* vitalikbuterin (začetnik ETH)
* SatoshiLite (začenik LTC)

pa nekaj znanih novinarjev v kripto družbi

* lopp
* fluffypony

in pa nekaj znanih kripto "exchangov"

* binance
* bittrex

Podatke smo zbrali v csv file: username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink

2. Objave medijev na spletu

S pomočjo Event Registry smo zbrali podatke in vsebino člankov, ki omenjajo koncept kriptovalut. Zbrali smo 220.000 člankov v 39 jezikih.

3. Podatki o kriptovalutah

Zaenkrat smo se osredotočili na Bitcoin in s pomočjo CryptoCompare API pridobili dnevne podatke v izbranem obdobju o ceni in volumnu. Pridobljene podatke v JSON formatu smo pretvorili v CSV format za lažje branje iz datoteke. Podatki vključujejo:

* čas v obliki timestamp
* close
* high
* low
* open
* volumefrom
* volumeto

Vrednosti so v valuti USD.

## Analiza vsebine objav

Objave smo poskusili klasificirati na tri kategorije:

* pozitivno
* negativno
* nevtralno

Za analizo smo večinoma uporabili Python knjižnico TextBlb, poleg tega pa uporabljamo tudi API od MonkeyLearn.
Trenutna ocena uspešnosti klasifikatorja: 

* 44% (62 testnih primerov)

Cilj: Izboljšanje klasifikatorja.

## Analize

![alt text] (http://url/to/img.png)
