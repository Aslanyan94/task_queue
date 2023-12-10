from dataclasses import dataclass


@dataclass
class Resources:
    ram: int
    cpu_cores: int
    gpu_count: int

    def to_dict(self):
        return {
            'ram': self.ram,
            'cpu_cores': self.cpu_cores,
            'gpu_count': self.gpu_count
        }


@dataclass
class Task:
    id: int
    priority: int
    resources: Resources
    content: str
    result: str

