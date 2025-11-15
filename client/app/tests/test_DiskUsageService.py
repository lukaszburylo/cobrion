from unittest.mock import patch
from Services.DiskUsageService import DiskUsageService
import ast
import json


def test_get_service_name():
    assert DiskUsageService.get_service_name() == "disk_usage"


@patch("Services.DiskUsageService.shutil.disk_usage")
def test_get_data_mocked(mock_disk_usage):
    # Arrange: mock disk usage values
    mock_disk_usage.return_value = (
        100 * (2**30),  # total 100 GB
        40 * (2**30),  # used 40 GB
        60 * (2**30),  # free 60 GB
    )

    # Act: call get_data
    data = DiskUsageService.get_data()

    # ResponseTemplate stores everything in class attribute `response`
    response_dict = json.loads(
        str(data)
    )  # use __str__ to get JSON string and parse it back
    output_data = ast.literal_eval(
        response_dict["output_data"]
    )  # convert string dict to actual dict

    # Assert
    assert response_dict["service_name"] == "disk_usage"
    assert response_dict["result_status"] is True

    assert output_data["total"] == 100
    assert output_data["used"] == 40
    assert output_data["free"] == 60
    assert output_data["unit"] == "GB"
