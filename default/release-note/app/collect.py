import release_note
import logging
import json
from pyarrow import fs
logging.basicConfig(level=logging.INFO)

for name in release_note.list_resources():
    logging.info(f'{name} collecting ...')
    file_path = f'/lake/red/release-note/{name}.json.gz'
    hdfs = fs.HadoopFileSystem('192.168.1.7', port=9000, user='root')
    group = []
    for release_item in release_note.get(name):
        row = {
            'product_name': release_item.product_name,
            'version': release_item.version,
            'release_date': release_item.release_date.isoformat(),
            'link': release_item.link,
            'body': release_item.body
        }

        group.append(json.dumps(row, ensure_ascii=False))
    with hdfs.open_output_stream(file_path, compression='gzip') as stream:
        stream.write('\n'.join(group).encode('utf-8'))