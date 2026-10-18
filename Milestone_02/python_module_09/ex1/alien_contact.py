from pydantic import BaseModel, model_validator, Field, ValidationError
from typing_extensions import Self
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str = Field(default="", max_length=500)
    is_verified: bool = Field(default=True)

    @model_validator(mode='after')
    def validator(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("The contact id must start with \"AC\"")
        if (self.contact_type == ContactType.physical
                and not self.is_verified):
            raise ValueError("The physical contact must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                "The telepathic contact requires at least 3 witnesses")
        if (self.signal_strength > 7.0 and self.message_received == ""):
            raise ValueError(
                "The strong signals (> 7.0) should include received messages")
        return self

    def displayer(self) -> None:
        print(
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: '{self.message_received}'\n"
        )


def main() -> None:
    print(
        "Alien Contact Log Validation\n"
        "========================================\n"
        "Valid contact report:"
    )
    ac: AlienContact
    ac = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=False
    )
    ac.displayer()
    print(
        "\n========================================\n"
        "Expected validation error:"
    )
    try:
        ac = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
    except (ValueError, ValidationError) as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
