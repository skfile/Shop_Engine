from django.db import models
from django.utils import timezone


class site(models.Model):
    CATEGORY = (
        ('Shopify', 'Shopify'),
        ('WooCommerce', 'WooCommerce'),
        ('BigCommerce', 'BigCommerce'),
        ('Demandware', 'Demandware'),
    )
    Website_Name = models.CharField(max_length=200, null=True)
    Website_Type = models.CharField(
        max_length=200, null=True, choices=CATEGORY)

    Product_Page_URL_p1 = models.CharField(max_length=300, null=True)
    Number_of_Pages = models.CharField(max_length=200, null=True)
    Product_Page_URL_p2_ifneeded = models.CharField(max_length=200, null=True)

    Product_HTMLCard_Path_Type = models.CharField(max_length=200, null=True)
    Product_HTMLCard_Path_Class = models.CharField(max_length=200, null=True)

    Container_Name_Path_Type = models.CharField(max_length=200, null=True)
    Container_Name_Path_Class = models.CharField(max_length=200, null=True)
    Container_Price_Path_Type = models.CharField(max_length=200, null=True)
    Container_Price_Path_Class = models.CharField(max_length=200, null=True)
    Container_Product_URL_Path_Type = models.CharField(
        max_length=200, null=True)
    Container_Product_URL_Path_Class = models.CharField(
        max_length=200, null=True)
    Container_Product_Tags_Path_Type = models.CharField(
        max_length=200, null=True)
    Container_Product_Tags_Path_Class = models.CharField(
        max_length=200, null=True)

    Root_URL = models.CharField(max_length=400, null=True)
    Container_Image_URL_Path_Type = models.CharField(max_length=200, null=True)
    Container_Image_URL_Path_Class = models.CharField(
        max_length=200, null=True)

    # add product tags too!!!

    def __str__(self):
        return self.Website_Name


class crawledData(models.Model):

    Product_Name = models.CharField(max_length=400, null=True)
    Product_Price = models.CharField(max_length=200, null=True)
    Product_Link = models.CharField(max_length=500, null=True)
    Product_Image_Link = models.CharField(max_length=500, null=True)
    Product_Website_Name = models.CharField(max_length=300, null=True)
    Product_Tags = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.Product_Name

    class Meta:
        # ordering = ['name']
        pass

    class Admin:
        pass
