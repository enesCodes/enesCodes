import csv  # https://docs.python.org/3/library/csv.html


# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:


        catg, created = Category.objects.get_or_create(name=row[7])
        region, created = Region.objects.get_or_create(name=row[9])
        state, created = State.objects.get_or_create(name=row[8])
        isoo, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            longt = float(row[4])
        except:
            longt = None

        try:
            latt = float(row[5])
        except:
            latt = None

        try:
            areah = float(row[6])
        except:
            areah = None


        site = Site(name=row[0],description=row[1],justification=row[2],year=y,longitude=longt,latitude=latt,area_hectares=areah,category=catg,region=region,state=state,iso=isoo)
        site.save()
        catg.save()
        region.save()
        state.save()
        isoo.save()








