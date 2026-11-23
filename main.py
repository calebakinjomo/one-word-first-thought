import os


def main():
    """Write the entry word, petrichor, to entry.txt.

    Petrichor is the chosen word because it is sensory and vivid: one
    word that carries a whole scene -- the smell of rain on dry earth
    after a long drought, dust settling, the first drops hitting warm
    ground. It is a single, concrete image rather than an abstraction.
    """
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write("petrichor")


if __name__ == "__main__":
    main()
