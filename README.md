# vmwaretooocpv

(alpha readme - 5-22-24 )

## What is it?
A small Python Pandas script to analyze RRV Tool output and (eventually) make architecture suggestions for creating a 1:1 OpenShift Virtualization environment.  This will assist in planning a new environment to migrate Virtual Machines from VSphere over to OpenShift Virtualization.

## What does it do?
Takes standard CSV from RRV Tool Output and summarizes it, generates summary data in PDF.

## Planned features
Output suggested architecture for Red Hat OpenShift Virtualization Clusters based on existing VMWare cluster data.

## Instructions
Within the repo directory (assuming you've git cloned this repo)

1. Create a python 3 venv
```
python3 -m venv venv
```

2. Source new env

```
source venv/bin/activate
```

3. Install requirements to venv

```
pip install -r requirements.txt
```

4. Save RRV Output
```
Save "sheet2" from RRV Tools output as CSV named "vsphere-hosts.csv" within repo dir.
```

5. Run The Python Script

```
./analyze.py
```

6. Review text output and the newly generated analysis.pdf file
