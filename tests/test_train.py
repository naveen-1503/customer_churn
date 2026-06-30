import os

def test_data_file_exists():
    # Sjekker om filen faktisk ligger der den skal
    assert os.path.exists('data/Telco_customer_churn.xlsx') == True