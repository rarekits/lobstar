from zipfile import ZipFile
from xml.etree.ElementTree import parse

__author__ = 'romilly'


def extract_net(filename):
    with ZipFile('%s.fzz' % filename) as zip:
        with zip.open('%s.fz' % filename) as fritzed:
            tree = parse(fritzed)
            elem = tree.getroot()

    instances =  elem.find('instances').findall('instance')
    for instance in instances:
        print instance.attrib['moduleIdRef'],instance.attrib['modelIndex']
        # views = instance.find('views')
        # if views is not None:
        #     breadboard_view = views.find('breadboardView')
        #     if breadboard_view is not None:
        #         connectors = breadboard_view.find('connectors')
        #         if connectors is not None:
        #             for connector in connectors.findall('connector'):
        #                 connect_attributes = connector.find('connects').find('connect').attrib
        #                 print connect_attributes['modelIndex'],connect_attributes['connectorId']

extract_net('test1')



