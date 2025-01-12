import requests
import logging
from typing import List, Dict, Any

class DiracLiveProcessor:
    def __init__(self, base_url: str) -> None:
        """
        Initializes the DiracLiveProcessor with a base URL.

        Args:
            base_url (str): The base URL for the Dirac Live Processor API.
        """
        if not base_url.startswith("http"):
            raise ValueError("The base_url must start with 'http' or 'https'.")
        self.base_url = base_url

    def get_slots(self) -> List[Dict[str, Any]]:
        """
        Retrieves the slots from the Dirac Live Processor.

        Returns:
            List[Dict[str, Any]]: A list of slot dictionaries containing slot details. i.e.
            [{'description': '',
                'filter_type': 'Dirac Live Bass Control',
                'gains_delays': [{'delay_ms': 217.438, 'gain_db': -1.57, 'index': 0},
                                {'delay_ms': 217.667, 'gain_db': 0.0, 'index': 1},
                                {'delay_ms': 0.0, 'gain_db': -8.36, 'index': 2},
                                {'delay_ms': 14.313, 'gain_db': -3.67, 'index': 3}],
                'index': 0,
                'is_trial': False,
                'name': 'Ojas1',
                'path': '/Users/jaime/Music/Audio Music '
                        'Apps/Dirac/filters/multi/custom_2_2/0'},
            ...]

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        try:
            return self.__request("get", "list-slots")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch slots: {e}")
            raise

    def get_active_slot(self) -> int:
        """
        Retrieves the active slot from the Dirac Live Processor.

        Returns:
           int: index of the active slot.

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        try:
            response = requests.get(f"{self.base_url}/active-slot")
            response.raise_for_status()  # Will raise HTTPError if != 200
            return response.json().get("index")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch slots: {e}")
            raise

    def set_active_slot(self, slot: int) -> None:
        """
        Sets the active slot in the Dirac Live Processor.

        Returns:
            None

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        try:
            self.__request("put", "active-slot", {"index": slot})
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set active slot: {e}")
            raise


    def get_filter_state(self) -> bool:
        """
        Retrieves the filter state from the Dirac Live Processor.

        Returns:
            bool: True if filtering is enabled, False otherwise.

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """

        try:
            response = self.__request("get", "filtering")
            return response.get("enabled") == 1
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch filter state: {e}")
            raise

    def set_filter_state(self, status: bool) -> None:
        """
        Sets the filter state in the Dirac Live Processor.
        
        Args:
            status (bool): True to enable filtering, False to disable it.
        
        Returns:
            None
        
        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """

        try:
            self.__request("put", "filtering", {"enabled": int(status)})
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set filter state: {e}")
            raise

    def get_speaker_limits(self) -> Dict[str, Any]:
        """
        Retrieves the speaker limits from the Dirac Live Processor.

        Returns:
            Dict[str, Any]: A dictionary containing the speaker limits. i.e. {'max': 0.0, 'min': -50.0, 'step': 0.5, 'units': ''}

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        try:
            return self.__request("get", "limits/speaker")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch speaker limits: {e}")
            raise
    
    def get_speaker_gain(self) -> float:
        """
        
        Retrieves the speaker gain from the Dirac Live Processor.
        
        Returns:
            float: The speaker gain.
            
        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        try:
            response = self.__request("get", "speaker")
            return response.get("gain")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch speaker gain: {e}")
            raise

    def set_speaker_gain(self, gain: float) -> None:
        """
        Sets the speaker gain in the Dirac Live Processor.
        
        Args:
            gain (float): The speaker gain to set.
            
        Returns:
            None
            
        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        try:
            self.__request("put", "speaker", {"gain": gain})
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set speaker gain: {e}")
            raise


    def __request(self, method: str, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Makes a request to the Dirac Live Processor API.
        """
        try:
            response = requests.request(method, f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()
            if (method == "get"):
                return response.json()
            return []
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            raise
