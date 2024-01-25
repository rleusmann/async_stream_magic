import asyncio

import aiohttp

from async_stream_magic import StreamMagic, Info, State, Source


async def main():
    async with aiohttp.ClientSession() as session: 
        async with StreamMagic("192.168.178.123", session=session) as sm:
            info: Info = await sm.get_info()
            #print(info)
            #await asyncio.sleep(0)
            state: State = await sm.get_state()
            #print("State:")
            #print(state)

            info: Info = await sm.get_info()
            #print("Info:")
            #print(info)
            print(state)
            #await sm.set_power_on()
            await sm.set_power_off()
            state: State = await sm.get_state()
            print(state)
            #source_list: Source = await sm.get_sources()
            #print(source_list[0])
            #print([item.name for item in sources])
            #print("Current Source:")
            #source = next((item for item in source_list if item.id == state.source), None)
            #print(source_list)
            #print(source.name)
            #print(state.volume_percent)

            #await sm.set_volume_mute_off()



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())