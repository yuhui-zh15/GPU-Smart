import os
import threading
import time

'''
[Requirement] python3
[Requirement] gpustat: pip install gpustat --user
'''

class Allocator(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running_hist = []
        self.waiting_list = []
        self.reserve_num = 0

    '''
    arthur1  Wed Aug 22 15:29:01 2018
    [0] GeForce GTX 1080 Ti | 83'C,  55 % | 10911 / 11170 MB | yuhuiz(10901M)
    [1] GeForce GTX 1080 Ti | 84'C,  98 % | 10931 / 11172 MB | yuhuiz(10921M)
    [2] GeForce GTX 1080 Ti | 34'C,   0 % | 10734 / 11172 MB | amiratag(307M) amiratag(10417M)
    [3] GeForce GTX 1080 Ti | 29'C,   0 % | 10490 / 11172 MB | amiratag(213M) amiratag(10267M)
    '''
    def GetIdleId(self):
        idleid = []
        info = os.popen('gpustat').readlines()
        for line in info[1:]:
            splitline = line.split('|')
            usage = splitline[-1].strip()
            if len(usage) == 0:
                gpuid = int(splitline[0].split(' ')[0][1:-1])
                idleid.append(gpuid)
        return idleid

    def Execute(self):
        if len(self.waiting_list) == 0: return
        idleid = self.GetIdleId()
        if len(idleid) <= self.reserve_num: return
        command = self.waiting_list.pop(0)
        command.append(idleid[0])
        command.append(time.asctime())
        run = os.popen('CUDA_VISIBLE_DEVICES=%s %s' % (idleid[0], command[0]))
        self.running_hist.append(command)

    def AddWaitList(self, command):
        self.waiting_list.append([command, time.asctime()])

    def ShowWaitList(self):
        if len(self.waiting_list) == 0:
            print('Waiting list is empty')
        else:
            for i, command in enumerate(self.waiting_list):
                print('[%s](%s): %s' % (i, command[1], command[0]))

    def ShowRunHist(self):
        if len(self.running_hist) == 0:
            print('Running history is empty')
        else:
            for i, command in enumerate(self.running_hist):
                print('[%s]{GPU: %s}(%s->%s): %s' % (i, command[2], command[1], command[3], command[0]))

    def run(self):
        while True:
            self.Execute()
            time.sleep(60)


def controller(allocator):
    while True:
        os.system('clear')
        print('Welcome to Smart GPU Queue')
        print('--------------------------')
        print('[1] New Command')
        print('[2] Running History')
        print('[3] Waiting List')
        print('[4] GPU Status')
        print('[5] Reserve Number')
        # print('[6] Exit')
        print('--------------------------')
        cid = input('Please input command ID\n')
        if cid == '1':
            command = input('Please input command\n')
            allocator.AddWaitList(command)
        elif cid == '2':
            allocator.ShowRunHist()
        elif cid == '3':
            allocator.ShowWaitList()
        elif cid == '4':
            os.system('gpustat')
        elif cid == '5':
            print('Current Reserve Number: %s' % (allocator.reserve_num))
            num = input('Please input how many GPUs you want to reserve\n')
            try:
                num = int(num)
                if num >= 0:
                    allocator.reserve_num = num
                    print('Set successfully')
                else:
                    print('Reserve Number must >= 0')
            except:
                print('Please input integer')
        # No way to stop...
        # elif cid == '6':
        #     i = input('[Warning]: Please make sure no running process! [Y/N]\n')
        #     if i == 'Y':
        #         exit(0)
        #     else:
        #         continue
        elif cid == '':
            continue
        else:
            print('Error command!')
        input('Press <Entey> return to the menu...\n')


if __name__ == '__main__':
    allocator = Allocator()
    allocator.start()
    controller(allocator)

