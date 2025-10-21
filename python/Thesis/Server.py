import asyncio
import sys
from bleak import BleakScanner
import subprocess

# Replace with the MAC address of your phone or client device
# You can find this by running the discovery script below once.
CLIENT_MAC_ADDRESS = "59804778-32A2-5740-AD1A-6F9787B5ADE5"  # <== PHONE MAC ADDRESS HERE

async def discover_and_authenticate():
    """Continuously scans for the client and authenticates upon discovery."""
    print("Starting Bluetooth authentication server...")
    print(f"Looking for device with MAC address: {CLIENT_MAC_ADDRESS}")

    loopCtl = True
    
    while loopCtl:
        try:
            # Perform a short, active scan
            devices = await BleakScanner.discover(timeout=5)
            found_client = False
            
            for d in devices:
                if d.address == CLIENT_MAC_ADDRESS:
                    print(f"\nDevice found: {d.name} ({d.address})")
                    found_client = True
                    
                    # Implement a more robust authentication check here.
                    # For this example, we assume discovery means "authenticated."
                    # A more secure method would involve a pre-shared key challenge.
                    print("Authentication successful!")
                    
                    # Call a function to perform the authenticated action
                    loopCtl = await execute_authenticated_action()
                    break

            if not found_client:
                print(".", end="", flush=True) # Print a dot to show it's still scanning
            
            await asyncio.sleep(10)  # Wait before the next scan

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Restarting scanner...")
            await asyncio.sleep(5)

async def execute_authenticated_action():
    """Unlocks the computer (Windows example)."""
    if sys.platform == "win32":
        try:
            # This is a placeholder. You can replace 
            # this with any command.
            # Example: Unlock your workstation (if supported) or perform another action.
            # Real-world unlocking requires more complex system-level APIs.
            # This example just shows where the action would go.
            print("Action: Unlocking computer...")
            # subprocess.run(["..."])  # Replace with actual unlock command
        except Exception as e:
            print(f"Failed to execute action: {e}")
    else:
        print("Authenticated on non-Windows platform. No unlock command configured.")
        return False
    return True    
if __name__ == "__main__":
    asyncio.run(discover_and_authenticate())
