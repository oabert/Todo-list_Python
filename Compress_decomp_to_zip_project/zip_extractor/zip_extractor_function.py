import zipfile


def extract_zip(zip_path, dest_dir):
    """archive represents actual file object"""
    with zipfile.ZipFile(zip_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_zip(zip_path='/Users/olenaabert/Desktop/python/Compress_decomp_to_zip_project/compress_zip/test_zip/compressed.zip',
                dest_dir='/Users/olenaabert/Desktop/python/Compress_decomp_to_zip_project/zip_extractor/zip_extract')
