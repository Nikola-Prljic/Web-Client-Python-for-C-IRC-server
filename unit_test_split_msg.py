import client.split_msg as split_msg

def test_example():
    msg = split_msg.splitMsg("")

    if msg.handelJoin(["niki@AfterLife JOIN #123"]) != "You joined #123\n":
        assert False
    assert True

if __name__ == '__main__':
    test_example()