#-*- encoding: UTF-8 -*-

import dateutil.rrule

#
# Die Feiertage

# Sonntag
rrule_sonntag = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 byweekday  = [dateutil.rrule.SU] )

# Neujahr
rrule_neujahr = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 1,                   \
 bymonthday = 1 )

# Heilige Drei Könige
rrule_dreik   = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 1,                   \
 bymonthday = 6 )

# Heilige Drei Könige
rrule_frauent = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 3,                   \
 bymonthday = 8 )

# Karfeitag
rrule_karf    = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 byeaster   = -2 )

# Ostermontag
rrule_ostermo = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 byeaster   = 1 )

# Tag der Arbeit
rrule_mai     = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 5,                   \
 bymonthday = 1 )

# Christi Himmelfahrt
rrule_himmelf = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 byeaster   = 39 )

# Pfingstmontag
rrule_pfingst = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 byeaster   = 50 )

# Fronleichnam
rrule_fronl   = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 byeaster   = 60 )

# Mariae Himmelfahrt
rrule_mariaeh = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 8,                  \
 bymonthday = 15 )

# Weltkindertag
rrule_kindert = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 9,                  \
 bymonthday = 20 )

# Tag der Deutschen Einheit
rrule_einheit = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 10,                  \
 bymonthday = 3 )

# Reformationstag
rrule_reform  = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 10,                  \
 bymonthday = 31 )

# Allerheiligen
rrule_allerh  = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 11,                  \
 bymonthday = 1 )

# Buß- & Bettag
rrule_bubt    = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byweekday  = (dateutil.rrule.WE), \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 11,                  \
 bymonthday = range(16,22) )

# Erster Weihnachtstag
rrule_xmas_1  = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 12,                  \
 bymonthday = 25 )

# Zweiter Weihnachtstag
rrule_xmas_2  = dateutil.rrule.rrule(
 dateutil.rrule.YEARLY,            \
 byhour   = 0, \
 byminute = 0, \
 bysecond = 0, \
 bymonth    = 12,                  \
 bymonthday = 26 )

#
# Sonn- und Feiertage in den einzelnen Bundeslaendern, repraesentiert als dict von rrules.

rr_dict =  {}

rr_dict["Baden-Wuerttemberg"] =  dateutil.rrule.rruleset()
rr_dict["Baden-Wuerttemberg"].rrule(rrule_sonntag)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_neujahr)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_dreik)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_karf)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_ostermo)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_mai)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_himmelf)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_pfingst)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_fronl)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_einheit)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_allerh)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_xmas_1)
rr_dict["Baden-Wuerttemberg"].rrule(rrule_xmas_2)

rr_dict["Bayern"] = dateutil.rrule.rruleset()
rr_dict["Bayern"].rrule(rrule_sonntag)
rr_dict["Bayern"].rrule(rrule_neujahr)
rr_dict["Bayern"].rrule(rrule_dreik)
rr_dict["Bayern"].rrule(rrule_karf)
rr_dict["Bayern"].rrule(rrule_ostermo)
rr_dict["Bayern"].rrule(rrule_mai)
rr_dict["Bayern"].rrule(rrule_himmelf)
rr_dict["Bayern"].rrule(rrule_pfingst)
rr_dict["Bayern"].rrule(rrule_fronl)
rr_dict["Bayern"].rrule(rrule_einheit)
rr_dict["Bayern"].rrule(rrule_allerh)
rr_dict["Bayern"].rrule(rrule_xmas_1)
rr_dict["Bayern"].rrule(rrule_xmas_2)

rr_dict["Berlin"] = dateutil.rrule.rruleset()
rr_dict["Berlin"].rrule(rrule_sonntag)
rr_dict["Berlin"].rrule(rrule_neujahr)
rr_dict["Berlin"].rrule(rrule_frauent)
rr_dict["Berlin"].rrule(rrule_karf)
rr_dict["Berlin"].rrule(rrule_ostermo)
rr_dict["Berlin"].rrule(rrule_mai)
rr_dict["Berlin"].rrule(rrule_himmelf)
rr_dict["Berlin"].rrule(rrule_pfingst)
rr_dict["Berlin"].rrule(rrule_einheit)
rr_dict["Berlin"].rrule(rrule_xmas_1)
rr_dict["Berlin"].rrule(rrule_xmas_2)

rr_dict["Brandenburg"] = dateutil.rrule.rruleset()
rr_dict["Brandenburg"].rrule(rrule_sonntag)
rr_dict["Brandenburg"].rrule(rrule_neujahr)
rr_dict["Brandenburg"].rrule(rrule_karf)
rr_dict["Brandenburg"].rrule(rrule_ostermo)
rr_dict["Brandenburg"].rrule(rrule_mai)
rr_dict["Brandenburg"].rrule(rrule_himmelf)
rr_dict["Brandenburg"].rrule(rrule_pfingst)
rr_dict["Brandenburg"].rrule(rrule_einheit)
rr_dict["Brandenburg"].rrule(rrule_reform)
rr_dict["Brandenburg"].rrule(rrule_xmas_1)
rr_dict["Brandenburg"].rrule(rrule_xmas_2)

rr_dict["Bremen"] = dateutil.rrule.rruleset()
rr_dict["Bremen"].rrule(rrule_sonntag)
rr_dict["Bremen"].rrule(rrule_neujahr)
rr_dict["Bremen"].rrule(rrule_karf)
rr_dict["Bremen"].rrule(rrule_ostermo)
rr_dict["Bremen"].rrule(rrule_mai)
rr_dict["Bremen"].rrule(rrule_himmelf)
rr_dict["Bremen"].rrule(rrule_pfingst)
rr_dict["Bremen"].rrule(rrule_einheit)
rr_dict["Bremen"].rrule(rrule_reform)
rr_dict["Bremen"].rrule(rrule_xmas_1)
rr_dict["Bremen"].rrule(rrule_xmas_2)

rr_dict["Hamburg"] = dateutil.rrule.rruleset()
rr_dict["Hamburg"].rrule(rrule_sonntag)
rr_dict["Hamburg"].rrule(rrule_neujahr)
rr_dict["Hamburg"].rrule(rrule_karf)
rr_dict["Hamburg"].rrule(rrule_ostermo)
rr_dict["Hamburg"].rrule(rrule_mai)
rr_dict["Hamburg"].rrule(rrule_himmelf)
rr_dict["Hamburg"].rrule(rrule_pfingst)
rr_dict["Hamburg"].rrule(rrule_einheit)
rr_dict["Hamburg"].rrule(rrule_reform)
rr_dict["Hamburg"].rrule(rrule_xmas_1)
rr_dict["Hamburg"].rrule(rrule_xmas_2)

rr_dict["Hessen"] = dateutil.rrule.rruleset()
rr_dict["Hessen"].rrule(rrule_sonntag)
rr_dict["Hessen"].rrule(rrule_neujahr)
rr_dict["Hessen"].rrule(rrule_karf)
rr_dict["Hessen"].rrule(rrule_ostermo)
rr_dict["Hessen"].rrule(rrule_mai)
rr_dict["Hessen"].rrule(rrule_himmelf)
rr_dict["Hessen"].rrule(rrule_pfingst)
rr_dict["Hessen"].rrule(rrule_fronl)
rr_dict["Hessen"].rrule(rrule_einheit)
rr_dict["Hessen"].rrule(rrule_xmas_1)
rr_dict["Hessen"].rrule(rrule_xmas_2)

rr_dict["Mecklenburg-Vorpommern"] = dateutil.rrule.rruleset()
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_sonntag)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_neujahr)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_karf)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_ostermo)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_mai)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_himmelf)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_pfingst)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_einheit)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_reform)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_xmas_1)
rr_dict["Mecklenburg-Vorpommern"].rrule(rrule_xmas_2)

rr_dict["Niedersachsen"] = dateutil.rrule.rruleset()
rr_dict["Niedersachsen"].rrule(rrule_sonntag)
rr_dict["Niedersachsen"].rrule(rrule_neujahr)
rr_dict["Niedersachsen"].rrule(rrule_karf)
rr_dict["Niedersachsen"].rrule(rrule_ostermo)
rr_dict["Niedersachsen"].rrule(rrule_mai)
rr_dict["Niedersachsen"].rrule(rrule_himmelf)
rr_dict["Niedersachsen"].rrule(rrule_pfingst)
rr_dict["Niedersachsen"].rrule(rrule_einheit)
rr_dict["Niedersachsen"].rrule(rrule_reform)
rr_dict["Niedersachsen"].rrule(rrule_xmas_1)
rr_dict["Niedersachsen"].rrule(rrule_xmas_2)

rr_dict["Nordrhein-Westfalen"] = dateutil.rrule.rruleset()
rr_dict["Nordrhein-Westfalen"].rrule(rrule_sonntag)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_neujahr)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_karf)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_ostermo)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_mai)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_himmelf)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_pfingst)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_fronl)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_einheit)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_allerh)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_xmas_1)
rr_dict["Nordrhein-Westfalen"].rrule(rrule_xmas_2)

rr_dict["Rheinland-Pfalz"] = dateutil.rrule.rruleset()
rr_dict["Rheinland-Pfalz"].rrule(rrule_sonntag)
rr_dict["Rheinland-Pfalz"].rrule(rrule_neujahr)
rr_dict["Rheinland-Pfalz"].rrule(rrule_karf)
rr_dict["Rheinland-Pfalz"].rrule(rrule_ostermo)
rr_dict["Rheinland-Pfalz"].rrule(rrule_mai)
rr_dict["Rheinland-Pfalz"].rrule(rrule_himmelf)
rr_dict["Rheinland-Pfalz"].rrule(rrule_pfingst)
rr_dict["Rheinland-Pfalz"].rrule(rrule_fronl)
rr_dict["Rheinland-Pfalz"].rrule(rrule_einheit)
rr_dict["Rheinland-Pfalz"].rrule(rrule_allerh)
rr_dict["Rheinland-Pfalz"].rrule(rrule_xmas_1)
rr_dict["Rheinland-Pfalz"].rrule(rrule_xmas_2)

rr_dict["Saarland"] = dateutil.rrule.rruleset()
rr_dict["Saarland"].rrule(rrule_sonntag)
rr_dict["Saarland"].rrule(rrule_neujahr)
rr_dict["Saarland"].rrule(rrule_karf)
rr_dict["Saarland"].rrule(rrule_ostermo)
rr_dict["Saarland"].rrule(rrule_mai)
rr_dict["Saarland"].rrule(rrule_himmelf)
rr_dict["Saarland"].rrule(rrule_pfingst)
rr_dict["Saarland"].rrule(rrule_fronl)
rr_dict["Saarland"].rrule(rrule_mariaeh)
rr_dict["Saarland"].rrule(rrule_einheit)
rr_dict["Saarland"].rrule(rrule_allerh)
rr_dict["Saarland"].rrule(rrule_xmas_1)
rr_dict["Saarland"].rrule(rrule_xmas_2)

rr_dict["Sachsen"] = dateutil.rrule.rruleset()
rr_dict["Sachsen"].rrule(rrule_sonntag)
rr_dict["Sachsen"].rrule(rrule_neujahr)
rr_dict["Sachsen"].rrule(rrule_karf)
rr_dict["Sachsen"].rrule(rrule_ostermo)
rr_dict["Sachsen"].rrule(rrule_mai)
rr_dict["Sachsen"].rrule(rrule_himmelf)
rr_dict["Sachsen"].rrule(rrule_pfingst)
rr_dict["Sachsen"].rrule(rrule_einheit)
rr_dict["Sachsen"].rrule(rrule_reform)
rr_dict["Sachsen"].rrule(rrule_bubt)
rr_dict["Sachsen"].rrule(rrule_xmas_1)
rr_dict["Sachsen"].rrule(rrule_xmas_2)

rr_dict["Sachsen-Anhalt"] = dateutil.rrule.rruleset()
rr_dict["Sachsen-Anhalt"].rrule(rrule_sonntag)
rr_dict["Sachsen-Anhalt"].rrule(rrule_neujahr)
rr_dict["Sachsen-Anhalt"].rrule(rrule_dreik)
rr_dict["Sachsen-Anhalt"].rrule(rrule_karf)
rr_dict["Sachsen-Anhalt"].rrule(rrule_ostermo)
rr_dict["Sachsen-Anhalt"].rrule(rrule_mai)
rr_dict["Sachsen-Anhalt"].rrule(rrule_himmelf)
rr_dict["Sachsen-Anhalt"].rrule(rrule_pfingst)
rr_dict["Sachsen-Anhalt"].rrule(rrule_einheit)
rr_dict["Sachsen-Anhalt"].rrule(rrule_reform)
rr_dict["Sachsen-Anhalt"].rrule(rrule_xmas_1)
rr_dict["Sachsen-Anhalt"].rrule(rrule_xmas_2)

rr_dict["Schleswig-Holstein"] = dateutil.rrule.rruleset()
rr_dict["Schleswig-Holstein"].rrule(rrule_sonntag)
rr_dict["Schleswig-Holstein"].rrule(rrule_neujahr)
rr_dict["Schleswig-Holstein"].rrule(rrule_karf)
rr_dict["Schleswig-Holstein"].rrule(rrule_ostermo)
rr_dict["Schleswig-Holstein"].rrule(rrule_mai)
rr_dict["Schleswig-Holstein"].rrule(rrule_himmelf)
rr_dict["Schleswig-Holstein"].rrule(rrule_pfingst)
rr_dict["Schleswig-Holstein"].rrule(rrule_einheit)
rr_dict["Schleswig-Holstein"].rrule(rrule_reform)
rr_dict["Schleswig-Holstein"].rrule(rrule_xmas_1)
rr_dict["Schleswig-Holstein"].rrule(rrule_xmas_2)

rr_dict["Thueringen"] = dateutil.rrule.rruleset()
rr_dict["Thueringen"].rrule(rrule_sonntag)
rr_dict["Thueringen"].rrule(rrule_neujahr)
rr_dict["Thueringen"].rrule(rrule_karf)
rr_dict["Thueringen"].rrule(rrule_ostermo)
rr_dict["Thueringen"].rrule(rrule_mai)
rr_dict["Thueringen"].rrule(rrule_himmelf)
rr_dict["Thueringen"].rrule(rrule_pfingst)
rr_dict["Thueringen"].rrule(rrule_kindert)
rr_dict["Thueringen"].rrule(rrule_einheit)
rr_dict["Thueringen"].rrule(rrule_reform)
rr_dict["Thueringen"].rrule(rrule_xmas_1)
rr_dict["Thueringen"].rrule(rrule_xmas_2)

