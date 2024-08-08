#!/usr/bin/env bash
# install raqm

archive=raqm-cmake-99300ff3

./download-and-extract.sh $archive https://raw.githubusercontent.com/python-pillow/pillow-depends/503ff2ff53e2f0446aa06a4a6c6cb17361b108e2/$archive.tar.gz

pushd $archive

mkdir build
cd build
cmake ..
make && sudo make install
cd ..

popd
