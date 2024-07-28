#!/usr/bin/env python3

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2024 The Linux Foundation <https://linuxfoundation.org>

"""Python wrapper for the sample/test Typer application."""

# External modules
import typer

app = typer.Typer()

# Define command structure with typer module
app = typer.Typer(no_args_is_help=True)


@app.command()
def hello(name: str):
    """Greets somebody."""
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    """Says goodbye."""
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


def run():
    """Provide main entry point for the sample/test application.

    This function sets up the Typer application with subcommands.

    Usage:
            devops-reusable-workflows hello
            devops-reusable-workflows goodbye

    """
    app()
