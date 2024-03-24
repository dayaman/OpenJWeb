import platform
import subprocess
import time
from datetime import datetime

pf = platform.system()


def convert_to_wav(t: str, server_id=None):
    open_jtalk = ['open_jtalk']
    if pf == 'Darwin':
        mech = ['-x', '/usr/local/Cellar/open-jtalk/1.11/dic']
        htsvoice = [
            '-m', '/usr/local/Cellar/open-jtalk/1.11/voice/htsvoice-tohoku-f01/tohoku-f01-neutral.htsvoice']
    else:
        mech = ['-x', '/usr/local/share/open_jtalk_dic']
        htsvoice = [
            '-m', '/usr/local/share/hts_voice/htsvoice-tohoku-f01/tohoku-f01-neutral.htsvoice']

    speed = ['-r', '1.0']
    outwav = ['-ow', '/dev/stdout']
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.run(
        cmd,
        shell=False,
        input=t.encode(),
        stdout=subprocess.PIPE
    )

    return c.stdout


def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    convert_to_wav(text)


if __name__ == '__main__':
    say_datetime()
