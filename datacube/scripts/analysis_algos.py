# Example usage - 
# RVI('ls8_ledaps_albers', 213539.9, 218463.5, 3433466.7, 3438883.6, 2015)
%matplotlib inline
import datacube
import numpy
from datetime import datetime
from datacube.analytics.analytics_engine import AnalyticsEngine
from datacube.execution.execution_engine import ExecutionEngine
from datacube.analytics.utils.analytics_utils import plot

dc = datacube.Datacube(config="/home/rishabh/.datacube.conf")

def RVI (product, x1, x2, y1, y2, year):
    a = AnalyticsEngine()
    e = ExecutionEngine()
    #assert product
    #dc.list_products() is pandas dataframe, .loc[:]['name'] selects
    #   the products is a pandas series. values is array
    assert (product in dc.list_products().loc[:]['name'].values), "Product not in database"
    
    # 2 index for platform, 3 for product type
    for prod  in dc.list_products().loc[:].values:
        if(product == prod[0]):
            platform = prod[2]
            product_type = prod[3]
    
    # assert time
    la = dc.load(product=product, x = (x1, x2),y = (y1, y2))
    # this is date of product (la.items()[0])[1].values[0]
    date_of_prod = (la.items()[0])[1].values[0]
    #this is numpy.datetime64
    
    # TO DO COMPARE numpy.datetime64 with datetime.datetime    
    #assert (date_of_prod >= time1 and date_of_prod <= time2), "Product not in the provided time"
    
    
    time1 = datetime(year, 1, 1)
    time2 = datetime(year, 12, 31)
    # calculate output
    dimensions = {'x':    {'range': (x1, x2)},
                  'y':    {'range': (y1, y2)},
                  'time': {'range': (time1, time2)}}
    
    # create arrays
    b40 = a.create_array((platform, product_type), ['nir'], dimensions, 'b40')
    b30 = a.create_array((platform, product_type), ['red'], dimensions, 'b30')
    
    #ratio vegetation index
    rvi = a.apply_expression([b40, b30], '(array1 / array2)', 'rvi')
    
    e.execute_plan(a.plan)
    
    #result x array
    res = e.cache['rvi']['array_result']['rvi']
    
    res.plot()
    
    
# Transformed vegetation index
def TVI (product, x1, x2, y1, y2, year):
    a = AnalyticsEngine()
    e = ExecutionEngine()
    #assert product
    #dc.list_products() is pandas dataframe, .loc[:]['name'] selects
    #   the products is a pandas series. values is array
    assert (product in dc.list_products().loc[:]['name'].values), "Product not in database"
    
    # 2 index for platform, 3 for product type
    for prod  in dc.list_products().loc[:].values:
        if(product == prod[0]):
            platform = prod[2]
            product_type = prod[3]
    
    # assert time
    la = dc.load(product=product, x = (x1, x2),y = (y1, y2))
    # this is date of product (la.items()[0])[1].values[0]
    date_of_prod = (la.items()[0])[1].values[0]
    #this is numpy.datetime64
    
    # TO DO COMPARE numpy.datetime64 with datetime.datetime    
    #assert (date_of_prod >= time1 and date_of_prod <= time2), "Product not in the provided time"
    
    
    time1 = datetime(year, 1, 1)
    time2 = datetime(year, 12, 31)
    # calculate output
    dimensions = {'x':    {'range': (x1, x2)},
                  'y':    {'range': (y1, y2)},
                  'time': {'range': (time1, time2)}}
    
    # create arrays
    b40 = a.create_array((platform, product_type), ['nir'], dimensions, 'b40')
    b30 = a.create_array((platform, product_type), ['red'], dimensions, 'b30')
    
    #ratio vegetation index
    tvi = a.apply_expression([b40, b30], '(sqrt(((array1 - array2) / (array1 + array2)) + 0.5) * 100)', 'tvi')
    
    e.execute_plan(a.plan)
    
    #result x array
    res = e.cache['tvi']['array_result']['tvi']
    
    res.plot()
