import asyncio
from bleak import BleakScanner

async def run():
    """Scans for all discoverable Bluetooth devices and prints their MAC addresses."""
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover(timeout=10)
    for d in devices:
        print(d)

if __name__ == "__main__":
    asyncio.run(run())