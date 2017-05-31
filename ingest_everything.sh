#!/bin/bash
#datacube product add ~/datacube-iirs/docs/config_samples/dataset_types/ls5_scenes.yaml

datacube product add ~/datacube-iirs/docs/config_samples/dataset_types/ls7_scenes.yaml
datacube product add ~/datacube-iirs/docs/config_samples/dataset_types/ls8_scenes.yaml
datacube product add ~/datacube-iirs/docs/config_samples/dataset_types/Cartosat_Def.yaml
#datacube dataset add LT* -a
datacube dataset add LE* -a
datacube dataset add CS10* -a
datacube dataset add LS* -a
#datcube dataset add LT*/*NDVI* -a
datcube dataset add LS*/*NDVI* -a
datcube dataset add LE*/*NDVI* -a
datcube dataset add LT*/*LST* -a
datcube dataset add LS*/*LST* -a
datcube dataset add LE*/*LST* -a

datacube ingest -c ~/datacube-iirs/docs/config_samples/ingester/ls5_lst.yaml
datacube ingest -c ~/datacube-iirs/docs/config_samples/ingester/ls7_lst.yaml
datacube ingest -c ~/datacube-iirs/docs/config_samples/ingester/ls8_lst.yaml
datacube ingest -c ~/datacube-iirs/docs/config_samples/ingester/ls7_ndvi.yaml
datacube ingest -c ~/datacube-iirs/docs/config_samples/ingester/ls8_ndvi.yaml
datacube ingest -c ~/datacube-iirs/docs/config_samples/ingester/ls8_ledaps_albers.yaml
datacube ingest -c ~/datacube-iirs/docs/config_samples/ingester/ls7_ledaps_albers.yaml
datacube ingest -c ~/datacube-iirs/docs/config_samples/ingester/Cartosat_Ingest.yaml
