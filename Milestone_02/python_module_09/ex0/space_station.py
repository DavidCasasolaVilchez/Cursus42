from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    notes: str = Field(min_length=0, max_length=200, default="")
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    is_operational: bool = Field(default=True)
    last_maintenance: datetime

    def displayer(self) -> None:
        print(
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%"
        )
        if (self.is_operational):
            print("Status: Operational")
        else:
            print("Status: Inoperational")
        if (self.notes != ""):
            print(f"Notes: {self.notes}")


def main() -> None:
    print(
        "Space Station Data Validation\n"
        "========================================\n"
        "Valid station created:"
    )
    ss: SpaceStation
    ss = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True
    )
    ss.displayer()
    print(
        "\n========================================\n"
        "Expected validation error:"
    )
    try:
        ss = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=35,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True
        )
    except ValidationError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
