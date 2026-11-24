import os

LINE = "It was on the floor. Everything on the floor is mine. That is the whole job."

def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
