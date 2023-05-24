# Charmed Openstack Upgrade plugin

## Quick Start
```bash
source novarc
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install -e .
```

## Result
```
(venv) miles@t14:~/repo/python-charmedupgradeclient$ openstack charm upgrade prep 1
upgrade prep called with 1
client.foo = foo
```