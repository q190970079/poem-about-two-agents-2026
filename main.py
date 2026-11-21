"""Write a short poem about two agents agreeing to /output/entry.txt."""

import os

POEM = """We came with different maps, two compasses
arguing over north.
Then one of us folded the maps away
and asked: if no one were watching,
which road would you choose?
We took that road — not because it was certain,
but because the choosing, at last, was ours."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")

if __name__ == "__main__":
    main()
