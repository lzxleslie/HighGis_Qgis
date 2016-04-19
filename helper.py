import urllib  
import httplib2 
import json
import qgis.core

from qgis.core import (QgsVectorLayer, QgsMapLayerRegistry, QgsFeature, QgsGeometry, QgsPoint, QgsField)
from PyQt4 import QtCore
def httpRequestGet(url):
    httpconn = httplib2.Http()
    response, content = httpconn.request(url, 'GET')
    return content
def saveHttpData(url,filename):
    content = httpRequestGet(url)
    m_file = open(filename,"w")
    m_file.write(content)
    m_file.close()    
def httpRequestPost(data):
    data_json = json.dumps(data)
    req = urllib2.Request(url,data_json)
    response_stream = urllib2.urlopen(req)
    res = response_stream.read() 
    return res
def addJsonVectorLayer(data_source,layer_name,iface):
    return iface.addVectorLayer(data_source,layer_name,"ogr")
def get_vector_layers(iface):
    """Returns all the opened vector layers"""
    layers = iface.legendInterface().layers()
    vector_layers = []

    for layer in layers:
        print layer.id()
        layerType = layer.type()
        if layerType == qgis.core.QgsMapLayer.VectorLayer:
            vector_layers.append(layer)
    return vector_layers