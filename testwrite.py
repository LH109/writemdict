# -*- coding: utf8 -*-

from __future__ import unicode_literals, print_function, absolute_import, division

from writemdict import MDictWriter, encrypt_key
from ripemd128 import ripemd128
import io

d = {
    "alpha":"<i>alpha</i>",
	"beta":"Letter <b>beta</b>",
	"gamma":"Capital version is Γ &lt;"
	}

# Basic writing test
outfile = open("testoutput/testbasic.mdx", "wb")

writer = MDictWriter(d, "Basic Test", "This is a basic test dictionary.")
writer.write(outfile)
outfile.close()

# UTF-16 test

outfile = open("testoutput/testutf16.mdx", "wb")
writer = MDictWriter(d, "UTF-16 Test", "This is a test for the \"UTF-16\" encoding.", encoding="utf-16")
writer.write(outfile)
outfile.close()

# UTF-16 test, characters outside basic multilingual plane

d2 = {"𩷶":"A fish"}
outfile = open("testoutput/testutf16nonbmp.mdx", "wb")
writer = MDictWriter(d2, "UTF16 non-BMP test", "This test support for characters outside the Basic Multilingual Plane",
                     encoding="utf-16")
writer.write(outfile)
outfile.close()

# Big5 test

outfile = open("testoutput/testbig5.mdx", "wb")
writer = MDictWriter(d, "Big5 Test", "This is a test for the \"Big5\" encoding.", encoding="big5")
writer.write(outfile)
outfile.close()

# GBK test

outfile = open("testoutput/testgbk.mdx", "wb")
writer = MDictWriter(d, "GBK Test", "This is a test for the \"GBK\" encoding", encoding="gbk")
writer.write(outfile)
outfile.close()

# key index encryption test

outfile = open("testoutput/testencrypt.mdx", "wb")
writer = MDictWriter(d, "Disallow export test", "This dictionary tests the \"Disallow Export\" option", encrypt_index=True)
writer.write(outfile)
outfile.close()

# Version 1.2 test

outfile = open("testoutput/test12.mdx", "wb")
writer = MDictWriter(d, "Version 1.2 test", "This dictionary tests version 1.2 of the file format", version="1.2")
writer.write(outfile)
outfile.close()

# Version 1.2 UTF-16 test
outfile = open("testoutput/test12utf16.mdx", "wb")
writer = MDictWriter(d, "Version 1.2 UTF-16 test", "This dictionary tests version 1.2 of the file format, using UTF-16", encoding="utf16", version="1.2")
writer.write(outfile)
outfile.close()

# encryption test, external key file
outfile = open("testoutput/test_enc_abc.mdx", "wb")
writer = MDictWriter(d, "Encryption test", "This dictionary tests encryption", encoding="utf8", version="2.0", encrypt_key=b"abc")
writer.write(outfile)
outfile.close()
key = encrypt_key(b"abc", "example@example.com".encode("ascii"))
keyfile = io.open("testoutput/test_enc_abc.key", "w", encoding="ascii")
keyfile.write(key)
keyfile.close()

# encryption test, key supplied with dictionary
outfile = open("testoutput/test_enc_included.mdx", "wb")
writer = MDictWriter(d, "Encryption test", "This dictionary tests encryption, with key supplied in dictionary header", encoding="utf8", version="2.0", encrypt_key=b"abc", user_email="example@example.com".encode("ascii"))
writer.write(outfile)
outfile.close()

# No compression test
outfile = open("testoutput/testnocomp.mdx", "wb")

writer = MDictWriter(d, "Compression type 0", "This is a test of the basic dictionary, with compression type 0 (no compression)", compression_type=0)
writer.write(outfile)
outfile.close()

# LZO compression
outfile = open("testoutput/testlzocomp.mdx", "wb")
try:
	writer = MDictWriter(d, "LZO compression test", "This tests the LZO compression type.", compression_type=1)
	writer.write(outfile)
except NotImplementedError:
	print("python-lzo not installed. Skipping LZO test.")
outfile.close()
	


