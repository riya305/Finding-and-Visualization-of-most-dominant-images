import pandas as pd
import xml.etree.ElementTree
import pickle
import networkx as nx
from importlib.machinery import SourceFileLoader




def getloc_id_mapping():
    e = xml.etree.ElementTree.parse('../devset/devset_topics.xml').getroot()
    moc1 = e.findall('topic')
    location_title = []
    location_id = []
    for moc in moc1:
        for node in moc.getiterator():
            if node.tag == 'title':
                location_title.append(node.text)
            if node.tag == 'number':
                location_id.append(node.text)
    return dict(zip(location_title, location_id))

def visualize_images_from_graph(image_id,graph_pickle):
    with open(graph_pickle,'rb') as f:
        img_img_graph = pickle.load(f)
    full_list = []
    full_list.append(image_id)
    img_list = list(img_img_graph.neighbors(image_id))
    full_list.extend(img_list)
    visualize = SourceFileLoader("visualise_images", "C:/Users/Omnipotent/Google Drive/US docs/Mission-MS/Acadamic/Fall 2018/MWD - CSE515/project/phase3/visualization/visualize.py").load_module()
    visualize.visualise_images("Awesome Test of images",full_list)

visualize_images_from_graph("8993176772",'pickles/cache/graph-20181111-185655.pkl')