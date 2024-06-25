import os
import asyncio
from sliver import SliverClientConfig, SliverClient

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".sliver-client", "configs")
DEFAULT_CONFIG = os.path.join(CONFIG_DIR, "")

async def main():
    Command = "ps -ef"
    config = SliverClientConfig.parse_config_file(DEFAULT_CONFIG)
    client = SliverClient(config)
    print('[*] Connected to server ...')
    await client.connect()
    sessions = await client.sessions()
    print('[*] Sessions: %r' % sessions)
    print(f"Sessions Count: {len(sessions)}")
    for session in sessions:
        try:
            print(f'[*] Interacting with session \033[1;32m{session.ID}\033[0m')
            interact = await client.interact_session(session.ID)

            '''
            ifconfig = await interact.ifconfig()
            for NetInterface in ifconfig.NetInterfaces:
                for ips in NetInterface.IPAddresses:
                    if ("::" not in ips) and ("127.0.0.1" not in ips):
                        print(ips)
                #print(f"\033[1;32m{' '.join(NetInterface.IPAddresses)}\033[0m")
                #print(NetInterface.IPAddresses)
            '''
            
            execute_result = await interact.execute( "bash", ["-c", Command] )
            print(execute_result.Stdout.decode())
            print(execute_result.Stderr.decode())

        except Exception as e:
            print(f"{session.ID}  {session.RemoteAddress}  Error: {e}")
            continue

if __name__ == '__main__':
    asyncio.run(main())
