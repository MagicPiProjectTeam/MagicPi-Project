from os import system

class SshAction:

    env = None
    BDDmodel = None

    def __init__(self, Environement):
        self.env = Environement
        self.BDDmodel = self.env.getModel('BDD')

    def run(self):
        tmpDir = '/home/imp/PycharmProjects/MagicPi-Project/MagicPi/tmpfiles'
        system("pkill -9 -f '^ssh.*magicpi@vps.imprezz.fr.*$'")
        if self.BDDmodel.selectFromBDD('HostInfo')[self.BDDmodel.activeInterface()]['PUBIP']:
            system('ssh -vTN magicpi@vps.imprezz.fr -p 80 -R 4242:127.0.0.1:4242 -E ' + tmpDir + ' &')
            print('[*] SSH connection initialized to "vps.imprezz.fr" server with remote forwarding port (4242:127.0.0.1:4242)')
        else:
            print('[x] Failed to connect to remote server over SSH : No access to the Internet...')
