import time

def self_clean():
    print("[AntiBanOverlay] Self-clean complete.")

def run():
    print("[AntiBanOverlay] Hiding overlay for screenshot detection.")
    time.sleep(2)
    print("[AntiBanOverlay] Overlay restored.")
    self_clean()

if __name__ == "__main__":
    run()