import json
import os
import tempfile
from zipfile import ZipFile

import pandas as pd
import requests
from dateutil.parser import parse as parsedate
from osgeo import ogr, osr
from rarfile import RarFile


class FileService:
    def get_remote_file_last_mod_date(self, url):
        try:
            last_modified = requests.head(url, verify=False) \
                .headers['Last-Modified']
        except Exception:
            last_modified = requests.get(url, verify=False) \
                .headers['Last-Modified']

        return parsedate(last_modified)

    def unzip_file(self, filepath, temp_dir=None):
        if temp_dir:
            dir = temp_dir
        else:
            dir = os.path.dirname(filepath)
        with ZipFile(filepath, 'r') as zip:
            zip.printdir()
            zip.extractall(path=dir)
            files = []
            for f in zip.filelist:
                path = f'{dir}{os.path.sep}{f.filename}'
                files.append(path)
        return files

    def unrar_file(self, filepath, temp_dir=None):
        if temp_dir:
            dir = temp_dir
        else:
            dir = os.path.dirname(filepath)
        with RarFile(filepath, 'r') as rar:
            rar.printdir()
            rar.extractall(path=dir)
            files = []
            for f in rar.namelist():
                path = f'{dir}{os.path.sep}{f}'
                files.append(path)
        return files

    def read_vector_file(self, file_path, iterate=False, epsg=4326):
        dataSource = ogr.Open(file_path)
        layer = dataSource.GetLayer()

        source_sr = layer.GetSpatialRef()
        target_sr = osr.SpatialReference()
        target_sr.ImportFromEPSG(epsg)

        coord_trans = osr.CoordinateTransformation(source_sr, target_sr)

        entries = []
        for feature in layer:
            geometry = feature.GetGeometryRef()

            if geometry and epsg:
                geometry.Transform(coord_trans)

            entry = json.loads(feature.ExportToJson())
            if iterate:
                yield entry
            else:
                entries.append(entry)

        if not iterate:
            return entries

    def read_csv(self, file_path, sep=None, decimal=None, encoding='utf-8',
                 iterate=False, chunksize=10000):
        entries = []
        with pd.read_csv(file_path, sep=sep,
                         decimal=decimal,
                         encoding=encoding,
                         chunksize=chunksize) as reader:

            for df in reader:
                df = df.where(pd.notnull(df), None)

                for index, row in df.iterrows():
                    if iterate:
                        yield row
                    else:
                        entries.append(row)

        if not iterate:
            return entries

    def download_file(self, url, filename):
        response = requests.get(url, verify=False)
        bytes = response.content
        temp_directory = tempfile.gettempdir()
        path = f'{temp_directory}{os.path.sep}{filename}'
        file = open(path, 'wb')
        file.write(bytes)
        file.close()
        return path
