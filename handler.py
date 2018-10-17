import json
import os
import stat
import subprocess


def prepare_yara():
    os.environ['LD_LIBRARY_PATH'] = '/action/yara'
    os.chmod('/action/yara/yextend', stat.S_IXUSR)


def run_yara(filename):
    output = subprocess.check_output([
        '/action/yara/yextend', '-r',
        '/action/binaryalert/compiled_yara_rules.bin', '-t', filename, '-j'
    ])
    return json.loads(output)[0]


def main(params):
    prepare_yara()
    return run_yara('/action/binaryalert/eicar.tar.gz.bz2')
