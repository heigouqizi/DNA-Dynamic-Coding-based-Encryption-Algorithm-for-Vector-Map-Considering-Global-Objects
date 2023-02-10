import ogr,sys,os

def Get_XY_fromshp(ori_shp):
    ds = ogr.Open(ori_shp, 0)
    if ds is None:
        sys.exit('Could not open {0}.'.format(ori_shp))
    layer = ds.GetLayer(0)
    feature_num = layer.GetFeatureCount(0)
    X, Y, Points = [], [], []
    for i in range(layer.GetFeatureCount(0)):
        feature = layer.GetFeature(i)
        geometry = feature.GetGeometryRef()
        if geometry.GetGeometryName() == 'POLYGON':
            geometry = geometry.GetGeometryRef(0)
        x, y = [0]*geometry.GetPointCount(), [0]*geometry.GetPointCount()
        for j in range(geometry.GetPointCount()):
            x[j] = geometry.GetX(j)
            y[j] = geometry.GetY(j)
        # X.append(x), Y.append(y)
        # Points.append([float(x[0]), float(y[0])])
        Points.append([(x[i], y[i]) for i in range(len(x))])
    ds.Destroy()
    return feature_num, Points

def write_encrytpion_shp(ori_shp,outputfile, Points):
    n_X, n_Y = [], []
    for feature in Points:
        n_X.append([point[0] for point in feature])
        n_Y.append([point[1] for point in feature])
    ds = ogr.Open(ori_shp, 0)
    if ds is None:
        sys.exit('Could not open {0}.'.format(ori_shp))
    '''1.创建数据源'''
    driver = ogr.GetDriverByName("ESRI Shapefile")
    if os.access( outputfile, os.F_OK ):
        driver.DeleteDataSource(outputfile)
    '''2.复制一个新的图层'''
    layer = ds.GetLayer(0)
    newds = driver.CreateDataSource(outputfile)
    pt_layer  = newds.CopyLayer(layer, 'a') # 第1个参数是OGR的Layer对象，第2个参数是要生成图层的名称。对于Shapefile来说，这个名称是没有用的，但必须给这个字符串赋变量值。
    # pt_layer  = newds.CreateLayer('wm_gis_osm_railways_free_1', None,ogr.wkbLineString)
    newds.Destroy()
    nds = ogr.Open(outputfile, 1)
    nlayer = nds.GetLayer(0)
    for i in range(nlayer.GetFeatureCount(0)):
        feature = nlayer.GetFeature(i)
        # geometry = feature.GetGeometryRef().GetGeometryRef(0)
        geometry = feature.GetGeometryRef()
        if geometry.GetGeometryName() == 'POLYGON':
            geometry = geometry.GetGeometryRef(0)        
        for k in range(geometry.GetPointCount()):            
            geometry.SetPoint_2D(k, n_X[i][k], n_Y[i][k])
        nlayer.SetFeature(feature)
    nds.Destroy()




# os.chdir('001 Experiments/.code/0 Paper Code/dna_encoding/china-latest-free.shp/')
# ori_shp, new_shp = 'water_henan.shp', 'results/water_henan_new.shp'
# feature_num, Points = Get_XY_fromshp(ori_shp)
# write_encrytpion_shp(ori_shp, new_shp, Points)
