#!/bin/bash
# install openjpeg

archive=openjpeg-2.3.1

./download-and-extract.sh $archive https://raw.githubusercontent.com/python-pillow/pillow-depends/503ff2ff53e2f0446aa06a4a6c6cb17361b108e2/$archive.tar.gz

pushd $archive

cmake -DCMAKE_INSTALL_PREFIX=/usr . && make -j4 && sudo make -j4 install

popd
