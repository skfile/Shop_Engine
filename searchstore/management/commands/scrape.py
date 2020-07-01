from django.core.management.base import BaseCommand
from urllib.request import urlopen
import lxml
from bs4 import BeautifulSoup
import json
import requests
# from progress.bar import Bar
from searchstore.admin import *
from searchstore.models import *


class Command(BaseCommand):
    # help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):

        crawledData.objects.all().delete()

        # bar = Bar('Processing')

        for x in site.objects.all():

            pages = range(1, int(x.Number_of_Pages) + 1)
            # pages = range(1, 2)

            for page in pages:

                # bar.next()
                page = requests.get(x.Product_Page_URL_p1 +
                                    str(page) + x.Product_Page_URL_p2_ifneeded)

                soup = BeautifulSoup(page.text, 'lxml')

                producthtml = soup.find_all(
                    x.Product_HTMLCard_Path_Type, class_=x.Product_HTMLCard_Path_Class)

                for container in producthtml:

                    notEnterCHECKER = True

                    name = container.find(
                        x.Container_Name_Path_Type, class_=x.Container_Name_Path_Class).text

                    price = str(container.find(
                        x.Container_Price_Path_Type, class_=x.Container_Price_Path_Class).text)

                    producturl = x.Root_URL + container.find(
                        x.Container_Product_URL_Path_Type, class_=x.Container_Product_URL_Path_Class)['href']

                    producttag = container.find(
                        x.Container_Product_Tags_Path_Type, class_=x.Container_Product_Tags_Path_Class).text

                    tempPage = requests.get(producturl)
                    tempsoup = BeautifulSoup(tempPage.text, 'lxml')
                    # for y in tempsoup.findAll('img'):
                    #     if y.get(x.Container_Image_URL_Path_Class) != None:
                    #         tempimageurl = y.get(
                    #             x.Container_Image_URL_Path_Class)
                    #         tempindex = tempimageurl.find("?")
                    #         imageurl = tempimageurl[0:tempindex]
                    #         break

                    if tempsoup.findAll('img')[0].get(
                            x.Container_Image_URL_Path_Class) != None:
                        imageurl = tempsoup.findAll('img')[0].get(
                            x.Container_Image_URL_Path_Class)  # KINA WORKS
                    else:
                        imageurl = None

                    # tempimageurls = []
                    # for a in tempsoup.findAll('img'):
                    #     checker = a.get(x.Container_Image_URL_Path_Class)
                    #     if checker != None:
                    #         tempimageurls.append(checker)
                    # imageurl = tempimageurls[0]

                    if imageurl == None:
                        imageurl = ""
                        # notEnterCHECKER = False  # sadly temporary

                    if imageurl == "":
                        notEnterCHECKER = False

                    if producttag.find("Gift") > 0:
                        notEnterCHECKER = False

                    website_name = x.Website_Name

                    if notEnterCHECKER == True:
                        crawledData.objects.create(
                            Product_Name=name,
                            Product_Price=price,
                            Product_Link=producturl,
                            Product_Image_Link=imageurl,
                            Product_Website_Name=website_name,
                            Product_Tags=producttag
                        )
                        self.stdout.write('%s added' % (name))
        # bar.finish()
        self.stdout.write('job complete')

        # try:
        #     # save in db
        #     crawledData.objects.create(
        #         Product_Name=name,
        #         Product_Price=price,
        #         Product_Link=producturl,
        #         Product_Image_Link=imageurl,
        #         Product_Website_Name=website_name
        #     )

        #     self.stdout.write('%s added' % (price))
        # except:
        #     self.stdout.write('%s already exists' % (price))

        # #     print('%s added' % (name,))
        # # except:
        # #     print('%s already exists' % (name,))
