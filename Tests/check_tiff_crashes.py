#!/usr/bin/env python

# Reproductions/tests for crashes/read errors in TiffDecode.c

# When run in python, all of these images should fail for
# one reason or another, either as a buffer overrun,
# unrecognized datastream, or truncated image file.
# There shouldn't be any segfaults.
#
# if run like
# `valgrind --tool=memcheck python check_tiff_crashes.py  2>&1 | grep TiffDecode.c`
# the output should be empty. There may be python issues
# in the valgrind especially if run in a debug python
# version.


from PIL import Image

repro_read_strip = (
    "images/crash_1.tif",
    "images/crash_2.tif",
    "Tests/images/crash-2020-10-test.tif",
    "Tests/images/crash-0c7e0e8e11ce787078f00b5b0ca409a167f070e0.tif",
    "Tests/images/crash-0e16d3bfb83be87356d026d66919deaefca44dac.tif",
    "Tests/images/crash-1152ec2d1a1a71395b6f2ce6721c38924d025bf3.tif",
    "Tests/images/crash-1185209cf7655b5aed8ae5e77784dfdd18ab59e9.tif",
    "Tests/images/crash-338516dbd2f0e83caddb8ce256c22db3bd6dc40f.tif",
    "Tests/images/crash-4f085cc12ece8cde18758d42608bed6a2a2cfb1c.tif",
    "Tests/images/crash-86214e58da443d2b80820cff9677a38a33dcbbca.tif",
    "Tests/images/crash-f46f5b2f43c370fe65706c11449f567ecc345e74.tif",
    "Tests/images/crash-63b1dffefc8c075ddc606c0a2f5fdc15ece78863.tif",
)

for path in repro_read_strip:
    with Image.open(path) as im:
        try:
            im.load()
        except Exception as msg:
            print(msg)
