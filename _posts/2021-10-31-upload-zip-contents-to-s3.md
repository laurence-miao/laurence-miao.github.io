---
title: How to upload contents in big zip file to AWS S3 bucket without uncompressing
description: A short boto3 script that uploads every file inside a zip archive to an S3 prefix, without extracting the archive to disk first.
tags: [aws, s3, python]
---

The script reads each file straight out of the archive and puts it under `s3://<bucket>/<prefix>/`, so nothing is unpacked locally. It takes the zip path, the bucket and the prefix as arguments.

```python
#!/bin/env python

import sys
from zipfile import ZipFile
import boto3

def main(zipfile_path, bucket, prefix):
    s3 = boto3.resource('s3')

    with ZipFile(zipfile_path, 'r') as zip:
        # printing all the contents of the zip file
        for f in zip.namelist():
            if not zip.getinfo(f).is_dir():
                obj = s3.Object(bucket, f"{prefix}/{f}")
                obj.put(Body=zip.read(f))
                print(f"uploaded s3://{bucket}/{prefix}/{f}")
        print('Done!')

if __name__ == "__main__":
    main(zipfile_path=sys.argv[1], bucket=sys.argv[2], prefix=sys.argv[3])
```
