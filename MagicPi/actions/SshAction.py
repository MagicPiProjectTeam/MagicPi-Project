from os import system

class SshAction:

    env = None
    BDDmodel = None

    def __init__(self, Environement):
        self.env = Environement
        self.BDDmodel = self.env.getModel('BDD')


    def run(self):
        tmpDir = self.env.appDir + '../tmpfiles/'
        system("pkill -9 -f '^ssh.*magicpi@srv.magicpiproject.com.*$'")
        if self.BDDmodel.selectFromBDD('HostInfo')[self.BDDmodel.activeInterface()]['PUBIP']:
            system('ssh -vTN magicpi@srv.magicpiproject.com -p 443 -R 4242:127.0.0.1:4242 -E ' + tmpDir + 'ssh.log &')
            print('\033[1m' + '--------------------------------------------\n'
                              '[*] SSH connection initialized to "srv.magicpiproject.com" server with remote forwarding port (4242:127.0.0.1:4242)' + '\033[0m')
        else:
            print('[x] Failed to connect to remote server over SSH : No access to the Internet...')