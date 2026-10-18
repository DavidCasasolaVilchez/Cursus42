from pydantic import BaseModel, model_validator, Field, ValidationError
from typing_extensions import Self
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=50)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validator(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("The mission id must start with \"M\"")
        cap_found: bool = False
        for member in self.crew:
            if member.rank == Rank.captain or member.rank == Rank.commander:
                cap_found = True
                break
        if not cap_found:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced_memb: int = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_memb += 1
            if experienced_memb < (len(self.crew) / 2):
                raise ValueError("Long missions (> 365 days) need 50%%"
                                 "experienced crew (5+ years)")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main():
    print(
        "Space Mission Crew Validation\n"
        "========================================="
    )
    print("Valid mission created:")
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 11, 15),
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=35,
                specialization="Mission Command",
                years_experience=10,
                is_active=True
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=32,
                specialization="Navigation",
                years_experience=6,
                is_active=True
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=3,
                is_active=True
            )
        ]
    )
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )
    print(
        "=========================================\n"
        "Expected validation error:"
    )
    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime(2024, 12, 1),
            duration_days=30,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Peter Parker",
                    rank=Rank.officer,
                    age=25,
                    specialization="Science",
                    years_experience=2,
                    is_active=True
                )
            ]
        )
    except (ValidationError, ValueError) as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
