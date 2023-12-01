# File: tests/test_slack_data_loader.py

import pytest
from your_module import SlackDataLoader  # Replace 'your_module' with the actual module where SlackDataLoader is defined
import pandas as pd

@pytest.fixture
def slack_data_loader():
    # Set up SlackDataLoader instance if needed
    return SlackDataLoader()

def test_load_data_columns(slack_data_loader):
    # Arrange
    expected_columns = ['column1', 'column2', 'column3']  # Replace with the expected column names

    # Act
    data_frame = slack_data_loader.load_data()  # Replace with the actual method you want to test

    # Assert
    assert isinstance(data_frame, pd.DataFrame)
    assert all(column in data_frame.columns for column in expected_columns), "Columns do not match the expected columns"

def test_process_data_columns(slack_data_loader):
    # Arrange
    expected_columns = ['processed_column1', 'processed_column2']  # Replace with the expected processed column names

    # Act
    data_frame = slack_data_loader.load_data()  # Assuming process_data depends on load_data
    processed_data_frame = slack_data_loader.process_data(data_frame)  # Replace with the actual method you want to test

    # Assert
    assert isinstance(processed_data_frame, pd.DataFrame)
    assert all(column in processed_data_frame.columns for column in expected_columns), "Processed columns do not match the expected columns"
