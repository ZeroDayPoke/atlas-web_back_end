#!/usr/bin/env python3
"""Unittests for client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
