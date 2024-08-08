#!/bin/bash
# install webp

archive=libwebp-1.1.0

./download-and-extract.sh $archive https://raw.githubusercontent.com/python-pillow/pillow-depends/503ff2ff53e2f0446aa06a4a6c6cb17361b108e2/$archive.tar.gz

pushd $archive

./configure --prefix=/usr --enable-libwebpmux --enable-libwebpdemux && make -j4 && sudo make -j4 install

popd
