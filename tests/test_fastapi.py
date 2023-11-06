from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
import httpx
import sys

sys.path.insert(1, '/workspace/fastapi-demo-3/')


from main import app

client = TestClient(app)

def test_read_main():
    responce = client.get("/")
    assert responce.status_code == 200
    assert responce.json() == {"msg": "Hello World"}

def test_read_item():
    responce = client.get("/items/3")
    assert responce.status_code == 200
    assert responce.json() == {"item_id": 3}