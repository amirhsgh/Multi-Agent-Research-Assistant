from typing import Dict, Any
from rich.console import Console
from rich.panel import Panel

console = Console()


class HumanApproval:

    def request_approval(
        self,
        step_name: str,
        content: str
    ) -> bool:

        console.print(
            Panel(
                content,
                title=f"Approval Required: {step_name}",
                border_style="yellow"
            )
        )


        while True:
            response = input("\nApprove? (y/n): ").strip().lower()

            if response in ["y", "yes"]:
                return True

            if response in ["n", "no"]:
                return False

            print("Invalid input")