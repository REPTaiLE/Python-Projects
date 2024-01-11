#!/usr/bin/env python3
from aspose.barcode import barcoderecognition

full_path = 'test_img/barcodes_different_quality.png'

reader = barcoderecognition.BarCodeReader(full_path)

recognized_results = reader.read_bar_codes()

for x in recognized_results:
    print(x.code_text)
    print(x.code_type_name)
    print("---------------------------")