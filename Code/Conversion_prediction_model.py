#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:29:32 2019

@author: mayur
"""

import pandas as pd

train = pd.read_csv('/Users/mayur/Documents/GitHub/Conversion_modeling'+
                    '/GA-conversion-modeling/Data/newtrain.csv')

trial_data = train.iloc[:10000,:]

# checking number of unique visitor ids

unique_visitors = list(trial_data.fullVisitorId.unique())
uniq

dict_channelGrouping = dict(enumerate(trial_data['channelGrouping'].astype(
        'category').cat.categories))

dict_socialEngagementType = dict(enumerate(
        trial_data['socialEngagementType'].astype('category').cat.categories))

dict_deviceBrowser = dict(enumerate(
        trial_data['device.browser'].astype('category').cat.categories))

dict_deviceCategory = dict(enumerate(
        trial_data['device.deviceCategory'].astype('category').cat.categories))

dict_isMobile = dict(enumerate(
        trial_data['device.isMobile'].astype('category').cat.categories))

dict_operatingSystem = dict(enumerate(
        trial_data['device.operatingSystem'].astype('category').cat.categories))

dict_city = dict(enumerate(
        trial_data['geoNetwork.city'].astype('category').cat.categories))

dict_continent = dict(enumerate(
        trial_data['geoNetwork.continent'].astype('category').cat.categories))

dict_country = dict(enumerate(
        trial_data['geoNetwork.country'].astype('category').cat.categories))

dict_networkDomain = dict(enumerate(
        trial_data['geoNetwork.networkDomain'].astype('category').cat.categories))

dict_subContinent = dict(enumerate(
        trial_data['geoNetwork.subContinent'].astype('category').cat.categories))

dict_medium = dict(enumerate(
        trial_data['trafficSource.medium'].astype('category').cat.categories))

dict_medium = dict(enumerate(
        trial_data['trafficSource.medium'].astype('category').cat.categories))

dict_source = dict(enumerate(
        trial_data['trafficSource.source'].astype('category').cat.categories))

enumerate(trial_data.columns)















