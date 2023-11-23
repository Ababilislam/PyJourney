import os.path
import tempfile

with tempfile.TemporaryDirectory() as temdir:
    print("created temporary dir",temdir)
    os.path.exists(temdir)

#out side of the access it already got deleted.
print(os.path.exists('/tmp/tmpzte67h4g'))