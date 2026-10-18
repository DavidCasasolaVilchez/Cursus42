import random
import typing


def gen_event() -> typing.Generator[tuple, None, None]:
    names = {"alice", "bob", "charlie", "dylan"}
    actions = {"move", "sleep", "eat", "run", "swim", "climb", "use", "grab"}
    while True:
        yield (random.choice(list(names)), random.choice(list(actions)))


def consume_event(event: list[tuple]) -> typing.Generator[tuple, None, None]:
    while len(event) > 0:
        yield event.pop(event.index(random.choice(list(event))))


def main() -> None:
    tupl = gen_event()
    for i in range(1001):
        t = next(tupl)
        print(f"Event {i}: Player {t[0]} did action {t[1]}")
    events: list[tuple] = list()
    for i in range(10):
        events.append(next(tupl))
    print(f"Built list of 10 events: {events}")
    consume = consume_event(events)
    for i in range(10):
        print(f"Got event from list: {next(consume)}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
