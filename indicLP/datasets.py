# coding:utf-8
from urllib import request, parse
from os import getcwd, listdir, mkdir, path as _path, walk
import pathlib
import tarfile
import codecs
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

csv_datasets = [{
            "name":"bbc_hindi",
            "url":"https://github.com/NirantK/hindi2vec/releases/download/bbc-hindi-v0.1/bbc-hindiv01.tar.gz",
            "source":"github",
            "sep":"\t"
        },
        {
            "name":"tamil-news-classification",
            "url":"vijayabhaskar96/tamil-news-classification-dataset-tamilmurasu",
            "source":"kaggle",
            "sep":","
        },
        {
            "name":"hindi-nli",
            "url":"https://github.com/midas-research/hindi-nli-data/tree/master/Classification",
            "source":"github"
        }]
csv_names = [name["name"] for name in csv_datasets]

corpus_data = [
                {
                    "name":"ponniyin-selvan",
                    "url":"rahulvks/ponniyin-selvan",
                    "source":"kaggle"
                },
            ]

corpus_names = [name["name"] for name in corpus_data]
class Dataset:
    def __init__(self):
        self.location = getcwd()        

    def extractGz(self, filepath, folder):
        print("Extracting gz file to datasets folder")
        file = tarfile.open(filepath)
        file.extractall("./datasets\\"+ folder)
        file.close()

    def getDetails(self, dataset):
        for data in csv_datasets:
            if data["name"] == dataset:
                return data
        for data in corpus_data:
            if data["name"] == dataset:
                return data
    def downloadFromKaggle(self, url, name):
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(url,"./datasets\\")
        mkdir("./datasets\\"+name)
        zf = zipfile.ZipFile("./datasets\\"+name+".zip")
        zf.extractall("./datasets\\"+name)
        zf.close()

    def downloadDataset(self, dataset):
        assert dataset in csv_names or dataset in corpus_names, "Dataset not supported, supported datasets" + "Datasets: "+str(csv_names) + "\nCorpus: "+ str(corpus_names)
        # downloadData = {}
        downloadData = self.getDetails(dataset)
        url = downloadData["url"]
        print ("Downloading dataset: "+dataset+" from "+url)
        if downloadData["source"] == "kaggle":
            self.downloadFromKaggle(url, dataset)
        else:
            file_path = parse.urlparse(url).path
            file_name = pathlib.PurePath(file_path).name
            filename, headers = request.urlretrieve(url, filename=self.location + "\\datasets\\"+file_name)
            print(filename)
            if pathlib.Path(filename).suffix == ".gz":
                self.extractGz(filename, dataset)
            print ("download complete!")


    def list_datasets(self):
        for key in srcs.keys:
            print(key + " "+ srcs.key)
    
    def load_corpus(self, dataset):
        assert dataset in corpus_data
    
    def load_dataset(self, dataset_name, combine = False):
        assert dataset_name in csv_names or dataset_name in corpus_names, "Dataset not supported, supported datasets" + "Datasets: "+str(csv_names) + "\nCorpus: "+ str(corpus_names)
        path = self.location + "\\datasets\\" + dataset_name
        details = self.getDetails(dataset_name)
        if not pathlib.Path(path).exists():
            print("Dataset not downloaded, do you want to download it (y/n)")
            resp = input()
            if resp == 'y' or resp == 'Y':
                self.downloadDataset(dataset_name)
            else:
                print("Dataset unavailable, try another dataset")
                return
        if dataset_name in csv_names:
            for files in listdir(path):
                if files.endswith(".csv"):
                    pd_dataset = pd.read_csv(str(path+"\\"+files), sep = details["sep"])
                    return pd_dataset
                        # if files.find("train") != -1:
                        # print(path+"\\"+files)
                        # tempfile = open(path+"\\"+files, encoding="utf-8") 
                        # line = tempfile.readline()
                        # print(line);
                        # sep = csv.Sniffer().sniff(line).escapechar
                        # print("Sep "+details["sep"])
                        # train = pd.read_csv(str(path+"\\"+files),sep = '\t')
                        # print(train.head())
                    # if files.find("test") != -1:
                        # test = pd.read_csv(str(path + "\\" + files),sep='\t')
                        # print(test.head())
        else:
            if combine:
                if dataset_name+"_combine.txt" in listdir(path):
                    return [path+"\\"+dataset_name+"_combine.txt"]
                self.combineFiles(path, dataset_name)
                return [path+"\\"+dataset_name+"_combine.txt"]
            else:
                path_list = []
                for root, dirs, files in walk(path):
                    for file in files:
                        if file.endswith(".txt"):
                            path_list.append(_path.join(root, file))
                return path_list

    def combineFiles(self, path, dataset_name):
        combine = codecs.open("datasets\\"+dataset_name+"\\"+dataset_name+"_combine.txt","w+","utf-8")
        for root, dirs, files in walk(path):
            for file in files:
                if file.endswith(".txt"):
                    f = open(_path.join(root, file), encoding='utf-8')
                    content = f.read()
                    combine.write(content)
                    f.close()
        combine.close()

                

if __name__ == "__main__":
    dt = Dataset()
    data = dt.load_dataset("ponniyin-selvan",True)
    if isinstance(data, pd.DataFrame):
        print(data.head())
    else:
        print(data)