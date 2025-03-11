# Bulk-fil-nedlastning
Python-script for å laste ned flere filer samtidig. Eksempelkoden laster ned fysikk-eksamener og løsningsforslag i TFY4107 fra 2015 til 2023. 


## Guide

**Steg 1**

Inspect element på siden du vil laste ned fra. Naviger deg til "console".
Kopier dette og trykk enter:

const links = Array.from(document.querySelectorAll('a[href$=".pdf"]'));

const pdfLinks = links.map(link => link.href);

console.log(pdfLinks);

Kopier arrayet du får ut, og bytt det ut med arrayet som er i python-skriptet. 
!Merk at du må høyreklikke arrayet, og velge "copy object". Det er ikke lurt å markere det for så å kopiere med cmd+c. Da vil du kanskje få problemer med avkortede lenker.

**Steg 2**

Lag en mappe du vil ha filene i, og lagre scriptet der. 
Åpne mappen i din favoritt-editor og skriv "pip install requests" i terminalen. 
Kjør scriptet.

Du er nå i mål:)
