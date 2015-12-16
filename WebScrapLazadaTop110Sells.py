# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 08:05:42 2015
@python_version Python3

@context: MaGIC Analytics 
@prof: goh.yongkheng_at_gmail.com
@author: chejoharia

@purpose: WebScraping Excercise
@         - Extract Lazada Daily Top 110 top sellers
@input      : http://www.lazada.com.my/highlights-top-sellers/?page=1'	
@output     : a tab delimted dataset in txt file of today's 110 top selling items
"""

############################################################
#
# Using Python3
# python3 ./WebScrapLazadaTop110Sells.py
#
############################################################

import time
import io
from urllib.request import urlopen
from bs4 import BeautifulSoup


############################################################
#
# Prepare a tab delimited file to store the data
#
############################################################

# date in YYYYMMDD format
# append date to filename
filename = 'Lazada_Top_Sellers' + time.strftime('%Y%m%d') + '.txt'

# use io.open() to avoid Unicode
f = io.open(filename,'w', encoding='utf8')

# write variable names
f.write('day-ranking'
	+'\t'+'product-sku'
	+'\t'+'product-name'
	+'\t'+'price-normal'
	+'\t'+'price-discount'
	+'\t'+'discount'+'\n')

   
############################################################
#
# Scrap data from Lazada web pages
# - iterate 4 different pages to get all top 110 selling products
#
############################################################

for x in range(1,5):
	url = 'http://www.lazada.com.my/highlights-top-sellers/?page='+str(x)	
	page = urlopen(url)
	bs_page = BeautifulSoup(page,'lxml')

	catalog_content = bs_page.find('div',class_='catalog-content-wrapper')
	products = catalog_content.find_all('div', class_='product-description')

	# Write products to file
	for product in products:
		# check for price-normal
		if product.find("span",class_='product-price-normal').string is None:
			price_normal = ''
		else:
			price_normal = product.find("span",class_='product-price-normal').string
		# check for price-discount
		if product.find("span",class_='product-price-discount') is None:
			price_discount = ''
		else:
			price_discount = product.find("span",class_='product-price-discount').string
		# check for product-discount
		if product.find("div",class_='product-discount') is None:
			product_discount = ''
		else:
			product_discount = product.find("div",class_='product-discount').string

		f.write(product.a['data-position']
		+'\t'+product.a['data-sku']
		+'\t'+product.img['alt']
		+'\t'+price_normal
		+'\t'+price_discount
		+'\t'+product_discount+'\n')

############################################################
#
# Close file
#
############################################################

f.close()
