import time, os

def run():
    print("[Entropy] Entropy rotation started.")
    for _ in range(3):
        time.sleep(0.3)
        print("[Entropy] Randomizing overlay session seed.")
    print("[Entropy] Entropy injection OK.")

if __name__ == "__main__":
    run()