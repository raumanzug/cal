#!/usr/bin/env python2
#-*- encoding: UTF-8 -*-

import argparse
import cal.holidays
import calendar
import datetime
import locale
import pyexiv2
import reportlab.pdfgen.canvas

#
# Einige Einstellungen

# Räumlicher Abstand von einem Tag zum nächsten.
diff_day  = (0, -25)

# Stelle, an der Monatsnamen erscheint.
month_name_place     =  (700, -100)

# Stellen, an denen Wochtagspanels gedruckt werden.
weekday_panel_places = [(600, -150), (600, -350)]

# Stellen, wo die Monatstage erscheinen (6 Wochen)
day_places           = [(700, -150), (700, -350),\
                        (750, -150), (750, -350),\
                        (800, -150), (800, -350) ]

# Stelle, an der das Kalenderbild erscheint.
pic_place            =  (50, -500)

# Abmessungen des Bildes
pic_dim               =  (489.6, 367.2)

# Stelle, an der die Bildunterschrift erscheint.
capt_place           =  (50, -550)

# Farbe, mit der Feiertage geschrieben werden:
RGB_free = (0.95, 0.3, 0.1)

# Farbe, mit der Werktage geschrieben werden:
RGB_work = (0.58, 0.58, 0.58)

# Standardfarbe für alles übrige:
RGB_standard = (0.58, 0.58, 0.58)

#
# Einige Hilfsprozeduren:

def get_col(day, weekday):
 """Ermittelt, in der wievielten Woche des Monats der Tag day
    enthalten ist.  ZÃ¤hlung beginnt mit 0."""
 col_cand = day // 7
 row_cand = day %  7
 if (weekday < row_cand):
  col_cand += 1
 return col_cand

def get_weekday_name(weekday):
 """Schreibt die abgekÃ¼rzten Wochentagsbezeichnungen aus."""
 if   (weekday == 0):
  return locale.nl_langinfo(locale.ABDAY_2)
 elif (weekday == 1):
  return locale.nl_langinfo(locale.ABDAY_3)
 elif (weekday == 2):
  return locale.nl_langinfo(locale.ABDAY_4)
 elif (weekday == 3):
  return locale.nl_langinfo(locale.ABDAY_5)
 elif (weekday == 4):
  return locale.nl_langinfo(locale.ABDAY_6)
 elif (weekday == 5):
  return locale.nl_langinfo(locale.ABDAY_7)
 elif (weekday == 6):
  return locale.nl_langinfo(locale.ABDAY_1)

def get_month_name(month):
 """Schreibt den Monatsnamen aus."""
 if   (month == 1):
  return locale.nl_langinfo(locale.MON_1)
 elif (month == 2):
  return locale.nl_langinfo(locale.MON_2)
 elif (month == 3):
  return locale.nl_langinfo(locale.MON_3)
 elif (month == 4):
  return locale.nl_langinfo(locale.MON_4)
 elif (month == 5):
  return locale.nl_langinfo(locale.MON_5)
 elif (month == 6):
  return locale.nl_langinfo(locale.MON_6)
 elif (month == 7):
  return locale.nl_langinfo(locale.MON_7)
 elif (month == 8):
  return locale.nl_langinfo(locale.MON_8)
 elif (month == 9):
  return locale.nl_langinfo(locale.MON_9)
 elif (month == 10):
  return locale.nl_langinfo(locale.MON_10)
 elif (month == 11):
  return locale.nl_langinfo(locale.MON_11)
 elif (month == 12):
  return locale.nl_langinfo(locale.MON_12)

def setcolor(rr, month, day, canvas):
 """Richtige Farbe fÃ¼r den entsprechenden Tag wÃ¤hlen"""
 if (datetime.datetime(cmdline_args.year, month, day, 0, 0, 0) in rr):
  canvas.setFillColorRGB(RGB_free[0], RGB_free[1], RGB_free[2])
 else:
  canvas.setFillColorRGB(RGB_work[0], RGB_work[1], RGB_work[2])

def coeff_R2(c, p):
 """Multipliziert c in R mit Vektor (x, y) in R^2"""
 return (c * p[0], c * p[1])

def add_R2(p_1, p_2):
 """Addiert zwei Vektoren (x_1, y_1), (x_2, y_2)"""
 return (p_1[0] + p_2[0], p_1[1] + p_2[1])

###################################


locale.setlocale(locale.LC_ALL, "")


#
#
# Kommandozeilenparameter auswerten:
#
cmdline = argparse.ArgumentParser(
 description = """...baut Wandkalender in Form von PDF-Dateien zum
                  Ausdrucken und AufhÃ¤ngen""")
countries =  list(cal.holidays.rr_dict.keys())
countries.sort()
cmdline.add_argument("country", choices = countries, help = "Bundesland")
cmdline.add_argument("year", type = int, help = "Jahr")
cmdline_args = cmdline.parse_args()
#
# cmdline_args.country enthält das Bundesland
# cmdline_args.year enthält jetzt das Jahr
#
#

#
#

rr =  cal.holidays.rr_dict[cmdline_args.country]

filename_out = str(cmdline_args.year).zfill(4) + ".PDF"

#
#
# Kalender bauen
#

calendar = calendar.Calendar()
canvas   = reportlab.pdfgen.canvas.Canvas(filename_out)

for month in range(1, 13):
 month_name  = get_month_name(month)
 filename_in = str(cmdline_args.year).zfill(4) + "-" + \
  str(month).zfill(2) + ".JPG"
 canvas.rotate(90)
 canvas.setFont("Helvetica", 25)
 canvas.setFillColorRGB(RGB_standard[0], RGB_standard[1], RGB_standard[2])
 canvas.drawString(month_name_place[0], month_name_place[1], month_name)
 canvas.drawImage(filename_in, pic_place[0], pic_place[1],
  width = pic_dim[0], height = pic_dim[1])
 for weekday_panel in weekday_panel_places:
  for weekday in range(0, 7):
   weekday_name = get_weekday_name(weekday)
   position     = add_R2(weekday_panel, coeff_R2(weekday, diff_day))
   canvas.drawString(position[0], position[1], weekday_name)
 image = pyexiv2.Image(filename_in)
 imageData =  image.read_exif()
 if 'Exif.Photo.UserComment' in imageData:
  metadata = imageData['Exif.Photo.UserComment']
  canvas.setFont("Helvetica", 13)
  canvas.drawString(capt_place[0], capt_place[1], metadata)
 canvas.setFont("Helvetica", 25)
 for (day, weekday) in calendar.itermonthdays2(cmdline_args.year, month):
  if (day == 0):
   continue

  weekday_name = get_weekday_name(weekday)
  col = get_col(day, weekday)
  position = add_R2(day_places[col], coeff_R2(weekday, diff_day))
  setcolor(rr, month, day, canvas)
  canvas.drawRightString(position[0], position[1], str(day))
 canvas.showPage()
canvas.save()

#
#
#
#
