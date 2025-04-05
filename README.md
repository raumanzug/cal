# `cal` - Ein Programm zum Erzeugen von Jahreswandkalendern

## Installation

F&uuml;hre folgende Zeile nach dem Auschecken aus:

	python -m pip install --upgrade build
	python -m build

Verzeichnis `dist` enth&auml;lt jetzt `cal-0.2.tar.gz`.  Installiere jetzt:

	python -m pip install dist/cal-0.2.tar.gz

## Anwendung

Um mit Hilfe dieses Programmes f&uuml;r das Jahr `<year>` einen Wandkalender im PDF-Format zu produzieren, ben&ouml;tigen wir zw&ouml;lf JPEG-Bilder.  F&uuml;r jeden Monat eines.  Diese JPEG-Bilder m&uuml;ssen jeweils in Dateien mit folgenden Namen vorliegen:

	<year>-01.JPG
	<year>-02.JPG
	<year>-03.JPG
	<year>-04.JPG
	<year>-05.JPG
	<year>-06.JPG
	<year>-07.JPG
	<year>-08.JPG
	<year>-09.JPG
	<year>-10.JPG
	<year>-11.JPG
	<year>-12.JPG

Folgendes Kommando erzeugt aus diesen Dateien eine Datei `<year>.PDF`, die den Kalender enth&auml;lt:

	python -m cal <country> <year>

worin `<country>` das Bundesland bezeichnet, dessen gesetzliche Feiertage im Kalender markiert sind.

Enthalten die o.g. Ausgangsdateien einen EXIF-Tag `Exif.Photo.UserComment`, so wird dessen Inhalt f&uuml;r eine Bildunterschrift verwendet.

