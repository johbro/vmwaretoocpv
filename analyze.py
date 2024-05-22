#!/usr/bin/env python
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



def makePDF(hosts):
# plots/graphs to a PDF
# accepts a pandas dataframe as argument

    with PdfPages('analysis.pdf') as pdf:
        #hosts per cluster
        hostfig = hosts["vHostCluster"].value_counts().plot(kind='bar', figsize=(20, 25), xlabel="Clusters", ylabel="Hosts", title="Hosts Per Cluster").get_figure()
        pdf.savefig(hostfig)
        #cpus per cluster
        cpufig = hosts.groupby("vHostCluster")['vHostNumCpuCores'].sum().plot(kind='bar', figsize=(20, 25), xlabel="Clusters", ylabel="Total Cores", title="Cores Per Cluster").get_figure()
        pdf.savefig(cpufig)
        #memory per cluster
        memfig = hosts.groupby("vHostCluster")['vHostMemInGB'].sum().plot(kind='bar', figsize=(20, 25), xlabel="Clusters", ylabel="Memory in GB", title="Memory (in GB) Per Cluster").get_figure()
        pdf.savefig(memfig)


def summarizeData():
# reads CSV and returns pandas dataframe
    hosts = pd.read_csv("vsphere-hosts.csv")
    formattedVMs = pd.DataFrame(hosts)

    #create a column of memory in GB
    hosts["vHostMemInGB"] = hosts["vHostMemorySize"] / 1000

    print("\n Analysing ", hosts["vHostCluster"].nunique(), " clusters")
    print("\nHosts per cluster:\n")
    print(hosts["vHostCluster"].value_counts())
    print("Total Hosts:",hosts["vHostName"].value_counts().sum())
    print("\n Cores Per Cluster:\n")
    print(hosts.groupby("vHostCluster")['vHostNumCpuCores'].sum())
    print("\n Memory(in GB) Per Cluster:\n")
    print(hosts.groupby("vHostCluster")['vHostMemInGB'].sum())
    return(hosts)


if __name__ == '__main__':
    data = summarizeData()
    makePDF(data)



