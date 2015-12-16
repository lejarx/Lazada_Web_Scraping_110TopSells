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
