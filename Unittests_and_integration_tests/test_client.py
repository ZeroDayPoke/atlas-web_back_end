#!/usr/bin/env python3
"""Unittests for client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


class MockResponse:
    """Mock class for the response object"""
    def __init__(self, json_data):
        self.json_data = json_data
    def json(self):
        return self.json_data


class TestGithubOrgClient(unittest.TestCase):
    """test class for GithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_org = {"name": org_name}
        mock_get_json.return_value = mock_org

        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, mock_org)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url."""
        mock_payload = {'repos_url': 'https://api.github.com/orgs/org/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_payload
            github_org_client = GithubOrgClient('org')
            self.assertEqual(github_org_client._public_repos_url,
                             'https://api.github.com/orgs/org/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos."""
        mock_repo_url = 'https://api.github.com/orgs/org/repos'
        mock_repos_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = mock_repos_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = mock_repo_url
            github_org_client = GithubOrgClient('org')
            repos = github_org_client.public_repos()

            self.assertEqual(repos,
                             [repo['name'] for repo in mock_repos_payload])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_repo_url)

    @parameterized.expand([
        ({"license": {"key": "license_to_uwu"}}, "license_to_uwu", True),
        ({"license": {"key": "other_license"}}, "license_to_uwu", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test that GithubOrgClient.has_license
        returns the expected boolean value."""
        github_org_client = GithubOrgClient('test_org')
        result = github_org_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {"org_payload": payload[0], "repos_payload": payload[1], "expected_repos": payload[2], "apache2_repos": payload[3]}
    for payload in fixtures.TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the tests by mocking requests.get."""
        def side_effect(url):
            """Helper function for side_effect to return the correct fixture."""
            response = None
            if url.startswith("https://api.github.com/orgs/"):
                response = MockResponse(cls.org_payload)
            if url.endswith("/repos"):
                response = MockResponse(cls.repos_payload)
            if not response:
                response = MockResponse({})
    
            print(f"URL: {url}, Response type: {type(response.json_data)}")
            return response

        cls.get_patcher = patch('requests.get', side_effect=side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the tests by stopping the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public repos with mocked data."""
        test_client = GithubOrgClient('test_org')
        repos = test_client.public_repos()
        self.assertEqual(repos, self.expected_repos)
