import os

def InstallGpuStat():
    os.system('pip install gpustat --user')

'''
arthur1  Wed Aug 22 15:29:01 2018
[0] GeForce GTX 1080 Ti | 83'C,  55 % | 10911 / 11170 MB | yuhuiz(10901M)
[1] GeForce GTX 1080 Ti | 84'C,  98 % | 10931 / 11172 MB | yuhuiz(10921M)
[2] GeForce GTX 1080 Ti | 34'C,   0 % | 10734 / 11172 MB | amiratag(307M) amiratag(10417M)
[3] GeForce GTX 1080 Ti | 29'C,   0 % | 10490 / 11172 MB | amiratag(213M) amiratag(10267M)
'''
def GetIdleGpuId():
    idleid = []
    info = os.popen('gpustat').readlines()
    for line in info[1:]:
        splitline = line.split('|')
        usage = splitline[-1].strip()
        if len(usage) == 0:
            gpuid = int(splitline[0].split(' ')[0][1:-1])
            idleid.append(gpuid)
    return idleid


def RunCommandOnIdle(command):
    idleid = GetIdleGpuId()
    if len(idleid) == 0: return
    os.system('CUDA_VISIBLE_DEVICES=%s %s' % (idleid[0], command))

if __name__ == '__main__':
    RunCommandOnIdle('python idle.py')
