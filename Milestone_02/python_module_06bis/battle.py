from ex3 import factory as f


def fight_tester(fa: f.CreatureFactory, fb: f.CreatureFactory) -> None:
    a = fa.create_base()
    a.to_print()
    print(" vs.")
    b = fb.create_base()
    b.to_print()
    print(" fight!")
    print(a.attack())
    print(b.attack())


def tester_creatures(factory: f.CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    base.to_print()
    print(base.attack())
    evolved.to_print()
    print(evolved.attack())


def main() -> None:
    ff: f.FlameFactory = f.FlameFactory()
    tf: f.TransformCreatureFactory = f.TransformCreatureFactory()
    tester_creatures(ff)
    print()
    tester_creatures(tf)
    print()
    fight_tester(ff, tf)


if __name__ == "__main__":
    main()
