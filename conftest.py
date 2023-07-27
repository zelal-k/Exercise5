# conftest.py
import pytest
import time

@pytest.fixture(autouse=True)
def measure_time(request):
    start_time = time.time()
    yield
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nTest '{request.node.name}' execution time: {execution_time:.5f} seconds")
