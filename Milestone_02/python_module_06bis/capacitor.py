from ex3 import factory as f


def main() -> None:
    tf: f.TransformCreatureFactory = f.TransformCreatureFactory()
    base = tf.create_base()
    evolved = tf.create_evolved()
    print("Testing Creature with transform capability\n base:")
    base.to_print()
    print(base.attack())
    base.transform()
    print(base.attack())
    base.revert()
    print(" evolved:")
    evolved.to_print()
    print(evolved.attack())
    evolved.transform()
    print(evolved.attack())
    evolved.revert()


if __name__ == "__main__":
    main()
