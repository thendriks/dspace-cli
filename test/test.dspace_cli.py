import unittest
import dspace_cli

class TestRestClient(unittest.TestCase):

    def test_create_community(self):
        response = dspace_cli.create_community('testcommunity')
        print(response)
        print(response.text)

if __name__ == '__main__':
    unittest.main()