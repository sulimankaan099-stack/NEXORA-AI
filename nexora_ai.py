# NEXORA AI
# Personal AI Assistant

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule

console = Console()


# ==============================
# NEXORA AI - INTRODUCTION
# ==============================

console.print(
    Panel(
        "[bold cyan]NEXORA AI[/bold cyan]\n"
        "[dim]Personal AI Assistant[/dim]",
        title="[bold white]SYSTEM ONLINE[/bold white]",
        border_style="cyan",
        padding=(1, 4)
    )
)

console.print()

console.print(
    Panel(
        "[bold green]Hello! I am Nexora AI.[/bold green]\n\n"
        "I am here to help you with tasks,\n"
        "calculations, and simple questions.\n\n"
        "[dim]Give me a command, and I will do my best to assist you.[/dim]",
        title="[bold green]INTRODUCTION[/bold green]",
        border_style="green",
        padding=(1, 2)
    )
)

console.print()

console.print(
    Panel(
        "[bold yellow]Enter a command to begin.[/bold yellow]\n"
        "[dim]Available modes: General Information • Calculations • Exit[/dim]",
        title="[bold yellow]COMMAND CENTER[/bold yellow]",
        border_style="yellow",
        padding=(1, 2)
    )
)


# ==============================
# MAIN COMMAND LOOP
# ==============================

while True:

    console.print()
    command = Prompt.ask("[bold cyan]Command[/bold cyan]")

    # ==============================
    # BASIC COMMANDS
    # ==============================

    if command in ["Hi", "Hello", "Hey"]:

        console.print(
            Panel(
                "[bold green]Hello! I am Nexora AI.[/bold green]\n"
                "How can I help you today?",
                title="[bold cyan]NEXORA[/bold cyan]",
                border_style="cyan"
            )
        )

    elif command == "What is your name?":

        console.print(
            "[bold cyan]Nexora:[/bold cyan] "
            "My name is [bold]Nexora AI[/bold]."
        )

    elif command == "What can you do?":

        console.print(
            Panel(
                "[bold]I can:[/bold]\n"
                "• Perform calculations\n"
                "• Answer basic questions\n"
                "• Provide general information",
                title="[bold cyan]NEXORA CAPABILITIES[/bold cyan]",
                border_style="cyan"
            )
        )

    elif command == "Who created you?":

        console.print(
            "[bold cyan]Nexora:[/bold cyan] "
            "I was created as a [bold]Python AI project by Suliman Shah[/bold]."
        )

    elif command == "Who is suliman shah?":

        console.print(
            "[bold cyan]Nexora:[/bold cyan] "
            "Suliman Shah is the [/bold] founder and developer of Nexora.ai.[/bold]"
        )

    elif command == "Done":

        console.print(
            "[bold green] Introduction session ended.[/bold green]"
        )
        




    # ==============================
    # GENERAL INFORMATION
    # ==============================

    elif command == "General Information":

        console.print()

        console.print(
            Panel(
                "[bold green]Let's start General Information.[/bold green]\n"
                "[dim]Ask a question or type 'Done' to return.[/dim]",
                title="[bold green]GENERAL INFORMATION[/bold green]",
                border_style="green"
            )
        )

        while True:

            information = Prompt.ask(
                "[bold green]General Information[/bold green]"
            )

            if information == "What is the capital of Pakistan?":

                console.print(
                    "[bold green]Nexora:[/bold green] "
                    "The capital of Pakistan is [bold]Islamabad[/bold]."
                )

            elif information == "What is the national language of Pakistan?":

                console.print(
                    "[bold green]Nexora:[/bold green] "
                    "The national language of Pakistan is [bold]Urdu[/bold]."
                )

            elif information == "How many planets are in our solar system?":

                console.print(
                    "[bold green]Nexora:[/bold green] "
                    "There are [bold]eight planets[/bold] in our solar system."
                )

            elif information == "What is the most powerful country in the world?":

                console.print(
                    "[bold green]Nexora:[/bold green] "
                    "It depends on how power is measured, but the "
                    "[bold]United States[/bold] is often considered one "
                    "of the world's most powerful countries."
                )

            elif information == "Done":

                console.print(
                    "[bold green]✓ General Information session ended.[/bold green]"
                )
                break

            else:

                console.print(
                    "[bold red]Nexora:[/bold red] "
                    "I don't understand this question yet."
                )


    # ==============================
    # CALCULATIONS
    # ==============================

    elif command == "Calculations":

        console.print()

        console.print(
            Panel(
                "[bold yellow]Let's start calculation.[/bold yellow]\n"
                "[dim]Enter a calculation or type 'Done' to return.[/dim]",
                title="[bold yellow]CALCULATION MODE[/bold yellow]",
                border_style="yellow"
            )
        )

        while True:

            calculation = Prompt.ask(
                "[bold yellow]Calculation[/bold yellow]"
            )

            if calculation == "20 + 30":

                console.print(
                    "[bold yellow]Nexora:[/bold yellow] "
                    "[bold green]50[/bold green]"
                )

            elif calculation == "100 / 4":

                console.print(
                    "[bold yellow]Nexora:[/bold yellow] "
                    "[bold green]25[/bold green]"
                )

            elif calculation == "10 * 10":

                console.print(
                    "[bold yellow]Nexora:[/bold yellow] "
                    "[bold green]100[/bold green]"
                )

            elif calculation == "100 - 50":

                console.print(
                    "[bold yellow]Nexora:[/bold yellow] "
                    "[bold green]50[/bold green]"
                )

            elif calculation == "Done":

                console.print(
                    "[bold green]✓ Calculation session ended.[/bold green]"
                )
                break

            else:

                console.print(
                    "[bold red]Nexora:[/bold red] "
                    "I don't understand this calculation yet."
                )


    # ==============================
    # EXIT
    # ==============================

    elif command == "Exit":

        console.print()

        console.print(
            Panel(
                "[bold cyan]Nexora AI shutting down...[/bold cyan]\n"
                "[dim]Thank you for using Nexora AI.[/dim]",
                title="[bold green]SYSTEM OFFLINE[/bold green]",
                border_style="cyan"
            )
        )

        break


    # ==============================
    # UNKNOWN COMMAND
    # ==============================

    else:

        console.print(
            "[bold red]Nexora:[/bold red] "
            "I don't understand that command yet."
        )