import time
import random

def run_round():
    input('Press Enter to begin the round...')
    delay = random.uniform(1.0, 3.0)
    print('Get ready...')
    time.sleep(delay)
    print('GO!')
    start = time.time()
    input()  # wait for player to press Enter
    elapsed = (time.time() - start) * 1000
    return int(elapsed)

def main():
    print('Reaction Timer')
    try:
        rounds = int(input('How many rounds? (3): ') or 3)
    except ValueError:
        rounds = 3

    results = []
    for i in range(1, rounds + 1):
        print(f'\nRound {i}:')
        rt = run_round()
        print(f'Your reaction: {rt} ms')
        results.append(rt)

    best = min(results)
    worst = max(results)
    avg = sum(results) // len(results)
    print('\nSummary: Best={} ms, Worst={} ms, Avg={} ms'.format(best, worst, avg))

if __name__ == '__main__':
    main()
