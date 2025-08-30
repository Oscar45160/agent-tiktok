import argparse
from .agent import run_once

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--theme", required=True)
    p.add_argument("--lang", default="fr")
    args = p.parse_args()
    out = run_once(theme=args.theme, lang=args.lang)
    print(out)

if __name__ == "__main__":
    main()
