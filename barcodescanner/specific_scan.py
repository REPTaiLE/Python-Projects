#!/usr/bin/env python3
from aspose.barcode import barcoderecognition

full_path = 'test_img/Code_128.png'

reader = barcoderecognition.BarCodeReader(full_path, barcoderecognition.DecodeType.CODE128)

recognized_results = reader.read_bar_codes()

for x in recognized_results:
    print("Code text: " + x.code_text)
    print("Barcode type: " + x.code_type_name)