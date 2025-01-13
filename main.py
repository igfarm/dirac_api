#!/usr/bin/env python3
import argparse
import sys
import requests
from dirac import DiracLiveProcessor

def main():
    # Set up top-level parser
    parser = argparse.ArgumentParser(
        description="CLI to interact with a Dirac Live Processor."
    )
    parser.add_argument(
        "--base-url",
        required=True,
        help="Base URL for the Dirac Live Processor, e.g. http://localhost:8080",
    )

    subparsers = parser.add_subparsers(
        title="Commands", dest="command", help="Available subcommands"
    )

    # ----------------
    #  get-slots
    # ----------------
    get_slots_parser = subparsers.add_parser(
        "get-slots",
        help="Retrieve and display all slots from the Dirac Live Processor",
    )

    # ----------------
    #  get-active-slot
    # ----------------
    get_active_slot_parser = subparsers.add_parser(
        "get-active-slot",
        help="Retrieve and display the index of the currently active slot",
    )

    # ----------------
    #  set-active-slot
    # ----------------
    set_active_slot_parser = subparsers.add_parser(
        "set-active-slot",
        help="Set the active slot by index",
    )
    set_active_slot_parser.add_argument(
        "slot", type=int, help="The index of the slot to activate"
    )

    # ----------------
    #  get-filter-state
    # ----------------
    get_filter_state_parser = subparsers.add_parser(
        "get-filter-state",
        help="Retrieve and display the current filter state (on/off)",
    )

    # ----------------
    #  set-filter-state
    # ----------------
    set_filter_state_parser = subparsers.add_parser(
        "set-filter-state",
        help="Enable or disable the filter",
    )
    set_filter_state_parser.add_argument(
        "status", choices=["true", "false"], help="Set filter on (true) or off (false)"
    )

    # ----------------
    #  get-speaker-limits
    # ----------------
    get_speaker_limits_parser = subparsers.add_parser(
        "get-speaker-limits",
        help="Retrieve and display the speaker gain limits",
    )

    # ----------------
    #  get-speaker-gain
    # ----------------
    get_speaker_gain_parser = subparsers.add_parser(
        "get-speaker-gain",
        help="Retrieve and display the current speaker gain",
    )

    # ----------------
    #  set-speaker-gain
    # ----------------
    set_speaker_gain_parser = subparsers.add_parser(
        "set-speaker-gain",
        help="Set the speaker gain",
    )
    set_speaker_gain_parser.add_argument(
        "gain", type=float, help="The speaker gain to set"
    )

    # Parse args
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Instantiate DiracLiveProcessor
    processor = DiracLiveProcessor(base_url=args.base_url)

    try:
        if args.command == "get-slots":
            slots = processor.get_slots()
            print("Slots:\n", slots)

        elif args.command == "get-active-slot":
            active = processor.get_active_slot()
            print(f"Active slot index: {active}")

        elif args.command == "set-active-slot":
            processor.set_active_slot(args.slot)
            print(f"Active slot set to: {args.slot}")

        elif args.command == "get-filter-state":
            state = processor.get_filter_state()
            print(f"Filter state: {'Enabled' if state else 'Disabled'}")

        elif args.command == "set-filter-state":
            status = True if args.status.lower() == "true" else False
            processor.set_filter_state(status)
            print(f"Filter state set to: {status}")

        elif args.command == "get-speaker-limits":
            limits = processor.get_speaker_limits()
            print("Speaker Limits:\n", limits)

        elif args.command == "get-speaker-gain":
            gain = processor.get_speaker_gain()
            print(f"Speaker Gain: {gain}")

        elif args.command == "set-speaker-gain":
            processor.set_speaker_gain(args.gain)
            print(f"Speaker gain set to: {args.gain}")

        else:
            parser.print_help()

    except requests.exceptions.RequestException as err:
        print(f"Error communicating with Dirac Live Processor: {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()