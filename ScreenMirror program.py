import subprocess

def mirror_screen():
    # The path to the scrcpy executable, adjust it according to your setup.
    scrcpy_path = "C:\\scrcpy-win64-v3.0\\scrcpy-win64-v3.0\\scrcpy.exe"
    
    try:
        # Run scrcpy to mirror the device screen
        result = subprocess.run(
            [scrcpy_path],  # Calls scrcpy to mirror the screen
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if scrcpy executed successfully
        if result.returncode == 0:
            print("Screen mirroring started successfully!")
        else:
            print(f"Error starting scrcpy: {result.stderr}")
    
    except FileNotFoundError:
        print("scrcpy executable not found. Ensure it is installed and added to your PATH.")

# Call the function to start screen mirroring
mirror_screen()
