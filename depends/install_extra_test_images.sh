#!/usr/bin/env bash
# install extra test images

archive=test_images

./download-and-extract.sh $archive https://raw.githubusercontent.com/python-pillow/pillow-depends/503ff2ff53e2f0446aa06a4a6c6cb17361b108e2/$archive.tar.gz

mv $archive/* ../Tests/images/

# Cleanup old tarball and empty directory
rm $archive.tar.gz
rmdir $archive
