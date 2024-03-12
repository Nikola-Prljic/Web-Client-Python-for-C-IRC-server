import client.split_msg as split_msg

def test_msg_split():
    msg = split_msg.splitMsg("")

    if msg.handelJoin(["niki@AfterLife JOIN #123"]) != "You joined #123\n":
        assert False
    assert True

from webserver import app

def test_flask_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


if __name__ == '__main__':
    test_msg_split()
    test_flask_status_code()