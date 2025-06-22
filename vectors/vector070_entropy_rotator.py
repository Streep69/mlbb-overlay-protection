import random, time

def run():
    print("[EntropyRotator] Rotating overlay entropy...")
    for _ in range(3):
        time.sleep(0.2)
        print(f"[EntropyRotator] New entropy: {random.randint(1000,9999)}")
    print("[EntropyRotator] Rotation complete.")

if __name__ == "__main__":
    run()