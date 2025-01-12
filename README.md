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

To use the [DiracLiveProcessor](http://_vscodecontentref_/0) class, you can create an instance and call its methods. For example:

```python
from dirac import DiracLiveProcessor

base_url = "http://your-api-url"
processor = DiracLiveProcessor(base_url)

# Get slots
slots = processor.get_slots()
print(slots)
```
