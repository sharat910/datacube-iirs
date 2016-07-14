import subprocess
import sys
import glob

gitpath = "~/datacube-iirs/"
path = (sys.argv)[1]

print "adding products for ls5, 7, 8, cartosat"

cmd = "datacube product add " + gitpath+"docs/config_samples/dataset_types/ls5_scenes.yaml"
print cmd
subprocess.call(cmd, shell = True)

cmd = "datacube product add " + gitpath+"docs/config_samples/dataset_types/ls7_scenes.yaml"
print cmd
subprocess.call(cmd, shell = True)

cmd = "datacube product add " + gitpath+"docs/config_samples/dataset_types/ls8_scenes.yaml"
print cmd
subprocess.call(cmd, shell = True)

cmd = "datacube product add " + gitpath+"docs/config_samples/dataset_types/Cartosat_Def.yaml"
print cmd
subprocess.call(cmd, shell = True)

print "added products for ls5, 7, 8, cartosat"

#################
#print "Ingesting LS8 Reflectance"
#print "adding datasets for landsat 8 reflectance"
#ls8 = glob.glob("LC8*")
#
#for ls8re in ls8:
#    finalpath = path+ls8re+"/"
#    cmd = "datacube dataset add " + finalpath + " -a"
#    print cmd
#    #subprocess.call(cmd, shell = True)
#
#print "ingesting landsat 8 reflectance"
#cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls8_ledaps_albers.yaml"
#print cmd
#subprocess.call(cmd, shell = True)
#print "Successfully ingested Landsat 8 reflectance"
##################

#################
print "Ingesting LS8 LST"
print "adding datasets for landsat 8 LST"
ls8 = glob.glob("LC8*")

for ls8re in ls8:
    lst = glob.glob(ls8re+"/*LST*")[0]
    finalpath = path+lst+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting landsat 8 LST"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls8_lst.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested Landsat 8 LST"
##################


#################
print "Ingesting LS8 NDVI"
print "adding datasets for landsat 8 NDVI"
ls8 = glob.glob("LC8*")

for ls8re in ls8:
    ndvi = glob.glob(ls8re+"/*NDVI*")[0]
    finalpath = path+ndvi+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting landsat 8 NDVI"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls8_ndvi.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested Landsat 8 NDVI"
##################

#################
print "Ingesting LS7 Reflectance"
print "adding datasets for landsat 7 reflectance"
le7 = glob.glob("LE7*")

for le7re in le7:
    finalpath = path+le7re+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting landsat 7 reflectance"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls7_ledaps_albers.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested Landsat 7 reflectance"
##################

#################
print "Ingesting LE7 LST"
print "adding datasets for landsat 7 LST"
le7 = glob.glob("LE7*")

for le7re in le7:
    lst = glob.glob(le7re+"/*LST*")[0]
    finalpath = path+lst+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting landsat 7 LST"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls7_lst.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested Landsat 7 LST"
##################


#################
print "Ingesting LE7 NDVI"
print "adding datasets for landsat 7 NDVI"
le7 = glob.glob("LE7*")

for le7re in le7:
    ndvi = glob.glob(le7re+"/*NDVI*")[0]
    finalpath = path+ndvi+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting landsat 7 NDVI"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls7_ndvi.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested Landsat 7 NDVI"
##################


#################
print "Ingesting LT5 Reflectance"
print "adding datasets for landsat 5 reflectance"
lt5 = glob.glob("LT5*")

for lt5re in lt5:
    finalpath = path+lt5re+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting landsat 5 reflectance"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls5_ledaps_albers.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested Landsat 5 reflectance"
##################

#################
print "Ingesting LT5 LST"
print "adding datasets for landsat 5 LST"
lt5 = glob.glob("LT5*")

for lt5re in lt5:
    lst = glob.glob(lt5re+"/*LST*")[0]
    finalpath = path+lst+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting landsat 5 LST"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls5_lst.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested Landsat 5 LST"
##################


#################
print "Ingesting LT5 NDVI"
print "adding datasets for landsat 5 NDVI"
le7 = glob.glob("LT5*")

for lt5re in lt5:
    ndvi = glob.glob(lt5re+"/*NDVI*")[0]
    finalpath = path+ndvi+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting landsat 5 NDVI"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/ls5_ndvi.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested Landsat 5 NDVI"
##################


#################
print "Ingesting Cartosat Data. Skipping 43 Zone data"
print "adding datasets for cartosat"
crt = glob.glob("CS10*")

for crtre in crt:
    finalpath = path+crtre+"/"
    cmd = "datacube dataset add " + finalpath + " -a"
    print cmd
    subprocess.call(cmd, shell = True)

print "ingesting cartosat data"
cmd = "datacube ingest -c " + gitpath+"docs/config_samples/ingester/Cartosat_Ingest.yaml"
print cmd
subprocess.call(cmd, shell = True)
print "Successfully ingested cartosat data"
##################
print "Successfully ingested all the data!!!"
