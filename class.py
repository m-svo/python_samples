import random

class PrivateComputer:
    ''' A unit for computing '''

    def __init__(self, id, hostname='unnamed_pc'+str(random.randint(0,10000))):
        self.id = id
        self.hostname = hostname
        self.cpu = ''
        self.video = ''
        self.storage = ''
        self.psu = ''
        self.powered = 0

    def place_cpu(self, string):
        new_val = self._check(string)
        self.cpu += new_val + ';'

    def place_psu(self, string):
        new_val = self._check(string)
        self.psu += new_val + ';'

    def place_video(self, string):
        new_val = self._check(string)
        self.video += new_val + ';'

    def place_storage(self, string):
        new_val = self._check(string)
        self.storage += new_val + ';'

    def print_config(self):
        print (self.cpu)
        print (self.video)
        print (self.storage)
        print (self.psu)

    def power_on(self):
        if self.powered == 0:
            self.powered = 1
        else:
            print ('PC ' + self.hostname + ' is already on')

    def _check(self, string):
        if isinstance(string, str) and len(string) > 0:
            return string
        else:
            raise ValueError('Invalid string: {}'.format(string))

ryzen = PrivateComputer(0)
ryzen.place_cpu('AMD Ryzen 2600X')
ryzen.place_video('Nvidia GTX 1060')
ryzen.place_storage('Samsung 256GB SSD')
ryzen.place_storage('Western Digital 500GB HDD')
ryzen.place_psu('Aerocool StrikeX 600W')

ryzen.print_config()

ryzen.power_on()
ryzen.power_on()

print('Check if powered (0/1): ' + str (ryzen.powered))
