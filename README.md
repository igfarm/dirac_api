# Dirac Live Processor

This project provides an interface to interact with the Dirac Live Processor API.

## API Endpoints

The following API endpoints are available:

- `/api/notification`
- `/api/active-slot`
- `/api/list-slots`
- `/api/filtering`
- `/api/limits/speaker`
- `/api/speaker`
- `/api/notify`
- `/api/config`
- `/api/limits/inputeq`
- `/api/inputeq`

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd <project-directory>
   ```
3. Create a virtual environment:
   ```sh
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```sh
   source venv/bin/activate
   ```
5. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To use the DiracLiveProcessor class, you can create an instance and call its methods. For example:

```python
from dirac import DiracLiveProcessor

base_url = "http://196.168.1.100:5006/api"
processor = DiracLiveProcessor(base_url)

# Get slots
slots = processor.get_slots()
print(slots)
```

Alternativerly you can use the command line utility provided:

```
% python main.py -h
usage: main.py [-h] --base-url BASE_URL
               {get-slots,get-active-slot,set-active-slot,get-filter-state,set-filter-state,get-speaker-limits,get-speaker-gain,set-speaker-gain} ...

CLI to interact with a Dirac Live Processor.

options:
  -h, --help            show this help message and exit
  --base-url BASE_URL   Base URL for the Dirac Live Processor, e.g. http://localhost:5006/api

Commands:
  {get-slots,get-active-slot,set-active-slot,get-filter-state,set-filter-state,get-speaker-limits,get-speaker-gain,set-speaker-gain}
                        Available subcommands
    get-slots           Retrieve and display all slots from the Dirac Live Processor
    get-active-slot     Retrieve and display the index of the currently active slot
    set-active-slot     Set the active slot by index
    get-filter-state    Retrieve and display the current filter state (on/off)
    set-filter-state    Enable or disable the filter
    get-speaker-limits  Retrieve and display the speaker gain limits
    get-speaker-gain    Retrieve and display the current speaker gain
    set-speaker-gain    Set the speaker gain
```
