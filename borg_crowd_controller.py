from typing import Dict


class Crowd:
    _shared_state: Dict[str, str] = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class CrowdController(Crowd):
    def __init__(self, state: str = None) -> None:
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "Stay"
    
    def __str__(self) -> str:
        return self.state


if __name__=="__main__":
    unit_1 = CrowdController()
    unit_2 = CrowdController()
    print(f"Unit 1 state: {unit_1}")
    print(f"Unit 2 state: {unit_2}")

    unit_1.state = "Play"
    unit_2.state = "Run"
    print(f"Unit 1 state: {unit_1}")
    print(f"Unit 2 state: {unit_2}")

    unit_3 = CrowdController()
    unit_3.state = "Stop"
    print(f"Unit 1 state: {unit_1}")
    print(f"Unit 2 state: {unit_2}")
    print(f"Unit 3 state: {unit_3}")
