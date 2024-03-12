import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from client.split_msg import splitMsg

def test_msg_split():
    msg = splitMsg("")

    if msg.handelJoin(["niki@AfterLife JOIN #123"]) != "You joined #123\n":
        assert False

from webserver import app

def test_flask_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


if __name__ == '__main__':
    test_msg_split()
    test_flask_status_code()
    assert True