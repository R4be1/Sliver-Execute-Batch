# Sliver-Execute-Batch

# build dependencies
```
sudo apt-get install build-essential python3-dev libssl-dev
```

# install sliver-py first, we will be over-writing the grpc version from source
```
pip install sliver-py
```

# install grpc from source
```
git clone https://github.com/grpc/grpc
cd grpc
git submodule update --init
pip install -r requirements.txt
pip uninstall protobuf
pip install protobuf==3.20.*
GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=True GRPC_PYTHON_BUILD_WITH_CYTHON=1 pip install .
```
